from bs4 import BeautifulSoup
import urllib.request
import re

if __name__ == '__main__':
    urls = 'https://blog.reimu.net/archives/13286'
    # 伪装浏览器头
    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36 Qiyu/2.0.0.3"}
    req = urllib.request.Request(url=urls, headers=header)
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    baiduyun = soup.find('pre')
    #磁力链接地址
    ciliurl = baiduyun.find(text=re.compile("magne.*")).replace("\n","")[6:-5]
    #百度云提取码
    tiquma = baiduyun.find(text=re.compile("提取码.*")).replace("\n","")
    yunurl = soup.find('pre').find('a')['href']
    a = "磁力链接:"+ciliurl
    b = '百度云:'+yunurl+tiquma

    print(a)
    print(b)

