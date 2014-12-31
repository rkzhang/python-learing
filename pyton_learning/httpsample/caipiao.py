#-*-coding:UTF-8-*-
'''
Created on 2014年12月31日

@author: zhangr01
'''
import cookielib
import urllib2
from urllib2 import Request
from itertools import combinations

listnum = str(30)

def setHead(req) :
    req.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
    req.add_header("Accept-Language", "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3")
    req.add_header("Accept-Type", "ok/json")
    req.add_header("Connection", "keep-alive")
    req.add_header("Host", "www.okooo.com")
    req.add_header("Referer", "http://www.okooo.com/gd11x5/gd11x5zs/r/"+listnum+"/")
    
def check(his_bonus_num) :
    
    def rfilter(record) :
        last_bonus_num = his_bonus_num[len(his_bonus_num) - 1]
        sec = list(set(last_bonus_num).intersection(set(record)))
        if len(sec) >= 2 : 
            return True
        else :
            return False
    return rfilter

#---------------------------------

url3 = "http://www.okooo.com/ajax/zoushitu/GDSYY/"+listnum+"/R/"
req3 = Request(url3)
setHead(req3)

cj = cookielib.CookieJar();
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

#---------------------------------------
rlist = []

resp = urllib2.urlopen(req3)
data = resp.read()
results = eval(data)
sorted(results)

con = 0
for record in results : 
    con = con + 1
    if con > 2 : 
        s = sorted(record['r'])
        rlist.append(s)

print(len(results) - 2)
print len(rlist)

print 'last bonus num is ' + str(rlist[len(rlist) - 1])
all_bonus_num = combinations(['01','02','03','04','05','06','07','08','09','10','11'], 5)
buy = filter(check(rlist), all_bonus_num)
for num in buy :
    print num

print 'will buy num is', len(buy)
