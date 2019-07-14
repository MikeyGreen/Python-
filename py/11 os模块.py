import os
# os.mkdir('dir3')  #创建单个文件
# os.makedirs('dir3\dir4') #创建多个文件
#只能删除空文件夹
# os.rmdir('dir3\dir4') #删除单个文件
# os.removedirs('dir3\dir4') #若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推

print(os.listdir(r'c:\Users\HUAWEI\Desktop\py'))
file_lst = os.listdir(r'c:\Users\HUAWEI\Desktop\py')
for path in file_lst:
    print('\\'.join((r'c:\Users\HUAWEI\Desktop\py',path)))

print("="*50)
#无法确实实在windows或者linux系统时
#使用 os.path.join()
file_lst = os.listdir(r'c:\Users\HUAWEI\Desktop\py')
for path in file_lst:
    print(os.path.join(r'c:\Users\HUAWEI\Desktop\py',path))
os.system('dir')
ret = os.popen('dir')
print(ret.read())
#查看当前工作目录
print(os.getcwd()) #并不是当前文件所在目录，而是执行的文件所在的目录

import sys
print(sys.path) #所有能导入的模块的文件路径都在sys.path列表中
print(sys.modules) #所有被导入的模块地址都在sys.modules

#返回规范化的文件路径
path = os.path.abspath(r'C:\Users\HUAWEI\Desktop\py\11 os模块.py')
print(path)
path2 = os.path.abspath(r'11 os模块.py')
print(path2)

#分割开文件和路径
print(os.path.split(r'C:\Users\HUAWEI\Desktop\py\11 os模块.py'))
print(os.path.split(r'C:\Users\HUAWEI\Desktop\py'))
#分离文件夹名和文件名
ret1 = os.path.dirname(r'C:\Users\HUAWEI\Desktop\py\11 os模块.py')
ret2 = os.path.basename(r'C:\Users\HUAWEI\Desktop\py\11 os模块.py')
print(ret1)
print(ret2)
#判断文件或者文件夹是否存在
res = os.path.exists(r'C:\Users\HUAWEI\Desktop\py\11 os模块.py')
print(res) #True
#判断是否是绝对路径
res1 = os.path.isabs(r'11 os模块.py')
res2 = os.path.isabs(r'C:\Users\HUAWEI\Desktop\py\11 os模块.py')
print(res1) #False
print(res2) #True
print(os.listdir(r'C:\Users\HUAWEI\Desktop'))
#判断是文件
print(os.path.isdir(r'C:\Users\HUAWEI\Desktop\py\11 os模块.py'))
print(os.path.isfile(r'C:\Users\HUAWEI\Desktop\py\11 os模块.py'))
#拼路径
print(os.path.join(r'C:\Users\HUAWEI\Desktop\py','11.txt'))
print(os.path.getatime(r'C:\Users\HUAWEI\Desktop\py\11 os模块.py')) #查看最后访问时间
print(os.path.getmtime(r'C:\Users\HUAWEI\Desktop\py\11 os模块.py')) #查看最后修改时间
print(os.path.getsize(r'C:\Users\HUAWEI\Desktop\py\11 os模块.py')) #查看文件大小
