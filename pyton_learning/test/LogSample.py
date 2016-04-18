#-*-coding:UTF-8-*-
'''
Created on 2014年12月10日

@author: zhangr01
'''
import logging.config

logging.config.fileConfig('../logger.ini')

app_log = logging.getLogger("app")

app_log.info("test log info")

