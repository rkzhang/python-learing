'''
@author: rkzhang
'''
import pymongo

class MongoConnecterFactory(object):
    '''
    classdocs
    '''
    
 
    def __init__(self, params):
        '''
        Constructor
        '''
    @staticmethod 
    def getConnection(ip, port) : 
        return pymongo.Connection(ip, port)
        