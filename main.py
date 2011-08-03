# -*- coding: utf8 -*-
import datetime
import time

import win32com.client
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import DATABASE, A_USERNAME, A_PASSWORD, PAPERS
from models import TradeType, AllTrade, Queue


def get_engine(drivername, username, password, host, port, database):
    url = URL(DATABASE['DRIVERNAME'], DATABASE['USERNAME'], DATABASE['PASSWORD'],
          DATABASE['HOST'], DATABASE['PORT'], DATABASE['DATABASE'])
    engine = create_engine(url)
    return engine


engine = get_engine(DATABASE['DRIVERNAME'], DATABASE['USERNAME'],
                    DATABASE['PASSWORD'], DATABASE['HOST'], 
                    DATABASE['PORT'], DATABASE['DATABASE'])


def connect_terminal(A_USERNAME, A_PASSWORD):
    terminal = win32com.client.Dispatch("ADLite.AlfaDirect")
    terminal.UserName = A_USERNAME
    terminal.Password = A_PASSWORD
    terminal.Connected = True
    return terminal


terminal = connect_terminal(A_USERNAME, A_PASSWORD)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


def check_trade_types(terminal_res, session_db):
    trades_types_str = terminal_res.GetLocalDBData("trade_types", 
                                                   "*", 
                                                   "trd_type_code > 0")
    trades_types_t = trades_types_str.split("\r\n")
    
    trades_types_row = session_db.query(TradeType).all()
    for num, row in enumerate(trades_types_row):
        if row.trd_type_code != trades_types_t[num].split("|")[0]:
            return False
    return True


if not check_trade_types(terminal, session):
    raise Exception("Trades_types not valid")
else:
    print "trade_types is valid"


def get_paper_no(p_code, terminal_res):
    condition = "p_code = '%s'" % p_code
    response = terminal_res.GetLocalDBData("papers", '*', condition)
    number = int(response.split("|")[0])
    return number


def write_trades(num, i_last_update, terminal_res, session_db):
    query_trades = "p_code = %s AND i_last_update > %s" % (num, i_last_update,)
    trades_str = terminal_res.GetLocalDBData("all_trades", '*', query_trades)
    if len(trades_str) == 0:
        raise ValueError('Not data in table "Trade_Types"')
    trades = []
    for trade_row_str in trades_str.split("\r\n"):
        if len(trade_row_str) == 0:
            continue
        trade_info = trade_row_str.split("|")
        i_last_update = trade_info[5]
        trades.append(AllTrade(*trade_info))
    session_db.add_all(trades)
    print "inserted trades"
    return i_last_update


def write_queue(num, terminal_res, session_db):
    query = "p_code = %s" % num
    queue_str = terminal_res.GetLocalDBData("queue", '*', query)
    if len(queue_str) == 0:
        raise ValueError('Not data in table "Queue"')
    queues = []
    for queue_row_str in queue_str.split("\r\n"):
        if len(queue_row_str) == 0:
            continue
        queue_info = queue_row_str.split("|")
        queue_info[0] = num
        del queue_info[4:]
        queues.append(Queue(queue_info))
    session_db.add_all(queues)
    print "inserted queue"
    return


def dispatch(terminal_res, session_db):
    paper_nums = dict([[get_paper_no(v, terminal), '0',] for v in PAPERS])
    last_updated_time = datetime.datetime.now()
    while 1:
        current_time = datetime.datetime.now()
        td = current_time - last_updated_time
        if td < datetime.timedelta(seconds=1):
            time.sleep(1)
            continue
        else:
            last_updated_time = current_time
        
        for num, i_last_update in paper_nums.items():
            try:
                i = write_trades(num, i_last_update, terminal_res, session_db)
                paper_nums[num] = i
            except ValueError:
                raise ValueError
                terminal_res.Connected = True
                continue
            write_queue(num, terminal_res, session_db)

dispatch(terminal, session)