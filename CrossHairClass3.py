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
        self.chWindow.wm_attributes("-disabled", True)
        self.chWindow.config(bg = '#808080')
        self.chWindow.wm_attributes("-transparentcolor", "#808080")
        self.chWindow.wm_attributes("-topmost", True)

        self.canvas = tk.Canvas(self.chWindow,background="#808080",highlightthickness=0)
        self.selectedDraw = None

    def update(self, message):
        self.stepNeed = not self.stepNeed
        self.canvas.delete('all')
        if(message == "updateConf"):
            self.height = int(self.config.getConf("height"))
            self.width = int(self.config.getConf("width"))
            self.step = int(self.config.getConf("step"))
            self.cwidth = self.width / 2
            self.cheight = self.height / 2
        self.SelectedCrossHair(self.selectedDraw)
        #print(self.chWindow.focus_get())#self.chWindow.()
        
    def SelectedCrossHair(self, Value):
        self.selectedDraw = Value
        self.canvas.delete('all')
        if Value == "Точка":
            self.__drawPoint()
        elif Value == "Перекрестие1":
            self.__drawCross1()
        elif Value == "Перекрестие2":
            self.__drawCross2()

    def __drawPoint(self):
        if(self.stepNeed):
            self.canvas.create_oval(self.cwidth-1+self.Thickness,self.cheight-1-self.step+self.Thickness,self.cwidth-self.Thickness,self.cheight-self.step-self.Thickness,fill="white", outline="white")
        else:
            self.canvas.create_oval(self.cwidth-1+self.Thickness,self.cheight-1+self.Thickness,self.cwidth-self.Thickness,self.cheight-self.Thickness,fill="white", outline="white")
        self.canvas.pack(fill="both",expand=1)

    def __drawCross1(self):
        edge = 24
        center = 6
        if(self.stepNeed):
            self.canvas.create_rectangle(self.cwidth-1,self.cheight-center-self.step,self.cwidth-1,self.cheight-edge-self.step,fill="white", outline="white")
            self.canvas.create_rectangle(self.cwidth-1,self.cheight+center-1-self.step,self.cwidth,self.cheight+edge-self.step,fill="white", outline="white")
            self.canvas.create_rectangle(self.cwidth-center,self.cheight-1-self.step,self.cwidth-edge,self.cheight-self.step,fill="white", outline="white")
            self.canvas.create_rectangle(self.cwidth+center-1,self.cheight-1-self.step,self.cwidth+edge,self.cheight-self.step,fill="white", outline="white")
        else:
            self.canvas.create_rectangle(self.cwidth-1,self.cheight-center,self.cwidth-1,self.cheight-edge,fill="white", outline="white")
            self.canvas.create_rectangle(self.cwidth-1,self.cheight+center-1,self.cwidth,self.cheight+edge,fill="white", outline="white")
            self.canvas.create_rectangle(self.cwidth-center,self.cheight-1,self.cwidth-edge,self.cheight,fill="white", outline="white")
            self.canvas.create_rectangle(self.cwidth+center-1,self.cheight-1,self.cwidth+edge,self.cheight,fill="white", outline="white")
        self.canvas.pack(fill="both",expand=1)

    def __drawCross2(self):
        edge = 45
        center = 20
        if(self.stepNeed):
            self.canvas.create_rectangle(self.cwidth-1,self.cheight-center-self.step,self.cwidth-1,self.cheight-edge-self.step,fill="white", outline="white")
            self.canvas.create_rectangle(self.cwidth-1,self.cheight+center-1-self.step,self.cwidth,self.cheight+edge-self.step,fill="white", outline="white")
            self.canvas.create_rectangle(self.cwidth-center,self.cheight-1-self.step,self.cwidth-edge,self.cheight-self.step,fill="white", outline="white")
            self.canvas.create_rectangle(self.cwidth+center-1,self.cheight-1-self.step,self.cwidth+edge,self.cheight-self.step,fill="white", outline="white")
        else:
            self.canvas.create_rectangle(self.cwidth-1,self.cheight-center,self.cwidth-1,self.cheight-edge,fill="white", outline="white")
            self.canvas.create_rectangle(self.cwidth-1,self.cheight+center-1,self.cwidth,self.cheight+edge,fill="white", outline="white")
            self.canvas.create_rectangle(self.cwidth-center,self.cheight-1,self.cwidth-edge,self.cheight,fill="white", outline="white")
            self.canvas.create_rectangle(self.cwidth+center-1,self.cheight-1,self.cwidth+edge,self.cheight,fill="white", outline="white")
        self.canvas.pack(fill="both",expand=1)

    def drawKill(self, message):
        print("Рисую")
        if(message == "kill"):
            self.canvas.create_text(self.width-100, 100, text="☠", tags="killtag", fill="white",font=("Arial", 36))
            self.canvas.pack(fill="both",expand=1)
        elif(message == "clear"):
            self.canvas.delete("killtag")