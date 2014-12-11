#-*-coding:UTF-8-*-
'''
Created on 2014年12月9日

@author: rkzhang
'''
from example import AppConfig
import logging
from logging import getLogger
from logging.handlers import RotatingFileHandler

cfg = AppConfig.getConfig()

file = cfg.get('output', 'LOGDIR') + '/log.txt'
print file

'''
级别    对应的值
CRITICAL     50
ERROR     40
WARNING     30
INFO     20
DEBUG     10
NOTSET     0

filename ：日志文件的保存路径。如果配置了些参数，将自动创建一个FileHandler作为Handler；
filemode ：日志文件的打开模式。 默认值为'a'，表示日志消息以追加的形式添加到日志文件中。如果设为'w', 那么每次程序启动的时候都会创建一个新的日志文件；
format ：设置日志输出格式；
datefmt ：定义日期格式；
level ：设置日志的级别.对低于该级别的日志消息将被忽略；
stream ：设置特定的流用于初始化StreamHandler；
'''
logging.basicConfig(filename = file, level = logging.WARN, filemode = 'a', format = '%(asctime)s - %(levelname)s: %(message)s')

logging.debug('debug')  #被忽略  
logging.info('info')    #被忽略  
logging.warning('warn')  
logging.error('error') 

#顶级记录器app
logger = getLogger('app')
logger.setLevel(logging.INFO)

MAXLOGSIZE = 10*1024*1024 #Bytes
BACKUPCOUNT = 10

#rotating日志处理器
handler = RotatingFileHandler(file, mode='a', maxBytes=MAXLOGSIZE, backupCount=BACKUPCOUNT)
logger.addHandler(handler)

#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logger.addHandler(console)

net_log = logging.getLogger('app.net')
net_log.setLevel(logging.ERROR)

class FilterFunc(logging.Filter) :  
    def __init__(self, name) : 
        self.funcName = name 
        
    def filter(self, record) : 
        if record.funcName == self.funcName :
            return False
        else : 
            return True
        
logger.addFilter(FilterFunc('foo'))
logger.addFilter(FilterFunc('bar'))

logger.debug('app debug')  #被忽略  
logger.info('app info')    #被忽略  
logger.warning('app warn')  
logger.error('app error') 

#用字典格式化日志消息
params = {
    'host' : 'www.python.org',
    'port' : 80
}
logger.info("Can't connect to %(host)s at port %(port)d", params)

#使用位置格式化的日志信息
host = 'www.python.org'
port = 80
logger.info("Can't connect to %s at port %d", host, port)

logger.info("app error")
net_log.info("app.net error")
