#-*-coding:UTF-8-*-
'''
@author: rkzhang
'''
import sys
import decimal
import math
from dis import dis
from base.Bird import Bird
import random
from random import randrange
from array import array

b = Bird("Tim")
b.sayHello()
dis(Bird) #鍙嶆眹缂�print sys.path
print sys.platform

x = decimal.Decimal('3.4')
y = decimal.Decimal('4.5')
print x * y 

c = decimal.getcontext()
print c.capitals
print c.Emax
print c.Emin
print c.prec
print c.flags
print c.rounding
print c.traps

print math.fmod(100, 18)
print math.fsum([1.8, 9.7, 3.12415926, 13, 35])

print random.randint(1, 100)
print random.getrandbits(12)
print random.randrange(0, 100, 5)
list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print random.choice(list)
print random.sample(list, 3)
numlist = range(1, 100000)
print random.sample(numlist, 3)

numbers = array('d', [1, 1.18, 1.6])
print numbers.itemsize
numbers.append(5)
print numbers

#Mac next commit

