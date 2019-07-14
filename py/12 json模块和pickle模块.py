dic = {'key':'value','key1':'value2'}
import json
ret = json.dumps(dic)
print(ret,type(ret)) #序列化
res = json.loads(ret) #反序列化
print(res,type(res))

dic = {1:[1,23]}
res = json.dumps(dic)
print(res,type(res))
con = json.loads(res)
print(con,type(con))
import json
dict = {'key1':'value1','down':'value2'}
# ret = json.dumps(dict)
# with open('json_file','a') as f:
#     f.write(ret)
# with open('json_file','r') as f:
#     str_read = f.read()
# res = json.loads(str_read)
# print(res.keys())

# #dump load
# with open('json_file','a') as f:
#     json.dump(dict,f)
# with open('json_file','r') as f:
#     res = json.load(f)
# print(res.keys())
pe = {'key1':'value1','down':'value2'}
with open('json_file','a') as f:
    str_file = json.dumps(pe)
    f.write(str_file + '\n')
    str_file = json.dumps(pe)
    f.write(str_file + '\n')
    str_file = json.dumps(pe)
    f.write(str_file + '\n')
with open('json_file','r') as f:
    for line in f:
        res = json.loads(line.strip())
        print(res.keys())
print(res.keys())

import pickle
data = ['aa', 'bb', 'cc']
# dumps 将数据通过特殊的形式转换为只有python语言认识的字符串
p_str = pickle.dumps(data)
print(p_str)