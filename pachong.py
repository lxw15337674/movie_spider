import spider
import main

class pachong():
    def __init__(self, url):
        self.url = self.Application.nameInput.get()
        self.spider = spider.spider()

    # 单进程爬虫功能
    def pachong(self):
        self.url = self.Application.nameInput.get()
        self.spider.main(self.url)

    # 多进程爬虫功能
    def morepachong(self):
        self.url = self.Application.nameInput.get()
        self.spider.moremain(self.url)
