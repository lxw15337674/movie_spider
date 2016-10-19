from tkinter import *
import tkinter.messagebox as messagebox
import spider


class Application(Frame):
    def __init__(self):
        self.spider = spider.spider()
        Frame.__init__(self)
        self.alertButton = Button(self, text='爬取', command=self.pachong)
        self.nameInput = Entry(self,width=50)
        self.createWidgets()

    def createWidgets(self):
        self.pack()
        self.nameInput.pack(padx=100, pady=20,)
        self.nameInput.insert(0,'https://blog.reimu.net/')
        self.alertButton.pack()

    def pachong(self):
        pachong_url = self.nameInput.get()
        # self.spider.create_folder()
        self.spider.downloading(pachong_url)

    def start(self):
        self.master.geometry('1024x800')
        self.master.title("hello_world")
        self.mainloop()


if __name__ == '__main__':
    app = Application()
    app.start()
