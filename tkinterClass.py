import tkinter as tk
from tkinter import ttk
#import win32gui as ui
from WorkProcClass import WorkProc
from ConfigClass import Config
from CrossHairClass import CrossHair
class tkinterClass:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('HuntShowCenter')
        self.window.geometry('280x100')
        self.window.resizable(False,False)
        self.labelStart = tk.Label(text="Hunt: Showdown не запущен")
        labelBind = tk.Label(text="Кнопка включения:")
        labelSizeDisplay = tk.Label(text="Размер монитора:")
        labelWidth = tk.Label(text="Ширина:")
        labelHeight = tk.Label(text="Высота:")
        labelStep = tk.Label(text="Отклонение:")
        self.textBind = tk.Entry(width=5)
        self.textWidth = tk.Entry(width=7)
        self.textHeight = tk.Entry(width=7)
        self.textStep = tk.Entry(width=4)
        crossHairsList = ["Нет","Точка","Перекрестие"]
        crossHairsBox = ttk.Combobox(values=crossHairsList,state="readonly")
        crossHairsBox.current(0)#Config

        self.config = Config()
        self.ch = CrossHair(self.config)
        self.textWidth.insert(0, self.config.getConf('width'))
        self.textHeight.insert(0, self.config.getConf('height'))
        self.textBind.insert(0, self.config.getConf('keybind'))
        self.textStep.insert(0,self.config.getConf('step'))
        self.textBind.bind("<KeyRelease>",lambda e: self.__keySet("keybind",self.textBind,2))
        self.textWidth.bind("<KeyRelease>",lambda e: self.__keySet("width",self.textWidth,5))
        self.textHeight.bind("<KeyRelease>",lambda e: self.__keySet("height",self.textHeight,5))
        self.textStep.bind("<KeyRelease>",lambda e: self.__keySet("step",self.textStep,5))
        crossHairsBox.bind("<<ComboboxSelected>>",lambda e: self.ch.SelectedCrossHair(crossHairsBox.get()))
        
        self.labelStart.place(x=5,y=10)
        labelSizeDisplay.place(x=5,y=58)
        labelBind.place(x=5,y=39)
        self.textBind.place(x=120,y=40)
        labelWidth.place(x=5,y=78)
        self.textWidth.place(x=60,y=80)
        labelHeight.place(x=110,y=78)
        self.textHeight.place(x=160,y=80)
        labelStep.place(x=160,y=39)
        self.textStep.place(x=240,y=40)
        crossHairsBox.place(x=220,y=80,width=60,height=21)

        self.wp = WorkProc(self.config, self.ch)#Изменения при перезапуке
        self.__update()
        self.window.protocol("WM_DELETE_WINDOW", self.__exit)

        self.window.mainloop()
    
    def __update(self):
        if self.wp.FindProc() == False:
            self.window.after(500,self.__update)
        else:
            self.labelStart.config(text='Hunt: Showdown запущен')
            #self.wp.ChangePos()

    def __keySet(self, confKey, textEntry, maxdigit):
        if len(textEntry.get()) >= maxdigit:
            textEntry.delete(len(textEntry.get())-1)
        elif len(textEntry.get()) != 0:
            self.config.setConf(confKey, textEntry.get())
            self.wp.ConfigChange=True

    def __exit(self):
        self.config.ConfigSave()
        self.ch.destoryAllCrossHairs()
        self.window.destroy()