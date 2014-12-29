#-*-coding:UTF-8-*-
'''
@author: rkzhang
'''
from my_util.validate_util import ensure, is_non_empty_str, is_in_range

class Foo(object):
    
    #指定合法的属性名称列表
    __slots__ = ('__name')
    
    def __init__(self, name) :
        self.__name = name
        
    @property   
    def name(self) : 
        print "get name ", self.__name
        return self.__name
    
    @name.setter
    def name(self, value) :
        print "set name ", self.__name
        if not isinstance(value, str) : 
            raise TypeError("Must be a string!")
        self.__name = value
    
    @name.deleter    
    def name(self) :
        print "delete name "
        raise TypeError("Can't delete name")
    
f = Foo("Guido")
n = f.name
f.name = "Monty"
#f.name = 33
#del f.name

from abc import ABCMeta, abstractmethod, abstractproperty

class AbstractFoo : 
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def spam(self, a, b) : 
        pass
    
    @abstractproperty
    def name(self) :
        pass

@ensure('title', is_non_empty_str)    
@ensure('price', is_in_range(1, 10000))
@ensure('quantity', is_in_range(0, 100000))
class Book : 
    
    def __init__(self, title, price, quantity) : 
        self.title = title
        self.price = price
        self.quantity = quantity
        
    @property
    def value(self) : 
        return self.price + self.quantity
