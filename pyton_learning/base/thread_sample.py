#-*-coding:UTF-8-*-
'''
Created on 2014年12月9日
@author: rkzhang
'''
import threading
import time
from threading import Timer, Lock

t = 0

lock = Lock()

def printCount() :
    lock.acquire()
    global t
    print t
    t = t + 1
    lock.release()

class ClockThread(threading.Thread) :
    def __init__(self, interval) : 
        threading.Thread.__init__(self)
        self.daemon = True #设置daemon标志会使解析器在主程序退出后立即退出
        self.interval = interval
        
    def run(self) : 
        while True :
            printCount()
            time.sleep(self.interval)   #休眠的秒数

t1 = ClockThread(10)
t1.start()

t2 = ClockThread(10)
t2.start()

t3 = ClockThread(10)
t3.start()


def p() :
    print 'task'
    
task = Timer(10, p) #多少秒后至执行一次
task.start()

while True:  
    time.sleep(10) 