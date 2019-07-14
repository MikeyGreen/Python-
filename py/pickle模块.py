import pickle
dic = {(1,2,3):"number",1:"one"}
ret = pickle.dumps(dic) #转换成python能认识的字节
print(ret)
s = pickle.loads(ret)
print(s) #形式不变
#dump
with open('pickle_file','wb') as f:
	pickle.dump(dic,f)
	pickle.dump(dic,f)
	pickle.dump(dic,f)
with open('pickle_file','rb') as f:
	res = pickle.load(f)
	print(res,type(res)) #逐行读取
	res = pickle.load(f)
	print(res)
	res = pickle.load(f)
	print(res)

import os
print(help(os))
