from PyQt5.QtWidgets import *
from addrUI import addrWholeUI
from addrSQL import sqlOperate
import sys
import os

__author__ = 'Tang Jie'

class addrList(QMainWindow, QWidget, addrWholeUI, sqlOperate):
    def __init__(self):
        super(addrList, self).__init__()
        self.setUI()
        self.openSQL()

        self.createComBoBox(self.getColvalue())
        self.dataSetTable(self.readAllSQL())

    def onChanged(self, text):
        self.removeTable()
        self.dataSetTable(self.findInTable(text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    exe = addrList()
    exe.show()
    sys.exit(app.exec_())