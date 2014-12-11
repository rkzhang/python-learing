'''
@author: rkzhang
'''

class Bird(object):
    '''
    classdocs
    '''
    def __init__(self, name):
        self.name = name
        
    def sayHello(self):
        print "say : My Name is " + self.name   
        