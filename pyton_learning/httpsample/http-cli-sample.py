#-*-coding:UTF-8-*-
'''
Created on 2014年12月24日
@author: zhangr01
'''
import httplib
import urllib

conn = httplib.HTTPConnection('www.sina.com.cn')  
conn.request('GET', '/')
r1 = conn.getresponse() 
print r1.reason, r1.status
print r1.msg
data1 = r1.read() 
print data1
conn.close()

headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}  
params = urllib.urlencode({'userId': 1001, 'appId': 100102, 'data': '{"itemId":"267583"}'})
conn = httplib.HTTPConnection("home.rrs.com") 
conn.request("POST", "/rcp/http-handler/request", params, headers) 

response = conn.getresponse()  
print response.status, response.reason 
data = response.read()  
print data
conn.close()

