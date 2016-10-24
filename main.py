import threading
from tkinter import *
import spider


class Application(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.spider = spider.spider()
        self.alertButton1 = Button(self, text='单进程爬取', command=self.pachong)
        self.alertButton2 = Button(self, text='多进程爬取', command=self.morepachong)
        self.nameInput = Entry(self, width=50)
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.createWidgets()

    def createWidgets(self):
        self.pack()
        self.nameInput.pack(padx=100, pady=20, )
        self.nameInput.insert(0, 'https://blog.reimu.net/')
        self.alertButton1.pack()
        self.alertButton2.pack()
        self.quitButton.pack()
    #窗口设置
    def start(self):
        self.master.geometry('1024x800')
        self.master.title("hello_world")
        self.mainloop()

    # 单进程爬虫功能
    def pachong(self):
        pachong_url = self.nameInput.get()
        self.spider.main(pachong_url)

    # 多进程爬虫功能
    def morepachong(self):
        pachong_url = self.nameInput.get()
        self.spider.moremain(pachong_url)



if __name__ == '__main__':
    app = Application()
    app.start()
