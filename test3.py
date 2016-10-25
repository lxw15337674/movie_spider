import threading
from tkinter import *
import spider


class Application(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.spider = spider.spider()
        self.text = Text()
        self.alertButton1 = Button(self, text='单进程爬取', command=lambda: thread_it(self.pachong))
        self.alertButton2 = Button(self, text='多进程爬取', command=lambda: thread_it(self.morepachong))
        self.nameInput = Entry(self, width=50)
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.createWidgets()

    # GUI界面创建
    def createWidgets(self):
        self.pack()
        self.text.pack()
        self.nameInput.pack(padx=100, pady=20, )
        self.nameInput.insert(0, 'https://blog.reimu.net/')
        self.alertButton1.pack()
        self.alertButton2.pack()
        self.quitButton.pack()

    # 插入text
    def insert_text(self,datas):
        self.text.insert(END, datas)

    # 窗口设置
    def start(self):
        self.master.geometry('1024x800')
        self.master.title("hello_world")
        self.mainloop()

    # 单进程爬取单个网站功能
    def pachong(self):
        pachong_url = self.nameInput.get()
        datas = self.spider.pagemain(pachong_url)
        print(datas)
        #self.insert_text(datas)

    # 多进程爬取整个网站功能
    def morepachong(self):
        pachong_url = self.nameInput.get()
        datas = self.spider.moremain(pachong_url)
        self.insert_text(datas)


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
