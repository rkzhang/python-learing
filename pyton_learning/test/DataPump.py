#-*-coding:UTF-8-*-
'''
@author: zhangr01
'''
import re
import pymongo
import threading
import time
from multiprocessing.queues import Queue
from threading import Lock
from test import app_log

print re.__file__  #这个文件是查看模块位置，在遇到模块冲突时候非常重要

f = open('D:/data/shuihezi_data.txt', 'r')
connection = pymongo.Connection('10.1.132.166', 22222)
db = connection.test

dataQueue = Queue(10000)

lock = Lock()
count = 1

def printCount() : 
    lock.acquire()
    global count 
    app_log.info('insert number : %d ', count)
    count = count + 1
    lock.release()
    

class Producer(threading.Thread) : 
    def __init__(self) : 
        threading.Thread.__init__(self)
        self.doemon = True
        
    def run(self) : 
        try : 
            head = re.split('\s+', f.readline(), maxsplit=5)
            print 'head', head
            
            line = f.readline()
        
            while line :
                try :
                    line = re.split('\s+', f.readline(), maxsplit=5)
                   
                    record = {}
                    index = 0
                    for field in head :
                        record[field.strip()] = line[index]
                        index = index + 1
                        
                    dataQueue.put(record)
                                  
                except Exception as e :
                    print e.message
                
                line = f.readline()
        finally : 
            f.close()
            
            
class Consumer(threading.Thread) :
    def __init__(self) :
        threading.Thread.__init__(self)
        self.doemon = True
        
    def run(self) : 
        while True :
            try : 
                record = dataQueue.get()
                printCount()
                db.shuihezi.insert(record)    
            except Exception as e :
                print e.message

p = Producer()
p.start()

for i in range(0,20) : 
    c = Consumer()
    c.start()
    print 'Consumer Thread-%d start' % i
    
while True : 
    time.sleep(10)
    