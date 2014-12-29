#-*-coding:UTF-8-*-
'''
Created on 2014年12月28日
@author: rkzhang
'''
import numbers

def is_non_empty_str(name, value):
    if not isinstance(value, str) : 
        raise ValueError("{} must be of type str".format(name))
    if not bool(value) : 
        raise ValueError("{} may not be empty".format(name))
    
def is_in_range(minmum=None, maxmum=None) : 
    assert minmum is not None or maxmum is not None
    def is_in_range(name, value) : 
        if not isinstance(value, numbers.Number) : 
            raise ValueError("{} must be a number".format(value))
        if minmum is not None and value < minmum : 
            raise ValueError("{} {} is too small".format(name, value))
        if maxmum is not None and value > maxmum : 
            raise ValueError("{} {} is too big".format(name, value))
    return is_in_range

def ensure(name, validate, doc=None) : 
    
    def decorator(Class): 
        privateName = '__' + name
        
        def getter(self):
            print 'process get ' + privateName
            return getattr(self, privateName)
        
        def setter(self, value):
            print 'process set ' + privateName
            validate(name, value)
            setattr(self, privateName, value)
            
        setattr(Class, name, property(getter, setter, doc=doc))
        return Class
    
    return decorator
            