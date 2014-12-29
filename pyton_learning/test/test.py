#-*-coding:UTF-8-*-
'''
Created on 2014年12月25日
@author: zhangr01
'''
from itertools import ifilter

#返回所有计算为True的对象, 对应ifilterfalse返回判断为false的
for i in ifilter(lambda num : num < 50, range(1, 100)) :
    print i 