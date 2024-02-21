import tkinter as tk
import PositionSet as PS
from win32 import win32gui
#import win32gui as ui
class tkinterClass:
    def __init__(self):
        window = tk.Tk()
        window.title('HuntShowCenter')
        window.geometry('200x70')
        window.resizable(False,False)
        from main import programmName
        self.programmName = programmName
        self.labelStart = tk.Label(text="Тестовый текст запущен")
        self.labelKey = tk.Label(text="Кнопка включения")
        self.btn = tk.Button(text='⟳')
        self.text = tk.Entry(width=5, state='disabled')
        self.__FindProc()
        self.btn.config(command=self.__FindProc)
        self.labelStart.place(x=5,y=10)
        self.labelKey.place(x=5,y=40)
        self.btn.place(x=160,y=10)
        self.text.place(x=160,y=40)
        window.mainloop()
    
    def __FindProc(self):
        #handler = win32gui.FindWindow(None, self.programmName) #ищем процесс prod
        handler = win32gui.FindWindow(self.programmName, None) #debuge
        if handler == 0:
            self.labelStart.config(text=self.programmName+' не запущен')
        else:
            self.labelStart.config(text=self.programmName+' запущен')
            self.btn.config(state=['disabled'])
            self.__ChangePos(handler)

    def __ChangePos(self,handler):
        pos = win32gui.GetWindowRect(handler)# берём его текущую позицию //плохо работает
        print(pos)
        PS.PositionSet('p',[0,0,1920,1080],[0,-100,1920,1180],handler)#не меняет разрешение выше разрешения вашего монитора, может изменить если есть другой монитор ниже основного 
        #[-7,-101,pos[2],pos[3]]