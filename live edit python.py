from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import os
from os import path
import sys
import clipboard


FORM_CLASS,_=loadUiType(path.join(path.dirname(__file__),"untitled.ui"))

class MainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.num()
        self.button()
        self.copyer()

    def num(self):
        global totalst
        price = self.spinBox.value()
        percent = self.spinBox2.value()
        profit = price * percent / 100  
        total = profit + price
        
        profitst = str(profit)
        totalst = str(total)
        
        self.label_4.setText(profitst+" EGP")
        self.label.setText(totalst+" EGP")

        
    def copyer(self):
        clipboard.copy(totalst)  
        #text = clipboard.paste()


    def button(self): 
        self.pushButton.clicked.connect(self.num)
        self.pushButton_2.clicked.connect(self.copyer)
def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()




