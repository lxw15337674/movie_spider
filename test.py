from bs4 import BeautifulSoup
import urllib.request
import re


class demo(object):
    def __init__(self):
        self.datas = []

    def get_baiduyun(self, url):
        soup = self.downloading(url)
        baiduyun = soup.find('pre')
        list = []
        for a in baiduyun:
            try:
                b = a.split('\n', 2)
                list.append(b[:2])
            except:
                pass
        yunurl = soup.find('pre').find('a')['href']
        a = "磁力链接:" + list[0][1]
        b = '百度云:' + yunurl + list[1][0]
        return a, b

    def get_data(self, soup):
        for a in soup.find_all('article'):
            b = a.find('h2', class_="entry-title")
            title = b.text
            # 去除没有番号的标题网页
            if re.match('【.*】', title) is None:
                continue
            c = a.find('a')
            url = c['href']
            # 获取图片地址
            try:
                for img in a.find_all('img'):
                    jpg = img['src']
            except:
                continue
            Magnet_URI, baiduurl = self.get_baiduyun(url)
            list = [title, url, jpg, Magnet_URI, baiduurl]
            print(list)
            self.datas.append(list)

    def downloading(self,urls):
        if urls is None:
            return None
        # 伪装浏览器头
        header = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36 Qiyu/2.0.0.3"}
        req = urllib.request.Request(url=urls, headers=header)
        html = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def main(self, urls):
        soup = self.downloading(urls)
        self.get_data(soup)

if __name__ == '__main__':
    demo1 = demo()
    demo1.main('https://blog.reimu.net/')
