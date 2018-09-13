print("hello")
#raw_input 在python3中取消了
file = open("Python_leaner.txt","w")
file.write("something\ni like learn \n python")
file.close()
#生成式
a = {x**2 for  x  in [1,3,4,5,6]}
print(a)
b = set([1,2,3,5])
#hash()和对象内容有关，和id内存地址有关
class test:
	def __init__(self,i):
		self.i = i
for i in range(10):
	a = test(i)
	print(hash(a),id(a))
#bool类型
print(type(True))
print(isinstance(45,int))
L=M=[1,2,4] #最好不要用共享引用
L = L + [5,6,7] 
print(L,M)
x = y = [11,22,33,44,55]
print(x,y)
x += [66,77,88,99] #增强赋值会在原处改变
print(x,y)
#字符串操作
s1 = ""
s2 = "123"
print(s1 + s2,s2*3,s2[1],s2[2:4],len(s2))
#字符串格式化方法
print("arrot is {1} {0}".format("someting","a"))
sentence = "hello ,Pyhton"
#字符串迭代
for x in sentence:
	print(x,end = "")
print("\n")
#字符串列表迭代
print([x * 2 for x in s2])
",".join(["a",'b','c'])
print(",".join(["a","b","c"]))
print("**".join(["a","b","c"]))
object = "the world is beatiful"
controvert = object.swapcase()#大小写互换
print(controvert)
print(controvert.swapcase())
print(controvert.capitalize()) #首字母大写
print(controvert.title())  #every word is title 每个单词首字母都大写
print(object.startswith("the"))
print(object.isalnum())
print(object.isalpha())
char = "noblank"
print(char.isalnum())
print(char.isalpha())
print(char.isupper())
print(char.islower())
manna = '''hello world 
this is dalily note
 of Python '''
print(manna)
#字符和ASCII码转换 ord(char),chr(num)
a = ord("Z")
print(a)
b = chr(116)
print(b)
print(int("00100101",2)) #将字符串作为二进制转换
print(int("00000010",8))#将字符串作为8进制转换成十进制
#字符串链接
name = "wang""hong" #单行
print(name)
#多行字符串链接
name = "wang\
hong"
print(name)
#字符串调用,基于位置的调用，基于key的调用
print("{0} and {momo}".format("read",momo = "someting"))
#基于字典的调用
print("%(one)d and %(two)d"%{"one":123,"two":345})
word = "hello world someone"
print(word.rjust(30))#共30个字符，右对齐
print(word.rjust(len(word))) #左对齐
print(word.ljust(30),word.rjust(30))
L= list("spam") #列表初始化
print(L) 
print(list(range(10)))
print(list(map(ord,"spam")))
L = ["a","b","c","a"]
print(L.count("a")) #查看列表中a的个数
list = [1,2,3,4,5]
print(list.append(6))
print("over")

a = []
a += [1]
print(a)
a2 = a + [2]
print(a2,a)
