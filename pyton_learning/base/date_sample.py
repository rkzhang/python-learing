#-*-coding:UTF-8-*-
'''
Created on 2014年12月8日
@author: rkzhang
'''
from datetime import date, datetime
import time
import os

print date(2012,12,21)

print date.today()

print date.fromtimestamp(time.time())

print datetime.now()

print os.getcwd()