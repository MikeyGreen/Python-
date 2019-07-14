import json
dic = {'key':"你好"}
str1 = json.dumps(dic)
print(str1)
str2 = json.dumps(dic,ensure_ascii = False)
print(str2)
dic2 = {"key":["你好",'我好','大家好'],'mother':"female",'father':'male'}
str3 = json.dumps(dic2,sort_keys = True,indent = 2,separators = (',',':'),ensure_ascii = False)
print(str3)