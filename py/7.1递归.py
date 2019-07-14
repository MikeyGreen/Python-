# i= 1
# def fun():
#     global i
#     print("调用%s"%i)
#     i += 1
#     fun()
# fun()

#查看路径下文件名
import os
def finding(filepath,n):
    filename = os.listdir(filepath)

    for file in filename:
        file_p = os.path.join(filepath, file)
        if os.path.isdir(file_p):
            print('\t'*n,file)
            finding(file_p,n +1)
        else:
            print("\t"*n,file)
    return
finding('D:/软件包',1)