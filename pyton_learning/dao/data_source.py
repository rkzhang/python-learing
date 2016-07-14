#-*-coding:UTF-8-*-
'''
Created on 2014骞�2鏈�0鏃�
@author: zhangr01
'''

import MySQLdb
import uuid
from contextlib import contextmanager

@contextmanager
def getConn() :
    conn= MySQLdb.connect(
        host='192.168.1.81',
        port = 3306,
        user='edu_user',
        passwd='123456',
        db ='edu_test',
        charset="utf8"
        )
    print 'achieve conn'
    yield conn
    conn.commit()
    conn.close()
    print 'close conn'
    
@contextmanager
def getCur(conn) : 
    cur = conn.cursor()
    print 'achieve cur'
    yield cur
    cur.close()
    print 'close cur'
    

