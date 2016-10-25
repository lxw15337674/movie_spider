from tkinter import *
import spider


class Application(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.spider = spider.spider()
        self.alertButton1 = Button(self, text='单进程爬取', command=self.quit)
        self.nameInput = Entry(self, width=50)
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.listbox = Listbox(self)
        for item in ['python', 'tkinter', 'widget']:
            self.listbox.insert(END, item)
        self.createWidgets()

    # GUI界面创建
    def createWidgets(self):
        self.pack()
        self.nameInput.pack(padx=100, pady=20, )
        self.nameInput.insert(0, 'https://blog.reimu.net/')
        self.listbox.pack()
        self.alertButton1.pack()
        self.quitButton.pack()

    # 窗口设置
    def start(self):
        self.master.geometry('1024x800')
        self.master.title("hello_world")
        self.mainloop()

if __name__ == '__main__':
    app = Application()
    app.start()