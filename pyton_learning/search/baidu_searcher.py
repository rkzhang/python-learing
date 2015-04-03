#-*-coding:UTF-8-*-
'''
Created on 2015年4月2日

@author: Administrator
'''
from urllib2 import Request
import urllib2
import re
import time
import random

queryStr = '足球'

pattern = re.compile(r'href="http://\S*"')
urlPattern = re.compile(r'http://\S*') 

def getPageContent(url):
    req = Request(url)
    resp = urllib2.urlopen(req)
    data = resp.read()
    return data
    
def check(url):
    results = urlPattern.findall(url)
    for web in results :
        distUrl = web.replace('"','')
        print distUrl       
        try : 
            pageContent = getPageContent(distUrl)
        except Exception, e :
            print e

def query(url) :
    data = getPageContent(url)    
    results = pattern.findall(data)    
    for web in results :
        check(web)
        
for page in range(100) : 
    url = 'http://www.sogou.com/web?oq=z&stj0=0&query=' + queryStr + '&stj=0%3B0%3B0%3B0&stj2=0&stj1=0&hp=0&hp1=&sut=6213&lkt=9%2C1428049223499%2C1428049227495&ri=0&sst0=1428049229712&page=' + str(page) + '&ie=utf8&p=40040100&dp=1&w=01015002&dr=1'
    query(url)
    time.sleep(random.randint(2, 5) )
