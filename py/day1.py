# print(1+1,1*2,10/3,10//3,10%3)
# #str
# print('马云')
# #多行字符串
# print('''窗前明月光，
# 疑是地上霜''')
# print('马化腾'*10)
# print('hello'+'world')
# #交互式
# content = input('你吃了吗')
# print('我们在控制台收到了',content)
# #两次输出的加到一起
# a = input('请输入a')  #input输入并付给变量a的值是字符串
# b = input('请输入b')
# print(a+b)    #打印字符串叠加后的结果
# print(int(a)+ int(b)) #将字符串转换成数值类型，然后相加，前提输入的是数字
#
# content = input('输入内容')
# if content == "是":
#     print('走向人生的巅峰')
#     print('先买他20栋房子')
# else:
#     print('继续过着屌丝生活')
# print('我要死')
# money = 88
# if money > 50:
#     print('打车回家')
# else:
#     print('走回去')
# print('有钱真好')

# wonderful = int(input("请输入数字"))
# if wonderful > 80:
#     print("大了")
# elif wonderful < 60:
#     print('小了')
# else:
#     print('合适了')

# age = int(input("请输入您的年龄："))
# if age < 10:
#     print("小屁孩")
# elif age >=10 and age < 20:
#     print("青春叛逆的小屁孩")
# elif age >=20 and age < 30:
#     print("开始定性，开始混社会的小屁孩")
# elif age >=30 and age<40:
#     print("看老大不小了，赶紧结婚小屁孩儿")
# elif age>=40 and age<50:
#     print("家里有个不听话的小屁孩儿")
# elif age>=50 and age<60:
#     print("马上变成不听话的老屁孩")
# elif age >=60 and age<70:
#     print("活着还不错的老屁孩儿")
# elif age>=70 and age<90:
#     print("人生快要结束的老屁孩儿")
# else:
#     print("再见了这个世界")

# # while循环
# while True:
#     print("一直输出，不停")
#     print("继续，嗨起来")
# n = 1
# while 1: #此处为非零数代表条件为True,因为True == 1 and False == 0
#     print("执行{}次".format(n)) #此处为格式化输出
#     n += 1
#     continue
#     print("前面有continue,所以此处不执行，此处为废话")
# # 采用break跳出循环，终止循环
# while 2:
#     print("执行一次")
#     break

# print(True == 1)
# print(False == 0)

'''python
1、使⽤while循环输出 1 2 3 4 5 6 8 9 10
2、求1-100的所有数的和
3、输出 1-100 内的所有奇数
4、输出 1-100 内的所有偶数
5、求1-2+3-4+5 ... 99的所有数的和
6、⽤户登陆（三次机会重试）
'''
# i = 0
# while i < 10:
#     i += 1
#     print("当前i={}".format(i))
#
# i = 0
# sum = 0
# while i < 100:
#     i += 1
#     sum += i
# print("1-100的所有数的和{}".format(sum))
#
# i = 1
# sum = 0
# while i < 100 :
#
#     sum += i
#     i += 2
# print("1-100的所有奇数的和{}".format(sum))

# i= 1
# sum = 0
# while i < 100:
#     if i % 2 ==0:
#         sum += -i
#     else:
#         sum += i
#     print(sum)
#     i += 1
# i = 0
# while i < 3:
#     a = input("请输入用户名")
#     b = input("请输入密码")
#     if a == "张三" and b =="1314rt":
#         print("登陆成功")
#         break
#     else:
#         print("登录失败，请重新输入密码或者用户名")
#     i += 1
# else:
#     print("超过次数，您的账户已被锁定")

#用户输入一段内容并打印，直到用户输入q的时候退出程序
# while True:
#     content = input("input your something you want to write(you can use q to turn down it):")
#     if content == "q":
#         print("game is over")
#         break #打断，终止本次循环
#     else:
#         print(content)
#
#也可以用bool布尔值控制是否跳出循环
# flag = True
# while flag:
#     content = input("say something or you can use 'q' to shutdown it")
#     if content == 'q':
#         print('用flag控制跳出循环')
#         flag = False             # 和break语句不同的是，下面语句仍要执行，只是下一循环 while条件变成false,从而无法执行
#     print("你输入的内容是：",content)

# count = 1
# while count < 10:
#     print(count)
#     if count == 5:
#         break       # break语句发生生时，就不会出发下面的else语句，
#     count += 1      #while esle相当于 if else，while else 死一个整体，而break语句是跳出while循环
# else:
#     print('game over')
# # 去掉break语句
# count = 1
# while count < 10:
#     print(count)
#     if count == 5:
#         pass       # pass是什么也不执行，路过就行。如果还不知道写什么代码，用pass占位
#     count += 1      #while esle相当于 if else，while else 死一个整体，而break语句是跳出while循环
# else:
#     print('count数超过10了') #当没有break语句时，while循环条件不满足时，然后执行else循环

# #逻辑运算符
# # （）优先 其次not，然后and，最后or ,相同运算符，从左往右，() > not > and > or
# print(1>5 or 4<6 and 4 < 3 ) # False    and > or
# print(1>5 or 4>3 and not 4>6) # not > and > or
# print(1>2 and 4<6 or 8<9 and 2<3 or 7<6) # 先算and，再简化为f or t or f
# #x or y 当x为零时，返回y,当x非零时，返回x\
# print(1 or 2)
# print(1 or 0)
# print(0 or 3)
# print(0 or 0)
# print(0 or 1 or 3 or 5)
# print(0 or 1 or 3 or 0)
# print(4 or 0 or 1 or 0 or 2)
# # and与or相反，不要总结and，记住or就可以了
# print(0 or 1 and 6) #先算and ,回忆or 和and 相反，1 or 6 为1 那么 and 相反，1 and 6 为6 ， 0 or 6 要后面的
# print(1 and 2 or 3) # 2
# print(1 and 0 or 3) # 3
# print(0 and 5 or 6) # 6
# print(0 and 5 or 6 and 2) # 2
# # false:0 , True : 1
# print(1 and False)
# print(1 or False)
# print(0 or False)
# print(False and 5)
# print(False or 6)
# print(1>2 or 0 and 3<6 or 5) #先计算and，0 and True == 0 ,然后计算or，fasle or 0 or 5 ,答案是5
# print(not(1>2 or 0 and 3<6 or 5))
# print(not(2))
# print(False or True)
# print(True or 3)
# print(True and 3)


# content = input("输入你要查询的内容：")
# if "操" in content:
#     print("查询的内容涉及违法、色情、暴力倾向，请立即停止")
# else:
#     print(content)
# print("%s,你好"%("小明")) #小明，你好
#变量
# a = "小明"
# print("%s,你好"%(a))
# #数字
# print("今年人均年收入是%d万元"%(6))
# #format
# print("{}和{}是好朋友".format("小明","小刚"))
# print("{0}和{1}是好朋友".format("小明","小刚")) #从0开始，数字对应format里面内容的顺序
# print("{1}和{0}是好朋友".format("小明","小刚")) #调换的输出顺序
# print("{1}和{2}是好朋友".format("小明","小刚",'小王'))
# a =1 #二进制是1
# b =3 #二进制11
# c =4 #二进制100
# print(a.bit_length(),b.bit_length(),c.bit_length())
# a = 10
# print(bool(a))
# b = "hahaha" #字符串的布尔值是True
# print(bool(a))
# c = ""
# print(bool(c)) # 空字符串的布尔值是False,此处可联想if条件
# if "" :
#     print("空字符串条件为True")
# else:
#     print("空字符串条件为Fasle")
# #空列表
# lst = []
# print(bool(lst))
# #空元组
# tl = ()
# print(bool(tl))
# #空字典
# dic = {}
# print(bool(dic))
# a = None   # 空，真空，表示什么都不是，什么都没有
# print(bool(a))
#总结，所有空的bool值为False,所有非空为True

#列表转换成元组
# lst = [1,23,45]
# print(type(lst))
# tu = tuple(lst)
# print(type(tu))

# #索引
# s = "野人对琼恩雪诺说：you know nothing"
# print(s[0],s[1],s[2],s[3])
# print(s.index(" "))  #表示第一个空格出现的索引位置
# print(s[-1],s[-2],s[-3])
# print(s[0:4]) #从零开始，顾头不顾尾
# print(s[:6])
# print(s[2:])
# print(s[-3:-6]) #这样写没有输出结果，所以索引值只能从左往右输出
# print(s[-12:-1]) #顾头不顾尾，-1索引位置不打印
# print(s[-12:])
# print(s[:])
# print(s[::2]) #步长为2
# print(s[:10:3])
# print(s[-1:-5:-1]) #倒着输出gnih     正着数还是倒着数要看步长的符号
# print(s[-1:-5]) #打不出来
# print(s[-5::1]) #正着输出 thing
# d = "0123456"
# print(d[::2])
# 起始位置为负值时，索引值从-1开始，和正着数不一样，正着数是从零开始
# content = "laO wang is a gay"
# #字符串的操作都是在复制的基础上进行操作，原字符串不变
# #首字母变大写
# print(content.capitalize())
# #所有字母变大写
# print(content.upper())
# #所有字母变小写
# print(content.lower())
# #大小写互相转换
# print(content.swapcase())
# #title把每个单词的首字母变大写
# print(content.title())
# s1 = "jo_hn is a boy"
# print(s1.title()) #把不属于英文字母的都看成是分割符，然后把每个分割开的单词都看成独立单词 Jo_Hn Is A Boy
# #居中
# p = "提莫"
# print(p.center(10)) #拉长10个字符
# print(p.center(10, "*")) #强行用*补齐空白位置
# #strip()去掉首尾空格 必须记住
# s = "  lao wang is a gay  "
# print(s)
# print(s.strip())
# print(len(s),len(s.strip()))
# #有时候用户输入密码或者用户名带空格，导致登陆失败，这时候需要去除空格
# User_name = input("请输入用户名：").strip()
# User_code = input("请输入密码：").strip()
# if User_name == "laowang" and User_code == "1234":
#     print("登陆成功")
# else:
#     print("登录失败")
# #strip()括号内指定内容时，删除指定内容
# s = "sb lao wang is a gay sb"
# print(s.strip("sb"))
# #替换字符串内容
# film = "速度与激情，黑客帝国，小猪佩奇，瑞克和莫迪"
# print(film.replace("黑客帝国","权力的游戏")) #把前面的替换 ==>速度与激情，权力的游戏，小猪佩奇，瑞克和莫迪
# print(film.replace("佩奇",'阿根')) #部分替换 ==>速度与激情，黑客帝国，小猪阿根，瑞克和莫迪

# s = "john_wow_of_happy_jason"
# print(s.replace("_","")) #把_用空符串取缔省略掉
# print(s.replace("o","0",2)) #替换两次，指定替换的个数
# #分割
# print(s.split("_")) #列表形式 用_去切，切什么少什么
# #切换行符
# s1 = """床前明月光，
# 疑是地上霜。
# 举头望明月，
# 低头思故乡。"""
# content = s1.split("\n")
# print(content)
# s2 = "今天下午打篮球"
# a = s2.split("今天下午打篮球") #整条切割，只剩下两边的空字符串
# print(a)
# print(type(a))
# lst = a
# print(bool(a)) # 结果为True，可见列表不是空列表。

# #格式化输出
# a = "我叫%s,今年%d，我喜欢%s"
# print(a%("老王",30,"撸代码"))
# a = "我叫{},今年{}，我喜欢{}"
# print(a.format("老王",30,"撸代码"))
# a = "我叫{2},今年{1}，我喜欢{0}"
# print(a.format("老王",30,"撸代码"))
# a = "我叫{name},今年{age}，我喜欢{hobby}"
# print(a.format(name = "老张",age = 18,hobby = "刷美剧"))

#startwith and endwith 以...开头，以...结尾
# s = "老王是一个怪胎"
# print(s.startswith("老王"))
# print(s.endswith("胎"))
# print(s.endswith("台"))
# # count查看字母或单词出现的次数
# s = "I am mad verry much,I want to kill somebody"
# print(s.count("a"))  #查询出现a字母的次数
# print((s.count("z"))) #查询出现z字母的次数
# print(s.count("much")) #查询出现much单词的次数
# print("------------------------------------------")
# # find查看索引位置
# # s = "I am mad verry much,I want to kill somebody"
# print(s.find("a")) #第一次出现a的索引位置，2
# print(s.find("mad")) #第6个字母，对应索引是5
# print(s.find("hello")) #d当找不到内容时，返回-1
# print(s.inddex("hello")) #index也是查找索引，和find相同，区别在于index找不到内容时会报错


# a = "1234"
# print(a.isdigit())#判断是否是整数
# print(a.isalpha()) #判断是否是字母
# b = "abcd123"
# print(b.isalpha(),b.isdigit()) #字母数字混合的都不符合判断，为false
# print(b.isalnum()) #判断是否包含数字或者字母，是前两个的综合体
#
# #识别中文的数字
# c = "壹万贰仟叁佰肆拾柒六三二一"
# print(c.isnumeric()) #可用于财务上，可以识别发票、财务上的中文数字

#判断一个字符串是否是数字
#        -3.21454
# s = "-3.21454"
# s1 = s.replace("-","")
# print(s1)
# if s1.isdigit():
#     print("是整数")
# else:
#     if s1.count(".") == 1 and not s1.startswith(".") and not s1.endswith("."): # 或者换成s1.count(".")==1 and "." in s1[1:-2]
#         print("是小数")
#     else:
#         print("不是小数")
#
# # 计算字符串的长度
# s1 = "权力的游戏"
# print(len(s1))
# print(type(len)) #内置函数 更多内置函数可看官网文档：https://docs.python.org/3/library/functions.html
#
# #字符串迭代
# s = "权力的游戏第八季4月14日开始"
# n = 0
# while n < len(s):
#     print(s[n]) # n是索引，从零开始到len(s)-1
#     n += 1
# #第二种迭代方法
# for c in s:
#     print(c) #for不用索引
#
# c = "312342564"
# print(c.isdecimal()) # 是否只包含十进制数 True
# b ="3.2152425"
# print(b.isdecimal()) #False

# # for 循环也可以存在else ，表示执行完for循环后，执行else里面的语句
# s = "123456"
# for c in s:
#     print(c)
# else:
#     print("game over")
# # 计算字符串中数字的个数
# count = 0
# s = "i am 12 years old , i am 175cn"
# for c in s:
#     if c.isdigit():
#         count += 1
# print(count)

# #移除name变量两边的空格
# name = " aleX leNb  "
# print(name.lstrip())
# #移除name变量坐标的al
# name = "alex lenb"
# print(name.lstrip("al"))
# #移除右边的nb
# print(name.rstrip("nb"))
# #将a和b字符去除
# print(name.strip("a").strip("b"))
# #倒计时
# s = "321"
# for c in s:
#     print("倒计时%s秒"%c)
# else:
#     print("出发")
#
# #多个数数相加计算器 1+2+3+4+10.....
# content = input("输入加法运算式")
# s1 = content.replace(" ","")
# lst = s1.split("+")
# sum = 0
# for l1 in lst:
#     sum = sum + int(l1)
# print(sum)
#
# #计算用户输入的有多少个整数
# content = input("请输入")
# count = 0
# for c in content:
#     if c.isdigit():
#         count += 1
# else:
#     print(count)
# #首字母大写
# print(name.capitalize())
# print(name.upper())
# #判断是否是以nb结尾
# print(name.endswith("nb"))
# #根据I分割
# name = "alexl nalex"
# print(name.split("l"))
# #根据第一个i分割
# print(name.split("l",1))
# #查找是否有N及索引
# print(name.index("n"))
# print(name.find("n"))
# #查找"l na"的索引
# print(name.find("l na"))
# #输出前三个字符
# print(name[:3]) #顾头不顾尾
# #输出后两个字符
# print(name[-2:])
# #例题
# choice = input("请出入A、B、C：（A代表大路，B小路，C代表绕路）")
# if choice == "A":
#     print("大路回家")
#     choice2 = input("公交车or步行")
#     if choice2 == "公交车":
#         print("10分钟到家")
#
#     if choice2 == "步行":
#         print("20分钟到家")
#
# if choice == "B":
#     print("沿小路回家")
#
# if choice == "C":
#     print("绕道回家")
#     flag = True
#     while flag:
#         choice3 = input("去网吧还是游戏厅")
#         if choice3 == "游戏厅":
#             print("一个半小时在家，爸爸在家等你")
#             flag = True
#         elif choice3 == "网吧":
#             print("两个半小时到家，妈妈已经做好战斗准备")
#             flag = True
#         else:
#             flag = False
#
# #另外一种方法
# while True:
#     choice = input("A,B,C")
#     if choice == "A":
#         print("大路回家")
#         traffic = input("公交车还是步行")
#         if traffic == "公交车":
#             print("10分钟到家")
#             #break
#         elif traffic == "步行":
#             print("20分钟到家")
#             #break
#         else:
#             print("在考虑吧")
#             #break
#         break     # break也可以放在里面if中，但是每个都要放
#     elif choice == "B":
#         print("小路回家")
#         break
#     elif choice == "C":
#         print("绕道回家")
#         place = input("网吧还是游戏厅")
#         if place == "网吧":
#             print("爸爸在家拿棍子等你")
#
#         elif place == "游戏厅":
#             print("妈妈在家等你")
#
#         else:
#             print("直接回家")
#             break
#     else:
#         print("不回家")

# 从1加到100不包括88
# i = 0
# sum = 0
# while i < 100:
#     i += 1
#     if i == 88:
#         continue
#     else:
#         sum += i
# else:
#     print(sum)
#======================================================
# #1-2+3-4.....+99 不包括88
# count = 1
# sum = 0
# while count<=99:
#     if count == 88:
#         count += 1   #此处必须写，否则无法跳出count=88
#         continue     #下面的语句不再执行，调到下一循环
#     if count % 2 == 1:
#         sum = sum + count
#     if count %2 ==0:
#         sum = sum - count
#     count += 1
# else:
#     print(sum)
#=================================
# # 判断大写，小写，数字 的数量
# name = input("输入点什么")
# shuzi = 0
# xiaoxie = 0
# daxie = 0
# other = 0
# for c in name:
#     if c.isdigit():
#         shuzi += 1
#     elif c.isupper():
#         daxie += 1
#     elif c.islower():
#         xiaoxie += 1
#     else:
#         other += 1
# print("大写%d小写%d数字%d其他%d"%(daxie,xiaoxie,shuzi,other))

# name = """赵钱孙李，周吴郑王。
# 冯陈褚卫，蒋沈韩杨。
# 朱秦尤许，何吕施张。
# 孔曹严华，金魏陶姜。
# 戚谢邹喻，柏水窦章。
# 云苏潘葛，奚范彭郎。
# 鲁韦昌马，苗凤花方。
# 俞任袁柳，酆鲍史唐。
# 费廉岑薛，雷贺倪汤。
# 滕殷罗毕，郝邬安常。
# 乐于时傅，皮卞齐康。
# 伍余元卜，顾孟平黄。
# 和穆萧尹，姚邵湛汪。
# 祁毛禹狄，米贝明臧。
# 计伏成戴，谈宋茅庞。
# 熊纪舒屈，项祝董梁。
# 杜阮蓝闵，席季麻强。
# 贾路娄危，江童颜郭。
# 梅盛林刁，钟徐邱骆。
# 高夏蔡田，樊胡凌霍。
# 虞万支柯，昝管卢莫。
# 经房裘缪，干解应宗。
# 丁宣贲邓，郁单杭洪。
# 包诸左石，崔吉钮龚。
# 程嵇邢滑，裴陆荣翁。
# 荀羊於惠，甄曲家封。
# 芮羿储靳，汲邴糜松。
# 井段富巫，乌焦巴弓。
# 牧隗山谷，车侯宓蓬。
# 全郗班仰，秋仲伊宫。
# 宁仇栾暴，甘钭厉戎。
# 祖武符刘，景詹束龙。
# 叶幸司韶，郜黎蓟薄。
# 印宿白怀，蒲邰从鄂。
# 索咸籍赖，卓蔺屠蒙。
# 池乔阴鬱，胥能苍双。
# 闻莘党翟，谭贡劳逄。
# 姬申扶堵，冉宰郦雍。
# 卻璩桑桂，濮牛寿通。
# 边扈燕冀，郏浦尚农。
# 温别庄晏，柴瞿阎充。
# 慕连茹习，宦艾鱼容。
# 向古易慎，戈廖庾终。
# 暨居衡步，都耿满弘。
# 匡国文寇，广禄阙东。
# 欧殳沃利，蔚越夔隆。
# 师巩厍聂，晁勾敖融。
# 冷訾辛阚，那简饶空。
# 曾毋沙乜，养鞠须丰。
# 巢关蒯相，查后荆红。
# 游竺权逯，盖益桓公。
# 万俟司马，上官欧阳。
# 夏侯诸葛，闻人东方。
# 赫连皇甫，尉迟公羊。
# 澹台公冶，宗政濮阳。
# 淳于单于，太叔申屠。
# 公孙仲孙，轩辕令狐。
# 钟离宇文，长孙慕容。
# 鲜于闾丘，司徒司空。
# 丌官司寇，仉督子车。
# 颛孙端木，巫马公西。
# 漆雕乐正，壤驷公良。
# 拓跋夹谷，宰父谷梁。
# 晋楚闫法，汝鄢涂钦。
# 段干百里，东郭南门。
# 呼延归海，羊舌微生。
# 岳帅缑亢，况郈有琴。
# 梁丘左丘，东门西门。
# 商牟佘佴，伯赏南宫。
# 墨哈谯笪，年爱阳佟。
# 第五言福，百家姓终。
# """
# content = input("输入你的名字") #答案有问题
# sum = ""
# for c  in content:
#     sum += c
#     if sum in name:
#         print("在")
#         break
# else:
#     print("不在")

# #列表里套列表
# lst = ["移动硬盘",'手机','电脑',['U盘','音响'],'键盘','耳机','主机']
# #索引也有切片和索引,索引也是从零开始
# print(lst[2])
# print(lst[2][1]) #脑
# print(lst[-2]) #电脑
# print(lst[1:3])#手机，电脑 ---顾头不顾尾
# print(lst[-3:-1]) #['电脑', ['U盘', '音响']]
# print(lst[-3:]) #['电脑', ['U盘', '音响'], '键盘']
# print(lst[1::2])
# print(lst[-2:-7:-2])

# #列表的增加
# lst = ['提里昂','丹妮莉丝','琼恩雪诺','布兰','莫尔蒙']
# lst.append("夜王") #在原列表基础上添加
# print(lst) #['提里昂', '丹妮莉丝', '琼恩雪诺', '布兰', '莫尔蒙', '夜王']
# #在xxx位置插入yyy
# lst.insert(1,"小恶魔")
# print(lst)#['提里昂', '小恶魔', '丹妮莉丝', '琼恩雪诺', '布兰', '莫尔蒙', '夜王']
# lst.extend("麻花藤")
# print(lst) #迭代添加字符['提里昂', '小恶魔', '丹妮莉丝', '琼恩雪诺', '布兰', '莫尔蒙', '夜王', '麻', '花', '藤']
# lst = ['提里昂', '小恶魔', '丹妮莉丝', '琼恩雪诺', '布兰', '莫尔蒙', '夜王']
# lst.extend(["野人",'小指头','二丫']) #列表形式添加进去，才能和原列表拼在一起
# print(lst)
# #-------------------------------------------------------------------------------
# #列表删除
# lst = ['提里昂', '小恶魔', '丹妮莉丝', '琼恩雪诺', '布兰', '莫尔蒙', '夜王']
# a = lst.pop(2) #返回删除的内容
# print(a) #丹妮莉丝
# print(lst) #['提里昂', '小恶魔', '琼恩雪诺', '布兰', '莫尔蒙', '夜王']
# lst.remove('小恶魔')#删除指定元素
# print(lst) #['提里昂', '琼恩雪诺', '布兰', '莫尔蒙', '夜王']
# del lst[1] #删除'琼恩雪诺'
# print(lst) #['提里昂', '布兰', '莫尔蒙', '夜王']
# del lst[1:4] #不包括4，到3为止，删除 '布兰', '莫尔蒙', '夜王'
# print(lst) #['提里昂']
# lst.clear() #清空列表
# print(lst) #[]
# game = ["英雄联盟",'dota','魔兽世界','堡垒之夜','QQ飞车','地下城与勇士','绝地求生大逃杀']
# game[1] = "CF"
# print(game) #['英雄联盟', 'CF', '魔兽世界', '堡垒之夜', 'QQ飞车', '地下城与勇士', '绝地求生大逃杀']
# game[1:3] = "跑跑卡丁车"
# print(game) #['英雄联盟', '跑', '跑', '卡', '丁', '车', '堡垒之夜', 'QQ飞车', '地下城与勇士', '绝地求生大逃杀']
# game = game = ["英雄联盟",'dota','魔兽世界','堡垒之夜','QQ飞车','地下城与勇士','绝地求生大逃杀']
# game[1:3] = ["跑跑卡丁车"] #先删除后添加
# print(game) #['英雄联盟', '跑跑卡丁车', '堡垒之夜', 'QQ飞车', '地下城与勇士', '绝地求生大逃杀']
# game[1::2] = ["QQ华夏","QQ水浒","QQ三国"] #有三个为止需要改变，所以后面要跟三个元素的列表
# print(game) #['英雄联盟', 'QQ华夏', '堡垒之夜', 'QQ水浒', '地下城与勇士', 'QQ三国']

#==================================================================================================
# #列表元素循环
# game = ['英雄联盟', '跑跑卡丁车', '堡垒之夜', 'QQ飞车', '地下城与勇士', '绝地求生大逃杀']
# for element in game:
#     print(element,end = "   ")

#==============================================
# #列表嵌套
# kl = ["name","sex",'place',["height","weight",["kg","cm",1]],'work','company']
# print(kl[3][2]) #['kg', 'cm', 123]
# print(kl[3][2][2]) #1
# kl[3][2][2] = kl[3][2][2] + 99 #修改元素值
# print(kl[3][2][2])
# print(kl) #['name', 'sex', 'place', ['height', 'weight', ['kg', 'cm', 100]], 'work', 'company']
# kl[3][2][1] = 'hobby'
# print(kl[3][2][1] )
# print(kl) #['name', 'sex', 'place', ['height', 'weight', ['kg', 'hobby', 100]], 'work', 'company']
# kl[3][2][1] = kl[3][2][1].capitalize()
# print(kl[3][2][1] )
# print(kl) #['name', 'sex', 'place', ['height', 'weight', ['kg', 'Hobby', 100]], 'work', 'company']
# kl[3][0] = kl[3][0].upper()
# print(kl) #['name', 'sex', 'place', ['HEIGHT', 'weight', ['kg', 'Hobby', 100]], 'work', 'company']

#------------------------------------------------
# #count
# lst = ["小王",'老王','校长','小王']
# print(lst.count("小王")) #2
# #排序正序
# lst = [1,2,3,4,32,12,22,34,54,42]
# lst.sort() # 在列表基础上修改，不能赋值给变量
# print(lst) #[1, 2, 3, 4, 12, 22, 32, 34, 42, 54]
# #倒序
# lst.sort(reverse=True)
# print(lst)
# name = ["王者",'大师','白金','青铜','黄金','黑铁']
# name.reverse()#列表翻转
# print(name) #['黑铁', '黄金', '青铜', '白金', '大师', '王者']
# #列表长度
# print(len(name))#6
#============================================
# #元组
# tu = tuple() #空元组
# print(type(tu))
# print((3+4)*5)
# print((3))
# tu = (3)
# print(type(tu))
# tu2 = (3,) #元组中只有一个元素时，需要在元素后面加，
# print(type(tu2))
# #列表增删改都无法在元组使用，但索引切片可用
# tu3 = ('黑铁', '黄金', '青铜', '白金', '大师', '王者')
# print(tu3[1]) #黄金
# print(tu3[1:3])#('黄金', '青铜')
# print(tu3[::-1]) #('王者', '大师', '白金', '青铜', '黄金', '黑铁')
# #查询
# for e in tu3:
#     print(e,end = " ") #黑铁 黄金 青铜 白金 大师 王者
# print("\n")
# #元组不可变，元素里面的可变
# name = ("王力宏",'刘德华','张伟','刘亦菲',[1,2,3,"abc"])
# name[4][3] = "new"
# print(name) #('王力宏', '刘德华', '张伟', '刘亦菲', [1, 2, 3, 'new'])
# name[4].extend(["4",'something']) #('王力宏', '刘德华', '张伟', '刘亦菲', [1, 2, 3, 'new', '4', 'something'])
# print(name)
# star = ("王力宏",'刘德华','张伟','刘亦菲',[1,2,3,"abc"],("周杰伦",'蔡依林'))
# print(star[-1] ) # 元组里面的元组不可变，里面的列表元素可变，但列表本身不可变
#===========================
# #range 从零开始，顾头不顾尾
# print(list(range(10)))
# print(list(range(1,10)))
# print(list(range(1,10,3)))
# print(list(range(100,90,-2)))
# star = ("王力宏",'刘德华','张伟','刘亦菲',[1,2,3,"abc"],("周杰伦",'蔡依林'))
# # 打印索引和 元素值
# for index in range(len(star)):
#     print(index,end = " ")
#     print(star[index])

#=============================
# print(range(1,10))
# li = ['alex','Wusir','ritian','barry','wenzhou']
# print(len(li))
# li.append("seven")
# print(li)
# li.insert(1,'Tony')
# print(li)
# li[2] = "Kelly"
# print(li)
# li = ['alex','Wusir','ritian','barry','wenzhou']
# l2 = [1,'a',3,4,'heart']
# li = l2
# print(li)
# s = 'qwert'
# li = list(s)
# print(li)
# li = ['alex','Wusir','ritian','barry','wenzhou']
# li.pop(4)
# print(li)
# li = ['alex','Wusir','ritian','barry','wenzhou']
# li.remove("wenzhou")
# print(li)
# li = ['alex','Wusir','ritian','barry','wenzhou']
# del li[2:4]
# print(li)
# li = ['alex','Wusir','ritian','barry','wenzhou']
# li.reverse()
# print(li)
# print(li.count("alex"))

# li = [1,3,2,"a",4,'b',5,'c']
# print(li[:3])
# print(li[3:6])
# print(li[:7:2])
# print(li[1:7:2])
# print(li[-1]) #c
# print(list(li[-1])) #'c'
# print(li[-3::-2]) #或者li[-3:-8:-2]

# lis = [2,3,'k',['qwe',20,['k1',['tt',3,'1']],89],'ab','adv']
# lis[3][2][1][0] = lis[3][2][1][0].upper()
# print(lis)
# lis[3][2][1][0] = lis[3][2][1][0].replace('tt','TT')
# print(lis)
# lis[3][2][1][1] = '100'
# print(lis)
# #后面不用写了
# li = ['alex','etric','rain']
# result = "_".join(li)
# print(result)

# li = ['alex','WuSir','ritian','barry','wenzhou']
# for i in range(len(li)):
#     print(i,":",end = " ")
#     print(li[i])
# ls = []
# for c in range(0,101,2):
#     ls.append(c)
# print(ls)
# print(list(range(0,101,2)))
# #方法1 直接倒序打印
# for c in range(100,-1,-1):
#     print(c,end = ' ')
# #方法2，在列表中倒序打印
# print('\n')
# a = list(range(101))
# a.reverse()
# print(a)
# #方法3
# count = 100
# while count > 0:
#     print(count)
#     count -= 1

#=====================
# #敏感字打码
# avstar = ['苍井空','武藤兰','小泽玛利亚','松岛枫','天海翼','桃谷绘里香','波多野结衣']
# user_input = input('输入查询内容')
# li = []
# for i in avstar:
#     if i in user_input:
#         user_input = user_input.replace(i,'*'*len(i))
# li.append(user_input)
# print(li)
#==========================
# li = [1,3,4,'alex',[3,7,8,'IG Champion S8'],5,'RiTiAn']
# for i in li:
#     if type(i) == list:
#         for c in i:
#             if type(c) == str:
#                 print(c.lower())
#             else:
#                 print(c)
#     elif type(i) == str:
#         print(i.lower())
#     else:
#         print(i)

# grade = []
# sum = 0
# while 1:
#     st = input("请输入学生名字和成绩（按 张三_85格式输入，输出Q退出）")
#     if st == 'Q':
#         break
#     else:
#
#         a = st.find('_')
#         if a == -1:
#             continue
#         else:
#             grade.append(st)
#             sum += int(st[a+1:])
# average = sum/len(grade)
# print(grade)
# print(average)


# #输入学生名字和成绩，格式 张三_80,并保存至列表中，以及求成绩的平均值
# grade = [] #新建一个里诶表保存成绩
# sum = 0 #成绩初始值
# while 1 :
#     content = input("请输入学生名字和成绩按照张三_95格式输入（输入Q退出）")
#     if content.lower() == 'q':
#         break
#     else:
#         ls = content.split('_')
#         grade.append(ls[1])
# for i in grade:
#     sum += int(i)
# print(sum/len(grade))


# #输入学生名字和成绩，并保存至列表中，最后计算成绩的平均值
# #输入的格式例如：张三_90
# ls = [] #新建一个空列表，用于存储成绩
# while 1:
#     content = input("请输入学生姓名与成绩，输入格式 张三_98,（输入Q时退出程序，打印所有学生的成绩的平均值）")
#     if content.lower() == 'q':
#         break
#     else:
#         a = content.split('_') # 将输入的姓名和成绩分割列表形式
#         ls.append(a[1]) #将分割的列表中第二个元素添加到新列表中
# sum = 0 #新建变量保存成绩总和
# for el in ls:
#     sum = sum + int(el) #因为输入的是str格式，需要转换成int格式，才能进行数学运算
# print(sum/len(ls)) #打印平均值

# #字典
# #键是不可变的，
# dic = {1:'ming',2:'jacklove'}
# print(dic)
# dic = {(1,3,4):"wish",('one','two'):"something"}
# print(dic)
# dic = {True:1,False:2}
# print(dic)
# dic = {'王岗':'first'}
# print(dic)
# #dic = {[1,2,3,4]:"number"} #会报错列表不可哈希，列表是可变得。
# dic = {'剑圣':'易大师','剑豪':'托儿所','无双剑姬':'雷奥娜'}
# #增
# dic.setdefault("武器大师",'单挑王')
# dic.setdefault("武器大师",'贾克斯') #setdefault先查看是否存在键武器大师，存在不进行操作，不存在进行添加
# print(dic)
# dic['武器大师'] = '贾克斯' #若字典中不存在键，则进行添加，若存在，则强制修改键对应的value
# print(dic)
# #删
# ret = dic.pop('剑豪')
# print(ret) #pop返回键对应的值
# print(dic)
# del dic['剑圣']
# print(dic)#{'无双剑姬': '雷奥娜', '武器大师': '贾克斯'}
# dic.clear()
# print(dic)
# ls = {'剑圣':'易大师','剑豪':'托儿所','无双剑姬':'雷奥娜'}
# set = ls.popitem() # 返回随机删除的键值对元组
# print(set) #s随机删除，返回删除的元组
# print(ls)
# #改
# ls["剑豪"] = "dada"
# print(ls)
# #查
# dic2 = {'剑圣':'js','武器大师':'贾克斯','剑豪':'哈萨开'}
# ls.update(dic2)
# print(ls)
# print(ls.setdefault('剑圣')) #没有返回None,可以指定内容
# print(ls.setdefault('剑魔'))
# # print(ls['剑圣大师']) 没有时会报错，keyerror
# print(ls.get('剑圣'))
# print(ls.get('剑圣师傅')) # 没有返回None
# print(ls.get('剑圣师傅','你傻啊，没有')) #第二个参数是返回值
# #print(ls.setdefault('剑圣')) 没有返回None,可以指定内容
# print(ls.keys())  #高仿列表 dict_keys(['剑圣', '剑豪', '武器大师'])
# for i in ls.keys():
#     print(i)
# for i in ls:
#     print(i) #获取字典中每一个键
# print(ls.values()) #高仿列表
# for i in ls.values():
#     print(i) #获取到字典中每一个值
# print(ls.items()) #获取带元组的列表 #dict_items([('剑圣', 'js'), ('剑豪', '哈萨开'), ('武器大师', '贾克斯'), ('剑魔', None)])
# for i in ls.items():
#     print(i,end = " ") #('剑圣', 'js') ('剑豪', 'dada') ('武器大师', '贾克斯')
# print('\n')
# #解构，解包
# a,b = (12,34)
# print(a)
# print(b)
# a,b = [12,34]
# print(a)
# print(b)
# for item in ls.items():
#     a,b = item
#     print(a)
#     print(b)
# #也可以省去元组解构给变量
# print("#"*20)
# for a,b in ls.items():
#     print(a)
#     print(b)
# a,b = '12'
# print(a)
# print(b)
# a,b = '张三' #解构，可以是字符串或者列表，元组，但里面的元素必须是两个
# print(a)
# print(b)
# dic1 = {}
# dic = dic1.fromkeys([1,2,3,4]) #fromkeys批量创建可迭代对象，参数是可迭代对象
# print(dic)
# dic = dic1.fromkeys([1,2,3,4],'abc')
# print(dic)
# dic = {'name':'汪峰',
#        'age':43,
#        'wife':{
#            'name':'国际章',
#            'age':39,
#            'salary':1000000
#        },
#        'baby':[
#            {'name':'西欧昂达','age':18},
#            {'name':'嘻嘻茉莉','age':15}
#        ]
# }
# print(dic['baby'][0]['age']) #打印西欧昂达的name
# dic['baby'][0]['age'] = 19 #涨了一岁
# print(dic)
# print(dic.get('baby')[0].get('age')) #可以用于输入，如果没有返回None

# # "k:1|k1:2|K2:3|k3:4"处理成字典{'k':1,'k1':2,'k2':3,'k3':4}
# s = "k:1|k1:2|K2:3|k3:4"
# ls = s.split('|')
# print(ls)
# dic = {}
# for wl in ls:
#     #dic[wl.split(':')[0]] = int(wl.split(':')[1])
#     k,v = wl.split(':')
#     dic[k] = int(v)
# print(dic)
#
# # 大于66，和小于66的数分别组成列表，然后组成字典{'k1': [77, 88, 99, 90], 'k2': [11, 22, 33, 44, 55]}
# el = []
# ml = []
# li = [11,22,33,44,55,66,77,88,99,90]
# for i in li:
#     if  i == 66:
#         continue
#     elif i < 66:
#         el.append(i)
#     else:
#         ml.append(i)
# dic = {}
# dic.setdefault('k1',ml)
# dic.setdefault('k2',el)
# print(dic)
# dic = {'武器大师':'贾克斯'}
# a = dic.setdefault('光辉女郎','拉克丝') #返回value 拉克丝
# print(dic)
# print(a)
# #可以这样
# li = [11,22,33,44,55,66,77,88,99,90]
# dic = {'k1':[],'k2':[]}
# for i in li:
#     if  i == 66:
#         continue
#     elif i < 66:
#         dic.setdefault('k1').append(i) # 因为原字典存在k1键，所以setdefault返回value（空列表）然后使用列表append添加
#     else:
#         dic.setdefault('k2').append(i)
# print(dic)
# '''
# 商品列表
# goods = [{'name':"电脑",'price':1999},
#         {'name':"鼠标",'price':10},
#         {'name':'游艇','price':'20',
#         {'name':'美女','price':998}]
# 按如下形式打印
# 1 电脑 1999
# 2 鼠标 10
# 3 游艇 20
# 4 美女 998
# '''
# goods = [{'name':"电脑",'price':1999},
#         {'name':"鼠标",'price':10},
#         {'name':'游艇','price':'20'},
#         {'name':'美女','price':998}]
# for i in goods:
#     index = goods.index(i)
#     print(index+1,goods[index]['name'],goods[index]['price'])
# #输入序列号，打印商品name和price
# while 1:
#     str_input = input("输入商品系列号或按Q结束")
#
#     if str_input.isdigit() and 0 <  int(str_input) < 5:
#         print(goods[int(str_input)-1]['name'],goods[int(str_input)-1]['price'])
#     elif str_input.upper() == 'Q':
#         break
#     else:
#         print("输入错误，请重新输入")

# n = 10
# n1= 10
# print(n == n1)
# #id()查看内存地址
# #所有数据类型都有内存地址
# # is 查看内存地址
# print(id(n))
# print(n is n1) #True
# #字符串
# a = 'alex'
# b = 'alex'
# print(a is b)  #True
# #列表
# l1 = [1,2,3]
# l2 = [1,2,3]
# print(l1 is l2) #False
# #元组
# tu = (1,2,3)
# tu1 = (1,2,3)
# print(tu is tu1) #False
# #字典
# dic = {'name':'alex'}
# dic1 = {'name':'alex'}
# print(dic is dic1) #false
# #元组
# tu = (1,4,6)
# tu1 = (1,4,6)
# print(tu is tu1) # False
# #小数据池 -5～256
# n = -10000
# n1 = -10000
# print(n is n1) #False，在pycharm运行超出小数据池也是True
# a = 10000
# b = 10000
# print(id(a),id(b))


#2019/5/19

#编码和解码
#ASCII码
#gbk 国标

#-*-encoding:utf-8 -*-

# s = '饿了吗'
# s1 = s.encode('gbk') #编码，gbk码，一个汉字2两字节
# print(s1) #b'\xb6\xf6\xc1\xcb\xc2\xf0'，\xb6算一个字节
# s2 = s1.decode('gbk')  #解码
# print(s2)
# print(s.encode('utf-8'))
# a = '大佬'
# print(a.encode('utf-8')) #b'\xe5\xa4\xa7\xe4\xbd\xac',两个汉字，六个字节，用gbk解码，两个字节一个汉字，则gbk解码应该是三个汉字
# print(a.encode('utf-8').decode('gbk')) #澶т浆,utf-8编码，gbk解码
# #注意用什么编码就用什么解码
# b = '中国'
# print(b.encode('gbk')) #编码 -----b'\xd6\xd0\xb9\xfa'
# print(b.encode('gbk').decode('gbk')) #先编码再解码----中国
# a = '谦虚'
# b = '谦虚'
# print(id(a),id(b))
# ls = [1,3,4,'哈哈']
# ls2 = [1,3,4,'哈哈']
# print(id(ls),id(ls2)) #列表内存地址不同
# print(not ls is ls2) #True
# print(id(ls[-1]),id(ls2[-1])) #提取元素，但相同元素内存地址是相同的 47059648 47059648
# ls = [1,3,4,'哈哈']
# ls2 = [1,3,4,'哈皮']
# print(id(ls[-1]),id(ls2[-1]))#47059648 47061664
# #以上说明字符串占内存中占据某个位置，第二次只需调用该内存地址下的字符串即可，不再创建。省内存
# #当字符串中包含特殊字符时，内存地址不同
# a = [1,2,3]
# b = a
# c = b
# print(a == c) #比较值 ，因为只创建一次列表，记住问题：有没有创建新的缓存，答案是没有
# print( a is c) #比较内存地址，三个变量都指向一个列表，故内存地址相同
#
# #比较内存地址时，要看创建了几次列表，这样记忆，创建一次列表，内存地址相同，创建多次列表，地址不同，但字符串不适用。
# a = [1,3,4]
# b = [1,3,4]
# c = b
# print(a == c) #True
# print(a is b) #fasle
# print(a is c) #false
# s = '你好'
# print(s.encode('gbk')) #b'\xc4\xe3\xba\xc3\xc2\xf0'
# c = b'\xc4\xe3\xba\xc3\xc2\xf0'
# print(c.decode('gbk'))#解码
# print(s.encode('utf-8')) #b'\xe4\xbd\xa0\xe5\xa5\xbd\xe5\x90\x97'
# print(s.encode('utf-8').decode('gbk')) #浣犲ソ,用什么编码就用什么解码，这种解码无意义

# #老男孩10位评委打分，5分到10分之间，并打印评委打分情况。将评委打分情况统计到字典中
# count = 1
# scores = dict()
# while count < 11:
#     score = int(input("请%d号评委输入分数："%count))
#     if score < 5 or score > 10:
#         print('你不是傻缺？')
#         continue
#         #注意此处不写count += 1因为此处并非要跳过某个评委，而是每个评委都要输出正确范围内的分数
#     else:
#         print("第%d号评委打分为：%d"%(count,score))
#         scores[count] = score
#         count += 1
# else:
#     print(scores) #{1: 8, 2: 8, 3: 8, 4: 8, 5: 8, 6: 8, 7: 8, 8: 9, 9: 9, 10: 8}
# ls = ['金瓶梅','解救吾先生','美国往事','西西里的美丽传说']
# print('''金瓶梅-请输入：1
# 解救吾先生-请输入：2
# 美国往事-请输入：3
# 西西里的美丽传说-请输入：4''')
# a = 0
# b = 0
# c = 0
# d = 0
# while 1:
#     choice = input('请输入您的选票')
#     if choice == 'q':
#
#         break
#     else:
#         if choice.isdigit():
#             if int(choice) not in [1,2,3,4]:
#                 print('不在范围内，重新输入')
#                 continue
#             elif int(choice) == 1:
#                 a += 1
#             elif int(choice) == 2:
#                 b += 1
#             elif int(choice) == 3:
#                 c += 1
#             else:
#                 d += 1
#         else:
#             print("输入的不是数字，请重新输入")
#             continue
# m = {}
# m['金瓶梅'] = a
# m['解救吾先生'] = b
# m['美国往事'] = c
# m['西西里的美丽传说'] = d
# print(m)



# m = {}
# m['金瓶梅'] = 0
# m['解救吾先生'] = 0
# m['美国往事'] = 0
# m['西西里的美丽传说'] = 0
# ls = ['金瓶梅','解救吾先生','美国往事','西西里的美丽传说']
# print('''金瓶梅-请输入：1
# 解救吾先生-请输入：2
# 美国往事-请输入：3
# 西西里的美丽传说-请输入：4''')
# a = 0
# b = 0
# c = 0
# d = 0
# while 1:
#     choice = input('请输入您的选票')
#     if choice == 'q':
#
#         break
#     else:
#         if choice.isdigit():
#             if int(choice) not in [1,2,3,4]:
#                 print('不在范围内，重新输入')
#                 continue
#             elif int(choice) == 1:
#                 m['金瓶梅'] += 1
#             elif int(choice) == 2:
#                 m['解救吾先生'] += 1
#             elif int(choice) == 3:
#                 m['美国往事'] += 1
#             else:
#                 m['西西里的美丽传说'] += 1
#         else:
#             print("输入的不是数字，请重新输入")
#             continue
# print(m)

# #给几部电影评分
# dic = dict()
# ls = ['金瓶梅','解救吾先生','美国往事','西西里的美丽传说']
# for el in ls:
#     score = input('请给%s评分'%el)
#     dic[el] = score
# print(dic) #{'金瓶梅': '100', '解救吾先生': '12', '美国往事': '34', '西西里的美丽传说': '67'}
#输入数字，打印数字拼音
# dic = {
#     '-':'fu',
#     '0':'ling',
#     '1':'yi',
#     '2':'er',
#     '3':'san',
#     '4':'si',
#     '5':'wu',
#     '6':'liu',
#     '7':'qi',
#     '8':'ba',
#     '9':'jiu'
# }
# #输入多个数字，打印多个拼音语音
# a = input("输入多个数字")
# for element in a:
#     print(dic[element],end = ' ')

# #车牌划分，统计各省份车牌量
# cars = ['鲁A3244','鲁B442','京2342','黑C3434','黑C6353','沪4234']
# locals = {'沪':"上海",'黑':'黑龙江','鲁':'山东','鄂':'湖北','湘':'湖南','京':'北京'}
# total = {}
# list = []
# for el in cars:
#     list.append(el[0])
# print(list)
# # count
# for e in list:
#     total[locals[e]] = list.count(e)
# print(total) #{'山东': 2, '北京': 1, '黑龙江': 2, '上海': 1}



# #干掉主播
# zhubo = {'卢本伟':1242324,'冯提莫':4234143,'若风':4344443,'骚男':234234}
# #计算主播收益平均值
# print(zhubo.values())
# ls = zhubo.values()
# average = sum(ls)/len(ls)
# print(average)
# #不能使用循环删除字典尺寸,所以只能通过列表删除元素
# ls = []
# for i in zhubo.keys():
#     ls.append(i)  #创建新列表，保存字典key值，高仿列表受限
# print(ls)
# for i in ls:
#     if zhubo[i] < average:
#         ls.remove(i) #删除列表元素
# print(ls)
# new_dic = {}
# for el in ls: #迭代更新后的列表
#     new_dic[el] = zhubo[el] #新字典添加元素
# print(new_dic)
# zhubo = new_dic #把新字典指向zhubo字典
# print(zhubo)
# #干掉卢本伟
# zhubo = {'卢本伟':1242324,'冯提莫':4234143,'若风':4344443,'骚男':234234}
# zhubo.pop('卢本伟')
# print(zhubo)
#
# cars = ['鲁A3244','鲁B442','京2342','鲁B442','黑C3434','黑C6353','沪4234','黑C6353']
# locals = {'沪':"上海",'黑':'黑龙江','鲁':'山东','鄂':'湖北','湘':'湖南','京':'北京'}
#
# dic = {}
#
# for el in cars:
#     place_short = el[0]
#     whole_name = locals[place_short]
#     value = dic.get(whole_name) #熟悉get用法,get返回的是value值
#     if value== None:
#         value = 1
#     else:
#         value += 1
#     dic[whole_name] = value
# print(dic)

# ls = ['崔大哥','王二麻子','曹操']
# s = '_'.join(ls)
# print(s) #崔大哥_王二麻子_曹操
# s1 = '**'.join(ls)
# print(s1) #崔大哥**王二麻子**曹操
# s2 = '崔大哥**王二麻子**曹操'
# print(s2.split('**')) #['崔大哥', '王二麻子', '曹操']
# s3 = '_'.join('朱元璋')
# print(s3) #朱_元_璋     迭代字符串中单个字符
#
# #字典删除
# dic = {'疾风剑豪':'压缩','无极剑圣':'js',"武器大师":'贾克斯'}
# dic.clear()
# print(dic)
# dic = {'疾风剑豪':'压缩','无极剑圣':'js',"武器大师":'贾克斯'}
# lst = []
# for e in dic: #循环字典的键
#     lst.append(e)
# for e2 in lst:
#     dic.pop(e2)
# print(dic)
# #综上，字典和列表都不能在循环中删除，字典在循环的时候不能改变大小
# son = dict.fromkeys("love","you")
# print(son) #{'l': 'you', 'o': 'you', 'v': 'you', 'e': 'you'} 迭代love(第一个参数）
# #坑
# a = ["son",'mother','father']
# total = dict.fromkeys("123",a)
# print(total) #{'1': ['son', 'mother', 'father'], '2': ['son', 'mother', 'father'], '3': ['son', 'mother', 'father']}
# a.append("grandpa") #只创建了一个列表，故和append的代码操作位置无关，列表发生改变，total也会变
# print(total) #{'1': ['son', 'mother', 'father', 'grandpa'], '2': ['son', 'mother', 'father', 'grandpa'], '3': ['son', 'mother', 'father', 'grandpa']}
#
# #set集合，无序
# #set集合中的元素必须是可hash的，不可变得；但是set本身是不可hash得.set是可变的.
# s = {'杰克','的老婆','肉丝',('hello',1)} #里面不能放列表，列表是可变的，不可哈希的,否则报错TypeError: unhashable type: 'list'
# print(s)
# #列表去重，可利用set无重复的特性
# lst = [1,2,3,4,5,34,23,3,34,32,3,1,3,15,32,34,2]
# s = set(lst)
# print(s)
# lst = list(s)
# print(lst)
# #set集合是可变的数据类型，不可哈希，因此可进行增删改查
# #增
# s = {"哈哈",'嘻嘻','嗯呢'}
# s.add("fuck")
# print(s) #{'哈哈', 'fuck', '嘻嘻', '嗯呢'}
# s = {"冰",'与','火'}
# s.update("树木森林")#迭代更新 {'林', '森', '木', '树', '冰', '与', '火'}
# print(s)
# #删
# s = {"哈哈",'嘻嘻','嗯呢'}
# s.pop() #随机删除
# print(s)
# s = {"哈哈",'嘻嘻','嗯呢'}
# s.remove("嗯呢")
# print(s)
# s.clear() #清空
# print(s)
# #修改就是先用remove删除然后用add添加，因为set本身无序，所以无索引
# #查询
# s = {"哈哈",'嘻嘻','嗯呢'}
# for e in s:
#     print(e)
# #集合基础操作
# s = {"fuck",'bitch','whore','**'}
# s2 = {'bitch','whore',"sun",'moon'}
# print(s & s2) #交集 ，共有的 {'bitch', 'whore'}
# print(s|s2)#并集二者所有的，重复的算一次 {'**', 'moon', 'sun', 'bitch', 'fuck', 'whore'}
# print(s - s2) #差集，前者独有的 {'**', 'fuck'}
# a = {"fuck"}
# b = {"fuck",'you'}
# print(a< b)#子集 True
# print(a>b)#超集 False
# #frozenset保存不可哈希元素，变成可哈希不可变元素
# s = frozenset([1,3,4,5])
# dic = {s,1}
# print(dic)
# for e in s:
#     print(e) #迭代查看frozenset中保存的元素
# #1st1=[“金毛狮王”，“紫衫龙王”，“青翼蝠王”，“白眉鹰王"]
# lst = ["金毛狮王",'紫衫龙王','青翼蝠王','白眉鹰王']
# lst2 = lst
# print(lst)
# lst.append("杨逍")
# print(lst) #['金毛狮王', '紫衫龙王', '青翼蝠王', '白眉鹰王', '杨逍']
# print(lst2) #['金毛狮王', '紫衫龙王', '青翼蝠王', '白眉鹰王', '杨逍']
# lst3 = lst[:] #浅拷贝 或者 lst3 = lst.copy()
# print(lst3) #['金毛狮王', '紫衫龙王', '青翼蝠王', '白眉鹰王', '杨逍']
# lst.append("大佬")
# print(lst) #['金毛狮王', '紫衫龙王', '青翼蝠王', '白眉鹰王', '杨逍', '大佬']
# print(lst3) # ['金毛狮王', '紫衫龙王', '青翼蝠王', '白眉鹰王', '杨逍']
# print(id(lst)) #60249152
# print(id(lst2)) #60249152
# print(id(lst3)) #60249192
# l = ["金毛狮王",'紫衫龙王','青翼蝠王','白眉鹰王',['张无忌','赵敏','周芷若']]
# l2 = l.copy()
# print(id(l),id(l2)) #浅拷贝，内存地址不一样
# l[4].append("小昭")
# print(l)
# print(l2) #['金毛狮王', '紫衫龙王', '青翼蝠王', '白眉鹰王', ['张无忌', '赵敏', '周芷若', '小昭']]
# print(id(l[4]),id(l2[4])) #48125032 48125032 浅拷贝---列表里面的列表并没有拷贝，直接指向同一个列表对象
# #深层拷贝，引入copy模块
# import copy
# l3 = copy.deepcopy(l)
# print(l3) #['金毛狮王', '紫衫龙王', '青翼蝠王', '白眉鹰王', ['张无忌', '赵敏', '周芷若', '小昭']]
# l[4].append("DD")
# print(l) #['金毛狮王', '紫衫龙王', '青翼蝠王', '白眉鹰王', ['张无忌', '赵敏', '周芷若', '小昭', 'DD']]
# print(l3) #['金毛狮王', '紫衫龙王', '青翼蝠王', '白眉鹰王', ['张无忌', '赵敏', '周芷若', '小昭']]
# print(id(l[4]),id(l3[4])) #60708224 60709424,可见深层拷贝与浅层拷贝不同，深层拷贝内部列表内存地址也变了，说明深层列表也进行了拷贝
# '''1.赋值操作，没有创建新对象
# 2.浅拷贝。只持贝第一层内容。[;]   copy()
# 3.深拷贝，把这个对象内部的内容全部拷贝一份，引入copy模块，deepcopy()'''
# a = dict.fromkeys('123','hai')
# print(a)
#方法一
# while 1:
#     a = int(input("输入数字"))
#     if len(str(a)) == 3:
#         if (a // 100)** 3 + (a % 100 // 10) ** 3 + (a % 10) ** 3 == a :
#             print("%d是水仙花数"%a)
#         else:
#             print("不是水仙花数")
#     else:
#         print("请重新输入一个三位数")
#         continue

# str = input("请输入数字")
# s = 0
# for c in str:
#     s += int(c)**3
# if s == int(str):
#     print("是水仙花数")
# else:
#     print("不是水仙花数")

# #生成无重复的随机数
# from random import randint
# b = set()
# while len(b) < 7:
#     a = randint(1, 36)
#     b.add(a)
# print(b)
#方法1
# s = set()
# while 1:
#     a = input("输入数字")
#     if a == 'q':
#         break
#     else:
#         s.add(int(a))
# lst = list(s)#创建无重复列表
# print(lst)
# for i in range(len(lst)-1):
#     for j in range(i+1,len(lst)):
#         if lst[i] > lst[j]:
#             lst[i],lst[j] = lst[j],lst[i]
# print(lst)
#方法2
# ls = [1,2,34,14,43,32,3,2,3,42,424,24,41,4]
# count = 0
# while count < len(ls):
#     i = 0
#     while  i < len(ls) -1-count: #优化了，减少不必要的循环
#         if ls[i] > ls[i+1]:
#             ls[i],ls[i+1] = ls[i+1],ls[i]
#         i += 1
#     count += 1
# print(ls)

# f = open("小护士.txt",mode = "r",encoding="utf-8")
# s = f.read()
# print(s)
# f.close()
# #绝对路径 磁盘中读取
# f = open("C:/Users/HUAWEI/Desktop/新建文本文档.txt",mode = "r",encoding="utf-8") #如果文本里有中文，需要用gbk解码 encoding = "gbk"
# s = f.read()
# print(s)
# f.close()
# #相对路径 ../
# f = open("../备份/poem.txt",mode = "r",encoding="gbk") #../表示当前文件夹的上级文件夹 ../../表示上级文件的再上级
# s = f.read()
# print(s)
# f.close()
#
# f = open("小护士.txt",mode = "r",encoding="utf-8")
# #当文件特别大时，不能一次性读完，容易爆内存
# s = f.readline() #一次读一行
# print(s.strip()) #strip除去末尾换行符\n \t 空格
# s = f.readline() #一次读一行
# print(s.strip())
# s = f.readline() #一次读一行
# print(s.strip())
# s = f.readline() #一次读一行
# print(s.strip())
# f.close()
#
# f = open("小护士.txt",mode = "r",encoding="utf-8")
# #利用循环读取
# while 1:
#     s = f.readline()
#     if s != "": #如果不是空字符才打印，空字符不打印，但是循环仍在继续
#         print("内容是",s.strip())
#
# f = open("小护士.txt",mode = "r",encoding="utf-8")
# for line in f: #文件也是可迭代对象
#     print(line.strip()) #一行一行读取数据
# f.close()
#
# # #写入文件
# # #带w,只要操作了，就会清空源文件
# '''flush() 方法是用来刷新缓冲区的，即将缓冲区中的
# 数据立刻写入文件，同时清空缓冲区，不需要是被动的等
# 待输出缓冲区写入。一般情况下，文件关闭后会自动刷新
# 缓冲区，但有时你需要在关闭前刷新它，这时就可以使用
# flush() 方法。'''
# f = open("大大",mode = 'w',encoding="utf-8")
# f.write("咚咚锵咚咚咚锵")
# f.write("滴滴滴滴答答")
# f.flush()
# f.close()
# #a模式，叠加文件
# f = open("钉钉",mode = "a",encoding= "utf-8")
# f.write("瓦大喜哇\n")
# f.write("八嘎呀路")
# f.flush()
# f.close()
#
# #rb,wb,ab,bytes处理非文本文件，mode里有b,则后面就没有encoding编码解码字符集
# f = open("c:/123.jpg",mode = 'rb') # 这里不能写encoding
# d = open('d:/345.jpg',mode = 'wb')
# for line in f: #从c盘读取 line你是不知道读取了多少数据的
#     d.write(line) # 写入到d盘
# f.close()
# e.flush() #写入后刷新缓冲区
# e.close()
#
# f = open("c:/123.jpg",mode = 'rb')
# e = open('d:/345.jpg',mode = 'wb')
# f2 = f.read() #一次性读完
# e.write(f2)  #一次性写入，和上面用循环读完一行写入一行不同，但最终结果一样
# f.close()
# e.flush() #写入后刷新缓冲区
# e.close()
#
#
# #r+读写模式
# #不论读取多少内容，光标在哪，写入的时候和光标无关，只在末尾写入，除非上来就写入，这时写入在开头
# #最好用的读写同时存在的模式
# # r+ 读写模式，先读后写
# # w+ 写读模式，先写后读
# f = open("小小",mode = "r+",encoding = "utf-8")
# s = f.read()
# f.write("没吃呢")
# f.flush()
# print(s)
#
# f = open("小小",mode = "a+",encoding = "utf-8")
# s = f.read()
# f.write("没吃呢")
# f.flush()
# print(s)
#
# f = open("小小",mode = "r+",encoding = "utf-8")
# s = f.read(2)
# f.write("大傻子")
# f.flush()
# print(s)
#
# f = open("淘宝",mode = 'w+',encoding='utf-8')
# f.write("阿西吧") #直接清空源文件
# s = f.read()
# print("读取的内容是",s) #经过写入操作，光标移动到末尾，所有读取不到内容
# f.flush()
# f.close()
#
# #seek(0)光标返回到开头
# f = open("淘宝",mode = 'w+',encoding='utf-8')
# f.write("阿西吧") #直接清空源文件
# f.seek(0)
# s = f.read()
# print("读取的内容是",s) #经过写入操作，光标移动到末尾，所有读取不到内容
# f.flush()
# f.close()
#
# # a+
# f = open("阿西吧",mode = "a+",encoding= "utf-8")
# #s = f.read() #追加模式，光标在末尾读取不到内容
# f.write("齐天大圣孙悟空") #清空源文件，再写入
# f.seek(0) #光标移动到开头再读取
# s = f.read()
# print(s)
# f.close()
#
# #反复读取
# f = open("green",mode = "r",encoding="utf-8")
# for line in f:
#     print(line.strip())
# f.seek(0) #关键点，将光标移动到开头才能才能进行第二次循环
# for line in f:
#     print(line.strip())
#
# f = open("green",mode = "r",encoding="utf-8")
# f.seek(3) #3个字节一个中文汉字
# s = f.read(1)
# print(s)
#
# #seek(偏移量,开头或结尾)
# #seek(0,0) 开头偏移量为0
# #seek(0,2)  结尾偏移量为0
# #seek(0,1) 当前偏移量为0
# f = open("green",mode = "r",encoding="utf-8")
# s = f.read(1)
# print(s)
# print(f.tell()) #告诉我们光标位置
# f.seek(0,2)
# s2 = f.read()
# print(s2) #光标移动到末尾，打印没有
# print(f.tell()) #告诉我们光标位置
# f.seek(6,0) #开头移动2个字符
# s3 = f.read(1)
# print(f.tell())
# f.seek(12)
# print(f.tell())
# print(s3)
#
# #⽂件修改: 只能将⽂件中的内容读取到内存中, 将信息修改完毕, 然后将源⽂件删除, 将新⽂件的名字改成老⽂件的名字
#
# import os
# import time
# with open("001",mode = 'r',encoding= "utf-8") as f1,\
#     open('001_副本',mode = "w",encoding = "utf-8") as f2:
#     for line in f1:
#         line = line.replace("大神",'sb')
#         f2.write(line)
# #删除文件
# time.sleep(5) #睡5秒，方便观察
# os.remove("001")
# time.sleep(3)
# os.rename("001_副本",'001')
#
# '''
# id,name,phone,car,home,salary,baby
# 1,alex,10086,特斯拉,于辛庄,5000000,1
# 2,wusir,10010,五菱宏光,青年,400000,2
# 3,taibai,10000,魔板单车,松兰堡,30000,3
# 4,ritian,12345,小黄车,广东,30000,4
# '''
# ls = []
# with open('123.log',mode = "r",encoding="utf-8") as f:
#     first = f.readline().strip().split(',')
#     print(first)
#     print(f.tell())
#     for line in f:
#         dict = {}
#         lst = line.strip().split(',')
#         for i in range(len(lst)):
#             dict[first[i]] = lst[i]
#         print(dict)
#         ls.append(dict)
# print(ls)

# ls = [1,2,3,4,5,6,7]
# print(ls[1:3])
# ls[1:3]  = "abcd"
# print(ls)
# ls = [1,"a","b",3,4,5,6,7]
# print(ls)
# a = ("hello")
# print(type(a)) #<class 'str'>
# a = (23)
# print(type(a)) #<class 'int'>
# a =(23,)
# print(type(a)) #<class 'tuple'>
# #可以表示FALSE的数据
# ls = ['',0,list(),set(),tuple(),None]
# s1 = "大哥大"
# s2 = s1.encode("utf-8")
# print(s2)
# s3 = s2.decode('utf-8').encode("gbk")
# print(s3)
# ls = "1,2,3".split(",")
# print(ls)
# s = ",".join(ls)
# print(s)
# ls = ['a','b','c','d']
# ls.insert(1,"hello")
# print(ls) #['a', 'hello', 'b', 'c', 'd']
# #range打印100,99.....1
# print(list(range(100,-1,-1)))
#
# sum = 0
# i = 1
# fuhao = 1
# for i in range(1,100,2):
#     sum = sum + i * fuhao
#     fuhao = fuhao * -1
# print(sum)
# sum = 0
# count = 1
# for i in range(1,100,2):
#     if count % 2 == 0:
#         sum = sum - i
#     else:
#         sum = sum + i
#     count += 1
# print(sum)
# sum = 0
# index = 1
# fuhao = 1
# while index < 100:
#     sum = sum + index * fuhao
#     index = index + 2
#     fuhao = fuhao * -1
#
# s = "js:剑圣|jj:剑姬|gg:吉吉"
# ls1 = s.split("|")
# print(ls1) #['js:剑圣', 'jj:剑姬', 'gg:吉吉']
# d = {}
# for el in ls1: #在for循环中更改
#     lst = el.split(':')
#     key = lst[0]
#     value = lst[1]
#     print(key,value)
#     d[key] = value
# print(d)
#
# #整数叠加器
# content= input('请输入运算')
# content.replace(" ","") #去掉空格
# ls = content.split("+")
# sum = 0
# for el in ls:
#     print(el)
#     sum = sum + int(el)
# print(sum)
#
# ls = []
# lst= ["波多野结衣",'麻仓优','苍井空','小泽玛利亚','janson']
# index = 0
# while index < 3:
#     content = input("shuru")
#     for el in lst:
#         if el in  content:
#             content  = content.replace(el,"*"*len(el)) #不赋值不能改变字符串
#     ls.append(content)
#     index += 1
# print(ls)
#
# a = "发大发发发地方撒"
# print(id(a))
# a = a.replace("发",'哈') #重新指向新的内存
# print(id(a))
# print(a)
#
# ls = []
# for i in range(10):
#     num = int(input("输入数字"))
#     ls.append(num)
# key1 = []
# key2 = []
# for el in ls:
#     if el > 55:
#         key1.append(el)
#     else:
#         key2.append(el)
# dic = {"key1":key1,"key2":key2}
# print(dic)
#
#
# f = open('11',mode = 'r',encoding="utf-8")
# # f.readline()若果有表头可以用来出去表头
# s = []
# for line in f:
#     ls = line.strip().split(" ")
#     d = {}
#     for el in ls:
#         l2 = el.split(':')
#         d[l2[0]] = l2[1]
#     s.append(d)
# print(s)

# def opensoftware(tools): #形参 变量
#     print("打开%s中，请稍等。。。"%tools)
#     print("软件升级中")
#     return
# opensoftware("微信") #实参
#
# def chi(good_food,no_good_food,drink,ice_cream):
#     print(good_food,no_good_food,drink,ice_cream)
#     return None
# chi("红烧肉",'鸡蛋炒饭','老白干','哈根达斯')
# chi(good_food='蛋炒饭',no_good_food='咸菜',ice_cream='哈根达斯',drink='哈尔滨啤酒')
# chi('蛋炒饭','咸菜',ice_cream='哈根达斯',drink='哈尔滨啤酒') #位置参数和实参不能交叉
# def register(name,num,sex):
#     return name,num,sex
# co = register('the shy','10086','male')
# print(co) #('the shy', '10086', 'male')，说明函数返回多个参数是以元组形式
# #默认参数
# def register(name,num,gender = 'male'): #默认值参数必须在位置参数后面
#     return name,num,gender
# co = register('Roocke','10010')
# print(co) #('Roocke', '10010', 'male')

# #输入三个参数，返回元组，解构
# def co(name,num,where):
#     return name,num,where
# a,b,c = co('jasen','10086','Singapore')
# print(a,b,c) #解构
#
# #打印索引值是奇数的元组列表
# lst = ["床",'前','明月','光']
# def jishu(l):
#     result = []
#     for i in range(len(lst)):
#         if i % 2 == 1:
#             result.append(l[i])
#     return result
# print(jishu(lst))
# #方法2
# def jishu(l):
#     return l[1::2]
# print(jishu(lst))
#
# #写函数，判断用户的输入对象（字符串，列表，元组）长度是否大于5
# def cx(sole):
#     if len(sole) > 5:
#         return "大于5"
#     elif len(sole) == 5:
#         return "等于5"
#     else:
#         return "小于5"
# print(cx("哈哈哈哈哈"))
#
# #给一个字符串，统计数字、空格、字母、其他出现的次数
# def tongji(content):
#     shuzi = 0
#     kongge = 0
#     zimu = 0
#     qita = 0
#     for el in content:
#         if el.isdigit():
#             shuzi += 1
#         elif el.isalpha():
#             zimu += 1
#         elif el == " ":
#             kongge+= 1
#         else:
#             qita += 1
#     return shuzi,kongge,zimu,qita
# print(tongji("iajfoifasd;ljk5345fhkl a afhh lahf hfkj哈"))
#
# #输入两个数，返回最大值
# def print_max_min(a,b):
#     if a > b:
#         return a
#     else:
#         return b
# print(print_max_min(34,67))
# #三元运算符
# #c = a if a > b else b
# a = input("a")
# b = input("b")
# c = a if a > b else b
# print(c)

# #字典，如果字典的value的长度大于2，则保留前两个字符,value仅限字符串或者列表,元组，数字不可以
# #{"zhang":"好迪真好","2":"大家","some":[1,2,3,4,5]}
# def fun(dic):
#     for k,v in dic.items():
#         if len(v) > 2:
#             v = v[:2]
#             dic[k] = v
#     return dic
# print(fun({"zhang":"好迪真好","2":"大家","some":[1,2,3,4,5],"元组":(1,2,3,4)}))
# #第二种方法，产生新字典
# def fun(dic):
#     new_dic = {}
#     for k,v in dic.items():
#         if len(v) > 2:
#             s = v[:2]
#             new_dic[k] = s
#         else:
#             new_dic[k] =v
#     return new_dic
# print(fun({"zhang":"好迪真好","2":"大家","some":[1,2,3,4,5],"元组":(1,2,3,4)}))

# #传入的列表，打印索引和对应元素形成的字典
# def fun(lst):
#     if type(lst) == list:
#         dic = {}
#         for i in range(len(lst)):
#             dic[i] = lst[i]
#         return dic
#     else:
#         return "不是列表"
# print(fun("ddadfadfdas"))
# print(fun(["哈哈",'嘻嘻','大大','忘记']))

# #输入name,gender,age，追加到某个文件中
# def fun(name,age,gender = "男"):
#     with open("阿西吧","a",encoding="utf-8") as f:
#         f.write(name + "-"+gender+"-"+age+'\n')
# while 1:
#     content = input("输入Q退出")
#     if content == "Q":
#         break
#     else:
#         name = input("输入name")
#         gender = input("输入gender") #默认是男，输入时跳过即可
#         age = input("输入age")
#         if gender == "": #如果不输入gender，可以用空字符代替,此时gender默认为男
#             fun(name,age)
#         else:
#             fun(name,age,gender)

# #用户给出要修改的文件名（包括路径）和内容如何进行修改
# def xiugai(path,old,new):
#     with open(path,'r',encoding='gbk') as f1,\
#          open(path+"_副本",'w',encoding="gbk") as f2: #汉字用gbk编码
#         for line in f1: #说明对象有line这个line子元素，可以进行迭代行，区别内容read()
#             line = line.replace(old,new)
#             f2.write(line)
# xiugai("C:/Users/HUAWEI/Desktop/123.txt",'啊',"哦")

# #登录函数
# def fun():
#     count = 0
#     while count < 3:
#         name = input("输入名字")
#         code = input("输入密码")
#         if name == "jack" and code == "1034":
#             print("登陆中")
#             return #break
#         else:
#             print("输入密码错误")
#             print("您还有%s次机会"%(2-count))
#         count += 1
# fun()
###########################################################################
##完成注册功能
# def zhuce(user_name):
#     with open("C:/Users/HUAWEI/Desktop/cd.txt",'r+',encoding='gbk') as f:
#         s = f.read()
#         for line in f:
#             result = line.find(user_name)
#             if result != -1:
#                 print("重新输入")
#                 return
#             else:
#                 continue
#         else:
#             print("用户名可以使用，请输入密码")
#             code = input('输入密码')
#             f.write('\n'+user_name+" "+code)
#             f.seek(0)
#             print(f.read())
# while 1:
#     user_name = input("用户名(输入Q退出)：")
#     if user_name.upper() == 'Q':
#         break
#     else:
#         zhuce(user_name)

# #动态传参
# # *代表接收位置参数的动态传参,接收到动态传参是元组
# #而且动态传参必须在位置参数后面
# #顺序：位置参数=>动态传参*args=>默认值参数=>关键字传参**kwarg
# def eat(name,*food):
#     print(name,food)
# eat('老王','小鸡炖蘑菇','肉丝','羊肉') #老王 ('小鸡炖蘑菇', '肉丝', '羊肉')
#
# def eat(name,location = '北京',*food):
#     print(location) #默认值未生效，打印的是'小鸡炖蘑菇'占了location位置
#     print(name+'想吃',food)
# eat('老王','小鸡炖蘑菇','肉丝','羊肉')
#
# def eat(name,*food,location = '北京'):
#     print(location) #默认值生效,所以默认值只能放到最后才生效，但是传入的值只会进入到动态传参的位置，地点默认值不会通过传参产生改变，可以通过关键字传参
#     print(name+'想吃',food)
# eat('老王','小鸡炖蘑菇','肉丝','羊肉','天津') # 北京 老王想吃 ('小鸡炖蘑菇', '肉丝', '羊肉', '天津')
# eat('老王','小鸡炖蘑菇','肉丝','羊肉',location='天津') # 天津 老王想吃 ('小鸡炖蘑菇', '肉丝', '羊肉')，不写地点，默认是北京
# #关键字的动态传参 **表示
# def eat(**food):
#     print(food)
# eat(good_food = '肉丝',drink = "wine") #一字典形式打印 {'good_food': '肉丝', 'drink': 'wine'}
#
# def play(name,*args,place = 'China',**kwargs):
#     print(place)
#     print(name+'想要玩',args,kwargs)
# play("老王",'pingpang','basketball','socerball',place = "北京",time = "tomorrow",location = 'tiananmen square')

# #文档注释
# def he(a,b):
#     '''
#     函数实现两个数的和
#     :param a: 第一个参数
#     :param b: 第二个参数
#     :return: 返回两个数和
#     '''
#     return a + b
# print(he.__doc__) #打印函数文档
# print(str.__doc__)
# print(str.upper.__doc__) #Return a copy of the string converted to uppercase.

# #聚合
# def fun(*args,**kwargs): #无敌参数
#     print(args,kwargs)
# fun(1,2,3,a = 1,b =2) #(1, 2, 3) {'a': 1, 'b': 2}
#
# def func(*food): #聚合，位置参数
#     print(food)
# lst = ["排骨",'猪蹄','鸡块']
# func(lst) #传入的是一个参数，返回的是一个元组，元组里面一个列表，(['排骨', '猪蹄', '鸡块'],)
# func(lst[0],lst[1],lst[2]) #('排骨', '猪蹄', '鸡块')
# #打散
# func(*lst) # *代表打散，打散. 把list, tuple, set, str 进行迭代打散
# #集合打散
# def func(*food): #聚合，位置参数
#     print(food)
# st = {"排骨",'猪蹄','鸡块'}
# func(*st) #集合打散无序
#
#
# def func(**kwargs):#聚合关键字参数
#     print(kwargs)
# dic = {"name":"jasen","age":28}
# func(name = dic["name"],age = dic["age"] ) #关键字传入的方法麻烦，使用下面把实参字典打散成关键字参数再导入到函数
# func(**dic) #实参，打散成关键字参数

# #名称空间
# # 内置=>全局=>局部(函数调用)
# a = 5 #全局
# def fn(): #全局
#     b = 20 #局部
#     def gn(): #局部
#         pass
# def en():
#     pass
# #globals()查看全局内容
# print(globals())
# print(locals())#查看当前作用域内容
# #当把locals()放置函数内部，则打印当前作用域内容(函数内部)
# def hello():
#     b = 5
#     def kk():
#         a = 45
#         print(locals()) #打印kk()函数内部内容
#     kk()
#     print(locals()) #打印hello()函数内部内容
# hello()

# def outer():
#     print("outside") #1
#     def inner(): #3
#         print('first_inner') #4
#         def inner_inner():#6
#             print("inside of inner")#7
#         inner_inner() #5
#         print("dingding")#8
#     inner() #2
#     print("outside")#9
# outer()

# # global
# a = 99
# def kill():
#     global a #函数内可以通过global修改全局变量的值
#     print(a) #99
#     a = 100 #全局变量修改为100
# print(a) #99
# kill()  #调用函数后，global声明a为全局变量，引用a变量指向新的数(内存地址)
# print(a) #100
#
# # nonlocal
# a = 120
# def outer():
#     a = 110 #经过nonlocal声明后变量名指向新的数字20
#     def inner():
#         nonlocal a #修改最近的外层函数相同的变量名，指向新的数值，如果没有继续往外层的外层找，直到最外层函数没有就报错。
#         a = 20
#     inner()
#     print(a) #20
# outer()
# print(a)

# 1 2 3 4 3 3 1
# a = 1
# def fun_1():
#     a = 2 #被修改为3
#     def fun_2():
#         nonlocal a
#         a = 3
#         def fun_3():
#             a = 4
#             print(a) # 4
#         print(a) # 3
#         fun_3()
#         print(a) #3
#     print(a) # 2
#     fun_2()
#     print(a) # 3
# print(a) # 1
# fun_1()
# print(a)
#
# print("=====================")
# a = 10
# def d():
#
#     global a
#     a = 11
#     def d2():
#         pass
#     d2()
#     print(a)
# d()
# print(a)

#
# a = 1
# def fun_1():
#     a = 2 #被修改为3
#     def fun_2():
#         global a #改动的是全局的a,而不是fun_1中的a
#         a = 3
#         def fun_3():
#             a = 4
#             print(a) # 4
#         print(a) # 3
#         fun_3()
#         print(a) #3
#     print(a) # 2
#     fun_2()
#     print(a) # 2 global 对函数里没有影响
# print(a) # 1
# fun_1()
# print(a)
# a = 10
# def f1():
#     a = 11
#     def f2():
#         global a
#         a = 12
#         def f3():
#             a = 11
#         f3()
#         print("f3",a)
#     print(a)
#     f2()
#     print(a)
# f1()
# print(a)
#
# b = 20
# def z1():
#     b = 22
#     def z2():
#         global b
#         b = 12
#         def z3():
#             print('z3',b) #如果函数中没有变量赋值，则使用全局变量指向的值
#         z3()
#     z2()
#     print("z1",b) #global改变的是全局变量的值，当函数里面变量有另外赋值，打印仍然打印函数里面变量的赋值，和global无影响
# z1()

#
# # 动态串串，接收n个数字，求这些参数的和
# #solution1
# def sum_all(*nums):
#     sum = 0
#     for e in nums:
#         sum += e
#     return sum
#
# lst = [1,2,3,4,5,56]
# print(sum_all(*lst)) #利用打散
#
# #solution2
# def sum_all2(*args):
#     sum = 0
#     print(args) #测试---args是一个可迭代的元组，故可以用for循环迭代
#     for el in args:
#         sum += el
#     return sum
# print(sum_all2(1,2,3,4,5))
#
# #solution3
# def sum_all3(*args):
#     return sum(args)
# print(sum_all3(1,2,3,4,5))
#
# #了解内置函数sum的使用
# print(sum([1,2,1,2],0))#sum内两个参数，第一个参数是可迭代对象，第二个参数是起始值，不写时默认为0，将每个元素和起始值叠加之和返回
# print(sum((1,2,3,4),6)) #16
# print(sum([1,2,3,4])) #第二个参数不写时，只计算迭代对象里面的元素和
#
# #查看传入a,b后打印结果
# a = 10
# b = 20
# def text(a,b):
#     return print(b,a)
# text(a,b)
# c = text(a,b)
# print(c) #None ,打印函数print没有返回值
#
# #实参带入，不容易混淆
# a = 10
# b = 20
# def text(a,b):
#     a = 3
#     b =5
#     print(a,b) #3,5没有global,函数内不能改变外部变量值
# c = text(b,a) #函数调用时，实参直接带入即可，不要把变量名和函数里面的变量参数混淆，实参带入c = text(20,10)这样不容易乱
# print(c) #None
# print(a,b) #10,20
#
#
# #将多个可迭代对象动态传参
# def funcs(*args):
#     return args
# lst = [1,2,3]
# tu = (4,5,6)
# st = "大家好我叫**"
# c = funcs(*lst,*tu)
# print(c)
# e = funcs(*tu,*st) #将每个可迭代对象都打散，变成动态传参
#
# def fb(**kwargs):
#     return kwargs
# dic1 = {"name":"jack","age":24}
# dic2 = {"hobby":"pingpang","drink":"wine"}
# c = fb(**dic1,**dic2) #打散成关键字参数
# print(c)
#
# a = 3
# def wrapper():
#     a = 1
#     def inner():
#         nonlocal a  #内部函数没有赋值，就会报错
#         a += 1 #函数内部必须有赋值或者global或者nonlocal声明
#         print(a) #2
#     inner()
#     print(a) #2
# wrapper()
# print(a)
#
# a = 3
# def wrapper():
#     a = 1
#     def inner():
#         global a  #内部函数没有赋值，就会报错
#         a += 1 #函数内部变量值更改前，函数内部必须对变量赋值或者global或者nonlocal声明变量为全局或者临近变量
#         print(a) #4
#     inner()
#     print(a) #1
# wrapper()
# print(a) #4
#
#
# def min(a,b):
#     '''
#     接收两个数字参数，返回较小值
#     '''
#     return a if a < b else b
# print(min(20,19))
#
# #回忆下join的用法
# c = "_".join(["hello","python"])
# print(c)
#
# #输入可迭代对象，并用下划线连接成新的字符串,只使用字符
# def fun(*args):
#     c = "_".join((args))
#     return c
# print(fun(*["China","Flying"]))#先打散成单个元素
#
# #如果数字和字符串同时存在
# def fun(lst):
#     s = ""
#     for el in lst:
#         s = s + str(el) + "_"
#     return s.strip("_")
# print(fun(["name",'jack',1]))
#
# def print_max_min(*args):
#     return {"max":max(args),"min":min(args)}
# print(print_max_min(1,2,3,4,5,43,423,43,42,-5))
#
# def jiecheng(n): #阶乘
#     s = 1
#     count = n
#     while count > 0:
#         s *= count
#         count -= 1
#     return s
# print(jiecheng(4))
#
# def func():
#     lst = ["红桃","黑桃",'方片','草花']
#     lst2 = ["A",'J',"Q","K"]
#     l = []
#     for el in lst:
#         for el2 in lst2:
#             c = (el,el2)
#             l.append(c)
#     return l
# result=func()
# print(result)
#
# def outer():
#     def inner():
#         print(666)
#     return inner()
#
# #九九乘法
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%s*%s=%s"%(i,j,i+j),end = " ")
#     print()    #print("",end = "\n")
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("*",end = " ")
#     print()    #print("",end = "\n")
#
# #金字塔
# def jinzita(n):
#         for j in range(1,n+1):
#             print(int((int(2*n-1)-int(2 * j  -1)) /2)* " " , int(2 *j -1) * "*")
#
# jinzita(11)
#
# #
# def cd(eval,list = []):
#     list.append(eval)
#     print(id(list))
#     return list
# print(cd(12)) # 使用默认值时，列表是函数创建时同时分配的，所以后续再次调用函数添加元素，内存不变
# print(cd(123,[])) #没有使用默认值，函数创建后才创建新列表，分配的新内存，每次调用时都会清空内存。所以列表元素不会累加
# print(cd(456,[])) #还是列表清空后添加新元素
# print(cd(234))

# for i in range(12):
#     if i % 11 == 0:
#         print("跳出去了，当有break时，没有执行else")
#         break
# else:
#     print("上面for循环执行完毕时，才会执行else")
#     print("not found")
#
# for i in range(12):
#     print("执行%s次"%(i))
# else:
#     print("上面for循环执行完毕时，才会执行else")
#     print("not found")

# def fun1():
#     print("我是1")
# def fun2():
#     print("我是2")
# def fun3():
#     print("我是3")
# lst = [fun1,fun2,fun3]
# for el in lst:
#     el()
#
# def  my():
#     print("我是my函数")
# def proxy(fx):
#     print("代理前")
#     fx()
#     print("代理后")
# proxy(my)
# #############################################
# def  func1():
#     print("我是func1")
# def func2():
#     print("我是func2")
# def func(fx,gx): #函数名可以通过参数传递
#     print("我是func")
#     fx()
#     gx()
#     print("函数传参完毕")
# func(func1,func2) #函数名可以通过参数传递
#
# def fx1():
#     print("first words")
#     def inside():
#         print("the function inside of fx1")
#         return 1
#     return inside #此处返回语法是函数名，内部返回的是内部函数的内存地址
# print(fx1()) #<function fx1.<locals>.inside at 0x035A5E88>
# var = fx1() #用变量赋值形式指向函数地址
# var() #等同于调用函数
# #也可以这样操作
# print("-"*20)
# fx1()() #结果同上
#
# #闭包,内层函数中访问外层函数变量
# def px():
#     a = 12     #常驻内存
#     def us():
#         print(a)
#     us()
# px()
# #或者，返回函数名再调用
# def px():
#     a = 12
#     def inner():
#         print(a)
#     return inner
# px()() #函数调用
#
# #简易爬虫
# from urllib.request import urlopen
# response = urlopen("https://www.baidu.com/")
# print(response.read())
#
# #闭包 来优化爬虫
# def fs():
#     s = urlopen("https://www.baidu.com/").read()
#     def inner():
#         return s
#     return inner
# set = fs()
# print("爬取中")
# ret =set()
# print(ret)
#
# #如何查看函数是否是闭包
#
# def fx():
#     print("是不是闭包啊")
#     def inner():
#         print("不知道啊，得用__closure__测试后才知道")
#     print(inner.__closure__)
# fx() #如果为None,则不是闭包
#
# def fx():
#     print("是不是闭包啊")
#     a = "哈哈哈，你猜"
#     def inner():
#         print("不知道啊，得用__closure__测试后才知道")
#         print(a)
#     print(inner.__closure__)
# fx() #如果内部函数的__closure__打印出东西，则为闭包

# #字符串是可迭代的
# st = "字符串"
# for el in st:
#     print(el)
# #列表，元组，集合，字典都可迭代
# lst = [1,2,3]
# for el in lst:
#     print(el)
# tu = (1,2,3)
# for el in tu:
#     print(el)
# s = {1,2,3,4}
# for el in s:
#     print(el)
# dic = {"first":1,"second":2}
# for el in dic:
#     print(el) #迭代的是字典的键
# for el in dic.keys(): #迭代key
#     print(el)
# for el in dic.values(): #迭代value
#     print(el)
#
# #如果有__iter__说明可迭代
# print(dir(str))
# print(dir(list))
# print(dir(set))
# print(dir(tuple))
# print(dir(dict))
# # __iter__()可得到迭代器
# s = "神秘人"
# k = s.__iter__() #变成迭代器 <str_iterator object at 0x02CF0BB0>
# print(k)
# print(dir(k)) #迭代器里面也有__iter__,迭代器的属性也很多，只需记住__iter__和__next__
#
# print(k.__next__()) #神
# print(k.__next__()) #秘
# print(k.__next__()) #人
#
# #for内部机制原理
# s = "I like Python,it's the best computer language that i have seen"
# k = s.__iter__()            #生成迭代器
# while 1:
#     try:
#         s = k.__next__()    #获取下一个
#         print(s)
#     except StopIteration :  #处理错误
#         break
# #判断是否是可迭代的和迭代器
# #野路子方法
# lst = ["人民币",'美元','欧元','港币']
# s = lst.__iter__()
# print('__iter__' in dir(lst)) #True
# print("__next__" in dir(lst)) # False   -->说明列表是可迭代的，但不是迭代器
# print("__next__" in dir(lst.__iter__())) # True -->当列表转换为迭代器，就存在__next__()方法了
#
# #官方判断是否是可迭代的和迭代器
# #需要导入两个包
# # iterable
# # iterator
# print("line","-"*20)
# from collections.abc import Iterable
# from collections.abc import Iterator
# print(isinstance(lst,Iterable)) #True
# print(isinstance(lst,Iterator)) #False
# print(isinstance(lst.__iter__(),Iterator)) #True
#
# #
# lst = ["发哥",'星爷','大咖']
# m = lst.__iter__() #转换成迭代器
# k = list(m) # 迭代器m转化成列表的过程，list一定会循环每个元素，最后写入到列表中，有for循环就一定就有__next__(),所以list(iterator)生成的列表元素仍然是迭代器中可迭代的元素
# print(k) #["发哥",'星爷','大咖']
# #print(m.__next__()) 这样写会报错StopIteration.因为迭代器m已经迭代到最后一个元素，并通过list()转换成列表，所以就没有下一个元素了。
#
# lst = ["发哥",'星爷','大咖']
# o = lst.__iter__()
# for i in range(len(lst)):
#     print(o.__next__())
#
# lst = [1,2,3]
# #也可以这样写
# s = iter(lst)
# print(next(s))
#
# #小例子
# lst = ["小白",'菜鸟','入门','大佬']
# import sys
# s = iter(lst)
# while 1:
#     try :
#         print(s.__next__()) #或者print(next(s))
#     except StopIteration :
#         sys.exit()



print(list(g)) #[20, 21, 22, 23]n = 20
for j in range(n,-1,-1):
    print(" "* j + "*" * ((n-j)*2 +1))

lst = [1,2,3]
for a in enumerate(lst):
    print(a)
#重构
for index,v in enumerate(lst):
    print(index,v)
#或者
for index in range(len(lst)):
    print(index,end = " ")
    print(lst[index])
#字典提取key和value的方法
dic = {1:"first",2:"second"}
for k in dic:
    print(k,dic[k])
#或者
for k,v in dic.items():
    print(k,v)

def funx():
    print("哈哈哈")
    yield 1
print(funx()) #<generator object funx at 0x015D0930> 打印出来是生成器
iterator = funx()
print(iterator.__next__()) #1

def get_num():
    for i in range(20):
        yield  "拿到" + str(i) + "号"
#生成器
generator = get_num()
print(next(generator))
print(next(generator))

while 1 :
    try:
        print(next(generator))
    except StopIteration:
        print("done")
        break

#send()
def print_1():
    print("first")
    yield 1
    print("second")
    yield 2
    print("third")
    yield 3
a = print_1()
print(a.__next__())
print(a.__next__())
print(a.__next__())


def print_1():
    print("first")
    a = yield 1
    print(a)
    print("second")
    b = yield 2
    print(b)
    print("third")
    yield 3         #结尾必须是yield 结尾

k  = print_1()
#send()可以起到和next()作用，而且可以给上一个yield传值
print(k.__next__()) #开头不能用send(),因为没有上一个next()，无法传值给上一个yield，
print(k.send("我来了")) #send()里面必须有一个参数
print(k.send("他走了"))


def eat():
    print("我吃什么啊")
    a = yield "馒头"
    print("a=",a)
    b = yield "⼤饼"
    print("b=",b)
    c = yield "⾲菜盒⼦"
    print("c=",c)
    yield "GAME OVER"
    #e = yield "GAME OVER"
    # print(e)
    # yield

g = eat() #获取生成器
print(next(g)) #馒头
print(g.send("现在执行第二个yield,并且通过send()给上一个yield的变量a传值"))
print(g.send("现在是第三个yield,韭菜盒子，同时把这个字符串赋值给b,可见send()的作用和next相同，不同之处在于，send既可以执行下一步操作，而且可以给上一步操作传值"))
print(g.send("执行第四个yield game over,同时赋值给c"))
#最后不能再调用send()，因为没有下一个yield可以执行了，除非在写一个yield


#
lst = []
for i in range(1,10):
    lst.append("00" + str(i))
print(lst) #['001', '002', '003', '004', '005', '006', '007', '008', '009']
#一句话完成上面列表生产
#列表生成式
new_lst  = ["00" + str(i) for i in range(1,10)]
print(new_lst) #效果同上，方法更便捷
#语法 [结果 + for 循环 条件]
lst = [i * i for i in range(1,6) if i % 2 == 0  ]
print(lst)  #[4, 16]
lst = [i * i for i in range(1,6) if i % 2   ] # 要满足if条件，if条件必须为True才会执行，所以 if 1才会执行，所以后面不写==0 则默认i%2 ==1
print(lst) # [1, 9, 25]

print(["分手第%s次"% i for i in range(1,20)])
# 寻找名字中带有两个e的⼈的名字
names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven',
'Joe'],['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]

lst = []
for line in names:
    for name in line:
        if name.count('e') == 2:
            lst.append(name)
print(lst)
#方法二
new_lst = [name for line in names for name in line if name.count("e") == 2]
print(new_lst)

lst = [11,22,33,44]
dic = {index: value for index,value in enumerate(lst)}
print(dic) #{0: 11, 1: 22, 2: 33, 3: 44}
dic2 = {index : lst[index] for index in range(len(lst))}
print(dic2) #{0: 11, 1: 22, 2: 33, 3: 44}
#语法 {k:v for 循环 if条件筛选}
#只要前三个
dic3 = {m:lst[m] for m in range(len(lst)) if  m < 3}
print(dic3)#{0: 11, 1: 22, 2: 33}

# k,v对调
dic1={0: 11, 1: 22, 2: 33}
dic2 = {dic1[co]:co for co in dic1}
print(dic2) #{11: 0, 22: 1, 33: 2}
#方法2
print({v:k for k,v in dic1.items()}) #{11: 0, 22: 1, 33: 2}
#集合推导式
lst = [1,2,3,412,34,2423,11,1,23,23,32]
#去重
ret = {i for i in lst}
print(ret)

#生成器表达式
tu = (i for i in range(10))
print(tu) #<generator object <genexpr> at 0x03050E30>
print(tu.__next__())
print(tu.__next__())
print(tu.__next__())
print(tu.__next__())
print(tu.__next__())


def fx():
    print("nothing")
    yield 123
    yield 456
g = fx() #生成器
g1 = (i for i in g) #生成器表达式
g2 = (i for i in g1)
# print(list(g))  #[123, 456]
print(list(g1)) #[]
print(list(g2)) #[]

def add(a,b):
    return a + b
def test():
    for k in range(4): # 0123
        print(k)
        yield k
g = test()
for n in [10000,10]:
    g = (add(n,i) for i in g)
    print(id(g))
    print(g)
print(g)


