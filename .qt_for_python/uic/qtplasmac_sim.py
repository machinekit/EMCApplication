# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qtplasmac_sim.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from qtvcp.widgets.simple_widgets import Slider
from qtvcp.widgets.simple_widgets import PushButton
from qtvcp.widgets.hal_label import HALLabel
from qtvcp.widgets.general_hal_input import GeneralHALInput
from qtvcp.widgets.general_hal_output import GeneralHALOutput


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(180, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(180, 0))
        MainWindow.setMaximumSize(QSize(180, 400))
        MainWindow.setBaseSize(QSize(0, 0))
        self.actionSetD1_50_50 = QAction(MainWindow)
        self.actionSetD1_50_50.setObjectName(u"actionSetD1_50_50")
        self.actionSetD1_0_1000 = QAction(MainWindow)
        self.actionSetD1_0_1000.setObjectName(u"actionSetD1_0_1000")
        self.actionSetD1_0_100 = QAction(MainWindow)
        self.actionSetD1_0_100.setObjectName(u"actionSetD1_0_100")
        self.actionDial_3 = QAction(MainWindow)
        self.actionDial_3.setObjectName(u"actionDial_3")
        self.actionDial_4 = QAction(MainWindow)
        self.actionDial_4.setObjectName(u"actionDial_4")
        self.actionSetD2_50_50 = QAction(MainWindow)
        self.actionSetD2_50_50.setObjectName(u"actionSetD2_50_50")
        self.actionSetD2_0_100 = QAction(MainWindow)
        self.actionSetD2_0_100.setObjectName(u"actionSetD2_0_100")
        self.actionSetD2_0_1000 = QAction(MainWindow)
        self.actionSetD2_0_1000.setObjectName(u"actionSetD2_0_1000")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setVerticalSpacing(8)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.sensor_brk = QPushButton(self.centralwidget)
        self.sensor_brk.setObjectName(u"sensor_brk")
        self.sensor_brk.setMinimumSize(QSize(54, 23))
        self.sensor_brk.setMaximumSize(QSize(54, 23))

        self.gridLayout.addWidget(self.sensor_brk, 9, 2, 1, 1)

        self.sensor_label = QLabel(self.centralwidget)
        self.sensor_label.setObjectName(u"sensor_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sensor_label.sizePolicy().hasHeightForWidth())
        self.sensor_label.setSizePolicy(sizePolicy1)
        self.sensor_label.setMinimumSize(QSize(170, 17))
        self.sensor_label.setMaximumSize(QSize(170, 17))
        self.sensor_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.sensor_label, 7, 0, 1, 2)

        self.move_label = QLabel(self.centralwidget)
        self.move_label.setObjectName(u"move_label")
        sizePolicy1.setHeightForWidth(self.move_label.sizePolicy().hasHeightForWidth())
        self.move_label.setSizePolicy(sizePolicy1)
        self.move_label.setMinimumSize(QSize(170, 17))
        self.move_label.setMaximumSize(QSize(170, 17))
        self.move_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.move_label, 15, 0, 1, 3)

        self.move_up = PushButton(self.centralwidget)
        self.move_up.setObjectName(u"move_up")
        sizePolicy1.setHeightForWidth(self.move_up.sizePolicy().hasHeightForWidth())
        self.move_up.setSizePolicy(sizePolicy1)
        self.move_up.setMinimumSize(QSize(54, 23))
        self.move_up.setMaximumSize(QSize(54, 23))

        self.gridLayout.addWidget(self.move_up, 16, 0, 1, 1)

        self.sensor_line = QFrame(self.centralwidget)
        self.sensor_line.setObjectName(u"sensor_line")
        sizePolicy1.setHeightForWidth(self.sensor_line.sizePolicy().hasHeightForWidth())
        self.sensor_line.setSizePolicy(sizePolicy1)
        self.sensor_line.setMinimumSize(QSize(170, 2))
        self.sensor_line.setMaximumSize(QSize(170, 2))
        self.sensor_line.setFrameShape(QFrame.HLine)
        self.sensor_line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.sensor_line, 11, 0, 1, 1)

        self.sensor_flt = QPushButton(self.centralwidget)
        self.sensor_flt.setObjectName(u"sensor_flt")
        self.sensor_flt.setMinimumSize(QSize(54, 23))
        self.sensor_flt.setMaximumSize(QSize(54, 23))

        self.gridLayout.addWidget(self.sensor_flt, 9, 0, 1, 1)

        self.arc_ok_line = QFrame(self.centralwidget)
        self.arc_ok_line.setObjectName(u"arc_ok_line")
        sizePolicy1.setHeightForWidth(self.arc_ok_line.sizePolicy().hasHeightForWidth())
        self.arc_ok_line.setSizePolicy(sizePolicy1)
        self.arc_ok_line.setMinimumSize(QSize(170, 2))
        self.arc_ok_line.setMaximumSize(QSize(170, 2))
        self.arc_ok_line.setFrameShape(QFrame.HLine)
        self.arc_ok_line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.arc_ok_line, 14, 0, 1, 3)

        self.sensor_breakaway = GeneralHALOutput(self.centralwidget)
        self.sensor_breakaway.setObjectName(u"sensor_breakaway")
        self.sensor_breakaway.setMaximumSize(QSize(16777215, 4))

        self.gridLayout.addWidget(self.sensor_breakaway, 8, 2, 1, 1)

        self.mode_label = QLabel(self.centralwidget)
        self.mode_label.setObjectName(u"mode_label")
        sizePolicy1.setHeightForWidth(self.mode_label.sizePolicy().hasHeightForWidth())
        self.mode_label.setSizePolicy(sizePolicy1)
        self.mode_label.setMinimumSize(QSize(170, 17))
        self.mode_label.setMaximumSize(QSize(170, 17))
        self.mode_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.mode_label, 0, 0, 1, 1)

        self.arc_voltage_in = HALLabel(self.centralwidget)
        self.arc_voltage_in.setObjectName(u"arc_voltage_in")
        self.arc_voltage_in.setMinimumSize(QSize(54, 17))
        self.arc_voltage_in.setMaximumSize(QSize(54, 17))
        self.arc_voltage_in.setTextFormat(Qt.AutoText)
        self.arc_voltage_in.setAlignment(Qt.AlignCenter)
        self.arc_voltage_in.setProperty("float_pin_type", True)

        self.gridLayout.addWidget(self.arc_voltage_in, 4, 1, 1, 1)

        self.arc_ok_label = QLabel(self.centralwidget)
        self.arc_ok_label.setObjectName(u"arc_ok_label")
        sizePolicy1.setHeightForWidth(self.arc_ok_label.sizePolicy().hasHeightForWidth())
        self.arc_ok_label.setSizePolicy(sizePolicy1)
        self.arc_ok_label.setMinimumSize(QSize(170, 17))
        self.arc_ok_label.setMaximumSize(QSize(170, 17))
        self.arc_ok_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.arc_ok_label, 12, 0, 1, 2)

        self.arc_voltage_line = QFrame(self.centralwidget)
        self.arc_voltage_line.setObjectName(u"arc_voltage_line")
        sizePolicy1.setHeightForWidth(self.arc_voltage_line.sizePolicy().hasHeightForWidth())
        self.arc_voltage_line.setSizePolicy(sizePolicy1)
        self.arc_voltage_line.setMinimumSize(QSize(170, 2))
        self.arc_voltage_line.setMaximumSize(QSize(170, 2))
        self.arc_voltage_line.setFrameShape(QFrame.HLine)
        self.arc_voltage_line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.arc_voltage_line, 6, 0, 1, 3)

        self.move_down = PushButton(self.centralwidget)
        self.move_down.setObjectName(u"move_down")
        sizePolicy1.setHeightForWidth(self.move_down.sizePolicy().hasHeightForWidth())
        self.move_down.setSizePolicy(sizePolicy1)
        self.move_down.setMinimumSize(QSize(54, 23))
        self.move_down.setMaximumSize(QSize(54, 23))

        self.gridLayout.addWidget(self.move_down, 16, 2, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(170, 17))
        self.label.setMaximumSize(QSize(170, 17))
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 19, 0, 1, 1)

        self.sensor_ohm = QPushButton(self.centralwidget)
        self.sensor_ohm.setObjectName(u"sensor_ohm")
        self.sensor_ohm.setMinimumSize(QSize(54, 23))
        self.sensor_ohm.setMaximumSize(QSize(54, 23))

        self.gridLayout.addWidget(self.sensor_ohm, 9, 1, 1, 1)

        self.sensor_ohmic = GeneralHALOutput(self.centralwidget)
        self.sensor_ohmic.setObjectName(u"sensor_ohmic")
        self.sensor_ohmic.setMaximumSize(QSize(16777215, 4))

        self.gridLayout.addWidget(self.sensor_ohmic, 8, 1, 1, 1)

        self.arc_voltage_label = QLabel(self.centralwidget)
        self.arc_voltage_label.setObjectName(u"arc_voltage_label")
        self.arc_voltage_label.setMinimumSize(QSize(170, 17))
        self.arc_voltage_label.setMaximumSize(QSize(170, 17))
        self.arc_voltage_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.arc_voltage_label, 3, 0, 1, 2)

        self.sensor_float = GeneralHALOutput(self.centralwidget)
        self.sensor_float.setObjectName(u"sensor_float")
        self.sensor_float.setMaximumSize(QSize(16777215, 4))

        self.gridLayout.addWidget(self.sensor_float, 8, 0, 1, 1)

        self.arc_voltage_out = Slider(self.centralwidget)
        self.arc_voltage_out.setObjectName(u"arc_voltage_out")
        sizePolicy1.setHeightForWidth(self.arc_voltage_out.sizePolicy().hasHeightForWidth())
        self.arc_voltage_out.setSizePolicy(sizePolicy1)
        self.arc_voltage_out.setMinimumSize(QSize(170, 23))
        self.arc_voltage_out.setMaximumSize(QSize(170, 23))
        self.arc_voltage_out.setMinimum(0)
        self.arc_voltage_out.setMaximum(300)
        self.arc_voltage_out.setOrientation(Qt.Horizontal)
        self.arc_voltage_out.setTickPosition(QSlider.TicksAbove)
        self.arc_voltage_out.setTickInterval(50)

        self.gridLayout.addWidget(self.arc_voltage_out, 5, 0, 1, 3)

        self.torch_on = GeneralHALInput(self.centralwidget)
        self.torch_on.setObjectName(u"torch_on")

        self.gridLayout.addWidget(self.torch_on, 16, 1, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        sizePolicy1.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy1)
        self.line.setMinimumSize(QSize(170, 2))
        self.line.setMaximumSize(QSize(170, 2))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 18, 0, 1, 1)

        self.mode_line = QFrame(self.centralwidget)
        self.mode_line.setObjectName(u"mode_line")
        sizePolicy1.setHeightForWidth(self.mode_line.sizePolicy().hasHeightForWidth())
        self.mode_line.setSizePolicy(sizePolicy1)
        self.mode_line.setMinimumSize(QSize(170, 2))
        self.mode_line.setMaximumSize(QSize(170, 2))
        self.mode_line.setFrameShape(QFrame.HLine)
        self.mode_line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.mode_line, 1, 0, 1, 1)

        self.arc_ok = PushButton(self.centralwidget)
        self.arc_ok.setObjectName(u"arc_ok")
        sizePolicy1.setHeightForWidth(self.arc_ok.sizePolicy().hasHeightForWidth())
        self.arc_ok.setSizePolicy(sizePolicy1)
        self.arc_ok.setMinimumSize(QSize(170, 23))
        self.arc_ok.setMaximumSize(QSize(170, 23))
        self.arc_ok.setCheckable(True)

        self.gridLayout.addWidget(self.arc_ok, 13, 0, 1, 3)

        self.estop = QPushButton(self.centralwidget)
        self.estop.setObjectName(u"estop")
        self.estop.setMinimumSize(QSize(54, 23))
        self.estop.setMaximumSize(QSize(54, 23))
        self.estop.setCheckable(False)

        self.gridLayout.addWidget(self.estop, 20, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Qtvcp", None))
        self.actionSetD1_50_50.setText(QCoreApplication.translate("MainWindow", u"Set +-  50", None))
        self.actionSetD1_0_1000.setText(QCoreApplication.translate("MainWindow", u"Set 0 - 1000", None))
        self.actionSetD1_0_100.setText(QCoreApplication.translate("MainWindow", u"Set 0 - 100", None))
        self.actionDial_3.setText(QCoreApplication.translate("MainWindow", u"Dial 3", None))
        self.actionDial_4.setText(QCoreApplication.translate("MainWindow", u"Dial 4", None))
        self.actionSetD2_50_50.setText(QCoreApplication.translate("MainWindow", u"Set +- 50", None))
        self.actionSetD2_0_100.setText(QCoreApplication.translate("MainWindow", u"Set 0 - 100", None))
        self.actionSetD2_0_1000.setText(QCoreApplication.translate("MainWindow", u"Set 0 - 1000", None))
        self.sensor_brk.setText(QCoreApplication.translate("MainWindow", u"BREAK", None))
        self.sensor_label.setText(QCoreApplication.translate("MainWindow", u"SENSORS", None))
        self.move_label.setText(QCoreApplication.translate("MainWindow", u"MOVE Z AXIS", None))
        self.move_up.setText(QCoreApplication.translate("MainWindow", u"UP", None))
        self.sensor_flt.setText(QCoreApplication.translate("MainWindow", u"FLOAT", None))
        self.mode_label.setText(QCoreApplication.translate("MainWindow", u"MODE 0", None))
        self.arc_voltage_in.setText(QCoreApplication.translate("MainWindow", u"0.00 V", None))
        self.arc_voltage_in.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%0.0f", None))
        self.arc_ok_label.setText(QCoreApplication.translate("MainWindow", u"ARC OK", None))
        self.move_down.setText(QCoreApplication.translate("MainWindow", u"DOWN", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"MACHINE", None))
        self.sensor_ohm.setText(QCoreApplication.translate("MainWindow", u"OHMIC", None))
        self.arc_voltage_label.setText(QCoreApplication.translate("MainWindow", u"ARC VOLTAGE", None))
        self.torch_on.setProperty("pin_name", QCoreApplication.translate("MainWindow", u"torch_on", None))
        self.arc_ok.setText(QCoreApplication.translate("MainWindow", u"ARC OK", None))
        self.estop.setText(QCoreApplication.translate("MainWindow", u"ESTOP", None))
    # retranslateUi

