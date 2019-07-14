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
</html>
"""
soup = BeautifulSoup(html_doc,'html.parser')
print(soup.p.next_sibling) #空行或者换行也是节点
print(soup.p.prev_sibling) #None
print(soup.p.next_sibling.next_sibling)
print(soup.p.next_sibling.next_sibling.next_sibling.next_sibling) #<p class="story">...</p>
print("@"*40)

#next只能针对单一元素进行.next，或者说是对contents列表元素的挨个清点
print(soup.contents[0].next) #换行符 \n

for sibling in soup.a.next_siblings:
    print(repr(sibling)) #repr()返回一个对象的字符串格式，空格和换行符都是打印出来
#next_element .previous_element
print("#"*40)
for element in soup.head.next_elements:
    print(repr(element))


print(soup.find_all('title'))
print(soup.find_all('a',"sister"))
print(soup.find_all('a',id = "link1"))
print(soup.find_all('a',href = "http://example.com/lacie"))
#如果传入列表参数,Beautiful Soup会将与列表中任一元素匹配的内容返回.下面代码找到文档中所有<a>标签和<b>标签
print(soup.find_all(['a','b']))
#True 可以匹配任何值,下面代码查找到所有的tag,但是不会返回字符串节点
for tag in soup.find_all(True):
    print(tag.name)
#关键字不能作为表达式，但是可以通过 find_all() 方法的 attrs 参数定义一个字典参数来搜索包含特殊属性的tag    
print(soup.find_all(attrs = {'class':"sister",'id':'link3'}))

print(soup.find_all(text = "Elsie")) #通过 text 参数可以搜搜文档中的字符串内容.与 name 参数的可选值一样, text 参数接受 字符串 , 正则表达式 , 列表, True。 

import re
print(soup.find_all(text = re.compile('Dormouse')))

#文档树中有3个tag符合搜索条件,但结果只返回了2个,因为我们限制了返回数量

print(soup.find_all('a',limit = 2))

print(soup.find(re.compile('^p')) )    # 搜索符合正则的tag, 如:find(re.compile('^p')) 搜索以p开头的tag  
print('----------')
print(soup.find(True))
