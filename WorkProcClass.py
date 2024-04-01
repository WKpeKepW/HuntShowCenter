import PositionSet as PS
from win32 import win32gui
class WorkProc:
    def __init__(self, config):
        self.handler = 0
        self.width = config.getConf("width")
        self.height = config.getConf("height")
        self.progname = config.getConf("programmName")
        self.step = config.getConf("step")
        self.keybind = config.getConf("keybind")
 
    def FindProc(self) -> bool:
        if self.progname == 'Hunt: Showdown':
            self.handler = win32gui.FindWindow(None, "Hunt: Showdown") #ищем процесс prod
        else:
            self.handler = win32gui.FindWindow("notepad", None) #debuge
            
        if self.handler == 0:
            return False
            #self.labelStart.config(text=self.programmName+' не запущен')
        else:
            #self.labelStart.config(text=self.programmName+' запущен')
            return True
            #self.btn.config(state=['disabled'])
            
            #self.__ChangePos(handler)

    def ChangePos(self):
        pos = win32gui.GetWindowRect(self.handler)# берём его текущую позицию //плохо работает 2560x1440
        print(pos)
        PS.PositionSet([0,0,int(self.width),int(self.height)],[0,int(self.step),int(self.width),int(self.height)],self.handler,self.keybind)#не меняет разрешение выше разрешения вашего монитора, может изменить если есть другой монитор ниже основного 
        #[-7,-101,pos[2],pos[3]]