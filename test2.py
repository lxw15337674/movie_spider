from bs4 import BeautifulSoup
import urllib.request
import re

if __name__ == '__main__':
    urls = 'https://blog.reimu.net/archives/13291'
    # 伪装浏览器头
    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36 Qiyu/2.0.0.3"}
    req = urllib.request.Request(url=urls, headers=header)
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    list = []
    baiduyun = soup.find('pre')
    for a in baiduyun:
        try:
            b = a.split('\n', 2)
            list.append(b[:2])
        except:
            pass
    yunurl = soup.find('pre').find('a')['href']
    a = "磁力链接:"+list[0][1]
    b = '百度云:'+yunurl+list[1][0]
    print(a)
    print(b)

