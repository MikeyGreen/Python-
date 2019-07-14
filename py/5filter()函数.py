#filter函数
#语法 filter(list,函数 True or False) #过滤掉False,保留True
def fu(el):
    if el % 2 == 0 :
        return False
    else:
        return True
lst = [1,2,3,4,5,6]
s =filter(fu,lst)
print(s)
print("__iter__" in dir(s)) # True 可迭代

for i in s:
    print(i)

e = filter(lambda el : el % 2 == 1,lst) #过滤掉偶数
for i in e:
    print(i)

