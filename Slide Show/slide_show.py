# PyQT Version
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, qApp, QFileDialog
from PyQt5.uic import loadUiType
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer
from circularLinkedList import CircularLinkedList
import random

form_class = loadUiType("imageViewer.ui")[0]

class ViewerClass(QMainWindow, form_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.actionSelect.triggered.connect(self.fileSelect) # file select window
        self.actionExit.triggered.connect(qApp.quit)
        self.pushButtonSlideShow.clicked.connect(self.buttonClickedSlideShow)
        self.pushButtonNext.clicked.connect(self.buttonClickedNext)
        self.pushButtonShuffle.clicked.connect(self.buttonClickedShuffle)
        
        self.fname = None
        self.fnameCircular = CircularLinkedList()
        self.qPixmapVar = QPixmap()

    def fileSelect(self): # 일단 fname을 증가시키면서 뽑아보는 것 부터
        self.fname = QFileDialog.getOpenFileNames(self) # 폴더 선택으로 뽑아보기 04.03
        for i in self.fname[0]:
            self.fnameCircular.append(i)
        self.fnameCircular = self.fnameCircular.root.link
        self.qPixmapVar.load(self.fnameCircular.item) # 
        self.qPixmapVar = self.qPixmapVar.scaled(700, 400, aspectRatioMode=True) 
        self.label.setPixmap(self.qPixmapVar)


    def buttonClickedSlideShow(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.buttonClickedNext)
        self.timer.start(3000)
            
    def buttonClickedNext(self):
        self.fnameCircular = self.fnameCircular.link
        self.qPixmapVar.load(self.fnameCircular.item)
        self.qPixmapVar = self.qPixmapVar.scaled(700, 400, aspectRatioMode=True) 
        self.label.setPixmap(self.qPixmapVar)

    def buttonClickedShuffle(self):
        random.shuffle(self.fname[0])
        self.fnameCircular = CircularLinkedList()
        for i in self.fname[0]:
            self.fnameCircular.append(i)
        self.fnameCircular = self.fnameCircular.root.link
        self.qPixmapVar.load(self.fnameCircular.item)
        self.qPixmapVar = self.qPixmapVar.scaled(700,400,aspectRatioMode=True)

app = QApplication(sys.argv)
myWindow = ViewerClass(None)
myWindow.show()
app.exec_()