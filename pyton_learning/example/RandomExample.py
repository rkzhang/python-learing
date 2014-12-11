'''
@author: rkzhang
'''

from random import *
from time import *

data1 = (2008, 1, 1, 0, 0, 0, -1, -1, -1)
time1 = mktime(data1)
data2 = (2009, 1, 1, 0, 0, 0, -1, -1, -1)
time2 = mktime(data2)

random_time = uniform(time1, time2)
print asctime(localtime(random_time))

num = input('How many dice?')
sides = input('How many sides per die')
sum = 0
for i in range(num) :
    sum += randrange(sides) + 1
print 'The result is', sum

