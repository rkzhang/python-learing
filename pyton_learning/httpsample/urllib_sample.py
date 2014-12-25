#-*-coding:UTF-8-*-
'''
Created on 2014年12月25日
@author: zhangr01
'''
from urllib2 import urlopen, Request
import urllib
from json import loads
from base64 import urlsafe_b64decode

u = urlopen("http://www.cnblogs.com/mingaixin/archive/2012/09/25/2701576.html")
data = u.read()
print data

params = urllib.urlencode({'userId': 1001, 'appId': 100101, 'data': '{"userId":"1200009"}'})
u = urlopen('http://home.rrs.com/rcp/http-handler/request', params)
data = u.read()
print data

req = Request('http://home.rrs.com/rcp/http-handler/request')
req.add_data(params)
req.add_header("Content-type", "application/x-www-form-urlencoded")
req.add_header("Accept", "text/plain")
u = urlopen(req)
data = u.read()
jsonobj = loads(data)
result = jsonobj['result']

len = len(result) % 4
for i in range(len) : 
    result += '='

print result
print urlsafe_b64decode(result.encode('utf-8'))
