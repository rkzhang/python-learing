'''
@author: rkzhang
'''
from copy import deepcopy

class Account(object):

    def __init__(self) :
        pass
    
    @property
    def name(self):
        return self.__name
    
    @property    
    def passwd(self):
        return self.__passwd
    
    @name.setter
    def name(self, value) : 
        self.__name = value
        
    @passwd.setter  
    def passwd(self, value) : 
        self.__passwd = value    
        
    def __str__(self):
        return "name is %s , passwd is %s" % (self.__name, self.__passwd)
    
account1 = Account()
account1.name = "aaa"
account1.passwd = "a123456"

account2 = deepcopy(account1)
account2.name = "bbb"
account2.passwd = "b123456"

print account1
print account2
    