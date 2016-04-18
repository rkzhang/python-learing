# encoding: UTF-8
import re
 
# 将正则表达式编译成Pattern对象
pattern = re.compile('src="http\S*"')
 
# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern.search('fasdf src="http://dl.web.sogoucdn.com/common/lib/resultheightreport.85442424.js" http')
 
if match:
    # 使用Match获得分组信息
    print match.group()