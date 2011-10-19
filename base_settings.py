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

PAPERS = ("RTSI-12.11", "SBER-12.11", "BVTB-12.11", "GAZP-12.11", 
          "LKOH-12.11", "ROSN-12.11", "GMKN-12.11", "GOLD-12.11",)