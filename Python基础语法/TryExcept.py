def function(x,y,food = "spam"):
	print(food)
function(3,5,"egg")
function(1,3)
print("="*12)
def tuple_num(fist,*arg):
	print(fist)
	print("*"*len("123456"))
	print(arg)
	return
tuple_num(1,2,3,4,5)

def tuple_num(fist,*arg):
	print(fist)
	print("*"*len("123456"))
	print(arg)
	return
tuple_num(1,2,3,4,5)

def tuple_num(fist,*arg):
	print(fist)
	print("*"*len("123456"))
	print(arg)
	return
tuple_num(1,2,3,4,5)

#**kwargs将等式返回为字典
def dic(x,y=3,*args,**kwargs):
	print(y)
	print(x,y,args,kwargs)
dic(1,4,4,5,6,7,a = 5,b = 6)
print("%"*35)
dic(1,4,4,5,6,7,a = 5,b = 6)

#元组拆包
a,b,c = ("zhangtao",True,123)
print(a)
print(b)
print(c)
a,b = b,a
print(a,b)
#元组拆包，获取其他变量遗留得值
a,b,*c,d = (1,2,3,4,5,6,7,8)
print(a)
print("="*12)
print(b)
print("\n *************")
print(c)
print("\n**************")
print(d)
#列表拆包,列表和元组一样
a,b,*c,d = [1,2,3,4,5,6,7,8]
print(a)
print("="*12)
print(b)
print("*************")
print(c)
print("**************")
print(d)

#条件表达式，又叫三元表达式
print("条件表达式，又叫三元表达式")
a = 7
b = True if a >= 4 else 43
print(b)
#instance2
a = 0
b = 23 if a == True  else 43 #此处 a == False
print(b)

#for instance3
#当条件为True时，返回前面得，否则返回后面的值
staus = 1 
msg = "login" if staus == 1 else "logout"
print(msg)

# try except else
try:
	print(1/0)
except ZeroDivisionError:
	print(4)
else:
	print(5)
print("$"*10)
try :
	print(4)
except ZeroDivisionError:
	print("ZeroDivisionError")
else:
	print("No error happenning")

print("*"*12)
try:
	print(3)
	print(1 + "4" == 5)
	print(5)
except TypeError:
	print(89)
else:         #只要except执行，else就不执行
	print(55)

def function():
	print("this is a function")
if __name__ == "__main__":
	print("this is script")
def function():
    print("This is a module function")
if __name__=="__main__":
    print("This is a script")\
