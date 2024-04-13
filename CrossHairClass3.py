import tkinter as tk
class CrossHair3:
    def __init__(self, config, MainWindow) -> None:
        self.config = config
        self.height = int(self.config.getConf("height"))
        self.width = int(self.config.getConf("width"))
        self.step = int(self.config.getConf("step"))
        self.config = config
        self.stepNeed = True
        self.cwidth = self.width / 2
        self.cheight = self.height / 2
        self.Thickness = 3

        self.chWindow = tk.Toplevel(MainWindow)
        self.chWindow.geometry(f"{self.width}x{self.height}")
        self.chWindow.overrideredirect(1)
        self.chWindow.wm_attributes("-topmost", True)
        self.chWindow.wm_attributes("-disabled", True)
        self.chWindow.config(bg = '#add123')
        self.chWindow.wm_attributes("-transparentcolor", "#add123")

        self.canvas = tk.Canvas(self.chWindow,background="#add123",highlightthickness=0)
        self.selectedDraw = None

    def update(self, messageResetConf):
        self.stepNeed = not self.stepNeed
        self.canvas.delete('all')
        if(messageResetConf):
            self.width = int(self.config.getConf("width")) / 2
            self.height = int(self.config.getConf("height")) / 2
        self.SelectedCrossHair(self.selectedDraw)
        
    def SelectedCrossHair(self, Value):
        self.selectedDraw = Value
        self.canvas.delete('all')
        if Value == "Точка":
            self.drawPoint()
        elif Value == "Перекрестие":
            self.drawCross()

    def drawPoint(self):
        if(self.stepNeed):
            self.canvas.create_oval(self.cwidth+self.Thickness,self.cheight-self.step+self.Thickness,self.cwidth-self.Thickness,self.cheight-self.step-self.Thickness,fill="white")
        else:
            self.canvas.create_oval(self.cwidth+self.Thickness,self.cheight+self.Thickness,self.cwidth-self.Thickness,self.cheight-self.Thickness,fill="white")
        self.canvas.pack(fill="both",expand=1)

    def drawCross(self):
        if(self.stepNeed):
            self.canvas.create_rectangle(self.cwidth-4,self.cheight-4-self.step,self.cwidth,self.cheight-18-self.step,fill="white")
            self.canvas.create_rectangle(self.cwidth-6,self.cheight-2-self.step,self.cwidth-20,self.cheight+2-self.step,fill="white")
            self.canvas.create_rectangle(self.cwidth-4,self.cheight+4-self.step,self.cwidth,self.cheight+18-self.step,fill="white")
            self.canvas.create_rectangle(self.cwidth+2,self.cheight-2-self.step,self.cwidth+16,self.cheight+2-self.step,fill="white")
        else:
            self.canvas.create_rectangle(self.cwidth-4,self.cheight-4,self.cwidth,self.cheight-18,fill="white")
            self.canvas.create_rectangle(self.cwidth-6,self.cheight-2,self.cwidth-20,self.cheight+2,fill="white")
            self.canvas.create_rectangle(self.cwidth-4,self.cheight+4,self.cwidth,self.cheight+18,fill="white")
            self.canvas.create_rectangle(self.cwidth+2,self.cheight-2,self.cwidth+16,self.cheight+2,fill="white")
        self.canvas.pack(fill="both",expand=1)