import PositionSet as PS
from win32 import win32gui
from ConfigClass import Config
class WorkProc:
    def __init__(self):
        self.handler = 0

    def FindProc(self) -> bool:
        if Config.getConf('programmName') == 'Hunt: Showdown':
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
        pos = win32gui.GetWindowRect(self.handler)# берём его текущую позицию //плохо работает
        print(pos)
        PS.PositionSet([0,0,1920,1080],[0,-100,1920,1180],self.handler)#не меняет разрешение выше разрешения вашего монитора, может изменить если есть другой монитор ниже основного 
        #[-7,-101,pos[2],pos[3]]