from urllib import request
import re


'''
<div class="item">
                <div class="pic">
                    <em class="">26</em>
                     <span class="title">蝙蝠侠：黑暗骑士</span>
                     <span class="rating45-t"></span>
                                <span class="rating_num" property="v:average">9.1</span>
                                <span property="v:best" content="10.0"></span>
                                <span>534896人评价</span>
                        </div>'''

def main(n):
    url = 'https://movie.douban.com/top250?start=%s&filter='%n
    response = request.urlopen(url)
    content = response.read().decode('utf-8')
    some = re.search('<div class="item">.*?<div class.*?<em class="">(?P<id>\d+)</em>',content,re.S)
    print(some)
    print(some.group('id'))
main(50)