dic = {1:"first",2:"second"}
print(dic.get(1))
print(dic.get("没有","没找到"))
print(11 // 2)

#递归阶乘
def plus(n):
    if n == 1:
        return 1
    return n * plus(n-1)
s = plus(4)
print(s)
#斐波拉切数列
def feibolaqie(n):
    if n == 1:
        return 1
    elif n == 2:
        return   1
    else:
        return feibolaqie(n-1) + feibolaqie(n-2)
print(feibolaqie(5))
print(feibolaqie(6))

