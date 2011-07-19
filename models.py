#-*- coding: utf8 -*-
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AllTrade(Base):
    id = Column(Integer, primary_key=True)
    trd_no = Column(Integer)
    paper_no = Column(Integer, key='paper_no')
    qty = Column(Integer)
    price = Column(Integer)
    ts_time = Column(DateTime)
    i_last_update = Column(Integer)
    change = Column(SmallInteger)
    type = Column(SmallInteger, ForeignKey('trade_type.id'))
    p_code = Column(String(12), key='p_code')
    place_code = Column(String(20))
    ansi_name = Column(String(20))
    place_name = Column(String(20))
    type_descr = Column(String(20))


class TradeType(Base):
    id = Column(Integer, primary_key=True)
    trd_type_code = Column(String(1), key='trd_type_code')
    trd_type_description = Column(String(12))
    i_last_update = Column(Integer)
    trd_type_num_code = Column(Integer)

    
class Queue(Base):
    id = Column(Integer, primary_key=True)
    paper_no = Column(Integer, key='paper_no')
    price = Column(Float)
    buy_qty = Column(Float)
    sell_qty = Column(Float)
    add_datetime = Column(DateTime, server_default=text('NOW()'))
    