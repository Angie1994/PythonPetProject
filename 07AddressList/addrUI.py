# -*- coding: utf-8 -*-

__author__ = 'Tang Jie'

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import  *
from addrUI2 import Ui_allForm

class addrWholeUI(object):
    def setUI(self):
        self.setWindowTitle("通讯录")  # 窗体名称

        self.createAllObj()
        self.setAllLayout()

        #self.setLayout(self.mainLayout)
        #self.setFixedSize(680, 440)
        self.setFixedSize(self.width(), self.height())  # 将文本框设置为窗体的中心控件，填补其余的空白

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
        self.flgButton = QtWidgets.QPushButton("显示收藏")
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
        #helpAction.triggered.connect(self.selectAboutQt)  # 连接信号

        aboutAction = QAction(QIcon(""), "关于", self)
        aboutAction.setStatusTip("关于软件")  # 显示到状态栏
        aboutAction.triggered.connect(self.selectAbout)  # 连接信号

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
            for x in range(0, len(entry)):
                if x == 2:
                    self.groupComb = QComboBox()
                    for groupName in self.ComboItem:
                        self.groupComb.addItem(groupName[0])
                    self.groupComb.setCurrentText(entry[x])
                    self.table.setCellWidget(row_count, x, self.groupComb)  # 将对象放入表格中
                elif x == 3:
                    self.checkBox1 = QCheckBox()
                    if entry[x] != '0':
                        self.checkBox1.setChecked(True)
                    self.table.setCellWidget(row_count, x, self.checkBox1)
                else:
                    self.table.setItem(row_count, x, QTableWidgetItem(entry[x]))

    def removeTable(self):
        self.table.clearContents();
        count = self.table.rowCount()
        for x in range(count, -1, -1):
            self.table.removeRow(x)

    def addAddr(self):
        self.operateUI = childrenListUI(title='添加联系人')  # 新开一个窗口
        self.operateUI.retSignal.connect(self.addAddrRefresh)
        self.operateUI.show()

    def delAddr(self):
        try:
            Data = self.table.item(self.table.currentRow(), 1).text()
            self.delARowData(Data)
        except:
            pass

    def chgAddr(self):
        '''解决方法：再设置一个tei作为key，在更新的时候将tel传到'''
        Data = self.table.item(self.table.currentRow(), 1).text()
        getData = self.getARowData(Data)
        print("Chg:",getData)
        self.operateUI = childrenListUI(title = '修改联系人',
                                        name  = getData[0],
                                        tel   = getData[1],
                                        agroup= getData[2],
                                        flag  = getData[3],
                                        email = getData[4],
                                        address=getData[5],
                                        remark =getData[6],
                                        birthday=getData[7])
        self.operateUI.retSignal.connect(self.updateAddrRefresh)
        self.operateUI.show()

    def selectAbout(self):
        # 简介信息框，只有一个YES按钮
        QMessageBox.about(self, "关于", "通讯录 version 1.0\nCopyright 2018 TangJ.\n All Right reserved.")



class childrenListUI(QWidget,Ui_allForm):
    retSignal = pyqtSignal(dict)        #定义一个信号，信号所携带的内容

    def __init__(self,**argv):
        super(childrenListUI,self).__init__()
        self.keyValue = ""                  #用于保存修改某些值之前的key值
        self.setupUi(self)
        self.setWindowTitle(argv['title'])  # 窗体名称
        print("children window data:", argv)
        try:
            if argv['tel'] != None:
                self.keyValue = argv['tel'] #保存关键字
            if argv['flag'] != '0':
                self.checkBox_like.setChecked(True)
            self.lineEdit_name.setText(argv['name'])
            self.lineEdit_tel.setText(argv['tel'])
            self.lineEdit_email.setText(argv['email'])
            self.dateEdit_birthday.setDate(argv['birthday'])
            self.textEdit_info.setText(argv['remark'])
            self.lineEdit_group.setText(argv['agroup'])
            self.textEdit_addr.setText(argv['address'])
        except:
            pass

    def okButtonEvent(self):
        #设置好的新值
        name = self.lineEdit_name.text()
        tel = self.lineEdit_tel.text()
        email = self.lineEdit_email.text()
        birthday = self.dateEdit_birthday.text()
        agroup = self.lineEdit_group.text()
        flag = self.checkBox_like.checkState()
        address = self.textEdit_addr.toPlainText()
        remark = self.textEdit_info.toPlainText()

        #修改之前的关键KEY

        keyvalue = self.keyValue
        getData = {
            'name' : name,
            'tel' : tel,
            'email' : email,
            'birthday' : birthday,
            'agroup' : agroup,
            'flag' : flag,
            'address' : address,
            'remark' : remark,
            'keyvalue' : keyvalue
        }

        self.retSignal.emit(getData)      #将pList信号发射出去，getData数据类型应该是list的
        self.close()                      #关闭窗口
