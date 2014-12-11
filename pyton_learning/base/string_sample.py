#-*-coding:UTF-8-*-
'''
Created on 2014年12月8日
@author: rkzhang
'''
import codecs
import struct

data = "在编程中我也一直这么用了，直到有一天发现了一个有趣的技巧"
c = codecs.lookup("utf-8")

bytes, length = c.decode(data)
print bytes, length
str, length = c.encode(bytes)
print str, length

r = "{0} {1} {2}".format('Good', 100, 490.10)
print r
r = "{name} {shares} {price}".format(name='Good', shares=100, price=490.10)
print r
r = "Hello {0}, your age is {age}".format("Elwood", age=47)
print r

a=12.34
#将a变为二进制
bytes=struct.pack('d',a)
print bytes
a,=struct.unpack('d',bytes)
print a

#如果是由多个数据构成的，可以这样：
a='hello'
b='world!'
c=2
d=45.123
bytes=struct.pack('5s6sif',a,b,c,d)
print bytes

#我们使用处理二进制文件时，需要用如下方法
binfile=open('filepath','rb')    #读二进制文件
binfile=open('filepath','wb')    #写二进制文件