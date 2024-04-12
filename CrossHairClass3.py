import tkinter as tk
class CrossHair3:
    def __init__(self, config, MainWindow) -> None:
        self.config = config
        self.height = int(self.config.getConf("height"))
        self.width = int(self.config.getConf("width"))
        self.step = int(self.config.getConf("step"))
        self.config = config
        #self.updateTrigger = False
        self.cwidth = self.width / 2
        self.cheight = self.width / 2

        self.chWindow = tk.Toplevel(MainWindow)
        self.chWindow.geometry(f"{self.width}x{self.height}")
        self.chWindow.overrideredirect(1)
        self.chWindow.wm_attributes("-topmost", True)
        self.chWindow.wm_attributes("-disabled", True)
        self.chWindow.config(bg = '#add123')
        self.chWindow.wm_attributes("-transparentcolor", "#add123")

    def SelectedCrossHair(self, Value):
        if Value == "Точка":
            # self.x = 50
            # self.y = 50
            self.drawPoint()
        elif Value == "Перекрестие":
            self.x = 5
            self.y = 10
            #self.xcrosshair()

    def drawPoint(self):
        self.canvas = tk.Canvas(self.chWindow,background="#add123",highlightthickness=0)
        #self.canvas.config(bg='')
        self.canvas.create_line(160,450,10,440) # л,длина,п
        self.canvas.pack(fill="both",expand=1)