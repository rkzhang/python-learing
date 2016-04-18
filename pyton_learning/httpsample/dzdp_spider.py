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

urlPattern = re.compile(r'<a class="tg-floor-title" target="_blank" href="\S*') 
titlePattern = re.compile(r'<h1 class="title">[\s\S]*</h1>') 

home = 'http://t.dianping.com'

def setHead(req) :
    req.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
    req.add_header("Accept-Language", "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3")
    req.add_header("Cache-Control", "max-age=0")
    req.add_header("Connection", "keep-alive")
    req.add_header("Host", "t.dianping.com")
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0")
    req.add_header("Host", "t.dianping.com")     
    req.add_header("Referer", "http://t.dianping.com/list/shanghai-category_44?")
    
def getPageContent(url):
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    urllib2.install_opener(opener)
    req = urllib2.Request(url)
    setHead(req)
    resp = urllib2.urlopen(req)
    data = resp.read()
    return data

        
for page in range(1, 17) : 
    url = 'http://t.dianping.com/list/shanghai-category_44?pageIndex=' + str(page)
    print url
    content = getPageContent(url)    
    results = urlPattern.findall(content)
    
    for web in results :
        web = web.replace('<a class="tg-floor-title" target="_blank" href="', '') 
        web = web.replace('"', '') 
        sub_url = home + web
        print sub_url
        record = {}
        
        product_page = getPageContent(sub_url)
        
        m = titlePattern.findall(product_page)
        for title in m :
            title = title.replace('<h1 class="title">', '')
            title = title.replace('</h1>', '') 
            title = title.replace(' ', '') 
            title = title.replace('\n', '') 
            record['title'] = title
            print title
               
        
    time.sleep(random.randint(3, 10))
    
    
    
    