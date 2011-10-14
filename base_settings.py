#-*- coding: utf8 -*-

# fake settings
DATABASE = {
    'DRIVERNAME': 'mysql+mysqldb',
    'USERNAME': '',
    'PASSWORD': '',
    'HOST': '',
    'PORT': '',
    'DATABASE': '',
    'QUERY': {'charset': 'utf8',}
}

POOL_RECYCLE = 3600 # 1 hour

# settings for terminal alfadirect
A_USERNAME = ''
A_PASSWORD = ''

PAPERS = ("RTS-12.11", "SBRF-12.11", "ROSN-12.11", "GMKR-12.11", 
          "GAZR-12.11", "LKOH-12.11", "VTBR-12.11", "Si-12.11", )