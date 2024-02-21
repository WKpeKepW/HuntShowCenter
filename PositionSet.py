import keyboard as keyb
from win32 import win32gui
class PositionSet:
    __windowMode = True
    __firstTab = True
    
    def __init__(self, keyValue, defPos, chgPos, handler):
        #from main import programmName
        #self.programmName = programmName
        self.keyValue = keyValue
        self.defPos = defPos
        self.chgPos = chgPos
        self.handler = handler
        self.keyEvent()


    def keyEvent(self):
        keyb.on_press_key(self.keyValue,lambda _:self.moveWindow())

    def moveWindow(self):
        if self.handler == 0:
            return
        #if self.__windowMode and self.__firstTab:
        #    ui.MoveWindow(self.handler,self.chgPos[0],self.chgPos[1],self.chgPos[2],self.chgPos[3],True)
        #    self.__firstTab = False
        #el
        if self.__windowMode:#chgPos
            win32gui.MoveWindow(self.handler,self.chgPos[0],self.chgPos[1],self.chgPos[2],self.chgPos[3],True)#0-7,0-1,1933,1080 default
        else:#defPos
            win32gui.MoveWindow(self.handler,self.defPos[0],self.defPos[1],self.defPos[2],self.defPos[3],True)
        self.__windowMode = not self.__windowMode
        print(self.__windowMode)
        print(win32gui.GetWindowRect(self.handler))
