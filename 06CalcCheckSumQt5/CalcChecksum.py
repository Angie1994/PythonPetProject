# -*- coding:utf-8 -*-
'''
使用了标签，编辑框，按钮控件，使用了水平和垂直,
在按下“计算”按钮之后进入计算方法内进行计算
'''
__author__ = 'TangJie'

# 导入模块
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QPushButton, QLineEdit, QVBoxLayout, QMessageBox
from PyQt5 import QtGui, QtCore
import sys

# 创建一个类继承Qwidget,QWidget是所有用户界面对象的基类，所有和用户界面相关的控件类都是继承自QWidget
class ShowWindow(QWidget):

    def __init__(self):
        super(ShowWindow, self).__init__()
        self.initCheckUI()

    def initCheckUI(self):
        # 创建成员：一个标签，一个编辑行，两个按钮
        self.inputLabel = QLabel("输入十六进制字符流")
        self.editLine = QLineEdit()
        self.printButton = QPushButton("计算")
        self.clearButton = QPushButton("清空")

        # 两个按钮的点击事件连接到某个函数
        self.printButton.clicked.connect(self.printText)
        self.clearButton.clicked.connect(self.clearText)

        # 创建一个水平布局(QHBoxLayout)，将创建的对象添加到布局中
        inputLayout = QHBoxLayout()
        inputLayout.addWidget(self.inputLabel)
        inputLayout.addWidget(self.editLine)

        # 再创建一个水平布局将2个按钮放进去
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.printButton)
        buttonLayout.addWidget(self.clearButton)

        # 创建一个垂直布局，将两个水平布局对象放入
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(inputLayout)
        mainLayout.addLayout(buttonLayout)

        # 将mainLayout设置为窗口LayOut
        self.setLayout(mainLayout)
        self.setWindowTitle('校验和计算工具')  # 窗口的标题
        self.setFixedSize(300, 100)
        # self.setWindowFlags(QtCore.Qt.SplashScreen)  #窗口风格选项键，链接：https://jingyan.baidu.com/article/ac6a9a5e7a79312b653eacc0.html
        self.setFixedSize(self.width(), self.height())
        self.show()  # 显示窗口

    def printText(self):
        Hexflow = self.editLine.text()  # 获取编辑框中的文本内容
        FlowLen = len(Hexflow)
        FlowSum = 0

        if (FlowLen / 4) > (FlowLen // 4):
            QMessageBox.information(self, "输入错误", "数据流不为4的倍数，请补充至4的倍数")
        else:
            if Hexflow == '':   # 是空显示的内容
                QMessageBox.information(self, "输入错误", "输入为空，请重新输入")
            else:  # 不是空显示的内容
                n = 0
                while FlowLen > 0:
                    FlowLen -= 4
                    FlowSum += int(Hexflow[n:n+4], 16)
                    n += 4
                FlowSum = ((FlowSum & 0xffff0000) >> 16) +  (FlowSum & 0x0000ffff)
                FlowSum = (~FlowSum) & 0xffff
                QMessageBox.information(self, "运算结果", "%s\n校验和计算结果为：%x" %  (Hexflow,FlowSum))

    def clearText(self):
        Hexflow = self.editLine.text()
        if Hexflow == '':
            return
        else:
            self.editLine.clear()  # 编辑框的清除

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ShowWindow()
    sys.exit(app.exec_())  # 时间开始处理进入主循环