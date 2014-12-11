#-*-coding:UTF-8-*-
'''
Created on 2014年12月9日

@author: rkzhang
'''
from ConfigParser import ConfigParser

defaults = {
    'basedir' : 'Users/beazley/app'
}
cfg = ConfigParser(defaults)
cfg.read("../appconfig.ini")

def getConfig() : 
    return cfg