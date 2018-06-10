#-*- coding:utf-8 -*-
'''
Create a simple window
'''

__author__ = 'TangJie'

import sys
from PyQt5.QtWidgets import QWidget, QApplication

if __name__ == '__main__':              #程序的入口
    app = QApplication(sys.argv)
    w = QWidget()
#    w.setWindowTitle('Hello PyQt5')
    w.show()
    sys.exit(app.exec_())               #保持窗口一直存在