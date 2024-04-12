
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor

class CrossHair2(QMainWindow):
    def __init__(self, config):
        super().__init__()

        self.setGeometry(0,0,QApplication.desktop().screenGeometry().width(),QApplication.desktop().screenGeometry().height())
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.painter = QPainter()

        self.config = config
        self.updateTrigger = False
        self.width = int(self.config.getConf("width")) / 2
        self.height = int(self.config.getConf("height")) / 2
        self.step = int(self.config.getConf("step"))
        self.x = 5
        self.y = 5
    
    def SelectedCrossHair(self, Value):
        #self.destoryAllCrossHairs()
        if Value == "Точка":
            self.x = 50
            self.y = 50
            self.PaintDot()
        #elif Value == "Перекрестие":
        #    self.x = 5
        #    self.y = 10
        #    self.xcrosshair()

    def paintEvent(self, event):
        self.painter.begin(self)
        self.painter.setPen(Qt.red)
        #self.painter.drawPoint(self.x,self.y)
        #self.painter.drawRoundedRect(x=int(self.width),y=int(self.height),w=int(self.x),h=int(self.y),xRadius=float(1),yRadius=float(1))
        self.painter.drawEllipse(int(self.x),int(self.y),int(self.width),int(self.height))
        self.painter.end()