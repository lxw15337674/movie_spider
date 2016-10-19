from multiprocessing import Pool
from bs4 import BeautifulSoup
import urllib.request

import os

class spider(object):
    def create_folder(self):
        try:
            os.mkdir('photo')
        finally:
            os.chdir('photo')

    def _get_data(self, soup):
        res_data = {}
        #<<h2 class="entry-title"><a href="https://blog.reimu.net/archives/13161" rel="bookmark">【S0323】[无修正][ぴょん吉] ぷにかの 汉化单行本</a></h2>
        print(soup.find('h2',class_="entry-title").get_text())
        url = soup.find('h2',class_="entry-title").get_text()


    def downloading(self, urls):
        if urls is None:
            return None
        # 伪装浏览器头
        header = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36 Qiyu/2.0.0.3"}
        req = urllib.request.Request(url=urls, headers=header)
        html = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')
        data = self._get_data(self,soup)
        #for img in soup.find_all('h2',class_="entry-title"):
             #print(img)
