# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'copy_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from qtvcp.widgets.screen_options import ScreenOptions
from qtvcp.widgets.file_manager import FileManager


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(350, 400)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.screen_options = ScreenOptions(self.centralwidget)
        self.screen_options.setObjectName(u"screen_options")
        self.screen_options.setProperty("catch_close_option", False)
        self.screen_options.setProperty("catch_errors_option", False)
        self.screen_options.setProperty("use_pref_file_option", False)
        self.screen_options.setProperty("embedded_program_option", False)
        self.screen_options.setProperty("fileDialog_option", True)
        self.verticalLayout_2 = QVBoxLayout(self.screen_options)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.screen_options)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.comboBox = QComboBox(self.screen_options)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_2.addWidget(self.comboBox)

        self.label_2 = QLabel(self.screen_options)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.filemanager = FileManager(self.screen_options)
        self.filemanager.setObjectName(u"filemanager")

        self.verticalLayout_2.addWidget(self.filemanager)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.cancelButton = QPushButton(self.screen_options)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout_3.addWidget(self.cancelButton)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)

        self.applyButton = QPushButton(self.screen_options)
        self.applyButton.setObjectName(u"applyButton")

        self.horizontalLayout_2.addWidget(self.applyButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addWidget(self.screen_options)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 350, 27))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.cancelButton.clicked.connect(MainWindow.close)
        self.applyButton.clicked.connect(MainWindow.applyClicked)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Screen Code Folder:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Destination Folder:", None))
        self.cancelButton.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.applyButton.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
    # retranslateUi

