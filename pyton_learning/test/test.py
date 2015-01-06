#-*-coding:UTF-8-*-
'''
Created on 2014年12月25日
@author: zhangr01
'''
from itertools import combinations


'''
cou = 0;
for b in product([3,1,0],[3,0],[3,1,0],[3,1,0],[3,1,0]) :
    cou = cou + 1
    print b

print cou

cou2 = 0;
for it in product([5.5,4.3,1.4],[4.5,1.53],[2.7,3.3,2.10],[3.7,3.75,1.69],[1.46,4.1,5.00]) :
    cou2 = cou2 + 1
    print it
    sum = reduce(lambda a,b : a * b, it)
    print sum * 2

print cou2


for a in permutations([], 2) :
    print a
'''

con = 0
for it in combinations([1,2,3,4,5,6,7,8,9,10,11], 5) : 
    con = con + 1
    print it
    
print con
