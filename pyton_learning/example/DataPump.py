#-*-coding:UTF-8-*-
'''
@author: zhangr01
'''
import re
from com.mongo.MongoTool import MongoConnecterFactory
from queue import Queue
import threading
import time

def parseLine(line) :
    return re.split('\s+', line, maxsplit=5)

f = open('C:/data/shuihezi_data.txt', 'r')

connection = MongoConnecterFactory.getConnection('127.0.0.1', 27017)
db = connection.test

dataQueue = Queue(10000)

class Producer(threading.Thread) : 
    def __init__(self) : 
        threading.Thread.__init__(self)
        self.daemon = True
        
    def run(self):
        head = re.split('\s+', f.readline(), maxsplit=5)
        print('head', head)    
        line = f.readline() 
        while line :
            try :
                line = parseLine(f.readline()) 
                record = {}
                index = 0
                for field in head :
                    record[field.strip()] = line[index]
                    index = index + 1
                                   
                dataQueue.put(record)
            except Exception : 
                pass
            line = f.readline()


class Consumer(threading.Thread):
    def __init__(self) : 
        threading.Thread.__init__(self)
        self.daemon = True
        
    def run(self):
        while True : 
            try :
                record = dataQueue.get()
                print(record)
                db.shuihezi.insert(record)
            except Exception : 
                pass
            

p = Producer()    
p.start()

for i in range(0, 7) :
    c = Consumer()
    c.start()
    
while True : 
    time.sleep(10)
    
    