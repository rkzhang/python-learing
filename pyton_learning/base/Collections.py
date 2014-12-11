#-*-coding:UTF-8-*-
'''
@author: rkzhang
'''
from array import array
from collections import namedtuple
from _collections import defaultdict
from random import shuffle
import heapq
from _heapq import heappop, heappush, heapreplace
from itertools import chain, combinations, count, ifilter, imap, product
import operator

numbers = array('d', [1, 1.18, 1.6])
print numbers.itemsize
numbers.append(5)
print numbers

#命名元组
NetworkAddress = namedtuple('NetworkAddress', ['hostname', 'port'])
a = NetworkAddress('www.python.org', 80)
print a.hostname, a.port
print type(a)
print isinstance(a, tuple)
print a

#双端队列
s = "yeah but no but yeah but no but yeah"
words = s.split()
wordlocations = defaultdict(list)
for n, w in enumerate(words) : 
    wordlocations[w].append(n)
print  wordlocations  

#堆
heap = range(1, 100)
shuffle(heap)
heapq.heapify(heap) 
print heap
print heappop(heap)
heappush(heap, 101)
heapreplace(heap, 102)
print heap

#itertools
for i in chain(range(1, 10), range(10, 20)) : 
    print i
    
#3个一组排列组合
for list in combinations(range(1,20), 3) : 
    print list

#从某个数开始，连续生产整数    
for i in count(100) : 
    if i == 200 :
        break
    print i
    
def checkNum(num) :
    if num > 50 :
        return True
    else :
        return False

#返回所有计算为True的对象, 对应ifilterfalse返回判断为false的
for i in ifilter(checkNum, range(1, 100)) :
    print i 
    
def addNum(num1, num2, num3) : 
    return num1 + num2 + num3

#多个迭代器提供值，由一个函数处理，直到有一个迭代器不在生成值为止
for i in imap(addNum, range(0, 100), range(100, 200), range(200,300)) : 
    print i

#生成笛卡尔积    
for a in product(range(0,10), range(10, 20), range(20, 30)) : 
    print a
    
print reduce(operator.mul, range(1, 6))    