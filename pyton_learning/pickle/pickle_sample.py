'''
@author: rkzhang
'''
import pickle
from pickle.UserInfo import Account

userAccount = Account();
userAccount.name = "username"
userAccount.passwd = "123456"
print userAccount

f = open('/Users/rkzhang/Learing/object_input.txt', 'wb')
pickle.dump(userAccount, f)
f.close()