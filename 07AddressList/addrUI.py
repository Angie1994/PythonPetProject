# -*- coding: utf-8 -*-

__author__ = 'Tang Jie'

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import  *
from addUI2 import Ui_Form

class addrWholeUI(object):
    def setUI(self):
        self.setWindowTitle("通讯录")  # 窗体名称

        self.createAllObj()
        self.setAllLayout()

        #self.setLayout(self.mainLayout)
        #self.setFixedSize(680, 440)
        self.setFixedSize(self.width(), self.height())  # 将文本框设置为窗体的中心控件，填补其余的空白

        self.operateUI = childrenListUI()

    def createAllObj(self):
        horizontalHeader = ["姓名", "电话", "分组","收藏"]
        self.addrTable = QTableWidget()

        self.table = QTableWidget()        #实例化一个表格对象
        self.table.setColumnCount(len(horizontalHeader))       #表格的列数
        self.table.setRowCount(0)          #表格的行数
        self.table.setHorizontalHeaderLabels(horizontalHeader)  #表格的每列标题
        self.table.setEditTriggers(QTableWidget.NoEditTriggers) #触发修改单元格的修改
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection)   #表示列表只能单行高亮
        self.table.setAutoScroll(True)
#        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
        for index in range(self.table.columnCount()):               #遍历每一列
            headItem = self.table.horizontalHeaderItem(index)       #获取每列的标题
            headItem.setFont(QFont("song", 10, QFont.Bold))         #设置当前列标题的字体大小
            headItem.setForeground(QBrush(Qt.gray))                 #列标题的背景色
            headItem.setTextAlignment(Qt.AlignHCenter)

        self.table.setColumnWidth(40,200)
        self.table.setRowHeight(40,40)
        self.table.setFrameShape(QFrame.Raised | QFrame.WinPanel)#设定表格在布局中的嵌入样式
        #self.table.setShowGrid(False) #取消网格线
        #self.table.verticalHeader().setVisible(False) #隐藏行标题表头

        self.findLineEdit = QLineEdit(self)  # 单行编辑框用于查找
        self.addButton = QtWidgets.QPushButton("新增")
        self.delButton = QtWidgets.QPushButton("删除")
        self.chgButton = QtWidgets.QPushButton("修改")
        self.flgButton = QtWidgets.QPushButton("标记")
        self.addButton.clicked.connect(self.addAddr)
        self.delButton.clicked.connect(self.delAddr)
        self.chgButton.clicked.connect(self.chgAddr)
        #self.flgButton.clicked.connect(self.addAddrButton)
        self.findLineEdit.textChanged[str].connect(self.onChanged)

        #创建一个QAction对象，有图标
        exitAction = QAction(QIcon("G:\\python\\project\\PythonPetProject\\07AddressList\\icon\\exit.png"), "退出", self)
        exitAction.setShortcut("Ctrl+Q")            #快捷键
        exitAction.setStatusTip("退出程序")         #显示到状态栏
        exitAction.triggered.connect(self.close)    #连接信号

        addAction = QAction(QIcon("G:\\python\\project\\PythonPetProject\\07AddressList\\icon\\add.png"), "添加", self)
        addAction.setShortcut("Ctrl+B")             # 快捷键
        addAction.setStatusTip("添加联系人")        # 显示到状态栏
        addAction.triggered.connect(self.addAddr)   # 连接信号

        delAction = QAction(QIcon("G:\\python\\project\\PythonPetProject\\07AddressList\\icon\\delete.png"), "删除", self)
        delAction.setShortcut("Ctrl+D")             # 快捷键
        delAction.setStatusTip("删除联系人")         # 显示到状态栏
        delAction.triggered.connect(self.delAddr)     # 连接信号

        chgAction = QAction(QIcon(""), "修改", self)
        chgAction.setShortcut("Ctrl+G")
        chgAction.setStatusTip("修改联系人信息")
        chgAction.triggered.connect(self.chgAddr)

        helpAction = QAction(QIcon("G:\\python\\project\\PythonPetProject\\07AddressList\\icon\\help.png"), "帮助", self)
        helpAction.setShortcut("Ctrl+H")  # 快捷键
        helpAction.setStatusTip("帮助信息")  # 显示到状态栏
        # chgAction.triggered.connect(self.close)  # 连接信号

        aboutAction = QAction(QIcon(""), "关于", self)
        aboutAction.setStatusTip("关于软件")  # 显示到状态栏
        # chgAction.triggered.connect(self.close)  # 连接信号

        self.statusBar()                            #添加状态栏

        menubar = self.menuBar()                    #实例化菜单栏
        exitMenubar = self.menuBar()  # 实例化菜单栏
        fileMenu = menubar.addMenu("菜单(&M)")
        helpMenu = menubar.addMenu("帮助(&H)")

        fileMenu.addAction(addAction)
        fileMenu.addAction(delAction)
        fileMenu.addAction(chgAction)
        fileMenu.addAction(exitAction)

        helpMenu.addAction(helpAction)
        helpMenu.addAction(aboutAction)

        toolbar = self.addToolBar("基本操作")
        helpToolbar = self.addToolBar("帮助")
        toolbar.addAction(addAction)
        toolbar.addAction(delAction)
        helpToolbar.addAction(helpAction)

    def setAllLayout(self):
        self.vBoxLayout = QVBoxLayout()
        self.wholeSplitter = QSplitter(Qt.Horizontal)   # 创建一个水平分割控件
        operatLay = QtWidgets.QWidget()                   # 用于放置布局
        self.wholeSplitter.addWidget(self.table)

        operatLay.setLayout(self.vBoxLayout)
        self.wholeSplitter.addWidget(operatLay)

        self.vBoxLayout.addWidget(self.findLineEdit)
        self.vBoxLayout.addWidget(self.addButton)
        self.vBoxLayout.addWidget(self.delButton)
        self.vBoxLayout.addWidget(self.chgButton)
        self.vBoxLayout.addWidget(self.flgButton)

        self.setCentralWidget(self.wholeSplitter)

    def createComBoBox(self, argv):
        self.ComboItem = argv;

    def dataSetTable(self, argv):
        print("argv = ",argv)
        for entry in argv:
            #在表格中新插一行
            row_count = self.table.rowCount()
            self.table.insertRow(row_count)
            for x in range(1, len(entry)):
                if x == 3:
                    self.groupComb = QComboBox()
                    for groupName in self.ComboItem:
                        self.groupComb.addItem(groupName[0])
                    self.groupComb.setCurrentText(entry[x])
                    self.table.setCellWidget(row_count, x - 1, self.groupComb)  # 将对象放入表格中
                elif x == 4:
                    self.checkBox1 = QCheckBox()
                    if entry[x] != None:
                        self.checkBox1.setChecked(True)
                    self.table.setCellWidget(row_count, x - 1, self.checkBox1)
                else:
                    self.table.setItem(row_count, x - 1, QTableWidgetItem(entry[x]))

    def removeTable(self):
        self.table.clearContents();
        count = self.table.rowCount()
        for x in range(count, -1, -1):
            self.table.removeRow(x)

    def addAddr(self):
        print("add")
        self.operateUI.show()
        pass

    def delAddr(self):
        print("del")
        pass

    def chgAddr(self):
        print("chg")
        pass

class childrenListUI(QWidget,Ui_Form):
    def __init__(self):
        super(childrenListUI,self).__init__()
        self.setupUi(self)