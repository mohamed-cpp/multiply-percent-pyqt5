from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os
from os import path
import sys


from window import Ui_MainWindow 

class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.num()
        self.button()

    def num(self):
        price = self.spinBox.value()
        percent = self.spinBox2.value()
        profit = price * percent / 100  
        total = profit + price
        
        profitst = str(profit)
        totalst = str(total)
        
        self.label_4.setText(profitst+" EGP")
        self.label.setText(totalst+" EGP")
        
    def button(self):
        self.pushButton.clicked.connect(self.num)
    
def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()




