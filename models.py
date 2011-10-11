#-*- coding: utf8 -*-
import datetime
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

metadata = MetaData()

ZERO = datetime.timedelta(0)


class MoscowTimeZone(datetime.tzinfo):
    def __init__(self, offset, name):
        self.__offset = datetime.timedelta(hours=offset)
        self.__name = name

    def utcoffset(self, dt):
        return self.__offset

    def tzname(self, dt):
        return self.__name

    def dst(self, dt):
        return ZERO


class AllTrade(Base):
    __tablename__ = 'all_trade'
    
    id = Column(Integer, primary_key=True)
    trd_no = Column(Integer)
    paper_no = Column(Integer, key='paper_no')
    qty = Column(Integer)
    price = Column(Integer)
    ts_time = Column(DateTime)
    i_last_update = Column(Integer)
    change = Column(SmallInteger)
    type = Column(SmallInteger)
    p_code = Column(String(12), key='p_code')
    place_code = Column(String(20))
    ansi_name = Column(String(20))
    place_name = Column(String(20))
    type_descr = Column(String(20))
    
    def __init__(self, trd_no, paper_no, qty, price, ts_time, i_last_update, 
                 change, type, p_code, place_code, ansi_name,
                 place_name, type_descr):
        self.trd_no = trd_no
        self.paper_no = paper_no
        self.qty = qty
        self.price = price
        self.ts_time = datetime.datetime.now(MoscowTimeZone(4, 'UTC+4'))
        self.i_last_update = i_last_update
        self.change = change
        self.type = type
        self.p_code = p_code
        self.place_code = place_code
        self.ansi_name = ansi_name
        self.place_name = place_name
        self.type_descr = type_descr


class TradeType(Base):
    __tablename__ = 'trade_type'
    
    id = Column(Integer, primary_key=True)
    trd_type_code = Column(String(1), key='trd_type_code')
    trd_type_description = Column(String(12))
    i_last_update = Column(Integer)
    trd_type_num_code = Column(Integer)


class Queue(Base):
    __tablename__ = 'queue'
    
    id = Column(Integer, primary_key=True)
    paper_no = Column(Integer, key='paper_no')
    price = Column(Float)
    buy_qty = Column(Float)
    sell_qty = Column(Float)
    i_last_update = Column(Integer)
    add_datetime = Column(DateTime)
    
    def __init__(self, paper_no, price, buy_qty, sell_qty, i_last_update):
        self.paper_no = paper_no
        self.price = price
        self.buy_qty = buy_qty
        self.sell_qty = sell_qty
        self.i_last_update = i_last_update
        self.add_datetime = datetime.datetime.now(MoscowTimeZone(4, 'UTC+4'))
        