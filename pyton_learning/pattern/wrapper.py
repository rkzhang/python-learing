#-*-coding:UTF-8-*-
'''
Created on 2014年12月30日
@author: zhangr01
'''
import functools

def filter_one(func) :
    @functools.wraps(func)
    def wrapper(name) :
        print 'filter_one name -- ' + name
        result = '<li>' + func(name) + '<li>'   
        print 'filter_one result -- ' + result
        return result
    return wrapper

def filter_two(func) :
    @functools.wraps(func)
    def wrapper(name) :
        print 'filter_two name -- ' + name
        result = '<br>' + func(name) + '<br>'   
        print 'filter_two result -- ' + result
        return result
    return wrapper
    
@filter_one
@filter_two
def createTitle(name) :
    return 'Hello, ' + name

print createTitle('Tim')