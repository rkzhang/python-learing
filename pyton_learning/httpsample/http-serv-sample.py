#-*-coding:UTF-8-*-
'''
Created on 2014年12月25日
@author: zhangr01
'''
from BaseHTTPServer import HTTPServer
from httpsample.request_handler import SampleHTTPHandle

http_server = HTTPServer(('127.0.0.1', 9000), SampleHTTPHandle)  

print 'Server start...'
http_server.serve_forever() #设置一直监听并接收请求  
