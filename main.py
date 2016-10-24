import threading
from tkinter import *
import spider


class Application(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.alertButton1 = Button(self, text='单进程爬取', command=pachong.pachong)
        self.alertButton2 = Button(self, text='多进程爬取', command=pachong.morepachong)
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

    def start(self):
        self.master.geometry('1024x800')
        self.master.title("hello_world")
        self.mainloop()


class pachong():
    def __init__(self):
        self.spider = spider.spider()

    def pachong(self):
        pachong_url = Application.nameInput.get()
        self.spider.main(pachong_url)

    def morepachong(self):
        pachong_url = Application.nameInput.get()
        self.spider.moremain(pachong_url)


class thread():
    def __init__(self):
        app = Application()
        app.start()

    def pachong(self):
        self.pachong = True
        self.thread1 = threading.Thread(target=pachong.pachong())
        self.thread1.start()

    def pgo(self):
        self.morepachong = True
        self.thread2 = threading.Thread(target=pachong.morepachong())
        self.thread2.start()

    def stop(self):
        self.pachong = False
        self.morepachong = False

    def destory(self):
        self.stop()

    def workerThread1(self):
        while self.running:
            print('1')


if __name__ == '__main__':
    thread()
