from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import  *

from addrUI import addrWholeUI
from addrUI2 import Ui_allForm
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

    #根据传入的参数，实时显示列表
    def onChanged(self, text):
        self.removeTable()
        self.createComBoBox(self.getColvalue())
        self.dataSetTable(self.findInTable(text))

    #添加联系人并刷新列表
    def addAddrRefresh(self, Data):
        self.dataWriteToSql(Data)
        self.removeTable()
        self.createComBoBox(self.getColvalue())
        self.dataSetTable(self.readAllSQL())


    def updateAddrRefresh(self, Data):
        #self.dataUpdateToSql(Data)
        self.delDataFromDB(Data['keyvalue'])
        self.dataWriteToSql(Data)
        self.removeTable()
        self.createComBoBox(self.getColvalue())
        self.dataSetTable(self.readAllSQL())

    def delARowData(self,Data):
        self.delDataFromDB(Data)
        self.removeTable()
        self.createComBoBox(self.getColvalue())
        self.dataSetTable(self.readAllSQL())

    def getARowData(self,Data):
        return self.getDataFromDB(Data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    exe = addrList()
    exe.show()
    sys.exit(app.exec_())