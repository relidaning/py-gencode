#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
from gui import main

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':

    try:
        # sys.setdefaultencoding('utf8')
        print('genCode v1.0 starting...')
        app = QApplication(sys.argv)
        mainWindow = QMainWindow()
        ui = main.Ui_MainWindow()
        ui.setupUi(mainWindow)
        mainWindow.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)
