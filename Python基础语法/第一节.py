#Python是一种动态语言
a = "hello world"
b = a
a = 123
print("b = ",b)


#列表创建，访问，删除，更新
list = [1,2,3,4,5,6,"son"]
print(list[2:4])
print(list[2]) # list[index]
del list[1]
print(list)


# set会过滤重复的元素
set1 = {1,2,3,4,523,42,23,32,23}


#列表创建，访问，删除，更新
list = [1,2,3,4,5,6,"son"]
print(list[2:4])
print(list[2]) # list[index]
list.append("water")
print(list)


#set添加元素,set过滤重复元素
set1 = {1,2,3,3,4,4}
print(set1)
set1.add("over")
print(set1)


# set删除元素
set1.remove("over")
print(set1)


# if条件语句多个条件语句
java = 55
python = 89
if java > 60 and python > 70:
    print("都合格")
elif java > 60 :
    print("java合格")
elif python > 70:
    print("python合格")
else:
    print("都不合格")


# 打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("{0}*{1}={2}\t".format(i,j,i*j),end = "") # 字符串末尾带换行符结尾，end = "" 表示在字符串末尾用空字符串代替换行符。 \t水平制表符，一个tab的间隔
    print("\n")
print("someting")
print("over")


# 判断是否是闰年



def sum(num1,num2):
    if not (isinstance(num1,(float,int)) and  isinstance(num2,(float,int))):
        raise TypeError
    return num1 + num2
print(sum(3,5)) #print(sum("2" ,5))


# 函数返回多值
def conversion(num1,num2):
    a = num1 + num2
    b = num1 - num2
    return a,b
m = conversion(6,3)
print(m)

_no_value = object()
def print_info(a, b = _no_value):
    if b is _no_value:
        print("没有赋值")
    return
print_info(5)
print("="*20)
print_info(3,5)

#关键字参数,用变量名，不用在乎顺序
def print_info(name,age,sex = "男"):
    print("{}".format(name))
    print("{}".format(age))
    print("{}".format(sex))
    return
print_info(age = 23,name = "Joe")


# 不定长参数 *argv
def print_info(name,age,*hobby):
    print("{}".format(name))
    print("{}".format(age))
    print("{}".format(hobby))
    return
print_info(23, "Joe","sing","kick","basketball")

# 不定长参数 **argv
def print_info(name,age,**hobby):
    print("{}".format(name))
    print("{}".format(age))
    print("{}".format(hobby))
    return
print_info(age = 23,name = "ruo",hobby = ("篮球","basketball"))

# isinstance(object,type)
print(isinstance(34,int)) # True
b = "Hello World"
print(id(b))
help(id)
# 判断类型
a,b,c,d = 123,True,1.223424,6.23 + 5j
print(type(a),type(b),type(c),type(d))
print(isinstance(a,int),isinstance(b, str),isinstance(c,(float,int)),\
isinstance(d,complex))

# 真正的除法
print(7/3)

# 切片
a = " Hello World"
print(a[-1])
print(a[:-1])
print(a[:])
print(a[::1])
# 美化字符串
print("hello worl\t\td")
print("Python\'format is good")
print("this {language} is {description}".format(language = "Python",description = "awsome"))

s = "a\tb\tc\td\te"
l = s.split()
print(l)
print("*".join(l))
line = "\tsmall\thello\t\n"
print(line.strip())
print(line.lstrip())
print(line.rstrip())


# 字符串内不可改变
sen = "srting"
print(type(sen))
#sen[1] = "o"
print(sen)


hot = True
summer = True
conditioning = 1
if hot & summer:
    conditioning = 12
print(conditioning)

#三元表达式
a,b = 3,4
max = a if a > b else b
print(max)

# 字符串，元组，列表创建迭代对象
# iter(),next()
# for循环遍历迭代对象，next()遍历
list = [1,2,3,4,5,6]
iter1 = iter(list)
for i in iter1:
    print(i,end = " ")
print("\n--------------------------")


# enumerate同步遍历索引和value
list = ["fs","ok","some"]
for index,value in enumerate(list):
    print(index,value)

# for -else
for i in range(5):
    print(i)
else:
    print("index finished")

iteror = iter([1,2,3,4])
while True:
    try:
        print(next(iteror))
    except StopIteration:
        break
# extend添加列表
list = [1,2,3,4,5]
list.extend([7,8,9,10]) # 添加到list本身，而不需要再另赋值其他列表名
print(list)
print(list[::-1])
print(type(list.reverse()))
list.reverse()
print(list)
print(list * 2)
print(list + list)

# 排序 M.sort() or sorted(M)
M = [23,5,3,4,12,21,0]
M.sort()
print(M)
print("--------------------")
M.reverse()
print(M)
print(sorted(M))

# 判断某个元素是否在列表中
list = ["I","think","av","is","bad","to","human"]
if "think" in list:
    print("Okay")


