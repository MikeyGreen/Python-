import requests
from bs4 import BeautifulSoup
res = requests.get("https://news.sina.com.cn/c/2019-07-10/doc-ihytcerm2556551.shtml")
print(type(res)) #<class 'requests.models.Response'>
res.encoding = 'utf-8'
#print(dir(res))
soup = BeautifulSoup(res.text,'html.parser')
print(soup.select('.main-title'))
print(soup.select('.main-title')[0].string)
