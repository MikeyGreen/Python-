
#不能用eval
s='1 - 2 * ((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'

print(eval(s))

import re
s = s.strip()
ret = re.search("\([^()]+\)",s)
print(type(ret.group()))
c = ret.group()
a = eval(ret.group())

print(s.replace(c,str(a)))