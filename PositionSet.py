import keyboard as keyb
from win32 import win32gui
from win32 import win32api
import pywintypes
import win32con
from ConfigClass import Config
class PositionSet:
    __windowMode = True
    #__firstTab = True
    
    def __init__(self, defPos, chgPos, handler):
        #from main import programmName
        #self.programmName = programmName
        self.defPos = defPos
        self.chgPos = chgPos
        self.handler = handler
        self.keyEvent()


    def keyEvent(self):
        keyb.on_press_key(Config.getConf('keybind'),lambda _:self.__moveWindow())
        #keyb.on_press_key(Config.getConf('keybind'),lambda _:self.ChgResolution())
        #print(win32api.EnumDisplayDevices())
        #self.ChgResolution(1920,1180)

    def __moveWindow(self):
        if self.handler == 0:
            return
        #if self.__windowMode and self.__firstTab:
        #    ui.MoveWindow(self.handler,self.chgPos[0],self.chgPos[1],self.chgPos[2],self.chgPos[3],True)
        #    self.__firstTab = False
        #el
        if self.__windowMode:#chgPos
            #win32gui.MoveWindow(self.handler,self.chgPos[0],self.chgPos[1],self.chgPos[2],self.chgPos[3],True)#0-7,0-1,1933,1080 default
            win32gui.SetWindowPos(self.handler,win32con.HWND_TOPMOST,self.chgPos[0],self.chgPos[1],self.chgPos[2],self.chgPos[3],win32con.SWP_NOSENDCHANGING)
        else:#defPos
            win32gui.SetWindowPos(self.handler,win32con.HWND_TOPMOST,self.defPos[0],self.defPos[1],self.defPos[2],self.defPos[3],win32con.SWP_NOSENDCHANGING)
            #win32gui.MoveWindow(self.handler,self.defPos[0],self.defPos[1],self.defPos[2],self.defPos[3],True)
        self.__windowMode = not self.__windowMode
        print(self.__windowMode)
        print(win32gui.GetWindowRect(self.handler))

    def ChgResolution(self, width = 1600, height = 900):
        #print("yes")
        win32api.SendMessage(self.handler,win32con.WM_DISPLAYCHANGE,None, width | height)
        