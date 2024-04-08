import PositionSet as PS
import keyboard as keyb
from win32 import win32gui
class WorkProc:
    def __init__(self, config):
        self.handler = 0
        self.config = config
        self.ps = None
        self.ConfigChange = False
        self.confUpdate()
        keyb.on_press_key(self.keybind,lambda _:self.keyEvent())

    def confUpdate(self):
        if self.ConfigChange == True:
            self.config.ConfigSave()
            self.config.Reopen()
            self.ConfigChange = False
        self.width = self.config.getConf("width")
        self.height = self.config.getConf("height")
        self.progname = self.config.getConf("programmName")
        self.step = self.config.getConf("step")
        self.keybind = self.config.getConf("keybind")
 
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

    def __ChangePos(self):
        self.ps = PS.PositionSet([0,0,int(self.width),int(self.height)],[0,int(self.step),int(self.width),int(self.height)],self.handler,self.keybind)#не меняет разрешение выше разрешения вашего монитора, может изменить если есть другой монитор ниже основного 
        #[-7,-101,pos[2],pos[3]]

    def keyEvent(self):
        change = False
        if(self.ps == None):
            self.FindProc()#ищем первый раз когда кнопка нажата чтобы точно убедиться что нашли нужный хендлер
            change = True
        if(self.ConfigChange):
            self.confUpdate()
            change = True
        if(change):
            self.__ChangePos()
        self.ps.moveWindow()