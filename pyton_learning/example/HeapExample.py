'''
@author: rkzhang
'''

from heapq import *
from random import shuffle

data = range(10)
shuffle(data)
print data

heap = []

for n in data :
    heappush(heap, n)
print heap

heappush(heap, 0.5)
print heap

print heappop(heap)
print heappop(heap)
print heappop(heap)

print heap

heap = [5, 8, 9, 3, 5, 6, 7, 10, 9]
heapify(heap)
print heap

print heapreplace(heap, 0.5)
print heap