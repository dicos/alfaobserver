#-*- coding: utf8 -*-

from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine

from settings import DATABASE

url = URL(DATABASE['DRIVERNAME'], DATABASE['USERNAME'], DATABASE['PASSWORD'],
          DATABASE['HOST'], DATABASE['PORT'], DATABASE['DATABASE'])

engine = create_engine(url)