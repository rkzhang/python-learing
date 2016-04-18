#-*-coding:UTF-8-*-
'''
Created on 2015年5月19日
@author: rkzhang
'''
import urllib2
import time
import random
import cookielib
import re
import json
from dao.data_source import getConn, getCur
import uuid
import MySQLdb

def setHead(req) :
    req.add_header("Accept", "application/json, text/plain, */*")
    req.add_header("Accept-Language", "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3")
    req.add_header("Cache-Control", "max-age=0")
    req.add_header("Connection", "keep-alive")
    req.add_header("Host", "api.1yd.me")
    req.add_header("Origin", "http://www.1yd.me")
    req.add_header("Referer", "http://www.1yd.me/")
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0")

def getPageContent(url):
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    urllib2.install_opener(opener)
    req = urllib2.Request(url)
    setHead(req)
    resp = urllib2.urlopen(req)
    data = resp.read()
    return data

def save(venues) :
    with getConn() as conn : 
        with getCur(conn) as cur :           
            try :                     
                sql = "insert into yd_venues_info values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (uuid.uuid4(), venues['name'], venues['telephone'], venues['address'], venues['province'], venues['city'], venues['district'], venues['category'], venues['photo'], venues['operation_start_time'], venues['operation_end_time'], venues['gpsx'], venues['gpsy'], venues['min_price'], venues['operation_days'], venues['summary'] )
                cur.execute(sql)  
            except Exception, cc :
                print cc

for i in range(0, 5000, 10) : 
    baseUrl = 'http://api.1yd.me/api/stadium_resources?city_id=310100&start=' + str(i)
    print baseUrl
    result = getPageContent(baseUrl)
    
    arrayList = json.loads(result)
    
    if len(arrayList) == 0 :
        break
        
    for venues in arrayList :
        print 'id ', venues['id']
        print 'name ', venues['name']
        print 'telephone ', venues['telephone']
        print 'address ', venues['address']
        print 'province ',venues['province']
        print 'city ', venues['city']
        print 'district ', venues['district']
        print 'photo ', venues['photo']
        print 'category ', venues['category']
        print 'operation_start_time ', venues['operation_start_time']
        print 'operation_end_time ', venues['operation_end_time']
        print 'gpsx ', venues['gpsx']
        print 'gpsy ',venues['gpsy']       
        print 'min_price ', venues['min_price']
        print 'operation_days ', venues['operation_days'] 
        print 'summary ', venues['summary']  
        save(venues)
        
    time.sleep(random.randint(3, 5))

print 'finish'
    