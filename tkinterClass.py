import tkinter as tk
#import win32gui as ui
from WorkProcClass import WorkProc
from ConfigClass import Config
class tkinterClass:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('HuntShowCenter')
        self.window.geometry('200x70')
        self.window.resizable(False,False)
        self.labelStart = tk.Label(text="Hunt: Showdown не запущен")
        labelKey = tk.Label(text="Кнопка включения")
        self.text = tk.Entry(width=5)
        self.text.insert(0, Config.getConf('keybind'))
        self.text.bind("<KeyRelease>",self.__keyBind)
        self.labelStart.place(x=5,y=10)
        labelKey.place(x=5,y=40)
        self.text.place(x=160,y=40)
        self.wp = WorkProc()
        self.__update()
        self.window.mainloop()
    
    def __update(self):
        if self.wp.FindProc() == False:
            self.window.after(500,self.__update)
        else:
            self.labelStart.config(text='Hunt: Showdown запущен')
            self.wp.ChangePos()

    def __keyBind(self, e):
        print(len(self.text.get()))
        if len(self.text.get()) >= 2:
            self.text.delete(1)
        elif len(self.text.get()) != 0:
            Config.setConf('keybind',self.text.get())