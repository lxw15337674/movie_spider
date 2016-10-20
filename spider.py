from bs4 import BeautifulSoup
import urllib.request
import re


class spider(object):
    def __init__(self):
        self.datas = []

    def get_downurl(self, url):
        soup = self.downloading(url)
        baiduyun = soup.find('pre')
        try:
            # 磁力链接地址
            ciliurl = baiduyun.find(text=re.compile("magne.*")).replace("\n", "")[6:-5]
            a = "磁力链接:" + ciliurl
        except:
            a = ""
        # 百度云提取码
        try:
            tiquma = baiduyun.find(text=re.compile("提取码.*")).replace("\n", "")
            yunurl = soup.find('pre').find('a')['href']
            b = '百度云:' + yunurl + tiquma
        except:
            b = ""
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
            Magnet_URI, baiduurl = self.get_downurl(url)
            if Magnet_URI:
                list = [title, url, jpg, Magnet_URI, baiduurl]
            else:
                list = [title, url, jpg, baiduurl]
            print(list)
            self.datas.append(list)

    def downloading(self, urls):
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
