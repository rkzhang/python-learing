#-*-coding:UTF-8-*-
'''
Created on 2014年12月25日
@author: zhangr01
'''

from base64 import urlsafe_b64decode

encode_str = "eyJuYW1lIjoiMTgwNDUwMzIxMDgiLCJtb2JpbGUiOiIxODA0NTAzMjEwOCIsInR5cGUiOjEsInN0YXR1cyI6MSwicmVhbE5hbWUiOiIiLCJiaXJ0aGRheSI6IiIsImFkZHJlc3MiOiIiLCJoZWFkUGhvdG8iOiIifQ"
len = len(encode_str) % 4
for i in range(len) : 
    encode_str += '='

print encode_str
print urlsafe_b64decode(encode_str)