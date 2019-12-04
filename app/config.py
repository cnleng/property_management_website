import os, secrets 

class Config(object):
    SECRET_KEY = secrets.token_hex(16)
    MYSQL_HOST = "classmysql.engr.oregonstate.edu"
    MYSQL_USER = "cs340_hollingx"
    MYSQL_PASSWORD = "7635"
    MYSQL_DB = "cs340_hollingx"