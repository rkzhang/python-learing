#-*-coding:UTF-8-*-
'''
Created on 2014年12月24日
@author: zhangr01
'''
import httplib
import urllib
from threading import Timer, Lock
import threading

count = 0

def request(conn) :
    conn.request('GET', '/api/home/eventList.do')
    r1 = conn.getresponse() 
    print r1.reason, r1.status
    print r1.msg
    data1 = r1.read() 
    
class PushThread(threading.Thread) :
    def __init__(self, interval) : 
        threading.Thread.__init__(self)
        self.daemon = False #设置daemon标志会使解析器在主程序退出后立即退出
        self.interval = interval
        
    def run(self) : 
        conn = httplib.HTTPConnection('192.168.1.86')  
        while True :
            request(conn)
            global count 
            count = count + 1
            print count
        conn.close()

for i in range(1, 20) : 
    t1 = PushThread(10)
    t1.start()
