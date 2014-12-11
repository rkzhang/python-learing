'''
@author: rkzhang
'''
import fileinput
#f = open('/Users/rkzhang/learngit/readme.txt', 'rw')
with open('/Users/rkzhang/learngit/readme.txt', 'rw') as f :
    try :    
        s = f.readline()
        while s:
            print s
            s = f.readline()
    finally:
        f.close()
    
'''
 modif mode
'''   
    
for line in fileinput.input('/Users/rkzhang/learngit/readme.txt', inplace=1) :
    line.replace('Git', 'git')
    


