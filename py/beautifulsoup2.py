from bs4 import BeautifulSoup
html_doc = """<html> 
    <head> 
        <title>The Dormouse's story</title> 
    </head> 
    <body> 
    <p class="title aq"> 
        <b> 
            The Dormouse's story 
        </b> 
    </p> 

    <p class="story">Once upon a time there were three little sisters; and their names were 
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>, 
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>  
        and 
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>; 
        and they lived at the bottom of a well. 
    </p> 

    <p class="story">...</p> 
    </body>
</html>"""
soup = BeautifulSoup(html_doc,'html.parser')
print(soup.p['class'])
#输出id为link2的标签
print(soup.find(id = 'link2'))

#获取所有文字内容
print(soup.get_text()) 

# 输出第一个  a 标签的所有属性信息
print(soup.a.attrs) #字典形式

#输出所有a标签的href内容
for link in soup.find_all('a'):	
	print(link.get('href')) # 或者 用  print(link['href'])
for child in soup.p.children:
	print(child)
#正则匹配，名字中带有b的标签
import re
for tag in soup.find_all(re.compile(r'b')):
	print(tag.name)

#标签两个属性 name .attrs
print(soup.name,soup.a.attrs)
#标签属性是字典形式，单个提取属性
print(soup.p['class']) #获取的第一个p标签
print(soup.p.get('class'))
head = soup.head
print(head)
print(soup.find('head'))
print(soup.contents)
print(soup.contents[0])

#NavigableString
print(type(soup.a.string))

print(type(soup.name)) #<class 'str'>

print(soup.a)
print(soup.a.string)
print(type(soup.a.string)) #<class 'bs4.element.NavigableString'>

#下标返回子节点
print(soup.contents)
print(soup.contents[0])

print("="*30)
#.children返回list生成器
for child in soup.body.children:
	print(child)
print("="*30)
#子孙节点
for son in soup.descendants:
	print(son)

print(soup.head.string) #None
print(soup.title.string)
print(soup.html.string) #None
print(soup.p.string) #None
print(soup.b.string)

print("="*30)
for string in soup.strings: #多个内容
	print(string)
print("@"*30)
for string in soup.stripped_strings: #出去多余的空白部分
	print(string)
#parent父节点
content = soup.head.title.string
print(content.parent)
print(content.parents) #<generator object PageElement.parents at 0x0310A330>
print("!"*40)
for parent in content.parents:
	print(parent.name)
p = soup.p
print(p.parent.name)

b = soup.b
print(b.parent.name)


