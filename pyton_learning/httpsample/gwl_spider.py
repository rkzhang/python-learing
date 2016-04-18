#-*-coding:UTF-8-*-
'''
Created on 2015年5月18日
@author: rkzhang
'''
import urllib2
import time
import random
import cookielib
import re
from dao.data_source import getConn, getCur
import uuid
import MySQLdb

urlPattern = re.compile(r'<h2><a[\s\S]*?</a></h2>') 
hrefPattern = re.compile(r'href="\S*')  
titlePattern = re.compile(r'<h1 class="title">[\s\S]*</h1>') 

home = 'http://www.gewara.com'

def setHead(req) :
    req.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
    req.add_header("Accept-Language", "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3")
    req.add_header("Cache-Control", "max-age=0")
    req.add_header("Connection", "keep-alive")
    req.add_header("Host", "t.dianping.com")
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0")
    req.add_header("Host", "www.gewara.com")     
    req.add_header("Referer", "www.gewara.com")
    
def getPageContent(url):
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    urllib2.install_opener(opener)
    req = urllib2.Request(url)
    setHead(req)
    resp = urllib2.urlopen(req)
    data = resp.read()
    return data

sportsPattern = re.compile(r'<b id="itemsTypeName">[\s\S]*?</b>')

def paseSports(venuesPage) :
    results = sportsPattern.findall(venuesPage)
    for sport in results :
        sport = sport.replace('<b id="itemsTypeName">', '')         
        sport = sport.replace('</b>', '') 
        return sport

districtPattern = re.compile(r'title="(\S*)" target="_blank">\1</a>')

def paseDistrict(venuesPage) :
    results = districtPattern.findall(venuesPage)
    for district in results :
        district = district.replace('target="_blank">', '')         
        district = district.replace('</a>', '') 
        return district

phonePattern = re.compile(r'<li class="iCall">\S*?</li>')

def pasePhone(venuesPage) :
    results = phonePattern.findall(venuesPage)
    for phone in results :
        phone = phone.replace('<li class="iCall">', '')         
        phone = phone.replace('</li>', '') 
        return phone

namePattern = re.compile(r'<h1>\S*?</h1>')  

def paseName(venuesPage) :
    results = namePattern.findall(venuesPage)
    for name in results :
        name = name.replace('<h1>', '')         
        name = name.replace('</h1>', '') 
        return name

addressPattern = re.compile(r'target="_blank">\S*?<span class="ffst">')  

def paseAddress(venuesPage) :
    results = addressPattern.findall(venuesPage)
    for address in results :
        address = address.replace('target="_blank">', '') 
        address = address.replace('</a>', '') 
        address = address.replace('<span class="ffst">', '') 
        return address
        
discriptionPattern = re.compile(r'<p class="ui_summary"><span class="first"></span>[\s\S]*?<span></span></p>')  

def paseDiscription(venuesPage) :
    results = discriptionPattern.findall(venuesPage)
    for disc in results :
        disc = disc.replace('<p class="ui_summary"><span class="first"></span>', '') 
        disc = disc.replace('<span></span></p>', '') 
        disc = disc.replace('&nbsp', '') 
        disc = disc.replace('\n', '') 
        disc = disc.replace('\s', '') 
        disc = disc.replace(' ', '') 
        disc = disc.replace('    ', '') 
        disc = disc.lstrip()
        disc = disc.rstrip()
        return disc
    
picGroupPattern = re.compile(r'<div class="ui_movieBigType">[\s\S]*?</div>')
picPattern = re.compile(r'src="\S*')

def pasePic(venuesPage) :
    picStr = ''
    results = picGroupPattern.findall(venuesPage)
    for pics in results :
        picRes = picPattern.findall(pics)
        count = 0
        for pic in picRes : 
            pic = pic.replace('src="', '') 
            pic = pic.replace('"', '') 
            if(count > 0) :
                picStr = picStr + ';' + pic
            else :
                picStr = picStr + pic    
            count = count + 1
        
    return picStr

def save(record) :
    with getConn() as conn : 
        with getCur(conn) as cur :           
            try :              
                discription = MySQLdb.escape_string(record['discription'])               
                sql = "insert into dzdp_venues_info values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (uuid.uuid4(), record['district'], record['name'], record['address'], record['phone'],  record['sports'], discription, record['pic'])
                cur.execute(sql)  
            except Exception, cc :
                print cc

def paseVenuesInfo(venuesUrl):
    print venuesUrl
    record = {}
    venuesPage = getPageContent(venuesUrl)
    
    print '###################################'
    record['district'] = paseDistrict(venuesPage)
    print 'district is ', record['district']
    record['name'] = paseName(venuesPage)
    print 'name is ', record['name']
    record['address'] = paseAddress(venuesPage)
    print 'address is ', record['address']
    record['phone'] = pasePhone(venuesPage)
    print 'phone is ', record['phone']
    record['discription'] = paseDiscription(venuesPage)
    print 'discription is ', record['discription']
    record['pic'] = pasePic(venuesPage)
    print 'pic is ', record['pic']
    record['sports'] = paseSports(venuesPage)
    print 'sports is ', record['sports']
    save(record)
        
def doPaseSport(serviceType):
    for page in range(0, 50) : 
        try :    
            url = 'http://www.gewara.com/sport/ajax/sportListPage.xhtml?servicetype=' + str(serviceType) + '&countycode=&indexareacode=&lineid=&park=&sale=&lease=&membercard=&booking=&sportname=&order=&pageNo=' + str(page)
            print url
            content = getPageContent(url)    
            results = urlPattern.findall(content)
            
            if len(results) == 0 :
                return
            
            for venus in results :
                try :  
                    print venus
                    hrefs = hrefPattern.findall(venus)
                    for href in hrefs :
                        href = href.replace('href="', '') 
                        href = href.replace('"', '') 
                        venues_url = home + href
                        paseVenuesInfo(venues_url)
                except Exception, aa :
                    print aa     
            time.sleep(random.randint(3, 10))
        except Exception, ee :
                print ee
    
serviceTypes = [288732,288699,288731,288721,288733,288722,6582889,133785894,296083,111006658,288734,301954,288704,303811,311713,288723,288690,288691,288692,312511,288711,3993698,181050637,224521440]
        
for type in serviceTypes :
    doPaseSport(type)

print 'finish'
