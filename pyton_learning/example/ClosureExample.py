#-*-coding:UTF-8-*-
'''
Created on 2014年12月26日
@author: rkzhang
'''
import functools
from compiler.ast import Function

def make_adder(addend):
    def adder(augend):
        return augend + addend
    return adder

p = make_adder(23)
q = make_adder(44)

print p(100)
print q(100)

#------------------------------------

def hellocounter (name):
    count=[0] 
    def counter():
        count[0]+=1
        print 'Hello,',name,',',str(count[0])+' access!'
    return counter

hello = hellocounter('ma6174')
hello()
hello()
hello()

#------------------------------------

def makebold(fn):
    
    @functools.wraps(fn)
    def wrapped(name):         
        print 'makebold -- ' + name
        return "<b>" + fn(name) + "</b>"
    return wrapped

def makeitalic(fn):
    
    @functools.wraps(fn)
    def wrapped(name):
        print 'makeitalic -- ' + name
        return "<i>" + fn(name) + "</i>"
    return wrapped

@makebold
@makeitalic
def hello(name):
    print __name__
    return 'hello ' + name
print hello('Jone') 
