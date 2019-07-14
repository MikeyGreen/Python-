#过滤掉长度小于3的字符串列表，并将剩下的字符串首字母大写
lst = ["hahahha",'something','java','QQ']
new = [a.capitalize() for a in lst if len(a)>= 3]
print(new)
#求（x,y）其中x是0-5之间的偶数，y是0-5之间的奇数组成的元祖列表
tu = [(x,y) for x in range(5) for y in range(5) if x % 2 == 0 and y % 2 == 1]
print(tu)
co = ["中国",'华为','小米','vivo']
new = [(v + str(k)) for k,v in enumerate(co)]
print(new)

a = 10
print(callable(a)) #False
def a():
    pass
print(callable(a)) #True
#查看二进制
print(bin(3))
print(bin(2))
print(oct(9)) #八进制
print(hex(16)) #16进制
print("ha\thb") #制表符
print("ha   hb")

print(format(12345,'e')) #科学计数法
print(format(1.2345,'0.10f')) #小数点后保留10位不足补0
print(format(1.23456,'0.2f')) #小数点后保留两位
print(format(1.23456e+10,'0.1F')) # 12345600000.0
print(format(1.23456e+10000,'F')) #INF 代表无穷大
print(all((1,True,2))) #True
print(all((1,True,0))) #False

ls1 = ["china",'japan','canada']
ls2 = ['beijing','dongjing','wotaihua']
ls3 = [1000,500,200]
s = zip(ls1,ls2,ls3)
print(s) #<zip object at 0x03816058>
for el in s:
    print(el)
#repr返回一个对象的string模式
s = repr("权利\n的游戏")
print(s) #'权利\n的游戏'
t = r"哈喽\t小明"
print(t) #哈喽\t小明
#exec()测试代码
exec("a = 10")
print(a)
exec("r = 20")
print(r)
s = "for i in range(10): print(i * 2)"
c = compile(s,"","exec") #编译
print(c)
exec(c) #执行

str = "3 *4 +5"
r = compile(str,"","eval")
s = eval(r)
print(s) #17



