#-*-coding:UTF-8-*-
'''
Created on 2015年4月2日
@author: rkzhang
'''
from urllib2 import Request
import urllib2
import re
import time
import random
from dao.data_source import getConn, getCur
import uuid
import MySQLdb

queryStr = '外烩'

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
        try :
            pageContent = getPageContent(distUrl)
        except Exception, a :
            print a
            
        print distUrl
        with getConn() as conn : 
            with getCur(conn) as cur :           
                try :              
                    content = MySQLdb.escape_string(pageContent)
                    topic = queryStr
                    sql = "insert into juju_spider values('%s', '%s', '%s', '%s')" % (uuid.uuid4(), topic, distUrl, content)
                    cur.execute(sql)  
                except Exception, e :
                    print e

def query(url) :
    data = getPageContent(url)       
    results = pattern.findall(data)    
    for web in results :
        check(web)
        
for page in range(11, 1000) : 
    url = 'http://www.sogou.com/web?query=外烩&cid=&page=' + str(page) + '&ie=utf8&p=40040100&dp=1&w=01029901&dr=1&repp=1'
    print url
    query(url)
    time.sleep(random.randint(3, 10))
