# -*- coding=utf-8 -*-
# name: nan chen
# date: 2021/7/4 14:09
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import mainUi as um
import cv2
import numpy as np
from display import Display

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainW = QMainWindow()
    ui = um.Ui_MainWindow()
    ui.setupUi(mainW)
    display = Display(ui, mainW)
    mainW.show()
    sys.exit(app.exec_())
