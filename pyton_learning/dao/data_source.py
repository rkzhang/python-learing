#-*-coding:UTF-8-*-
'''
Created on 2014骞�2鏈�0鏃�
@author: zhangr01
'''

import MySQLdb
import uuid

conn= MySQLdb.connect(
        host='115.29.245.7',
        port = 3306,
        user='bridal',
        passwd='bridal',
        db ='wedding',
        charset="utf8"
        )

cur = conn.cursor()

id = "0027472d-622c-44aa-8e04-545992e01528"
cur.execute("select * from wd_shop where id=%s limit 0, 10", id)    
for row in cur.fetchall():    
    print row

n = cur.execute("update wd_shop set stat=0 where id=%s ", id)
print n

cur.execute("select * from wd_shop where id=%s limit 0, 10", id)    
for row in cur.fetchall():    
    print row
print uuid.uuid4()

cur.close()    
conn.close() 