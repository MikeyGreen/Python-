def fs(n):
    return n * n
a = fs(3)
print(a)
b = lambda n : n * n
ret = b(3)
print(ret)

x = lambda a ,b : a + b
def co(x,y):
    return x ,y
print(co(2,5))
x = lambda a,b : (a,b)
print(x(1,2))
x = lambda a,b:(a,111)
print(x(2,12))
two = lambda a,b : 2,4  #这是两部分
print(two) #(<function <lambda> at 0x00915D20>, 4)
#返回最大值
fn = lambda x,y : max(x,y)
print(fn(1,2))
#多个数比较时
fn = lambda *args : max(args)
print(fn(234,42,31,32,42,4,534,423,12))

