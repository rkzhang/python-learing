'''
@author: zhangr01
'''

import pymongo
connection = pymongo.Connection('10.1.132.166', 22222)
db = connection.test
    
db.user.insert({'id': '123','name': 'name' ,'sex': 'man', 'info' : "{ 'id' : 1, 'name' : 'rkz' }" }) 


for rec in db.user.find() :
    print rec['info']
