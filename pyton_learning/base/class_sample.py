#-*-coding:UTF-8-*-
'''
@author: rkzhang
'''

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
