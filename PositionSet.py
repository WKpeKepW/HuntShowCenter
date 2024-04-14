from win32 import win32gui
import win32con
class PositionSet:
    __windowMode = True
    
    def __init__(self, defPos, chgPos, handler, keybind):
        self.defPos = defPos
        self.chgPos = chgPos
        self.handler = handler
        self.keybind = keybind

    def moveWindow(self):
        if self.handler == 0:
            return
        if self.__windowMode:#chgPos
            win32gui.SetWindowPos(self.handler,win32con.HWND_NOTOPMOST,self.chgPos[0],self.chgPos[1],self.chgPos[2],self.chgPos[3],win32con.SWP_NOSENDCHANGING)
        else:#defPos
            win32gui.SetWindowPos(self.handler,win32con.HWND_NOTOPMOST,self.defPos[0],self.defPos[1],self.defPos[2],self.defPos[3],win32con.SWP_NOSENDCHANGING)
        self.__windowMode = not self.__windowMode
        #print(self.__windowMode)
        #print(win32gui.GetWindowRect(self.handler))