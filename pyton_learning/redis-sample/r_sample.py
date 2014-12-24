#-*-coding:UTF-8-*-
'''
Created on 2014年12月18日

@author: zhangr01
'''

from redis import Redis
import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0) 
 
r.save()
