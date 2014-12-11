#-*-coding:UTF-8-*-
'''
Created on 2014年12月8日

@author: rkzhang
'''
from ConfigParser import ConfigParser

defaults = {
    'basedir' : 'Users/beazley/app'
}
cfg = ConfigParser(defaults)
cfg.read("../appconfig.ini")

print cfg.get('output', 'LOGFILE')
print cfg.getboolean('output', 'logging')