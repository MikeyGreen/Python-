# #listdir stat
# import os
# print(os.listdir('d:'))
# files = os.listdir('d:')
# for file in files:
# 	print(file)

# print(os.stat("D:/345.jpg")) #返回文件的相关系统信息
# print(os.stat('d:/345.jpg').st_atime) #查看最后访问文件的时间
# print(os.stat('d:/345.jpg').st_mtime) #查看文件的最后修改时间
# print(os.stat('d:/345.jpg').st_ctime) #文件创建时间
# print(os.stat('d:/345.jpg').st_size) #文件字节大小

# import time
# print(dir(time))
# print(time.localtime())
# print(time.asctime(time.localtime(time.time()))) #格式化时间

# #查看当前工作目录
# print(os.getcwd())
# name = "jao"
# age = 16
# sex = 'man'
# print(name,age,sex,end = " ",sep = "**") #sep分隔符

# f = open("日记本.txt",'w')
# print('2019年7月13日阅读完一本书'，file = f)
from pillowfrom PIL import Image, ImageDraw, ImageFont

def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text((width-40, 0), '99', font=myfont, fill=fillcolor)
    img.save('result.jpg','jpeg')

    return 0
if __name__ == '__main__':
    image = Image.open('image.jpg')
    add_num(image) import Image, ImageDraw, ImageFont

def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text((width-40, 0), '99', font=myfont, fill=fillcolor)
    img.save('result.jpg','jpeg')

    return 0
if __name__ == '__main__':
    image = Image.open('image.jpg')
    add_num(image)