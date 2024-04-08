import tkinter as tk
class CrossHair:
    def __init__(self, config) -> None:
        self.config = config
        self.listWindows = list()
        self.updateTrigger = False
        self.width = int(self.config.getConf("width")) / 2
        self.height = int(self.config.getConf("height")) / 2
        self.step = int(self.config.getConf("step"))
        self.x = 5
        self.y = 5
    
    def update(self, message):
        if len(self.listWindows):
            if(message):
                self.width = int(self.config.getConf("width")) / 2
                self.height = int(self.config.getConf("height")) / 2
            if(self.updateTrigger):
                for elem in self.listWindows:
                    elem.geometry(f"{self.x}x{self.y}+{self.height}+{self.width}")
            else:
                for elem in self.listWindows:
                    elem.geometry(f"{self.x}x{self.y}+{self.height - self.step}+{self.width}")
        self.updateTrigger = not self.updateTrigger

    def SelectedCrossHair(self, Value):
        self.destoryAllCrossHairs()
        if Value == "Точка":
            self.x = 50
            self.y = 50
            self.PointCrossHair()
        elif Value == "Перекрестие":
            self.x = 5
            self.y = 10
            self.xcrosshair()

    def PointCrossHair(self):
        pch = self.__defaultCreate(int(self.height),int(self.width))

    def xcrosshair(self):
        pass

    def __defaultCreate(self, height, width, color = "red"):
        chWindow = tk.Tk()
        chWindow.overrideredirect(True)
        print(self.x)
        print(self.y)
        print(height)
        print(width)
        chWindow.geometry(f"{self.x}x{self.y}+{width}+{height}")
        #chWindow.geometry(f"50x50+0+0")#Перестало отображаться окно
        chWindow.lift()
        chWindow.wm_attributes("-disabled", True)
        chWindow.wm_attributes("-transparentcolor","white")
        chWindow.configure(background=color)#Белый не отображажеться
        self.listWindows.append(chWindow)
        return chWindow
    
    def destoryAllCrossHairs(self):
        if len(self.listWindows) != 0:
            for elem in self.listWindows:
                elem.destroy()
            self.listWindows.clear()