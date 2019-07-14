#
import re
s = re.split("\d+","japan123china456omygod789") #按正则表达式分割
print(s)
s = re.split("(\d+)","japan123china456omygod789") #分组
print(s) #['japan', '123', 'china', '456', 'omygod', '789', '']

s = '<a>wahahahaha</a>'
ret =re.search(">(\w+)<",s)
print(ret.group(1))
#给分组起名 ?P<name>
s = '<a>wahahahaha</a>'
ret =re.search(">(?P<con>\w+)",s)
print(ret.group("con"))

#前后标签不一致,如何识别
s = '<a>wahahahaha</b>'
#这种方法无法发现前后两个标签不一致
rr = re.search(">(\w+)<",s)
print(rr.group()) #>wahahahaha<
print(rr.group(1)) #wahahahaha
rr = re.search("(\w+)>(\w+)</(\w+)>",s)
print(rr.group(1),rr.group(3)) # a  b
#分组命名方式
rr = re.search("(?P<name1>\w+)>(\w+)</(?P<name2>\w+)",s)
print(rr.group('name1'),rr.group('name2'))
