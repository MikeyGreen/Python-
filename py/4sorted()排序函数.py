lst = [1,2,42,43,32,54,32,122,3211,423]
lst.sort()
print(lst)
#内置函数排序
lst = [1,2,42,43,32,54,32,122,3211,423]
s = sorted(lst)
print(s)
#sorted条件排序
l2 = ["china",'Canada','America','Japan']
def fo(el):
    return len(el)
#按照key的值大小排序
t = sorted(l2,key=fo,reverse= True) #reverse默认为False,False为正序，True为倒序
print(t)

lst = [
    {"name":"smith","age":25},
{"name":"jack","age":22},
{"name":"kra","age":45},
{"name":"smi","age":55},
]
def fu(el):
    return el["age"]
s =sorted(lst,key = fu,reverse = False)
print(s)