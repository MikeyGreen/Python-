from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
res = requests.get('http://news.sina.com.cn/c/nd/2017-04-05/doc-ifycwymx3892472.shtml')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,'html.parser')
#获取新闻标题
title = soup.select('#artibodyTitle') # id用#检索
print(title)
print(title[0].string)
print(title[0].text)
date = soup.select('.time-source') #class 用.
print(date[0].contents[1])
print(date[0].contents[0])
print(soup.select('.time-source span a')[0].string)
print(soup.select('.article-editor')[0].get_text().lstrip("责任编辑：")) #或者用string 或者text结果一样
# print(soup.select('#artibody p'))
for p in soup.select('#artibody p'):

	print(p.text) #p.string由于有换行，所以会打印出None

article = []
for p in soup.select('#artibody p'):
	article.append(p.text.strip())
print(article)
print('\u3000') #相当于换行
print(2)