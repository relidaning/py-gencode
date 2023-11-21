# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from datasource.mysqlConnect import MysqlConnector
from gen.gen import Generator


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(447, 273)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.datasource_lab = QtWidgets.QLabel(self.centralwidget)
        self.datasource_lab.setObjectName("datasource_lab")
        # datasource
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.datasource_lab)
        self.datasource_line = QtWidgets.QLineEdit(self.centralwidget)
        self.datasource_line.setObjectName("datasource_line")
        self.datasource_line.setText("127.0.0.1:3306/database")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.datasource_line)
        self.username_lab = QtWidgets.QLabel(self.centralwidget)
        self.username_lab.setObjectName("username_lab")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.username_lab)
        self.username_line = QtWidgets.QLineEdit(self.centralwidget)
        self.username_line.setObjectName("username_line")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.username_line)
        self.pwd_lab = QtWidgets.QLabel(self.centralwidget)
        self.pwd_lab.setObjectName("pwd_lab")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.pwd_lab)
        self.pwd_line = QtWidgets.QLineEdit(self.centralwidget)
        self.pwd_line.setObjectName("pwd_line")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pwd_line)
        self.tableName_lab = QtWidgets.QLabel(self.centralwidget)
        self.tableName_lab.setObjectName("tableName_lab")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.tableName_lab)
        self.tableName_line = QtWidgets.QLineEdit(self.centralwidget)
        self.tableName_line.setObjectName("tableName_line")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.tableName_line)
        self.saveat_lab = QtWidgets.QLabel(self.centralwidget)
        self.package_lab = QtWidgets.QLabel(self.centralwidget)
        self.package_lab.setObjectName("package_lab")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.package_lab)
        self.package_line = QtWidgets.QLineEdit(self.centralwidget)
        self.package_line.setObjectName("package_line")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.package_line)
        self.module_lab = QtWidgets.QLabel(self.centralwidget)
        self.module_lab.setObjectName("module_lab")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.module_lab)
        self.module_line = QtWidgets.QLineEdit(self.centralwidget)
        self.module_line.setObjectName("module_line")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.module_line)
        self.saveat_lab.setObjectName("saveat_lab")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.saveat_lab)
        self.saveat_line = QtWidgets.QLineEdit(self.centralwidget)
        self.saveat_line.setObjectName("saveat_line")
        self.saveat_line.setText("e:")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.saveat_line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.formLayout.setLayout(7, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(MainWindow.close) # type: ignore
        self.pushButton.clicked.connect(lambda:self.connDataSource()) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.datasource_lab.setText(_translate("MainWindow", "数据源："))
        self.username_lab.setText(_translate("MainWindow", "用户名："))
        self.pwd_lab.setText(_translate("MainWindow", "密码："))
        self.pushButton_2.setText(_translate("MainWindow", "取消"))
        self.pushButton.setText(_translate("MainWindow", "生成"))
        self.tableName_lab.setText(_translate("MainWindow", "表名:"))
        self.saveat_lab.setText(_translate("MainWindow", "保存于:"))
        self.package_lab.setText(_translate("MainWindow", "包路径:"))
        self.module_lab.setText(_translate("MainWindow", "模块名:"))

    def connDataSource(self):
        #数据库连接
        host = self.datasource_line.text().split(':')[0]
        port = int(self.datasource_line.text().split(':')[1].split('/')[0])
        database = self.datasource_line.text().split('/')[1]
        user = self.username_line.text()
        pwd = self.pwd_line.text()

        #业务相关
        table = self.tableName_line.text()
        package = self.package_line.text()
        module = self.module_line.text()

        #保存路径
        saveat = self.saveat_line.text()

        print('host:', host, ', port:', port, ', database:', database, ', username:', user, ', password:', pwd)
        print('table:', table, ', package:', package, ', module:', module, ', saveat:', saveat)

        #数据库连接
        db = MysqlConnector(host, port, user, pwd, database)

        #生成
        gen = Generator(db, database, package, module, table, saveat)
        gen.genController()
        gen.genDomain()
        gen.genMapperJava()
        gen.genMapperXml()
        gen.genService()
        gen.genServiceImpl()