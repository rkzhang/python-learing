#-*-coding:UTF-8-*-
'''
Created on 2014年12月30日
@author: zhangr01
'''

class Father(object):
    
    def __init__(self, name):
        self.name = name
    


class Sun(Father):
    
    def __init__(self, fname, own_name):
        Father.__init__(self, fname)
        self.own_name = own_name
        
    def __str__(self):
        return "father is %s,  name is %s" % (self.name, self.own_name)
    
sun = Sun('A', 'B')

print type(sun) is Sun          #判断是否是某类型
print type(sun) is Father
print isinstance(sun, Father)   #判断是否是某类型以及子类实现
