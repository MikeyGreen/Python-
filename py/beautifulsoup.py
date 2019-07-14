import requests
r = requests.get('http://news.sina.com.cn/china/')
print(r)
from  bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
	<h1 id="title">我是标题</h1>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc,'html.parser')
print(soup.text) 
print(type(soup))
header = soup.select('h1') #从汤里找出含有h1标签的内容
print(header)
print(type(header))
print(header[0])
soup = BeautifulSoup(html_doc,'html.parser')
alink = soup.select('a')
print(type(alink))
print(alink)
print(alink[0])
for link in alink:
	print(link)
print('输出第一个标签',alink[0])
#使用select找出id为title的标签
soup = BeautifulSoup(html_doc,'html.parser')
ti = soup.select('#title')  # #不明白
print(ti)
res = soup.find(id = "title")
print(res) #不是列表形式
print([res])
print(soup.title) #输出第一个title标签
print(soup.title.name) #输出第一个title标签的标签名字
#tile的父标签
print(soup.title.parent)
#打印父标签name
print(soup.title.parent.name)

print(soup.head.string) #打印标签内容

# 查看p标签class属性内容
print(soup.p['class'])

#输出a标签的href内容
print(soup.a['href'])

#a标签添加一个属性
soup.a['name'] = u'china'
print(soup)  #查看是否多了一个name属性，答案是必然的

#输出所有a标签内容
print(soup.find_all('a'))








