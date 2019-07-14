#
import random
print(random.random()) #0-1小数
print(random.randint(1,3)) #[1,3]
print(random.randrange(1,3))  #[1,3)顾头不顾尾
print(random.randrange(1,200,3))
#从一个列表中随机抽取值
l = ['a','b',(1,2),123]
print(random.choice(l))
print(random.sample(l,2)) #随机抽取2个或者多个值
#打乱一个列表的顺序,在原列表的顺序上直接进行修改，节省空间
random.shuffle(l)
print(l)
#四位数字验证码
print(random.randint(1000,9999))
#六位数字验证码
print(random.randint(100000,999999))
#6位数字加字母验证码
l = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','F','G']
result = random.sample(l,6)
print(result)
s ="".join([str(x) for x in result])
print(s)

#四位数验证码
s = ""
for i in range(4):
    num = random.randint(0,9)
    s = s + str(num)
print(s)

def cal(n):
    s = ""
    for i in range(n):
        num = random.randint(0, 9)
        s = s + str(num)
    print(s)
#六位数验证码
cal(6)

#
print(chr(65)) #A

s = ""
for i in range(6):
    num = random.randint(0,9)
    alpha_lower = chr(random.randint(65,90))
    alpha_upper = chr(random.randint(97, 122))
    res = random.choice([str(num),alpha_lower,alpha_upper])
    s += res
print(s)

#时间模块time
import time
time.sleep(2)
print(time.time())  #1560752427.7262976 以秒为单位 时间戳时间 给机器计算 用的
#格式化时间
print(time.strftime("%Y-%m-%d %H:%M:%S")) # 2019-06-17 14:29:09
print(time.strftime("%y-%m-%d %H:%M:%S")) # 19-06-17 14:30:24
#结构化时间
print(time.localtime()) #time.struct_time(tm_year=2019, tm_mon=6, tm_mday=17, tm_hour=14, tm_min=30, tm_sec=24, tm_wday=0, tm_yday=168, tm_isdst=0)
t = time.localtime()
print(t.tm_year) #2019

# 1.查看一下2000000000时间戳时间表示的年月日
print(time.time())
struct_time = time.localtime(2000000000)
res = time.strftime('%Y-%m-%d %H:%M:%S',struct_time)
print(res)

# 2.将2008-8-8转换成时间戳时间

struct_time = time.strptime('2008-8-8','%Y-%m-%d')
print(struct_time)
res = time.mktime(struct_time)
print(res) #1218124800.0

# 3.请将当前时间的当前月1号的时间戳时间取出来

st1 = time.localtime()
st2 = time.strptime('%s-%s-1'%(st1.tm_year,st1.tm_mon),'%Y-%m-%d')
print(time.time())
print(time.mktime(st2))

# 4.计算时间差 - 函数
    # 2018-8-19 22:10:8 2018-8-20 11:07:3
    # 经过了多少时分秒

struct_time = time.strptime('2018-8-20 11:07:3','%Y-%m-%d %H:%M:%S')
print(struct_time)
res = time.mktime(struct_time)
print(res)

struct_time = time.strptime('2018-8-19 22:10:8','%Y-%m-%d %H:%M:%S')
print(struct_time)
res2 = time.mktime(struct_time)
print(res2)
ti = res - res2
gm_time = time.gmtime(ti) #转换成伦敦时间
print("过去了%d年%sd月%d天%d小时%d分钟%d秒"%(gm_time.tm_year-1970,gm_time.tm_mon-1,gm_time.tm_mday-1,gm_time.tm_hour,gm_time.tm_min,gm_time.tm_sec))

#sys模块 和python解释器打交道
#sys.argv
#sys.path
#sys.modules
import sys
print(sys.path)
# import re
# print(sys.modules)
# import sys
# usr = input("username")
# password = input('password')
# user = sys.argv[1]
# password = sys.argv[2]
# if user == 'alex' and password == 'alex123':
#     print('登录成功')
# else:
#     exit()
print(sys.argv)