#-*-coding:UTF-8-*-
'''
Created on 2014年12月30日
@author: zhangr01
'''
import sys
import copy

class Point(object) : 
    
    #对象只有继承object类时候，__slots__才有效
    __slots__ = ("x", "y")
    
    def __init__(self, x, y) :
        self.x = x
        self.y = y
        
    def __str__(self, *args, **kwargs):
        return "Point(%d, %d)" % (self.x, self.y)

p = Point(1, 2)

def make_object(Class, *args, **kwargs) : 
    return Class(*args, **kwargs)

point1 = Point(1, 2)
print point1

point2 = eval("{}({}, {})".format("Point", 2, 3))
print point2

point3 = getattr(sys.modules[__name__], "Point")(3, 6)
print point3

point4 = globals()['Point'](4, 8)
print point4

point5 = make_object(Point, 5, 10)
print point5

point6 = copy.deepcopy(point5)
point6.x = 6
print point6

point7 = point1.__class__(7,13)
print point7

point8 = type(point7)(8,13)
print point8

print type(point8).__name__


    