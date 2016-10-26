import threading
from tkinter import *

import time

import spider


class Application(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.spider = spider.spider()
        self.text = Text()
        self.alertButton1 = Button(self, text='单进程爬取网页', command=lambda: thread_it(self.pachong))
        self.alertButton2 = Button(self, text='多进程爬取网站', command=lambda: thread_it(self.morepachong))
        self.nameInput = Entry(self, width=50)
        self.listbox = Listbox(self)
        self.quitButton = Button(self, text='Quit', command=self.quit)


    # GUI界面创建
    def createWidgets(self):
        self.pack()
        self.text.pack()
        self.nameInput.pack(padx=100, pady=20)
        self.nameInput.insert(END,'https://blog.reimu.net/')
        self.alertButton1.pack()
        self.alertButton2.pack()
        self.quitButton.pack()

    # 插入text
    def insert_text(self,datas):
        self.text.insert(END, datas)

    # 窗口设置
    def start(self):
        self.createWidgets()
        self.master.geometry('600x400')
        self.master.title("hello_world")
        self.mainloop()

    # 单进程爬取单个网页功能
    def pachong(self):
        start = time.time()
        self.insert_text('爬取开始\n')
        pachong_url = self.nameInput.get()
        self.spider.main(pachong_url)
        end = time.time()
        self.insert_text("爬取结束,用时%s秒" % (round(end - start, 3)))


    # 多进程爬取整个网站功能
    def morepachong(self):
        start = time.time()
        self.insert_text('爬取开始\n')
        pachong_url = self.nameInput.get()
        self.spider.moremain(pachong_url)
        end = time.time()
        self.insert_text("爬取结束,用时%s秒" % (round(end - start, 3)))


# 功能创建线程并运行
def thread_it(func, *args):
    # 创建
    t = threading.Thread(target=func, args=args)
    # 守护
    t.setDaemon(True)
    # 启动
    t.start()
    # 阻塞--卡死界面
    # t.join()


if __name__ == '__main__':
    app = Application()
    app.start()
