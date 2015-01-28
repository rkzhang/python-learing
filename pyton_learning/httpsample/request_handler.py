#-*-coding:UTF-8-*-
'''
Created on 2014年12月25日
@author: zhangr01
'''
from BaseHTTPServer import BaseHTTPRequestHandler
import urllib

class SampleHTTPHandle(BaseHTTPRequestHandler):
    
    def __init__(self, *args, **kwargs) :
        BaseHTTPRequestHandler.__init__(self, *args, **kwargs)
        
     
    def do_GET(self) :   
        print self.client_address
        print self.command
        print self.headers
        print self.path
        
        self.send_response(200, 'OK')
        self.send_header('content-type', 'text/plain')
        self.send_header('charset', 'utf-8')
        self.end_headers()
        
        resp = '你好  Python Server'.encode('utf-8')
        
        print '响应内容', resp
        self.wfile.write(resp)  
        