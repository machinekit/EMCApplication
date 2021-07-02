# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'woodpecker.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from qtvcp.widgets.action_button import ActionButton
from qtvcp.widgets.basic_probe import BasicProbe
from qtvcp.widgets.camview_widget import CamView
from qtvcp.widgets.container_widgets import StateEnableGridLayout
from qtvcp.widgets.gcode_graphics import GCodeGraphics
from qtvcp.widgets.jog_increments import JogIncrements
from qtvcp.widgets.led_widget import LED
from qtvcp.widgets.simple_widgets import LCDNumber
from qtvcp.widgets.macro_widget import MacroTab
from qtvcp.widgets.origin_offsetview import OriginOffsetView
from qtvcp.widgets.status_slider import StatusSlider
from qtvcp.widgets.state_label import StateLabel
from qtvcp.widgets.axis_tool_button import AxisToolButton
from qtvcp.widgets.simple_widgets import Dial
from qtvcp.widgets.state_led import StateLED
from qtvcp.widgets.screen_options import ScreenOptions
from qtvcp.widgets.simple_widgets import PushButton
from qtvcp.widgets.machine_log import MachineLog
from qtvcp.widgets.status_label import StatusLabel
from qtvcp.widgets.tool_offsetview import ToolOffsetView
from qtvcp.widgets.dro_widget import DROLabel
from qtvcp.widgets.virtualkeyboard import VirtualKeyboard
from qtvcp.widgets.widget_switcher import WidgetSwitcher
from qtvcp.widgets.file_manager import FileManager
from qtvcp.widgets.system_tool_button import SystemToolButton
from qtvcp.widgets.gcode_editor import GcodeEditor
from qtvcp.widgets.mdi_history import MDIHistory
from qtvcp.widgets.mdi_touchy import MDITouchy

import woodpecker_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 960)
        MainWindow.setMinimumSize(QSize(1280, 960))
        MainWindow.setMaximumSize(QSize(1280, 960))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.screen_options = ScreenOptions(self.centralwidget)
        self.screen_options.setObjectName(u"screen_options")
        self.screen_options.setGeometry(QRect(0, 0, 1281, 931))
        self.screen_options.setProperty("embedded_program_option", False)
        self.screen_options.setProperty("focusOverlay_option", True)
        self.screen_options.setProperty("entryDialog_option", True)
        self.screen_options.setProperty("entryDialogSoftkey_option", True)
        self.screen_options.setProperty("toolDialog_option", True)
        self.screen_options.setProperty("fileDialog_option", True)
        self.screen_options.setProperty("calculatorDialog_option", True)
        self.screen_options.setProperty("machineLogDialog_option", True)
        self.screen_options.setProperty("runFromLineDialog_option", True)
        self.screen_options.setProperty("styleEditorDialog_option", True)
        self.frame = QFrame(self.screen_options)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-1, -1, 1281, 931))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_main_btns_vertical = QFrame(self.frame)
        self.frame_main_btns_vertical.setObjectName(u"frame_main_btns_vertical")
        self.frame_main_btns_vertical.setGeometry(QRect(1210, 432, 70, 408))
        self.frame_main_btns_vertical.setMinimumSize(QSize(70, 408))
        self.frame_main_btns_vertical.setMaximumSize(QSize(70, 408))
        self.frame_main_btns_vertical.setFrameShape(QFrame.WinPanel)
        self.frame_main_btns_vertical.setFrameShadow(QFrame.Raised)
        self.action_machine_on = ActionButton(self.frame_main_btns_vertical)
        self.action_machine_on.setObjectName(u"action_machine_on")
        self.action_machine_on.setGeometry(QRect(3, 338, 63, 64))
        self.action_machine_on.setMinimumSize(QSize(63, 64))
        self.action_machine_on.setMaximumSize(QSize(63, 64))
        self.action_machine_on.setStyleSheet(u"font: 12pt \"Sans\";")
        self.action_machine_on.setCheckable(True)
        self.action_machine_on.setAutoExclusive(False)
        self.action_machine_on.setProperty("indicator_option", True)
        self.action_machine_on.setProperty("indicator_status_option", True)
        self.action_machine_on.setProperty("checked_state_text_option", True)
        self.action_machine_on.setProperty("python_command_option", False)
        self.action_machine_on.setProperty("on_color", QColor(0, 255, 0))
        self.action_machine_on.setProperty("off_color", QColor(255, 0, 0))
        self.action_machine_on.setProperty("invert_the_status", True)
        self.action_machine_on.setProperty("is_estopped_status", True)
        self.action_machine_on.setProperty("machine_on_action", True)
        self.manual_mode_button = ActionButton(self.frame_main_btns_vertical)
        self.manual_mode_button.setObjectName(u"manual_mode_button")
        self.manual_mode_button.setGeometry(QRect(3, 271, 63, 64))
        self.manual_mode_button.setMinimumSize(QSize(63, 64))
        self.manual_mode_button.setMaximumSize(QSize(63, 64))
        self.manual_mode_button.setStyleSheet(u"font: 15pt \"Sans\";")
        self.manual_mode_button.setCheckable(True)
        self.manual_mode_button.setAutoExclusive(True)
        self.manual_mode_button.setProperty("python_command_option", True)
        self.manual_mode_button.setProperty("manual_action", True)
        self.abtn_mainv_mode_mdi = ActionButton(self.frame_main_btns_vertical)
        self.abtn_mainv_mode_mdi.setObjectName(u"abtn_mainv_mode_mdi")
        self.abtn_mainv_mode_mdi.setGeometry(QRect(3, 204, 63, 64))
        self.abtn_mainv_mode_mdi.setMinimumSize(QSize(63, 64))
        self.abtn_mainv_mode_mdi.setMaximumSize(QSize(63, 64))
        self.abtn_mainv_mode_mdi.setStyleSheet(u"font: 15pt \"Sans\";")
        self.abtn_mainv_mode_mdi.setCheckable(True)
        self.abtn_mainv_mode_mdi.setAutoExclusive(True)
        self.abtn_mainv_mode_mdi.setProperty("python_command_option", True)
        self.abtn_mainv_mode_mdi.setProperty("mdi_action", True)
        self.abtn_mainv_mode_auto = ActionButton(self.frame_main_btns_vertical)
        self.abtn_mainv_mode_auto.setObjectName(u"abtn_mainv_mode_auto")
        self.abtn_mainv_mode_auto.setGeometry(QRect(3, 137, 63, 64))
        self.abtn_mainv_mode_auto.setMinimumSize(QSize(63, 64))
        self.abtn_mainv_mode_auto.setMaximumSize(QSize(63, 64))
        self.abtn_mainv_mode_auto.setStyleSheet(u"font: 15pt \"Sans\";")
        self.abtn_mainv_mode_auto.setCheckable(True)
        self.abtn_mainv_mode_auto.setAutoExclusive(True)
        self.abtn_mainv_mode_auto.setProperty("python_command_option", False)
        self.abtn_mainv_mode_auto.setProperty("auto_action", True)
        self.pbtn_mainv_spare_2 = PushButton(self.frame_main_btns_vertical)
        self.pbtn_mainv_spare_2.setObjectName(u"pbtn_mainv_spare_2")
        self.pbtn_mainv_spare_2.setGeometry(QRect(3, 70, 63, 64))
        self.pbtn_mainv_spare_2.setCheckable(True)
        self.pbtn_mainv_spare_1 = PushButton(self.frame_main_btns_vertical)
        self.pbtn_mainv_spare_1.setObjectName(u"pbtn_mainv_spare_1")
        self.pbtn_mainv_spare_1.setGeometry(QRect(3, 3, 63, 64))
        self.pbtn_mainv_spare_1.setCheckable(True)
        self.frame_misc_btns_Vertical = QFrame(self.frame)
        self.frame_misc_btns_Vertical.setObjectName(u"frame_misc_btns_Vertical")
        self.frame_misc_btns_Vertical.setGeometry(QRect(1210, 10, 70, 421))
        self.frame_misc_btns_Vertical.setMinimumSize(QSize(70, 272))
        self.frame_misc_btns_Vertical.setMaximumSize(QSize(70, 16777215))
        self.frame_misc_btns_Vertical.setFrameShape(QFrame.WinPanel)
        self.frame_misc_btns_Vertical.setFrameShadow(QFrame.Raised)
        self.btn_full = PushButton(self.frame_misc_btns_Vertical)
        self.btn_full.setObjectName(u"btn_full")
        self.btn_full.setGeometry(QRect(5, 150, 60, 55))
        self.btn_full.setStyleSheet(u"font: 15pt \"Sans\";")
        self.btn_full.setCheckable(True)
        self.btn_keyboard = PushButton(self.frame_misc_btns_Vertical)
        self.btn_keyboard.setObjectName(u"btn_keyboard")
        self.btn_keyboard.setGeometry(QRect(5, 220, 60, 55))
        self.btn_keyboard.setStyleSheet(u"\n"
"font: 75 12pt \"Bebas Kai\";")
        self.btn_keyboard.setCheckable(True)
        self.btn_keyboard.setProperty("checked_state_text_option", False)
        self.btn_keyboard.setProperty("python_command_option", True)
        self.actionbutton_2 = ActionButton(self.frame_misc_btns_Vertical)
        self.actionbutton_2.setObjectName(u"actionbutton_2")
        self.actionbutton_2.setGeometry(QRect(5, 5, 60, 60))
        icon = QIcon()
        icon.addFile(u"images/exit_application.png", QSize(), QIcon.Normal, QIcon.On)
        self.actionbutton_2.setIcon(icon)
        self.actionbutton_2.setIconSize(QSize(36, 36))
        self.actionbutton_2.setProperty("exit_action", True)
        self.btn_accessories = QPushButton(self.frame_misc_btns_Vertical)
        self.page_buttonGroup = QButtonGroup(MainWindow)
        self.page_buttonGroup.setObjectName(u"page_buttonGroup")
        self.page_buttonGroup.addButton(self.btn_accessories)
        self.btn_accessories.setObjectName(u"btn_accessories")
        self.btn_accessories.setGeometry(QRect(4, 280, 61, 61))
        self.btn_accessories.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.btn_accessories.setCheckable(True)
        self.btn_accessories.setProperty("index", 12)
        self.btn_handwheel_spare = PushButton(self.frame_misc_btns_Vertical)
        self.btn_handwheel_spare.setObjectName(u"btn_handwheel_spare")
        self.btn_handwheel_spare.setGeometry(QRect(4, 350, 61, 61))
        self.btn_handwheel_spare.setStyleSheet(u"\n"
"font: 75 12pt \"Bebas Kai\";")
        self.btn_handwheel_spare.setCheckable(True)
        self.btn_handwheel_spare.setProperty("indicator_status_option", False)
        self.btn_handwheel_spare.setProperty("checked_state_text_option", True)
        self.btn_handwheel_spare.setProperty("python_command_option", True)
        self.frame_estop = QFrame(self.frame)
        self.frame_estop.setObjectName(u"frame_estop")
        self.frame_estop.setGeometry(QRect(1210, 840, 70, 90))
        self.frame_estop.setFrameShape(QFrame.WinPanel)
        self.frame_estop.setFrameShadow(QFrame.Raised)
        self.action_estop = ActionButton(self.frame_estop)
        self.action_estop.setObjectName(u"action_estop")
        self.action_estop.setGeometry(QRect(3, 5, 63, 80))
        self.action_estop.setMinimumSize(QSize(60, 80))
        self.action_estop.setMaximumSize(QSize(63, 80))
        self.action_estop.setStyleSheet(u"font: 12pt \"Sans\";")
        self.action_estop.setIconSize(QSize(24, 24))
        self.action_estop.setCheckable(True)
        self.action_estop.setAutoExclusive(False)
        self.action_estop.setProperty("indicator_option", True)
        self.action_estop.setProperty("indicator_HAL_pin_option", False)
        self.action_estop.setProperty("indicator_status_option", True)
        self.action_estop.setProperty("checked_state_text_option", True)
        self.action_estop.setProperty("python_command_option", False)
        self.action_estop.setProperty("on_color", QColor(255, 0, 0))
        self.action_estop.setProperty("off_color", QColor(0, 255, 0))
        self.action_estop.setProperty("invert_the_status", True)
        self.action_estop.setProperty("is_estopped_status", True)
        self.action_estop.setProperty("joint_number_status", 0)
        self.action_estop.setProperty("estop_action", True)
        self.action_estop.setProperty("machine_on_action", False)
        self.frame_aux_btns_horizontal = QFrame(self.frame)
        self.frame_aux_btns_horizontal.setObjectName(u"frame_aux_btns_horizontal")
        self.frame_aux_btns_horizontal.setGeometry(QRect(831, 860, 380, 70))
        self.frame_aux_btns_horizontal.setMaximumSize(QSize(16777215, 70))
        self.frame_aux_btns_horizontal.setFrameShape(QFrame.WinPanel)
        self.frame_aux_btns_horizontal.setFrameShadow(QFrame.Raised)
        self.abtn_mainh_aux_flood = ActionButton(self.frame_aux_btns_horizontal)
        self.abtn_mainh_aux_flood.setObjectName(u"abtn_mainh_aux_flood")
        self.abtn_mainh_aux_flood.setGeometry(QRect(10, 4, 60, 60))
        self.abtn_mainh_aux_flood.setMinimumSize(QSize(60, 60))
        self.abtn_mainh_aux_flood.setMaximumSize(QSize(60, 60))
        self.abtn_mainh_aux_flood.setStyleSheet(u"\n"
"font: 75 12pt \"Bebas Kai\";")
        self.abtn_mainh_aux_flood.setIconSize(QSize(24, 24))
        self.abtn_mainh_aux_flood.setCheckable(True)
        self.abtn_mainh_aux_flood.setProperty("estop_action", False)
        self.abtn_mainh_aux_flood.setProperty("flood_action", True)
        self.abtn_mainh_aux_mist = ActionButton(self.frame_aux_btns_horizontal)
        self.abtn_mainh_aux_mist.setObjectName(u"abtn_mainh_aux_mist")
        self.abtn_mainh_aux_mist.setGeometry(QRect(110, 4, 60, 60))
        self.abtn_mainh_aux_mist.setMinimumSize(QSize(60, 60))
        self.abtn_mainh_aux_mist.setMaximumSize(QSize(60, 60))
        self.abtn_mainh_aux_mist.setStyleSheet(u"\n"
"font: 75 12pt \"Bebas Kai\";")
        self.abtn_mainh_aux_mist.setIconSize(QSize(24, 24))
        self.abtn_mainh_aux_mist.setCheckable(True)
        self.abtn_mainh_aux_mist.setProperty("estop_action", False)
        self.abtn_mainh_aux_mist.setProperty("mist_action", True)
        self.statuslabel_6 = StatusLabel(self.frame_aux_btns_horizontal)
        self.statuslabel_6.setObjectName(u"statuslabel_6")
        self.statuslabel_6.setGeometry(QRect(200, 4, 171, 61))
        self.statuslabel_6.setStyleSheet(u"font: 75 14pt \"Monospace\";")
        self.statuslabel_6.setFrameShape(QFrame.WinPanel)
        self.statuslabel_6.setFrameShadow(QFrame.Sunken)
        self.statuslabel_6.setProperty("time_stamp_status", True)
        self.stateled_flood = StateLED(self.frame_aux_btns_horizontal)
        self.stateled_flood.setObjectName(u"stateled_flood")
        self.stateled_flood.setGeometry(QRect(70, 20, 30, 30))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stateled_flood.sizePolicy().hasHeightForWidth())
        self.stateled_flood.setSizePolicy(sizePolicy)
        self.stateled_flood.setMinimumSize(QSize(30, 30))
        self.stateled_flood.setMaximumSize(QSize(30, 30))
        self.stateled_flood.setColor(QColor(0, 255, 0))
        self.stateled_flood.setProperty("is_flood_status", True)
        self.stateled_mist = StateLED(self.frame_aux_btns_horizontal)
        self.stateled_mist.setObjectName(u"stateled_mist")
        self.stateled_mist.setGeometry(QRect(170, 20, 30, 30))
        sizePolicy.setHeightForWidth(self.stateled_mist.sizePolicy().hasHeightForWidth())
        self.stateled_mist.setSizePolicy(sizePolicy)
        self.stateled_mist.setMinimumSize(QSize(30, 30))
        self.stateled_mist.setMaximumSize(QSize(30, 30))
        self.stateled_mist.setColor(QColor(0, 255, 0))
        self.stateled_mist.setProperty("is_mist_status", True)
        self.stateled_mist.setProperty("is_optional_stop_status", False)
        self.frame_main_btns_horizontal = QFrame(self.frame)
        self.frame_main_btns_horizontal.setObjectName(u"frame_main_btns_horizontal")
        self.frame_main_btns_horizontal.setGeometry(QRect(0, 860, 831, 70))
        self.frame_main_btns_horizontal.setMinimumSize(QSize(642, 70))
        self.frame_main_btns_horizontal.setMaximumSize(QSize(16777215, 70))
        self.frame_main_btns_horizontal.setFrameShape(QFrame.WinPanel)
        self.frame_main_btns_horizontal.setFrameShadow(QFrame.Raised)
        self.btn_main = QPushButton(self.frame_main_btns_horizontal)
        self.page_buttonGroup.addButton(self.btn_main)
        self.btn_main.setObjectName(u"btn_main")
        self.btn_main.setGeometry(QRect(7, 4, 60, 60))
        self.btn_main.setStyleSheet(u"font: 15pt \"Sans\";")
        self.btn_main.setCheckable(True)
        self.btn_main.setChecked(True)
        self.btn_main.setAutoExclusive(True)
        self.btn_main.setProperty("index", 0)
        self.btn_file = QPushButton(self.frame_main_btns_horizontal)
        self.page_buttonGroup.addButton(self.btn_file)
        self.btn_file.setObjectName(u"btn_file")
        self.btn_file.setGeometry(QRect(70, 4, 60, 60))
        self.btn_file.setStyleSheet(u"\n"
"font: 75 12pt \"Bebas Kai\";")
        self.btn_file.setCheckable(True)
        self.btn_file.setAutoExclusive(True)
        self.btn_file.setProperty("index", 1)
        self.btn_offset = QPushButton(self.frame_main_btns_horizontal)
        self.page_buttonGroup.addButton(self.btn_offset)
        self.btn_offset.setObjectName(u"btn_offset")
        self.btn_offset.setGeometry(QRect(133, 4, 60, 60))
        self.btn_offset.setStyleSheet(u"\n"
"font: 75 12pt \"Bebas Kai\";")
        self.btn_offset.setCheckable(True)
        self.btn_offset.setAutoExclusive(True)
        self.btn_offset.setProperty("index", 2)
        self.btn_tool = QPushButton(self.frame_main_btns_horizontal)
        self.page_buttonGroup.addButton(self.btn_tool)
        self.btn_tool.setObjectName(u"btn_tool")
        self.btn_tool.setGeometry(QRect(196, 4, 60, 60))
        self.btn_tool.setStyleSheet(u"\n"
"font: 75 12pt \"Bebas Kai\";")
        self.btn_tool.setCheckable(True)
        self.btn_tool.setAutoExclusive(True)
        self.btn_tool.setProperty("index", 3)
        self.btn_status = QPushButton(self.frame_main_btns_horizontal)
        self.page_buttonGroup.addButton(self.btn_status)
        self.btn_status.setObjectName(u"btn_status")
        self.btn_status.setGeometry(QRect(259, 4, 60, 60))
        self.btn_status.setStyleSheet(u"\n"
"font: 75 12pt \"Bebas Kai\";")
        self.btn_status.setCheckable(True)
        self.btn_status.setAutoExclusive(True)
        self.btn_status.setProperty("index", 4)
        self.btn_macro = QPushButton(self.frame_main_btns_horizontal)
        self.page_buttonGroup.addButton(self.btn_macro)
        self.btn_macro.setObjectName(u"btn_macro")
        self.btn_macro.setGeometry(QRect(385, 4, 60, 60))
        self.btn_macro.setStyleSheet(u"\n"
"font: 75 12pt \"Bebas Kai\";")
        self.btn_macro.setCheckable(True)
        self.btn_macro.setAutoExclusive(True)
        self.btn_macro.setProperty("index", 6)
        self.btn_settings = QPushButton(self.frame_main_btns_horizontal)
        self.page_buttonGroup.addButton(self.btn_settings)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setGeometry(QRect(448, 4, 60, 60))
        icon1 = QIcon()
        icon1.addFile(u"images/configure-2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_settings.setIcon(icon1)
        self.btn_settings.setIconSize(QSize(36, 36))
        self.btn_settings.setCheckable(True)
        self.btn_settings.setAutoExclusive(True)
        self.btn_settings.setProperty("index", 7)
        self.btn_camera = QPushButton(self.frame_main_btns_horizontal)
        self.page_buttonGroup.addButton(self.btn_camera)
        self.btn_camera.setObjectName(u"btn_camera")
        self.btn_camera.setGeometry(QRect(511, 4, 60, 60))
        self.btn_camera.setStyleSheet(u"\n"
"font: 75 12pt \"Bebas Kai\";")
        self.btn_camera.setCheckable(True)
        self.btn_camera.setAutoExclusive(True)
        self.btn_camera.setProperty("index", 8)
        self.btn_setup = QPushButton(self.frame_main_btns_horizontal)
        self.page_buttonGroup.addButton(self.btn_setup)
        self.btn_setup.setObjectName(u"btn_setup")
        self.btn_setup.setGeometry(QRect(574, 4, 60, 60))
        self.btn_setup.setStyleSheet(u"\n"
"font: 75 12pt \"Bebas Kai\";")
        self.btn_setup.setCheckable(True)
        self.btn_setup.setAutoExclusive(True)
        self.btn_setup.setProperty("index", 9)
        self.btn_probe = QPushButton(self.frame_main_btns_horizontal)
        self.page_buttonGroup.addButton(self.btn_probe)
        self.btn_probe.setObjectName(u"btn_probe")
        self.btn_probe.setGeometry(QRect(322, 4, 60, 60))
        self.btn_probe.setStyleSheet(u"\n"
"font: 75 12pt \"Bebas Kai\";")
        self.btn_probe.setCheckable(True)
        self.btn_probe.setAutoExclusive(True)
        self.btn_probe.setProperty("index", 5)
        self.tab_mdi_touchy = QPushButton(self.frame_main_btns_horizontal)
        self.page_buttonGroup.addButton(self.tab_mdi_touchy)
        self.tab_mdi_touchy.setObjectName(u"tab_mdi_touchy")
        self.tab_mdi_touchy.setGeometry(QRect(640, 5, 60, 60))
        self.tab_mdi_touchy.setMinimumSize(QSize(60, 55))
        self.tab_mdi_touchy.setMaximumSize(QSize(16777215, 60))
        self.tab_mdi_touchy.setStyleSheet(u"\n"
"font: 75 12pt \"Bebas Kai\";")
        self.tab_mdi_touchy.setCheckable(True)
        self.tab_mdi_touchy.setAutoExclusive(True)
        self.tab_mdi_touchy.setProperty("index", 10)
        self.btn_gcode = QPushButton(self.frame_main_btns_horizontal)
        self.page_buttonGroup.addButton(self.btn_gcode)
        self.btn_gcode.setObjectName(u"btn_gcode")
        self.btn_gcode.setGeometry(QRect(710, 4, 61, 61))
        sizePolicy.setHeightForWidth(self.btn_gcode.sizePolicy().hasHeightForWidth())
        self.btn_gcode.setSizePolicy(sizePolicy)
        self.btn_gcode.setMinimumSize(QSize(0, 55))
        self.btn_gcode.setMaximumSize(QSize(16777215, 16777215))
        self.btn_gcode.setStyleSheet(u"\n"
"font: 75 12pt \"Bebas Kai\";")
        self.btn_gcode.setCheckable(True)
        self.btn_gcode.setAutoExclusive(True)
        self.btn_gcode.setProperty("index", 11)
        self.stackedWidget_0 = QStackedWidget(self.frame)
        self.stackedWidget_0.setObjectName(u"stackedWidget_0")
        self.stackedWidget_0.setGeometry(QRect(0, 0, 1211, 861))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget_2 = QStackedWidget(self.page)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(0, 590, 954, 271))
        self.panel_spindle_and_dro = QWidget()
        self.panel_spindle_and_dro.setObjectName(u"panel_spindle_and_dro")
        self.frame_spindle_and_dro = QFrame(self.panel_spindle_and_dro)
        self.frame_spindle_and_dro.setObjectName(u"frame_spindle_and_dro")
        self.frame_spindle_and_dro.setGeometry(QRect(0, 0, 954, 271))
        self.frame_spindle_and_dro.setFrameShape(QFrame.StyledPanel)
        self.frame_spindle_and_dro.setFrameShadow(QFrame.Raised)
        self.frame_stackedWidget_5_btns = QFrame(self.frame_spindle_and_dro)
        self.frame_stackedWidget_5_btns.setObjectName(u"frame_stackedWidget_5_btns")
        self.frame_stackedWidget_5_btns.setGeometry(QRect(0, 0, 58, 271))
        self.frame_stackedWidget_5_btns.setFrameShape(QFrame.WinPanel)
        self.frame_stackedWidget_5_btns.setFrameShadow(QFrame.Raised)
        self.pbtn_axis4_select_quick_zero = PushButton(self.frame_stackedWidget_5_btns)
        self.pbtn_axis4_select_quick_zero.setObjectName(u"pbtn_axis4_select_quick_zero")
        self.pbtn_axis4_select_quick_zero.setGeometry(QRect(4, 60, 51, 42))
        self.pbtn_axis4_select_quick_zero.setStyleSheet(u"\n"
"font: 75 12pt \"Bebas Kai\";")
        self.pbtn_axis4_select_quick_zero.setCheckable(True)
        self.pbtn_axis4_select_quick_zero.setAutoExclusive(True)
        self.pbtn_axis4_select_quick_zero.setProperty("python_command_option", True)
        self.pbtn_axis4_select_macro = PushButton(self.frame_stackedWidget_5_btns)
        self.pbtn_axis4_select_macro.setObjectName(u"pbtn_axis4_select_macro")
        self.pbtn_axis4_select_macro.setGeometry(QRect(4, 110, 51, 42))
        self.pbtn_axis4_select_macro.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.pbtn_axis4_select_macro.setCheckable(True)
        self.pbtn_axis4_select_macro.setAutoExclusive(True)
        self.pbtn_axis4_select_macro.setProperty("python_command_option", True)
        self.pbtn_axis4_select_overrides = PushButton(self.frame_stackedWidget_5_btns)
        self.pbtn_axis4_select_overrides.setObjectName(u"pbtn_axis4_select_overrides")
        self.pbtn_axis4_select_overrides.setGeometry(QRect(4, 170, 51, 42))
        self.pbtn_axis4_select_overrides.setCheckable(True)
        self.pbtn_axis4_select_overrides.setAutoExclusive(True)
        self.pbtn_axis4_select_overrides.setProperty("python_command_option", True)
        self.pbtn_axis4_select_dro = PushButton(self.frame_stackedWidget_5_btns)
        self.pbtn_axis4_select_dro.setObjectName(u"pbtn_axis4_select_dro")
        self.pbtn_axis4_select_dro.setGeometry(QRect(4, 220, 51, 42))
        self.pbtn_axis4_select_dro.setCheckable(True)
        self.pbtn_axis4_select_dro.setAutoExclusive(True)
        self.pbtn_axis4_select_dro.setProperty("indicator_option", False)
        self.pbtn_axis4_select_dro.setProperty("python_command_option", True)
        self.pushbutton_5 = PushButton(self.frame_stackedWidget_5_btns)
        self.pushbutton_5.setObjectName(u"pushbutton_5")
        self.pushbutton_5.setGeometry(QRect(4, 10, 51, 41))
        self.pushbutton_5.setStyleSheet(u"\n"
"font: 75 12pt \"Bebas Kai\";")
        self.pushbutton_5.setCheckable(True)
        self.pushbutton_5.setAutoExclusive(True)
        self.pushbutton_5.setProperty("python_command_option", True)
        self.frame_for_stack_3 = QFrame(self.frame_spindle_and_dro)
        self.frame_for_stack_3.setObjectName(u"frame_for_stack_3")
        self.frame_for_stack_3.setGeometry(QRect(58, 0, 321, 271))
        self.frame_for_stack_3.setFrameShape(QFrame.StyledPanel)
        self.frame_for_stack_3.setFrameShadow(QFrame.Raised)
        self.stackedWidget_3 = QStackedWidget(self.frame_for_stack_3)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setGeometry(QRect(0, 0, 321, 271))
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.frame_2 = QFrame(self.page_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 321, 271))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_program = QFrame(self.frame_2)
        self.frame_program.setObjectName(u"frame_program")
        self.frame_program.setGeometry(QRect(0, 0, 320, 271))
        self.frame_program.setMinimumSize(QSize(320, 271))
        self.frame_program.setFrameShape(QFrame.WinPanel)
        self.frame_program.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_program)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setSpacing(4)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(4, 0, 6, 0)
        self.frame_cycle_start = QFrame(self.frame_program)
        self.frame_cycle_start.setObjectName(u"frame_cycle_start")
        self.frame_cycle_start.setMinimumSize(QSize(150, 50))
        self.horizontalLayout_30 = QHBoxLayout(self.frame_cycle_start)
        self.horizontalLayout_30.setSpacing(8)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 8, 0)
        self.lbl_cycle_start = QLabel(self.frame_cycle_start)
        self.lbl_cycle_start.setObjectName(u"lbl_cycle_start")
        self.lbl_cycle_start.setStyleSheet(u"\n"
"font: 75 12pt \"Bebas Kai\";")
        self.lbl_cycle_start.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.lbl_cycle_start)

        self.lbl_start_line = QLineEdit(self.frame_cycle_start)
        self.lbl_start_line.setObjectName(u"lbl_start_line")
        sizePolicy.setHeightForWidth(self.lbl_start_line.sizePolicy().hasHeightForWidth())
        self.lbl_start_line.setSizePolicy(sizePolicy)
        self.lbl_start_line.setMinimumSize(QSize(60, 24))
        self.lbl_start_line.setMaximumSize(QSize(60, 24))
        self.lbl_start_line.setMaxLength(8)
        self.lbl_start_line.setAlignment(Qt.AlignCenter)
        self.lbl_start_line.setReadOnly(True)

        self.horizontalLayout_30.addWidget(self.lbl_start_line)

        self.led_cycle_start = StateLED(self.frame_cycle_start)
        self.led_cycle_start.setObjectName(u"led_cycle_start")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.led_cycle_start.sizePolicy().hasHeightForWidth())
        self.led_cycle_start.setSizePolicy(sizePolicy1)
        self.led_cycle_start.setMinimumSize(QSize(20, 0))
        self.led_cycle_start.setMaximumSize(QSize(20, 16777215))
        self.led_cycle_start.setDiameter(15)
        self.led_cycle_start.setColor(QColor(0, 255, 0))
        self.led_cycle_start.setProperty("invert_state_status", True)
        self.led_cycle_start.setProperty("is_paused_status", False)
        self.led_cycle_start.setProperty("is_idle_status", True)

        self.horizontalLayout_30.addWidget(self.led_cycle_start)


        self.horizontalLayout_64.addWidget(self.frame_cycle_start)


        self.gridLayout_17.addLayout(self.horizontalLayout_64, 0, 0, 1, 1)

        self.widget_runtime = QWidget(self.frame_program)
        self.widget_runtime.setObjectName(u"widget_runtime")
        sizePolicy.setHeightForWidth(self.widget_runtime.sizePolicy().hasHeightForWidth())
        self.widget_runtime.setSizePolicy(sizePolicy)
        self.widget_runtime.setMinimumSize(QSize(90, 50))
        self.widget_runtime.setMaximumSize(QSize(90, 50))
        self.label_57 = QLabel(self.widget_runtime)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(9, 5, 72, 16))
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_57.sizePolicy().hasHeightForWidth())
        self.label_57.setSizePolicy(sizePolicy2)
        self.label_57.setMinimumSize(QSize(0, 0))
        self.label_57.setMaximumSize(QSize(16777215, 16777215))
        self.label_57.setStyleSheet(u"\n"
"font: 75 12pt \"Bebas Kai\";")
        self.label_57.setAlignment(Qt.AlignCenter)
        self.lbl_runtime = QLineEdit(self.widget_runtime)
        self.lbl_runtime.setObjectName(u"lbl_runtime")
        self.lbl_runtime.setGeometry(QRect(3, 23, 85, 27))
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lbl_runtime.sizePolicy().hasHeightForWidth())
        self.lbl_runtime.setSizePolicy(sizePolicy3)
        self.lbl_runtime.setMinimumSize(QSize(0, 27))
        self.lbl_runtime.setMaximumSize(QSize(16777215, 27))
        self.lbl_runtime.setStyleSheet(u"\n"
"font: 75 17pt \"Bebas Kai\";")
        self.lbl_runtime.setAlignment(Qt.AlignCenter)
        self.lbl_runtime.setReadOnly(True)

        self.gridLayout_17.addWidget(self.widget_runtime, 0, 1, 1, 1)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setSpacing(4)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(-1, 0, -1, 0)
        self.action_pause = ActionButton(self.frame_program)
        self.action_pause.setObjectName(u"action_pause")
        sizePolicy.setHeightForWidth(self.action_pause.sizePolicy().hasHeightForWidth())
        self.action_pause.setSizePolicy(sizePolicy)
        self.action_pause.setMinimumSize(QSize(80, 49))
        self.action_pause.setMaximumSize(QSize(80, 49))
        self.action_pause.setStyleSheet(u"font: 12pt \"Sans\";")
        self.action_pause.setCheckable(True)
        self.action_pause.setProperty("indicator_option", False)
        self.action_pause.setProperty("indicator_HAL_pin_option", False)
        self.action_pause.setProperty("indicator_status_option", True)
        self.action_pause.setProperty("checked_state_text_option", True)
        self.action_pause.setProperty("python_command_option", False)
        self.action_pause.setProperty("on_color", QColor(255, 255, 0))
        self.action_pause.setProperty("shape_option", 1)
        self.action_pause.setProperty("off_color", QColor(0, 0, 0))
        self.action_pause.setProperty("indicator_size", 0.200000000000000)
        self.action_pause.setProperty("is_paused_status", True)
        self.action_pause.setProperty("pause_action", True)
        self.action_pause.setProperty("template_label_option", False)
        self.action_pause.setProperty("joint_number", 0)
        self.action_pause.setProperty("incr_imperial_number", 0.010000000000000)
        self.action_pause.setProperty("incr_mm_number", 0.025000000000000)
        self.action_pause.setProperty("incr_angular_number", -1.000000000000000)
        self.action_pause.setProperty("toggle_float_option", False)
        self.action_pause.setProperty("float_num", 100.000000000000000)
        self.action_pause.setProperty("float_alt_num", 50.000000000000000)
        self.action_pause.setProperty("ini_mdi_number", 0)
        self.action_pause.setProperty("paused", False)

        self.horizontalLayout_66.addWidget(self.action_pause)

        self.action_abort = ActionButton(self.frame_program)
        self.action_abort.setObjectName(u"action_abort")
        sizePolicy.setHeightForWidth(self.action_abort.sizePolicy().hasHeightForWidth())
        self.action_abort.setSizePolicy(sizePolicy)
        self.action_abort.setMinimumSize(QSize(80, 49))
        self.action_abort.setMaximumSize(QSize(80, 49))
        self.action_abort.setStyleSheet(u"font: 12pt \"Sans\";")
        self.action_abort.setProperty("abort_action", True)
        self.action_abort.setProperty("template_label_option", False)
        self.action_abort.setProperty("joint_number", 0)
        self.action_abort.setProperty("incr_imperial_number", 0.010000000000000)
        self.action_abort.setProperty("incr_mm_number", 0.025000000000000)
        self.action_abort.setProperty("incr_angular_number", -1.000000000000000)
        self.action_abort.setProperty("toggle_float_option", False)
        self.action_abort.setProperty("float_num", 100.000000000000000)
        self.action_abort.setProperty("float_alt_num", 50.000000000000000)
        self.action_abort.setProperty("ini_mdi_number", 0)

        self.horizontalLayout_66.addWidget(self.action_abort)


        self.gridLayout_17.addLayout(self.horizontalLayout_66, 1, 0, 1, 1)

        self.spindle_pause = PushButton(self.frame_program)
        self.spindle_pause.setObjectName(u"spindle_pause")
        sizePolicy.setHeightForWidth(self.spindle_pause.sizePolicy().hasHeightForWidth())
        self.spindle_pause.setSizePolicy(sizePolicy)
        self.spindle_pause.setMinimumSize(QSize(80, 49))
        self.spindle_pause.setMaximumSize(QSize(80, 49))
        self.spindle_pause.setStyleSheet(u"")
        self.spindle_pause.setCheckable(True)
        self.spindle_pause.setProperty("checked_state_text_option", True)
        self.spindle_pause.setProperty("on_color", QColor(255, 255, 0))
        self.spindle_pause.setProperty("shape_option", 1)

        self.gridLayout_17.addWidget(self.spindle_pause, 1, 1, 1, 1)

        self.stateled_paused = StateLED(self.frame_program)
        self.stateled_paused.setObjectName(u"stateled_paused")
        self.stateled_paused.setColor(QColor(255, 255, 0))
        self.stateled_paused.setProperty("is_paused_status", True)

        self.gridLayout_17.addWidget(self.stateled_paused, 1, 2, 1, 1)

        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setSpacing(4)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(-1, 0, -1, 0)
        self.action_opt_blk = ActionButton(self.frame_program)
        self.action_opt_blk.setObjectName(u"action_opt_blk")
        sizePolicy.setHeightForWidth(self.action_opt_blk.sizePolicy().hasHeightForWidth())
        self.action_opt_blk.setSizePolicy(sizePolicy)
        self.action_opt_blk.setMinimumSize(QSize(80, 49))
        self.action_opt_blk.setMaximumSize(QSize(80, 50))
        self.action_opt_blk.setCheckable(True)
        self.action_opt_blk.setProperty("indicator_option", True)
        self.action_opt_blk.setProperty("indicator_HAL_pin_option", False)
        self.action_opt_blk.setProperty("indicator_status_option", True)
        self.action_opt_blk.setProperty("on_color", QColor(0, 255, 0))
        self.action_opt_blk.setProperty("shape_option", 1)
        self.action_opt_blk.setProperty("off_color", QColor(255, 0, 0))
        self.action_opt_blk.setProperty("indicator_size", 0.200000000000000)
        self.action_opt_blk.setProperty("right_edge_offset", 5.000000000000000)
        self.action_opt_blk.setProperty("top_edge_offset", 5.000000000000000)
        self.action_opt_blk.setProperty("is_block_delete_status", True)
        self.action_opt_blk.setProperty("block_delete_action", True)

        self.horizontalLayout_67.addWidget(self.action_opt_blk)

        self.action_step = ActionButton(self.frame_program)
        self.action_step.setObjectName(u"action_step")
        sizePolicy.setHeightForWidth(self.action_step.sizePolicy().hasHeightForWidth())
        self.action_step.setSizePolicy(sizePolicy)
        self.action_step.setMinimumSize(QSize(80, 49))
        self.action_step.setMaximumSize(QSize(80, 49))
        self.action_step.setStyleSheet(u"font: 12pt \"Sans\";")
        self.action_step.setProperty("step_action", True)
        self.action_step.setProperty("template_label_option", False)
        self.action_step.setProperty("joint_number", 0)
        self.action_step.setProperty("incr_imperial_number", 0.010000000000000)
        self.action_step.setProperty("incr_mm_number", 0.025000000000000)
        self.action_step.setProperty("incr_angular_number", -1.000000000000000)
        self.action_step.setProperty("toggle_float_option", False)
        self.action_step.setProperty("float_num", 100.000000000000000)
        self.action_step.setProperty("float_alt_num", 50.000000000000000)
        self.action_step.setProperty("ini_mdi_number", 0)

        self.horizontalLayout_67.addWidget(self.action_step)


        self.gridLayout_17.addLayout(self.horizontalLayout_67, 2, 0, 1, 1)

        self.action_flood = ActionButton(self.frame_program)
        self.action_flood.setObjectName(u"action_flood")
        sizePolicy.setHeightForWidth(self.action_flood.sizePolicy().hasHeightForWidth())
        self.action_flood.setSizePolicy(sizePolicy)
        self.action_flood.setMinimumSize(QSize(80, 49))
        self.action_flood.setMaximumSize(QSize(80, 49))
        self.action_flood.setCheckable(True)
        self.action_flood.setChecked(False)
        self.action_flood.setProperty("indicator_option", True)
        self.action_flood.setProperty("indicator_HAL_pin_option", False)
        self.action_flood.setProperty("indicator_status_option", True)
        self.action_flood.setProperty("checked_state_text_option", True)
        self.action_flood.setProperty("on_color", QColor(0, 255, 0))
        self.action_flood.setProperty("shape_option", 1)
        self.action_flood.setProperty("off_color", QColor(255, 0, 0))
        self.action_flood.setProperty("indicator_size", 0.200000000000000)
        self.action_flood.setProperty("right_edge_offset", 5.000000000000000)
        self.action_flood.setProperty("top_edge_offset", 5.000000000000000)
        self.action_flood.setProperty("is_on_status", False)
        self.action_flood.setProperty("is_flood_status", True)
        self.action_flood.setProperty("flood_action", True)

        self.gridLayout_17.addWidget(self.action_flood, 2, 1, 1, 1)

        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setSpacing(4)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(-1, 0, -1, 0)
        self.action_opt_stp = ActionButton(self.frame_program)
        self.action_opt_stp.setObjectName(u"action_opt_stp")
        sizePolicy.setHeightForWidth(self.action_opt_stp.sizePolicy().hasHeightForWidth())
        self.action_opt_stp.setSizePolicy(sizePolicy)
        self.action_opt_stp.setMinimumSize(QSize(80, 49))
        self.action_opt_stp.setMaximumSize(QSize(80, 49))
        self.action_opt_stp.setCheckable(True)
        self.action_opt_stp.setProperty("indicator_option", True)
        self.action_opt_stp.setProperty("indicator_HAL_pin_option", False)
        self.action_opt_stp.setProperty("indicator_status_option", True)
        self.action_opt_stp.setProperty("on_color", QColor(0, 255, 0))
        self.action_opt_stp.setProperty("shape_option", 1)
        self.action_opt_stp.setProperty("off_color", QColor(255, 0, 0))
        self.action_opt_stp.setProperty("indicator_size", 0.200000000000000)
        self.action_opt_stp.setProperty("right_edge_offset", 5.000000000000000)
        self.action_opt_stp.setProperty("top_edge_offset", 5.000000000000000)
        self.action_opt_stp.setProperty("is_block_delete_status", False)
        self.action_opt_stp.setProperty("is_optional_stop_status", True)
        self.action_opt_stp.setProperty("optional_stop_action", True)

        self.horizontalLayout_68.addWidget(self.action_opt_stp)

        self.btn_reload_file = QPushButton(self.frame_program)
        self.btn_reload_file.setObjectName(u"btn_reload_file")
        sizePolicy.setHeightForWidth(self.btn_reload_file.sizePolicy().hasHeightForWidth())
        self.btn_reload_file.setSizePolicy(sizePolicy)
        self.btn_reload_file.setMinimumSize(QSize(80, 49))
        self.btn_reload_file.setMaximumSize(QSize(80, 49))
        self.btn_reload_file.setStyleSheet(u"font: 12pt \"Sans\";")

        self.horizontalLayout_68.addWidget(self.btn_reload_file)


        self.gridLayout_17.addLayout(self.horizontalLayout_68, 3, 0, 1, 1)

        self.action_mist = ActionButton(self.frame_program)
        self.action_mist.setObjectName(u"action_mist")
        sizePolicy.setHeightForWidth(self.action_mist.sizePolicy().hasHeightForWidth())
        self.action_mist.setSizePolicy(sizePolicy)
        self.action_mist.setMinimumSize(QSize(80, 49))
        self.action_mist.setMaximumSize(QSize(80, 49))
        self.action_mist.setCheckable(True)
        self.action_mist.setChecked(False)
        self.action_mist.setProperty("indicator_option", True)
        self.action_mist.setProperty("indicator_HAL_pin_option", False)
        self.action_mist.setProperty("indicator_status_option", True)
        self.action_mist.setProperty("checked_state_text_option", True)
        self.action_mist.setProperty("on_color", QColor(0, 255, 0))
        self.action_mist.setProperty("shape_option", 1)
        self.action_mist.setProperty("off_color", QColor(255, 0, 0))
        self.action_mist.setProperty("indicator_size", 0.200000000000000)
        self.action_mist.setProperty("right_edge_offset", 5.000000000000000)
        self.action_mist.setProperty("top_edge_offset", 5.000000000000000)
        self.action_mist.setProperty("is_mist_status", True)
        self.action_mist.setProperty("mist_action", True)

        self.gridLayout_17.addWidget(self.action_mist, 3, 1, 1, 1)

        self.progressBar = QProgressBar(self.frame_program)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy3.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy3)
        self.progressBar.setMinimumSize(QSize(0, 24))
        self.progressBar.setMaximumSize(QSize(16777215, 24))
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setMaximum(99)
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setInvertedAppearance(False)

        self.gridLayout_17.addWidget(self.progressBar, 4, 0, 1, 3)

        self.stackedWidget_3.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.frame_3 = QFrame(self.page_5)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 0, 321, 271))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_override = QFrame(self.frame_3)
        self.frame_override.setObjectName(u"frame_override")
        self.frame_override.setGeometry(QRect(0, 0, 321, 271))
        self.frame_override.setMinimumSize(QSize(300, 250))
        self.frame_override.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_override.setFrameShape(QFrame.WinPanel)
        self.frame_override.setFrameShadow(QFrame.Raised)
        self.abtn_override_spindle_rate = ActionButton(self.frame_override)
        self.abtn_override_spindle_rate.setObjectName(u"abtn_override_spindle_rate")
        self.abtn_override_spindle_rate.setGeometry(QRect(10, 21, 60, 40))
        self.abtn_override_spindle_rate.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.abtn_override_spindle_rate.setProperty("feed_over_action", False)
        self.abtn_override_spindle_rate.setProperty("rapid_over_action", False)
        self.abtn_override_spindle_rate.setProperty("spindle_over_action", True)
        self.abtn_override_spindle_rate.setProperty("toggle_float_option", True)
        self.abtn_override_spindle_rate.setProperty("float_alt_num", 90.000000000000000)
        self.abtn_override_feed_rate = ActionButton(self.frame_override)
        self.abtn_override_feed_rate.setObjectName(u"abtn_override_feed_rate")
        self.abtn_override_feed_rate.setGeometry(QRect(80, 21, 60, 40))
        self.abtn_override_feed_rate.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.abtn_override_feed_rate.setProperty("feed_over_action", True)
        self.abtn_override_feed_rate.setProperty("toggle_float_option", True)
        self.abtn_override_feed_rate.setProperty("float_alt_num", 75.000000000000000)
        self.abtn_override_rapid_rate = ActionButton(self.frame_override)
        self.abtn_override_rapid_rate.setObjectName(u"abtn_override_rapid_rate")
        self.abtn_override_rapid_rate.setGeometry(QRect(150, 21, 60, 40))
        self.abtn_override_rapid_rate.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.abtn_override_rapid_rate.setProperty("feed_over_action", False)
        self.abtn_override_rapid_rate.setProperty("rapid_over_action", True)
        self.abtn_override_rapid_rate.setProperty("toggle_float_option", True)
        self.abtn_override_rapid_rate.setProperty("float_alt_num", 25.000000000000000)
        self.label_override_panel_label = QLabel(self.frame_override)
        self.label_override_panel_label.setObjectName(u"label_override_panel_label")
        self.label_override_panel_label.setGeometry(QRect(0, 0, 320, 21))
        font = QFont()
        font.setFamily(u"Bebas Kai")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        self.label_override_panel_label.setFont(font)
        self.label_override_panel_label.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.label_override_panel_label.setFrameShape(QFrame.NoFrame)
        self.label_override_panel_label.setFrameShadow(QFrame.Plain)
        self.label_override_panel_label.setAlignment(Qt.AlignCenter)
        self.frame_11 = QFrame(self.frame_override)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(10, 100, 301, 161))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.slider_spindle_ovr = StatusSlider(self.frame_11)
        self.slider_spindle_ovr.setObjectName(u"slider_spindle_ovr")
        self.slider_spindle_ovr.setGeometry(QRect(20, 10, 30, 151))
        self.slider_spindle_ovr.setMinimumSize(QSize(30, 0))
        self.slider_spindle_ovr.setStyleSheet(u"QSlider::groove:vertical {\n"
"border: 1px solid #bbb;\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"width: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"background: white;\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal  {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"width: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:vertical  {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 2"
                        "55, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"height: 30px;\n"
"margin-top: -1.3px;\n"
"margin-bottom: -1.3px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #444;\n"
"border-color: rgb(241, 239, 237);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
""
                        "}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.slider_spindle_ovr.setProperty("spindle_rate", True)
        self.slider_feed_ovr = StatusSlider(self.frame_11)
        self.slider_feed_ovr.setObjectName(u"slider_feed_ovr")
        self.slider_feed_ovr.setGeometry(QRect(90, 10, 30, 151))
        self.slider_feed_ovr.setMinimumSize(QSize(30, 0))
        self.slider_feed_ovr.setStyleSheet(u"QSlider::groove:vertical {\n"
"border: 1px solid #bbb;\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"width: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"background: white;\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal  {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"width: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:vertical  {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 2"
                        "55, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"height: 30px;\n"
"margin-top: -1.3px;\n"
"margin-bottom: -1.3px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #444;\n"
"border-color: rgb(241, 239, 237);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
""
                        "}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.slider_feed_ovr.setProperty("feed_rate", True)
        self.slider_rapid_ovr = StatusSlider(self.frame_11)
        self.slider_rapid_ovr.setObjectName(u"slider_rapid_ovr")
        self.slider_rapid_ovr.setGeometry(QRect(160, 10, 30, 151))
        self.slider_rapid_ovr.setMinimumSize(QSize(30, 0))
        self.slider_rapid_ovr.setStyleSheet(u"QSlider::groove:vertical {\n"
"border: 1px solid #bbb;\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"width: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"background: white;\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal  {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"width: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:vertical  {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 2"
                        "55, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"height: 30px;\n"
"margin-top: -1.3px;\n"
"margin-bottom: -1.3px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #444;\n"
"border-color: rgb(241, 239, 237);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
""
                        "}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.slider_rapid_ovr.setMaximum(100)
        self.slider_jog_angular = StatusSlider(self.frame_11)
        self.slider_jog_angular.setObjectName(u"slider_jog_angular")
        self.slider_jog_angular.setGeometry(QRect(220, 10, 30, 151))
        self.slider_jog_angular.setMinimumSize(QSize(30, 0))
        self.slider_jog_angular.setStyleSheet(u"QSlider::groove:vertical {\n"
"border: 1px solid #bbb;\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"width: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"background: white;\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal  {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"width: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:vertical  {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 2"
                        "55, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"height: 30px;\n"
"margin-top: -1.3px;\n"
"margin-bottom: -1.3px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #444;\n"
"border-color: rgb(241, 239, 237);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
""
                        "}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.slider_jog_angular.setMaximum(100)
        self.slider_jog_angular.setProperty("jograte_angular_rate", True)
        self.btn_jog_a_slow = PushButton(self.frame_11)
        self.btn_jog_a_slow.setObjectName(u"btn_jog_a_slow")
        self.btn_jog_a_slow.setGeometry(QRect(250, 10, 50, 50))
        sizePolicy.setHeightForWidth(self.btn_jog_a_slow.sizePolicy().hasHeightForWidth())
        self.btn_jog_a_slow.setSizePolicy(sizePolicy)
        self.btn_jog_a_slow.setMinimumSize(QSize(50, 50))
        self.btn_jog_a_slow.setMaximumSize(QSize(50, 50))
        self.btn_jog_a_slow.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.btn_jog_a_slow.setCheckable(True)
        self.btn_jog_a_slow.setProperty("checked_state_text_option", True)
        self.statuslabel = StatusLabel(self.frame_override)
        self.statuslabel.setObjectName(u"statuslabel")
        self.statuslabel.setGeometry(QRect(10, 64, 61, 31))
        self.statuslabel.setMinimumSize(QSize(60, 0))
        self.statuslabel.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.statuslabel.setFrameShape(QFrame.WinPanel)
        self.statuslabel.setFrameShadow(QFrame.Sunken)
        self.statuslabel.setProperty("spindle_override_status", True)
        self.statuslabel_2 = StatusLabel(self.frame_override)
        self.statuslabel_2.setObjectName(u"statuslabel_2")
        self.statuslabel_2.setGeometry(QRect(80, 64, 60, 31))
        self.statuslabel_2.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.statuslabel_2.setFrameShape(QFrame.WinPanel)
        self.statuslabel_2.setFrameShadow(QFrame.Sunken)
        self.statuslabel_2.setProperty("feed_override_status", True)
        self.statuslabel_2.setProperty("spindle_override_status", False)
        self.statuslabel_3 = StatusLabel(self.frame_override)
        self.statuslabel_3.setObjectName(u"statuslabel_3")
        self.statuslabel_3.setGeometry(QRect(150, 64, 60, 31))
        self.statuslabel_3.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.statuslabel_3.setFrameShape(QFrame.WinPanel)
        self.statuslabel_3.setFrameShadow(QFrame.Sunken)
        self.statuslabel_3.setProperty("rapid_override_status", True)
        self.statuslabel_3.setProperty("spindle_override_status", False)
        self.status_label_jog_angular = StatusLabel(self.frame_override)
        self.status_label_jog_angular.setObjectName(u"status_label_jog_angular")
        self.status_label_jog_angular.setGeometry(QRect(220, 64, 60, 31))
        self.status_label_jog_angular.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.status_label_jog_angular.setFrameShape(QFrame.WinPanel)
        self.status_label_jog_angular.setFrameShadow(QFrame.Sunken)
        self.status_label_jog_angular.setProperty("rapid_override_status", False)
        self.status_label_jog_angular.setProperty("spindle_override_status", False)
        self.status_label_jog_angular.setProperty("jograte_angular_status", True)
        self.lbl_jog_angular = QLabel(self.frame_override)
        self.lbl_jog_angular.setObjectName(u"lbl_jog_angular")
        self.lbl_jog_angular.setGeometry(QRect(220, 30, 60, 30))
        sizePolicy3.setHeightForWidth(self.lbl_jog_angular.sizePolicy().hasHeightForWidth())
        self.lbl_jog_angular.setSizePolicy(sizePolicy3)
        self.lbl_jog_angular.setMinimumSize(QSize(0, 30))
        self.lbl_jog_angular.setMaximumSize(QSize(60, 30))
        self.lbl_jog_angular.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.lbl_jog_angular.setAlignment(Qt.AlignCenter)
        self.stackedWidget_3.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.frame_4 = QFrame(self.page_6)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 0, 321, 271))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.widget_max_vel_ovr_2 = QWidget(self.frame_4)
        self.widget_max_vel_ovr_2.setObjectName(u"widget_max_vel_ovr_2")
        self.widget_max_vel_ovr_2.setGeometry(QRect(10, 80, 221, 131))
        sizePolicy1.setHeightForWidth(self.widget_max_vel_ovr_2.sizePolicy().hasHeightForWidth())
        self.widget_max_vel_ovr_2.setSizePolicy(sizePolicy1)
        self.widget_max_vel_ovr_2.setMinimumSize(QSize(180, 0))
        self.verticalLayout_40 = QVBoxLayout(self.widget_max_vel_ovr_2)
        self.verticalLayout_40.setSpacing(4)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(4, 0, 0, 0)
        self.label_50 = QLabel(self.widget_max_vel_ovr_2)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setStyleSheet(u"font: 15pt \"Sans\";")
        self.label_50.setAlignment(Qt.AlignCenter)

        self.verticalLayout_40.addWidget(self.label_50)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setSpacing(4)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(-1, 1, -1, 1)
        self.action_max_vel_ovr_241 = ActionButton(self.widget_max_vel_ovr_2)
        self.action_max_vel_ovr_241.setObjectName(u"action_max_vel_ovr_241")
        sizePolicy2.setHeightForWidth(self.action_max_vel_ovr_241.sizePolicy().hasHeightForWidth())
        self.action_max_vel_ovr_241.setSizePolicy(sizePolicy2)
        self.action_max_vel_ovr_241.setMinimumSize(QSize(50, 30))
        self.action_max_vel_ovr_241.setMaximumSize(QSize(50, 30))
        self.action_max_vel_ovr_241.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.action_max_vel_ovr_241.setProperty("rapid_over_action", False)
        self.action_max_vel_ovr_241.setProperty("max_velocity_over_action", True)
        self.action_max_vel_ovr_241.setProperty("float_num", 240.000000000000000)

        self.horizontalLayout_37.addWidget(self.action_max_vel_ovr_241, 0, Qt.AlignLeft)

        self.action_max_vel_ovr_401 = ActionButton(self.widget_max_vel_ovr_2)
        self.action_max_vel_ovr_401.setObjectName(u"action_max_vel_ovr_401")
        sizePolicy2.setHeightForWidth(self.action_max_vel_ovr_401.sizePolicy().hasHeightForWidth())
        self.action_max_vel_ovr_401.setSizePolicy(sizePolicy2)
        self.action_max_vel_ovr_401.setMinimumSize(QSize(50, 30))
        self.action_max_vel_ovr_401.setMaximumSize(QSize(50, 30))
        self.action_max_vel_ovr_401.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.action_max_vel_ovr_401.setProperty("rapid_over_action", False)
        self.action_max_vel_ovr_401.setProperty("max_velocity_over_action", True)
        self.action_max_vel_ovr_401.setProperty("float_num", 400.000000000000000)

        self.horizontalLayout_37.addWidget(self.action_max_vel_ovr_401, 0, Qt.AlignHCenter)

        self.action_max_vel_ovr_801 = ActionButton(self.widget_max_vel_ovr_2)
        self.action_max_vel_ovr_801.setObjectName(u"action_max_vel_ovr_801")
        sizePolicy2.setHeightForWidth(self.action_max_vel_ovr_801.sizePolicy().hasHeightForWidth())
        self.action_max_vel_ovr_801.setSizePolicy(sizePolicy2)
        self.action_max_vel_ovr_801.setMinimumSize(QSize(50, 30))
        self.action_max_vel_ovr_801.setMaximumSize(QSize(50, 30))
        self.action_max_vel_ovr_801.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.action_max_vel_ovr_801.setProperty("rapid_over_action", False)
        self.action_max_vel_ovr_801.setProperty("max_velocity_over_action", True)
        self.action_max_vel_ovr_801.setProperty("float_num", 800.000000000000000)
        self.action_max_vel_ovr_801.setProperty("float_alt_num", 50.000000000000000)

        self.horizontalLayout_37.addWidget(self.action_max_vel_ovr_801)

        self.action_max_vel_ovr_1601 = ActionButton(self.widget_max_vel_ovr_2)
        self.action_max_vel_ovr_1601.setObjectName(u"action_max_vel_ovr_1601")
        sizePolicy2.setHeightForWidth(self.action_max_vel_ovr_1601.sizePolicy().hasHeightForWidth())
        self.action_max_vel_ovr_1601.setSizePolicy(sizePolicy2)
        self.action_max_vel_ovr_1601.setMinimumSize(QSize(50, 30))
        self.action_max_vel_ovr_1601.setMaximumSize(QSize(50, 30))
        self.action_max_vel_ovr_1601.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.action_max_vel_ovr_1601.setProperty("rapid_over_action", False)
        self.action_max_vel_ovr_1601.setProperty("max_velocity_over_action", True)
        self.action_max_vel_ovr_1601.setProperty("float_num", 1600.000000000000000)
        self.action_max_vel_ovr_1601.setProperty("float_alt_num", 50.000000000000000)

        self.horizontalLayout_37.addWidget(self.action_max_vel_ovr_1601, 0, Qt.AlignRight)


        self.verticalLayout_40.addLayout(self.horizontalLayout_37)

        self.slider_maxv_ovr = StatusSlider(self.widget_max_vel_ovr_2)
        self.slider_maxv_ovr.setObjectName(u"slider_maxv_ovr")
        sizePolicy3.setHeightForWidth(self.slider_maxv_ovr.sizePolicy().hasHeightForWidth())
        self.slider_maxv_ovr.setSizePolicy(sizePolicy3)
        self.slider_maxv_ovr.setMinimumSize(QSize(180, 51))
        self.slider_maxv_ovr.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal  {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255"
                        ", 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"width: 30px;\n"
"margin-top: -13px;\n"
"margin-bottom: -13px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #444;\n"
"border-color: rgb(241, 239, 237);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
""
                        "}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.slider_maxv_ovr.setInputMethodHints(Qt.ImhNone)
        self.slider_maxv_ovr.setMaximum(100)
        self.slider_maxv_ovr.setSingleStep(1)
        self.slider_maxv_ovr.setPageStep(10)
        self.slider_maxv_ovr.setValue(100)
        self.slider_maxv_ovr.setOrientation(Qt.Horizontal)
        self.slider_maxv_ovr.setProperty("rapid_rate", False)
        self.slider_maxv_ovr.setProperty("feed_rate", False)
        self.slider_maxv_ovr.setProperty("jograte_rate", False)
        self.slider_maxv_ovr.setProperty("max_velocity_rate", True)

        self.verticalLayout_40.addWidget(self.slider_maxv_ovr)

        self.horizontalLayoutWidget_4 = QWidget(self.frame_4)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 40, 211, 41))
        self.horizontalLayout_18 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.horizontalLayoutWidget_4)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.label_max_welocity = StatusLabel(self.frame_15)
        self.label_max_welocity.setObjectName(u"label_max_welocity")
        self.label_max_welocity.setGeometry(QRect(1, 1, 205, 37))
        sizePolicy3.setHeightForWidth(self.label_max_welocity.sizePolicy().hasHeightForWidth())
        self.label_max_welocity.setSizePolicy(sizePolicy3)
        self.label_max_welocity.setMinimumSize(QSize(187, 37))
        self.label_max_welocity.setMaximumSize(QSize(16777215, 16777215))
        self.label_max_welocity.setStyleSheet(u"font: 15pt \"Sans\";")
        self.label_max_welocity.setFrameShape(QFrame.WinPanel)
        self.label_max_welocity.setFrameShadow(QFrame.Raised)
        self.label_max_welocity.setAlignment(Qt.AlignCenter)
        self.label_max_welocity.setProperty("index_number", 0)
        self.label_max_welocity.setProperty("max_velocity_override_status", True)
        self.label_max_welocity.setProperty("current_feedrate_status", False)
        self.label_max_welocity.setProperty("gcode_selected_status", False)

        self.horizontalLayout_18.addWidget(self.frame_15)

        self.lbl_maxv_percent = QLineEdit(self.frame_4)
        self.lbl_maxv_percent.setObjectName(u"lbl_maxv_percent")
        self.lbl_maxv_percent.setGeometry(QRect(230, 42, 81, 37))
        self.lbl_maxv_percent.setStyleSheet(u"font: 15pt \"Sans\";")
        self.lbl_maxv_percent.setMaxLength(5)
        self.lbl_maxv_percent.setAlignment(Qt.AlignCenter)
        self.stackedWidget_3.addWidget(self.page_6)
        self.frame_dro = QFrame(self.frame_spindle_and_dro)
        self.frame_dro.setObjectName(u"frame_dro")
        self.frame_dro.setGeometry(QRect(380, 0, 573, 271))
        sizePolicy1.setHeightForWidth(self.frame_dro.sizePolicy().hasHeightForWidth())
        self.frame_dro.setSizePolicy(sizePolicy1)
        self.frame_dro.setMinimumSize(QSize(573, 271))
        self.frame_dro.setMaximumSize(QSize(16777215, 251))
        self.frame_dro.setFrameShape(QFrame.WinPanel)
        self.frame_dro.setFrameShadow(QFrame.Raised)
        self.frame_dro_buttons = QFrame(self.frame_dro)
        self.frame_dro_buttons.setObjectName(u"frame_dro_buttons")
        self.frame_dro_buttons.setGeometry(QRect(-2, 0, 65, 271))
        sizePolicy.setHeightForWidth(self.frame_dro_buttons.sizePolicy().hasHeightForWidth())
        self.frame_dro_buttons.setSizePolicy(sizePolicy)
        self.frame_dro_buttons.setMinimumSize(QSize(65, 271))
        self.frame_dro_buttons.setMaximumSize(QSize(65, 271))
        self.frame_dro_buttons.setFrameShape(QFrame.WinPanel)
        self.frame_dro_buttons.setFrameShadow(QFrame.Raised)
        self.abtn_dro_dtg = ActionButton(self.frame_dro_buttons)
        self.abtn_dro_dtg.setObjectName(u"abtn_dro_dtg")
        self.abtn_dro_dtg.setGeometry(QRect(2, 200, 60, 50))
        self.abtn_dro_dtg.setMinimumSize(QSize(60, 50))
        self.abtn_dro_dtg.setMaximumSize(QSize(60, 50))
        self.abtn_dro_dtg.setStyleSheet(u"font: 12pt \"Sans\";")
        self.abtn_dro_dtg.setCheckable(True)
        self.abtn_dro_dtg.setAutoExclusive(True)
        self.abtn_dro_dtg.setProperty("dro_dtg_action", True)
        self.actionbutton_rel = ActionButton(self.frame_dro_buttons)
        self.actionbutton_rel.setObjectName(u"actionbutton_rel")
        self.actionbutton_rel.setGeometry(QRect(2, 140, 60, 50))
        self.actionbutton_rel.setMinimumSize(QSize(60, 50))
        self.actionbutton_rel.setMaximumSize(QSize(60, 50))
        self.actionbutton_rel.setStyleSheet(u"font: 12pt \"Sans\";")
        self.actionbutton_rel.setCheckable(True)
        self.actionbutton_rel.setChecked(False)
        self.actionbutton_rel.setAutoExclusive(True)
        self.actionbutton_rel.setProperty("checked_state_text_option", False)
        self.actionbutton_rel.setProperty("dro_relative_action", True)
        self.actionbutton_rel.setProperty("dro_dtg_action", False)
        self.abtn_dro_abs = ActionButton(self.frame_dro_buttons)
        self.abtn_dro_abs.setObjectName(u"abtn_dro_abs")
        self.abtn_dro_abs.setGeometry(QRect(2, 79, 60, 50))
        sizePolicy.setHeightForWidth(self.abtn_dro_abs.sizePolicy().hasHeightForWidth())
        self.abtn_dro_abs.setSizePolicy(sizePolicy)
        self.abtn_dro_abs.setMinimumSize(QSize(60, 50))
        self.abtn_dro_abs.setMaximumSize(QSize(60, 50))
        self.abtn_dro_abs.setStyleSheet(u"font: 12pt \"Sans\";")
        self.abtn_dro_abs.setCheckable(True)
        self.abtn_dro_abs.setChecked(True)
        self.abtn_dro_abs.setAutoExclusive(True)
        self.abtn_dro_abs.setProperty("dro_absolute_action", True)
        self.abtn_dro_abs.setProperty("dro_dtg_action", False)
        self.systemtoolbutton = SystemToolButton(self.frame_dro_buttons)
        self.systemtoolbutton.setObjectName(u"systemtoolbutton")
        self.systemtoolbutton.setGeometry(QRect(2, 17, 60, 50))
        self.systemtoolbutton.setMinimumSize(QSize(60, 50))
        self.systemtoolbutton.setMaximumSize(QSize(60, 50))
        self.systemtoolbutton.setStyleSheet(u"font: 12pt \"Sans\";")
        self.systemtoolbutton.setPopupMode(QToolButton.InstantPopup)
        self.frame_home_all = QFrame(self.frame_dro)
        self.frame_home_all.setObjectName(u"frame_home_all")
        self.frame_home_all.setGeometry(QRect(510, 20, 51, 150))
        sizePolicy3.setHeightForWidth(self.frame_home_all.sizePolicy().hasHeightForWidth())
        self.frame_home_all.setSizePolicy(sizePolicy3)
        self.frame_home_all.setMinimumSize(QSize(50, 150))
        self.frame_home_all.setMaximumSize(QSize(16777215, 50))
        self.frame_home_all.setFrameShape(QFrame.WinPanel)
        self.frame_home_all.setFrameShadow(QFrame.Raised)
        self.lbl_home_all = QLabel(self.frame_home_all)
        self.lbl_home_all.setObjectName(u"lbl_home_all")
        self.lbl_home_all.setGeometry(QRect(0, 53, 50, 100))
        sizePolicy.setHeightForWidth(self.lbl_home_all.sizePolicy().hasHeightForWidth())
        self.lbl_home_all.setSizePolicy(sizePolicy)
        self.lbl_home_all.setMinimumSize(QSize(50, 100))
        self.lbl_home_all.setMaximumSize(QSize(50, 16777215))
        self.lbl_home_all.setStyleSheet(u"")
        self.lbl_home_all.setAlignment(Qt.AlignCenter)
        self.led_all_homed = StateLED(self.frame_home_all)
        self.led_all_homed.setObjectName(u"led_all_homed")
        self.led_all_homed.setGeometry(QRect(0, 8, 50, 40))
        sizePolicy.setHeightForWidth(self.led_all_homed.sizePolicy().hasHeightForWidth())
        self.led_all_homed.setSizePolicy(sizePolicy)
        self.led_all_homed.setMinimumSize(QSize(50, 40))
        self.led_all_homed.setMaximumSize(QSize(50, 40))
        self.led_all_homed.setDiameter(15)
        self.led_all_homed.setColor(QColor(0, 255, 0))
        self.led_all_homed.setProperty("is_homed_status", True)
        self.led_all_homed.setProperty("joint_number_status", -1)
        self.widget_dro = QWidget(self.frame_dro)
        self.widget_dro.setObjectName(u"widget_dro")
        self.widget_dro.setGeometry(QRect(70, 10, 421, 251))
        self.gridLayout_dro = QGridLayout(self.widget_dro)
        self.gridLayout_dro.setSpacing(4)
        self.gridLayout_dro.setObjectName(u"gridLayout_dro")
        self.gridLayout_dro.setContentsMargins(4, 0, 4, 4)
        self.label_axis_z = QLabel(self.widget_dro)
        self.label_axis_z.setObjectName(u"label_axis_z")
        sizePolicy.setHeightForWidth(self.label_axis_z.sizePolicy().hasHeightForWidth())
        self.label_axis_z.setSizePolicy(sizePolicy)
        self.label_axis_z.setMinimumSize(QSize(64, 50))
        self.label_axis_z.setMaximumSize(QSize(64, 50))
        self.label_axis_z.setFrameShape(QFrame.WinPanel)
        self.label_axis_z.setFrameShadow(QFrame.Raised)
        self.label_axis_z.setLineWidth(2)
        self.label_axis_z.setAlignment(Qt.AlignCenter)

        self.gridLayout_dro.addWidget(self.label_axis_z, 2, 0, 1, 1)

        self.label_axis_a = QLabel(self.widget_dro)
        self.label_axis_a.setObjectName(u"label_axis_a")
        sizePolicy.setHeightForWidth(self.label_axis_a.sizePolicy().hasHeightForWidth())
        self.label_axis_a.setSizePolicy(sizePolicy)
        self.label_axis_a.setMinimumSize(QSize(64, 50))
        self.label_axis_a.setMaximumSize(QSize(64, 50))
        self.label_axis_a.setFrameShape(QFrame.WinPanel)
        self.label_axis_a.setFrameShadow(QFrame.Raised)
        self.label_axis_a.setLineWidth(2)
        self.label_axis_a.setAlignment(Qt.AlignCenter)

        self.gridLayout_dro.addWidget(self.label_axis_a, 3, 0, 1, 1)

        self.dro_axis_y = DROLabel(self.widget_dro)
        self.dro_axis_y.setObjectName(u"dro_axis_y")
        sizePolicy3.setHeightForWidth(self.dro_axis_y.sizePolicy().hasHeightForWidth())
        self.dro_axis_y.setSizePolicy(sizePolicy3)
        self.dro_axis_y.setMinimumSize(QSize(0, 50))
        self.dro_axis_y.setMaximumSize(QSize(16777215, 50))
        self.dro_axis_y.setStyleSheet(u"DROLabel {\n"
"    background-color: black;\n"
"    font: 20pt \"Lato Heavy\";\n"
"    color: #00FF00;\n"
"}\n"
"\n"
"DROLabel[homed=false] {\n"
"   color: #FFFF00;\n"
"}\n"
"")
        self.dro_axis_y.setFrameShape(QFrame.WinPanel)
        self.dro_axis_y.setFrameShadow(QFrame.Sunken)
        self.dro_axis_y.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dro_axis_y.setProperty("Qjoint_number", 1)
        self.dro_axis_y.setProperty("homed", False)

        self.gridLayout_dro.addWidget(self.dro_axis_y, 1, 1, 1, 2)

        self.action_zero_y = ActionButton(self.widget_dro)
        self.action_zero_y.setObjectName(u"action_zero_y")
        sizePolicy.setHeightForWidth(self.action_zero_y.sizePolicy().hasHeightForWidth())
        self.action_zero_y.setSizePolicy(sizePolicy)
        self.action_zero_y.setMinimumSize(QSize(64, 50))
        self.action_zero_y.setMaximumSize(QSize(64, 50))
        self.action_zero_y.setStyleSheet(u"font: 12pt \"Sans\";")
        self.action_zero_y.setProperty("indicator_option", False)
        self.action_zero_y.setProperty("indicator_HAL_pin_option", False)
        self.action_zero_y.setProperty("on_color", QColor(0, 255, 0))
        self.action_zero_y.setProperty("off_color", QColor(255, 0, 0))
        self.action_zero_y.setProperty("indicator_size", 0.200000000000000)
        self.action_zero_y.setProperty("mdi_action", False)
        self.action_zero_y.setProperty("zero_axis_action", True)
        self.action_zero_y.setProperty("template_label_option", False)
        self.action_zero_y.setProperty("joint_number", 1)
        self.action_zero_y.setProperty("incr_imperial_number", 0.010000000000000)
        self.action_zero_y.setProperty("incr_mm_number", 0.025000000000000)
        self.action_zero_y.setProperty("incr_angular_number", -1.000000000000000)
        self.action_zero_y.setProperty("toggle_float_option", False)
        self.action_zero_y.setProperty("float_num", 100.000000000000000)
        self.action_zero_y.setProperty("float_alt_num", 50.000000000000000)
        self.action_zero_y.setProperty("ini_mdi_number", 0)

        self.gridLayout_dro.addWidget(self.action_zero_y, 1, 3, 1, 1)

        self.action_zero_z = ActionButton(self.widget_dro)
        self.action_zero_z.setObjectName(u"action_zero_z")
        sizePolicy.setHeightForWidth(self.action_zero_z.sizePolicy().hasHeightForWidth())
        self.action_zero_z.setSizePolicy(sizePolicy)
        self.action_zero_z.setMinimumSize(QSize(64, 50))
        self.action_zero_z.setMaximumSize(QSize(64, 50))
        self.action_zero_z.setStyleSheet(u"font: 12pt \"Sans\";")
        self.action_zero_z.setProperty("indicator_option", False)
        self.action_zero_z.setProperty("indicator_HAL_pin_option", False)
        self.action_zero_z.setProperty("on_color", QColor(0, 255, 0))
        self.action_zero_z.setProperty("off_color", QColor(255, 0, 0))
        self.action_zero_z.setProperty("indicator_size", 0.200000000000000)
        self.action_zero_z.setProperty("mdi_action", False)
        self.action_zero_z.setProperty("zero_axis_action", True)
        self.action_zero_z.setProperty("template_label_option", False)
        self.action_zero_z.setProperty("joint_number", 2)
        self.action_zero_z.setProperty("incr_imperial_number", 0.010000000000000)
        self.action_zero_z.setProperty("incr_mm_number", 0.025000000000000)
        self.action_zero_z.setProperty("incr_angular_number", -1.000000000000000)
        self.action_zero_z.setProperty("toggle_float_option", False)
        self.action_zero_z.setProperty("float_num", 100.000000000000000)
        self.action_zero_z.setProperty("float_alt_num", 50.000000000000000)
        self.action_zero_z.setProperty("ini_mdi_number", 0)

        self.gridLayout_dro.addWidget(self.action_zero_z, 2, 3, 1, 1)

        self.action_zero_x = ActionButton(self.widget_dro)
        self.action_zero_x.setObjectName(u"action_zero_x")
        sizePolicy.setHeightForWidth(self.action_zero_x.sizePolicy().hasHeightForWidth())
        self.action_zero_x.setSizePolicy(sizePolicy)
        self.action_zero_x.setMinimumSize(QSize(64, 50))
        self.action_zero_x.setMaximumSize(QSize(64, 50))
        self.action_zero_x.setStyleSheet(u"font: 12pt \"Sans\";")
        self.action_zero_x.setProperty("indicator_option", False)
        self.action_zero_x.setProperty("indicator_HAL_pin_option", False)
        self.action_zero_x.setProperty("on_color", QColor(0, 255, 0))
        self.action_zero_x.setProperty("off_color", QColor(255, 0, 0))
        self.action_zero_x.setProperty("indicator_size", 0.200000000000000)
        self.action_zero_x.setProperty("mdi_action", False)
        self.action_zero_x.setProperty("zero_axis_action", True)
        self.action_zero_x.setProperty("template_label_option", False)
        self.action_zero_x.setProperty("joint_number", 0)
        self.action_zero_x.setProperty("incr_imperial_number", 0.010000000000000)
        self.action_zero_x.setProperty("incr_mm_number", 0.025000000000000)
        self.action_zero_x.setProperty("incr_angular_number", -1.000000000000000)
        self.action_zero_x.setProperty("toggle_float_option", False)
        self.action_zero_x.setProperty("float_num", 100.000000000000000)
        self.action_zero_x.setProperty("float_alt_num", 50.000000000000000)
        self.action_zero_x.setProperty("ini_mdi_number", 0)

        self.gridLayout_dro.addWidget(self.action_zero_x, 0, 3, 1, 1)

        self.dro_axis_x = DROLabel(self.widget_dro)
        self.dro_axis_x.setObjectName(u"dro_axis_x")
        sizePolicy3.setHeightForWidth(self.dro_axis_x.sizePolicy().hasHeightForWidth())
        self.dro_axis_x.setSizePolicy(sizePolicy3)
        self.dro_axis_x.setMinimumSize(QSize(0, 50))
        self.dro_axis_x.setMaximumSize(QSize(16777215, 50))
        self.dro_axis_x.setStyleSheet(u"DROLabel {\n"
"    background-color: black;\n"
"    font: 20pt \"Lato Heavy\";\n"
"    color: #00FF00;\n"
"}\n"
"\n"
"DROLabel[homed=false] {\n"
"    color: #FFFF00;\n"
"}\n"
"\n"
"")
        self.dro_axis_x.setFrameShape(QFrame.WinPanel)
        self.dro_axis_x.setFrameShadow(QFrame.Sunken)
        self.dro_axis_x.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dro_axis_x.setProperty("Qjoint_number", 0)
        self.dro_axis_x.setProperty("homed", False)

        self.gridLayout_dro.addWidget(self.dro_axis_x, 0, 1, 1, 2)

        self.dro_axis_a = DROLabel(self.widget_dro)
        self.dro_axis_a.setObjectName(u"dro_axis_a")
        sizePolicy3.setHeightForWidth(self.dro_axis_a.sizePolicy().hasHeightForWidth())
        self.dro_axis_a.setSizePolicy(sizePolicy3)
        self.dro_axis_a.setMinimumSize(QSize(0, 50))
        self.dro_axis_a.setMaximumSize(QSize(16777215, 50))
        self.dro_axis_a.setStyleSheet(u"DROLabel {\n"
"    background-color: black;\n"
"    font: 20pt \"Lato Heavy\";\n"
"    color: #00FF00;\n"
"}\n"
"\n"
"DROLabel[homed=false] {\n"
"   color: #FFFF00;\n"
"}\n"
"")
        self.dro_axis_a.setFrameShape(QFrame.WinPanel)
        self.dro_axis_a.setFrameShadow(QFrame.Sunken)
        self.dro_axis_a.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dro_axis_a.setProperty("Qjoint_number", 3)
        self.dro_axis_a.setProperty("Qreference_type", 0)
        self.dro_axis_a.setProperty("homed", False)

        self.gridLayout_dro.addWidget(self.dro_axis_a, 3, 1, 1, 2)

        self.axistoolbutton_z = AxisToolButton(self.widget_dro)
        self.axistoolbutton_z.setObjectName(u"axistoolbutton_z")
        self.axistoolbutton_z.setMinimumSize(QSize(64, 50))
        self.axistoolbutton_z.setMaximumSize(QSize(64, 50))
        self.axistoolbutton_z.setStyleSheet(u"font: 12pt \"Sans\";")
        self.axistoolbutton_z.setPopupMode(QToolButton.InstantPopup)
        self.axistoolbutton_z.setArrowType(Qt.NoArrow)
        self.axistoolbutton_z.setProperty("joint_number", 2)
        self.axistoolbutton_z.setProperty("halpin_option", False)

        self.gridLayout_dro.addWidget(self.axistoolbutton_z, 2, 4, 1, 1)

        self.axistoolbutton_x = AxisToolButton(self.widget_dro)
        self.axistoolbutton_x.setObjectName(u"axistoolbutton_x")
        self.axistoolbutton_x.setMinimumSize(QSize(64, 50))
        self.axistoolbutton_x.setMaximumSize(QSize(64, 50))
        self.axistoolbutton_x.setStyleSheet(u"font: 12pt \"Sans\";")
        self.axistoolbutton_x.setPopupMode(QToolButton.InstantPopup)
        self.axistoolbutton_x.setArrowType(Qt.NoArrow)
        self.axistoolbutton_x.setProperty("halpin_option", False)

        self.gridLayout_dro.addWidget(self.axistoolbutton_x, 0, 4, 1, 1)

        self.axistoolbutton_a = AxisToolButton(self.widget_dro)
        self.axistoolbutton_a.setObjectName(u"axistoolbutton_a")
        self.axistoolbutton_a.setMinimumSize(QSize(64, 50))
        self.axistoolbutton_a.setMaximumSize(QSize(64, 50))
        self.axistoolbutton_a.setStyleSheet(u"font: 12pt \"Sans\";")
        self.axistoolbutton_a.setPopupMode(QToolButton.InstantPopup)
        self.axistoolbutton_a.setArrowType(Qt.NoArrow)
        self.axistoolbutton_a.setProperty("joint_number", 3)
        self.axistoolbutton_a.setProperty("halpin_option", False)

        self.gridLayout_dro.addWidget(self.axistoolbutton_a, 3, 4, 1, 1)

        self.action_home_a = ActionButton(self.widget_dro)
        self.action_home_a.setObjectName(u"action_home_a")
        self.action_home_a.setEnabled(True)
        sizePolicy.setHeightForWidth(self.action_home_a.sizePolicy().hasHeightForWidth())
        self.action_home_a.setSizePolicy(sizePolicy)
        self.action_home_a.setMinimumSize(QSize(64, 50))
        self.action_home_a.setMaximumSize(QSize(64, 50))
        self.action_home_a.setStyleSheet(u"font: 12pt \"Sans\";")
        self.action_home_a.setProperty("indicator_option", False)
        self.action_home_a.setProperty("indicator_HAL_pin_option", False)
        self.action_home_a.setProperty("on_color", QColor(0, 255, 0))
        self.action_home_a.setProperty("off_color", QColor(255, 0, 0))
        self.action_home_a.setProperty("indicator_size", 0.200000000000000)
        self.action_home_a.setProperty("mdi_action", False)
        self.action_home_a.setProperty("home_action", False)
        self.action_home_a.setProperty("mdi_command_action", True)
        self.action_home_a.setProperty("template_label_option", False)
        self.action_home_a.setProperty("joint_number", 3)
        self.action_home_a.setProperty("incr_imperial_number", 0.010000000000000)
        self.action_home_a.setProperty("incr_mm_number", 0.025000000000000)
        self.action_home_a.setProperty("incr_angular_number", -1.000000000000000)
        self.action_home_a.setProperty("toggle_float_option", False)
        self.action_home_a.setProperty("float_num", 100.000000000000000)
        self.action_home_a.setProperty("float_alt_num", 50.000000000000000)
        self.action_home_a.setProperty("ini_mdi_number", 0)

        self.gridLayout_dro.addWidget(self.action_home_a, 3, 5, 1, 1)

        self.label_axis_y = QLabel(self.widget_dro)
        self.label_axis_y.setObjectName(u"label_axis_y")
        sizePolicy.setHeightForWidth(self.label_axis_y.sizePolicy().hasHeightForWidth())
        self.label_axis_y.setSizePolicy(sizePolicy)
        self.label_axis_y.setMinimumSize(QSize(64, 50))
        self.label_axis_y.setMaximumSize(QSize(64, 50))
        self.label_axis_y.setFrameShape(QFrame.WinPanel)
        self.label_axis_y.setFrameShadow(QFrame.Raised)
        self.label_axis_y.setLineWidth(2)
        self.label_axis_y.setAlignment(Qt.AlignCenter)

        self.gridLayout_dro.addWidget(self.label_axis_y, 1, 0, 1, 1)

        self.dro_axis_z = DROLabel(self.widget_dro)
        self.dro_axis_z.setObjectName(u"dro_axis_z")
        sizePolicy3.setHeightForWidth(self.dro_axis_z.sizePolicy().hasHeightForWidth())
        self.dro_axis_z.setSizePolicy(sizePolicy3)
        self.dro_axis_z.setMinimumSize(QSize(0, 50))
        self.dro_axis_z.setMaximumSize(QSize(16777215, 50))
        self.dro_axis_z.setStyleSheet(u"DROLabel {\n"
"    background-color: black;\n"
"    font: 20pt \"Lato Heavy\";\n"
"    color: #00FF00;\n"
"}\n"
"\n"
"DROLabel[homed=false] {\n"
"   color: #FFFF00;\n"
"}\n"
"")
        self.dro_axis_z.setFrameShape(QFrame.WinPanel)
        self.dro_axis_z.setFrameShadow(QFrame.Sunken)
        self.dro_axis_z.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dro_axis_z.setProperty("Qjoint_number", 2)
        self.dro_axis_z.setProperty("homed", False)

        self.gridLayout_dro.addWidget(self.dro_axis_z, 2, 1, 1, 2)

        self.action_zero_a = ActionButton(self.widget_dro)
        self.action_zero_a.setObjectName(u"action_zero_a")
        sizePolicy.setHeightForWidth(self.action_zero_a.sizePolicy().hasHeightForWidth())
        self.action_zero_a.setSizePolicy(sizePolicy)
        self.action_zero_a.setMinimumSize(QSize(64, 50))
        self.action_zero_a.setMaximumSize(QSize(64, 50))
        self.action_zero_a.setStyleSheet(u"font: 12pt \"Sans\";")
        self.action_zero_a.setProperty("indicator_option", False)
        self.action_zero_a.setProperty("indicator_HAL_pin_option", False)
        self.action_zero_a.setProperty("on_color", QColor(0, 255, 0))
        self.action_zero_a.setProperty("off_color", QColor(255, 0, 0))
        self.action_zero_a.setProperty("indicator_size", 0.200000000000000)
        self.action_zero_a.setProperty("mdi_action", False)
        self.action_zero_a.setProperty("zero_axis_action", True)
        self.action_zero_a.setProperty("template_label_option", False)
        self.action_zero_a.setProperty("joint_number", 3)
        self.action_zero_a.setProperty("incr_imperial_number", 0.010000000000000)
        self.action_zero_a.setProperty("incr_mm_number", 0.025000000000000)
        self.action_zero_a.setProperty("incr_angular_number", -1.000000000000000)
        self.action_zero_a.setProperty("toggle_float_option", False)
        self.action_zero_a.setProperty("float_num", 100.000000000000000)
        self.action_zero_a.setProperty("float_alt_num", 50.000000000000000)
        self.action_zero_a.setProperty("ini_mdi_number", 0)

        self.gridLayout_dro.addWidget(self.action_zero_a, 3, 3, 1, 1)

        self.btn_home_z = PushButton(self.widget_dro)
        self.btn_home_z.setObjectName(u"btn_home_z")
        sizePolicy.setHeightForWidth(self.btn_home_z.sizePolicy().hasHeightForWidth())
        self.btn_home_z.setSizePolicy(sizePolicy)
        self.btn_home_z.setMinimumSize(QSize(64, 50))
        self.btn_home_z.setMaximumSize(QSize(64, 50))
        self.btn_home_z.setStyleSheet(u"font: 12pt \"Sans\";")
        self.btn_home_z.setProperty("indicator_option", True)
        self.btn_home_z.setProperty("indicator_status_option", True)
        self.btn_home_z.setProperty("checked_state_text_option", True)
        self.btn_home_z.setProperty("python_command_option", False)
        self.btn_home_z.setProperty("on_color", QColor(0, 255, 0))
        self.btn_home_z.setProperty("off_color", QColor(255, 0, 0))
        self.btn_home_z.setProperty("is_homed_status", True)
        self.btn_home_z.setProperty("joint_number_status", 2)
        self.btn_home_z.setProperty("joint", 2)

        self.gridLayout_dro.addWidget(self.btn_home_z, 2, 5, 1, 1)

        self.axistoolbutton_y = AxisToolButton(self.widget_dro)
        self.axistoolbutton_y.setObjectName(u"axistoolbutton_y")
        self.axistoolbutton_y.setMinimumSize(QSize(64, 50))
        self.axistoolbutton_y.setMaximumSize(QSize(64, 50))
        self.axistoolbutton_y.setStyleSheet(u"font: 12pt \"Sans\";")
        self.axistoolbutton_y.setPopupMode(QToolButton.InstantPopup)
        self.axistoolbutton_y.setArrowType(Qt.NoArrow)
        self.axistoolbutton_y.setProperty("joint_number", 1)
        self.axistoolbutton_y.setProperty("halpin_option", False)

        self.gridLayout_dro.addWidget(self.axistoolbutton_y, 1, 4, 1, 1)

        self.label_axis_x = QLabel(self.widget_dro)
        self.label_axis_x.setObjectName(u"label_axis_x")
        sizePolicy.setHeightForWidth(self.label_axis_x.sizePolicy().hasHeightForWidth())
        self.label_axis_x.setSizePolicy(sizePolicy)
        self.label_axis_x.setMinimumSize(QSize(64, 50))
        self.label_axis_x.setMaximumSize(QSize(64, 50))
        self.label_axis_x.setFrameShape(QFrame.WinPanel)
        self.label_axis_x.setFrameShadow(QFrame.Raised)
        self.label_axis_x.setLineWidth(2)
        self.label_axis_x.setAlignment(Qt.AlignCenter)

        self.gridLayout_dro.addWidget(self.label_axis_x, 0, 0, 1, 1)

        self.btn_home_x = PushButton(self.widget_dro)
        self.btn_home_x.setObjectName(u"btn_home_x")
        sizePolicy.setHeightForWidth(self.btn_home_x.sizePolicy().hasHeightForWidth())
        self.btn_home_x.setSizePolicy(sizePolicy)
        self.btn_home_x.setMinimumSize(QSize(64, 50))
        self.btn_home_x.setMaximumSize(QSize(64, 50))
        self.btn_home_x.setStyleSheet(u"font: 12pt \"Sans\";")
        self.btn_home_x.setProperty("indicator_option", True)
        self.btn_home_x.setProperty("indicator_status_option", True)
        self.btn_home_x.setProperty("checked_state_text_option", True)
        self.btn_home_x.setProperty("python_command_option", False)
        self.btn_home_x.setProperty("on_color", QColor(0, 255, 0))
        self.btn_home_x.setProperty("shape_option", 0)
        self.btn_home_x.setProperty("off_color", QColor(255, 0, 0))
        self.btn_home_x.setProperty("is_homed_status", True)
        self.btn_home_x.setProperty("joint", 0)

        self.gridLayout_dro.addWidget(self.btn_home_x, 0, 5, 1, 1)

        self.btn_home_y = PushButton(self.widget_dro)
        self.btn_home_y.setObjectName(u"btn_home_y")
        sizePolicy.setHeightForWidth(self.btn_home_y.sizePolicy().hasHeightForWidth())
        self.btn_home_y.setSizePolicy(sizePolicy)
        self.btn_home_y.setMinimumSize(QSize(64, 50))
        self.btn_home_y.setMaximumSize(QSize(64, 50))
        self.btn_home_y.setStyleSheet(u"font: 12pt \"Sans\";")
        self.btn_home_y.setProperty("indicator_option", True)
        self.btn_home_y.setProperty("indicator_status_option", True)
        self.btn_home_y.setProperty("checked_state_text_option", True)
        self.btn_home_y.setProperty("python_command_option", False)
        self.btn_home_y.setProperty("on_color", QColor(0, 255, 0))
        self.btn_home_y.setProperty("shape_option", 0)
        self.btn_home_y.setProperty("off_color", QColor(255, 0, 0))
        self.btn_home_y.setProperty("is_homed_status", True)
        self.btn_home_y.setProperty("joint_number_status", 1)
        self.btn_home_y.setProperty("joint", 1)

        self.gridLayout_dro.addWidget(self.btn_home_y, 1, 5, 1, 1)

        self.stackedWidget_2.addWidget(self.panel_spindle_and_dro)
        self.panel_keyboard = QWidget()
        self.panel_keyboard.setObjectName(u"panel_keyboard")
        self.frame_keyboard = QFrame(self.panel_keyboard)
        self.frame_keyboard.setObjectName(u"frame_keyboard")
        self.frame_keyboard.setGeometry(QRect(0, 0, 954, 271))
        self.frame_keyboard.setFrameShape(QFrame.WinPanel)
        self.frame_keyboard.setFrameShadow(QFrame.Raised)
        self.virtualkeyboard = VirtualKeyboard(self.frame_keyboard)
        self.virtualkeyboard.setObjectName(u"virtualkeyboard")
        self.virtualkeyboard.setGeometry(QRect(0, 0, 951, 271))
        self.stackedWidget_2.addWidget(self.panel_keyboard)
        self.horizontalLayoutWidget = QWidget(self.page)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(950, 590, 261, 271))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.horizontalLayoutWidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.WinPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.widget_spindle = QWidget(self.frame_5)
        self.widget_spindle.setObjectName(u"widget_spindle")
        self.widget_spindle.setGeometry(QRect(0, 0, 261, 271))
        sizePolicy2.setHeightForWidth(self.widget_spindle.sizePolicy().hasHeightForWidth())
        self.widget_spindle.setSizePolicy(sizePolicy2)
        self.widget_spindle.setMinimumSize(QSize(210, 200))
        self.widget_spindle.setMaximumSize(QSize(16777215, 16777215))
        self.label_spindle = QLabel(self.widget_spindle)
        self.label_spindle.setObjectName(u"label_spindle")
        self.label_spindle.setGeometry(QRect(16, 10, 101, 21))
        font1 = QFont()
        font1.setFamily(u"Sans")
        font1.setPointSize(15)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_spindle.setFont(font1)
        self.label_spindle.setStyleSheet(u"font: 15pt \"Sans\";")
        self.label_spindle.setAlignment(Qt.AlignCenter)
        self.widget_spindle_control = QWidget(self.widget_spindle)
        self.widget_spindle_control.setObjectName(u"widget_spindle_control")
        self.widget_spindle_control.setGeometry(QRect(10, 40, 241, 44))
        sizePolicy2.setHeightForWidth(self.widget_spindle_control.sizePolicy().hasHeightForWidth())
        self.widget_spindle_control.setSizePolicy(sizePolicy2)
        self.widget_spindle_control.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_16 = QHBoxLayout(self.widget_spindle_control)
        self.horizontalLayout_16.setSpacing(4)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(2, 2, 2, 2)
        self.spindle_reverse = ActionButton(self.widget_spindle_control)
        self.spindle_reverse.setObjectName(u"spindle_reverse")
        sizePolicy.setHeightForWidth(self.spindle_reverse.sizePolicy().hasHeightForWidth())
        self.spindle_reverse.setSizePolicy(sizePolicy)
        self.spindle_reverse.setMinimumSize(QSize(70, 40))
        self.spindle_reverse.setMaximumSize(QSize(50, 40))
        self.spindle_reverse.setFocusPolicy(Qt.NoFocus)
        self.spindle_reverse.setStyleSheet(u"font: 15pt \"Sans\";")
        icon2 = QIcon()
        icon2.addFile(u":/../../images/qtdragon/images/ccw_arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.spindle_reverse.setIcon(icon2)
        self.spindle_reverse.setIconSize(QSize(18, 18))
        self.spindle_reverse.setCheckable(False)
        self.spindle_reverse.setAutoExclusive(False)
        self.spindle_reverse.setProperty("indicator_option", True)
        self.spindle_reverse.setProperty("indicator_HAL_pin_option", False)
        self.spindle_reverse.setProperty("indicator_status_option", True)
        self.spindle_reverse.setProperty("on_color", QColor(255, 255, 0))
        self.spindle_reverse.setProperty("indicator_size", 0.300000000000000)
        self.spindle_reverse.setProperty("is_spindle_rev_status", True)
        self.spindle_reverse.setProperty("spindle_rev_action", True)

        self.horizontalLayout_16.addWidget(self.spindle_reverse)

        self.spindle_stop = ActionButton(self.widget_spindle_control)
        self.spindle_stop.setObjectName(u"spindle_stop")
        sizePolicy.setHeightForWidth(self.spindle_stop.sizePolicy().hasHeightForWidth())
        self.spindle_stop.setSizePolicy(sizePolicy)
        self.spindle_stop.setMinimumSize(QSize(70, 40))
        self.spindle_stop.setMaximumSize(QSize(50, 40))
        self.spindle_stop.setFocusPolicy(Qt.NoFocus)
        self.spindle_stop.setStyleSheet(u"font: 15pt \"Sans\";")
        self.spindle_stop.setCheckable(False)
        self.spindle_stop.setChecked(False)
        self.spindle_stop.setAutoExclusive(False)
        self.spindle_stop.setProperty("indicator_option", True)
        self.spindle_stop.setProperty("indicator_HAL_pin_option", False)
        self.spindle_stop.setProperty("indicator_status_option", True)
        self.spindle_stop.setProperty("on_color", QColor(0, 0, 0))
        self.spindle_stop.setProperty("off_color", QColor(255, 0, 0))
        self.spindle_stop.setProperty("indicator_size", 0.300000000000000)
        self.spindle_stop.setProperty("is_spindle_stopped_status", True)
        self.spindle_stop.setProperty("spindle_stop_action", True)

        self.horizontalLayout_16.addWidget(self.spindle_stop)

        self.spindle_forward = ActionButton(self.widget_spindle_control)
        self.spindle_forward.setObjectName(u"spindle_forward")
        sizePolicy.setHeightForWidth(self.spindle_forward.sizePolicy().hasHeightForWidth())
        self.spindle_forward.setSizePolicy(sizePolicy)
        self.spindle_forward.setMinimumSize(QSize(70, 40))
        self.spindle_forward.setMaximumSize(QSize(50, 40))
        self.spindle_forward.setFocusPolicy(Qt.NoFocus)
        self.spindle_forward.setLayoutDirection(Qt.LeftToRight)
        self.spindle_forward.setStyleSheet(u"font: 15pt \"Sans\";")
        icon3 = QIcon()
        icon3.addFile(u":/../../images/qtdragon/images/cw_arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.spindle_forward.setIcon(icon3)
        self.spindle_forward.setIconSize(QSize(18, 18))
        self.spindle_forward.setCheckable(False)
        self.spindle_forward.setAutoExclusive(False)
        self.spindle_forward.setProperty("indicator_option", True)
        self.spindle_forward.setProperty("indicator_HAL_pin_option", False)
        self.spindle_forward.setProperty("indicator_status_option", True)
        self.spindle_forward.setProperty("on_color", QColor(0, 255, 0))
        self.spindle_forward.setProperty("indicator_size", 0.300000000000000)
        self.spindle_forward.setProperty("is_spindle_fwd_status", True)
        self.spindle_forward.setProperty("spindle_fwd_action", True)

        self.horizontalLayout_16.addWidget(self.spindle_forward)

        self.lcdnumber = LCDNumber(self.widget_spindle)
        self.lcdnumber.setObjectName(u"lcdnumber")
        self.lcdnumber.setGeometry(QRect(10, 90, 101, 45))
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lcdnumber.sizePolicy().hasHeightForWidth())
        self.lcdnumber.setSizePolicy(sizePolicy4)
        self.lcdnumber.setMinimumSize(QSize(100, 45))
        self.lcdnumber.setStyleSheet(u"color: rgb(51, 255, 0);\n"
"background-color: rgb(46, 52, 54);")
        self.lcdnumber.setDigitCount(6)
        self.lcdnumber.setSegmentStyle(QLCDNumber.Flat)
        self.widget_spindle_data = QWidget(self.widget_spindle)
        self.widget_spindle_data.setObjectName(u"widget_spindle_data")
        self.widget_spindle_data.setGeometry(QRect(10, 140, 241, 61))
        self.horizontalLayout_11 = QHBoxLayout(self.widget_spindle_data)
        self.horizontalLayout_11.setSpacing(4)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setSpacing(4)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_28 = QLabel(self.widget_spindle_data)
        self.label_28.setObjectName(u"label_28")
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        self.label_28.setMinimumSize(QSize(60, 24))
        self.label_28.setMaximumSize(QSize(60, 24))
        self.label_28.setStyleSheet(u"font: 12pt \"Sans\";")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_28, 0, Qt.AlignHCenter)

        self.status_rpm = StatusLabel(self.widget_spindle_data)
        self.status_rpm.setObjectName(u"status_rpm")
        sizePolicy.setHeightForWidth(self.status_rpm.sizePolicy().hasHeightForWidth())
        self.status_rpm.setSizePolicy(sizePolicy)
        self.status_rpm.setMinimumSize(QSize(75, 30))
        self.status_rpm.setMaximumSize(QSize(75, 30))
        self.status_rpm.setStyleSheet(u"font: 15pt \"Sans\";")
        self.status_rpm.setFrameShape(QFrame.WinPanel)
        self.status_rpm.setFrameShadow(QFrame.Raised)
        self.status_rpm.setAlignment(Qt.AlignCenter)
        self.status_rpm.setProperty("requested_spindle_speed_status", False)
        self.status_rpm.setProperty("actual_spindle_speed_status", True)

        self.verticalLayout_23.addWidget(self.status_rpm)


        self.horizontalLayout_11.addLayout(self.verticalLayout_23)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setSpacing(4)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_37 = QLabel(self.widget_spindle_data)
        self.label_37.setObjectName(u"label_37")
        sizePolicy.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy)
        self.label_37.setMinimumSize(QSize(60, 24))
        self.label_37.setMaximumSize(QSize(60, 24))
        self.label_37.setStyleSheet(u"font: 12pt \"Sans\";")
        self.label_37.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_37)

        self.lbl_spindle_power = QLineEdit(self.widget_spindle_data)
        self.lbl_spindle_power.setObjectName(u"lbl_spindle_power")
        sizePolicy.setHeightForWidth(self.lbl_spindle_power.sizePolicy().hasHeightForWidth())
        self.lbl_spindle_power.setSizePolicy(sizePolicy)
        self.lbl_spindle_power.setMinimumSize(QSize(75, 30))
        self.lbl_spindle_power.setMaximumSize(QSize(75, 30))
        self.lbl_spindle_power.setStyleSheet(u"font: 15pt \"Sans\";")
        self.lbl_spindle_power.setMaxLength(8)
        self.lbl_spindle_power.setCursorPosition(3)
        self.lbl_spindle_power.setAlignment(Qt.AlignCenter)
        self.lbl_spindle_power.setReadOnly(True)

        self.verticalLayout_32.addWidget(self.lbl_spindle_power)


        self.horizontalLayout_11.addLayout(self.verticalLayout_32)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setSpacing(4)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_40 = QLabel(self.widget_spindle_data)
        self.label_40.setObjectName(u"label_40")
        sizePolicy.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy)
        self.label_40.setMinimumSize(QSize(60, 24))
        self.label_40.setMaximumSize(QSize(60, 24))
        self.label_40.setStyleSheet(u"font: 12pt \"Sans\";")
        self.label_40.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.label_40)

        self.lbl_spindle_amps = QLineEdit(self.widget_spindle_data)
        self.lbl_spindle_amps.setObjectName(u"lbl_spindle_amps")
        sizePolicy.setHeightForWidth(self.lbl_spindle_amps.sizePolicy().hasHeightForWidth())
        self.lbl_spindle_amps.setSizePolicy(sizePolicy)
        self.lbl_spindle_amps.setMinimumSize(QSize(75, 30))
        self.lbl_spindle_amps.setMaximumSize(QSize(75, 30))
        self.lbl_spindle_amps.setStyleSheet(u"font: 15pt \"Sans\";")
        self.lbl_spindle_amps.setMaxLength(8)
        self.lbl_spindle_amps.setCursorPosition(3)
        self.lbl_spindle_amps.setAlignment(Qt.AlignCenter)
        self.lbl_spindle_amps.setReadOnly(True)

        self.verticalLayout_33.addWidget(self.lbl_spindle_amps)


        self.horizontalLayout_11.addLayout(self.verticalLayout_33)

        self.layoutWidget = QWidget(self.widget_spindle)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(120, 90, 131, 42))
        self.horizontalLayout_46 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.btn_spindle_slover = QPushButton(self.layoutWidget)
        self.btn_spindle_slover.setObjectName(u"btn_spindle_slover")
        sizePolicy.setHeightForWidth(self.btn_spindle_slover.sizePolicy().hasHeightForWidth())
        self.btn_spindle_slover.setSizePolicy(sizePolicy)
        self.btn_spindle_slover.setMinimumSize(QSize(60, 40))
        self.btn_spindle_slover.setMaximumSize(QSize(50, 16777215))
        self.btn_spindle_slover.setStyleSheet(u"\n"
"font: 75 12pt \"Bebas Kai\";")
        self.btn_spindle_slover.setAutoRepeat(True)

        self.horizontalLayout_46.addWidget(self.btn_spindle_slover)

        self.btn_spindle_faster = QPushButton(self.layoutWidget)
        self.btn_spindle_faster.setObjectName(u"btn_spindle_faster")
        sizePolicy.setHeightForWidth(self.btn_spindle_faster.sizePolicy().hasHeightForWidth())
        self.btn_spindle_faster.setSizePolicy(sizePolicy)
        self.btn_spindle_faster.setMinimumSize(QSize(60, 40))
        self.btn_spindle_faster.setMaximumSize(QSize(50, 16777215))
        self.btn_spindle_faster.setStyleSheet(u"\n"
"font: 75 12pt \"Bebas Kai\";")
        self.btn_spindle_faster.setAutoRepeat(True)

        self.horizontalLayout_46.addWidget(self.btn_spindle_faster)

        self.slider_spindle_ovr_2 = StatusSlider(self.widget_spindle)
        self.slider_spindle_ovr_2.setObjectName(u"slider_spindle_ovr_2")
        self.slider_spindle_ovr_2.setGeometry(QRect(350, 40, 30, 151))
        self.slider_spindle_ovr_2.setMinimumSize(QSize(30, 0))
        self.slider_spindle_ovr_2.setStyleSheet(u"QSlider::groove:vertical {\n"
"border: 1px solid #bbb;\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"width: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"background: white;\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal  {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"width: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:vertical  {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 2"
                        "55, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"height: 30px;\n"
"margin-top: -1.3px;\n"
"margin-bottom: -1.3px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #444;\n"
"border-color: rgb(241, 239, 237);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
""
                        "}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.slider_spindle_ovr_2.setProperty("spindle_rate", True)
        self.layoutWidget_2 = QWidget(self.widget_spindle)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(0, 220, 92, 40))
        self.verticalLayout_35 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_35.setSpacing(4)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.layoutWidget_2)
        self.label_14.setObjectName(u"label_14")
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QSize(90, 16))
        self.label_14.setMaximumSize(QSize(90, 16))
        self.label_14.setStyleSheet(u"font: 12pt \"Sans\";")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_35.addWidget(self.label_14, 0, Qt.AlignHCenter)

        self.led_at_speed = LED(self.layoutWidget_2)
        self.led_at_speed.setObjectName(u"led_at_speed")
        sizePolicy.setHeightForWidth(self.led_at_speed.sizePolicy().hasHeightForWidth())
        self.led_at_speed.setSizePolicy(sizePolicy)
        self.led_at_speed.setMinimumSize(QSize(20, 0))
        self.led_at_speed.setMaximumSize(QSize(20, 20))
        self.led_at_speed.setDiameter(15)
        self.led_at_speed.setColor(QColor(0, 255, 0))
        self.led_at_speed.setProperty("state", False)

        self.verticalLayout_35.addWidget(self.led_at_speed, 0, Qt.AlignHCenter)

        self.layoutWidget_3 = QWidget(self.widget_spindle)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(170, 200, 81, 61))
        self.verticalLayout_34 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_34.setSpacing(4)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.label_41 = QLabel(self.layoutWidget_3)
        self.label_41.setObjectName(u"label_41")
        sizePolicy.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy)
        self.label_41.setMinimumSize(QSize(70, 24))
        self.label_41.setMaximumSize(QSize(70, 24))
        self.label_41.setStyleSheet(u"font: 12pt \"Sans\";")
        self.label_41.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_41)

        self.lbl_spindle_fault = QLineEdit(self.layoutWidget_3)
        self.lbl_spindle_fault.setObjectName(u"lbl_spindle_fault")
        sizePolicy.setHeightForWidth(self.lbl_spindle_fault.sizePolicy().hasHeightForWidth())
        self.lbl_spindle_fault.setSizePolicy(sizePolicy)
        self.lbl_spindle_fault.setMinimumSize(QSize(75, 30))
        self.lbl_spindle_fault.setMaximumSize(QSize(75, 30))
        self.lbl_spindle_fault.setStyleSheet(u"font: 15pt \"Sans\";")
        self.lbl_spindle_fault.setAlignment(Qt.AlignCenter)
        self.lbl_spindle_fault.setReadOnly(True)

        self.verticalLayout_34.addWidget(self.lbl_spindle_fault)

        self.widget_probe = QWidget(self.widget_spindle)
        self.widget_probe.setObjectName(u"widget_probe")
        self.widget_probe.setGeometry(QRect(100, 210, 63, 51))
        self.verticalLayout_31 = QVBoxLayout(self.widget_probe)
        self.verticalLayout_31.setSpacing(4)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(4, 0, 4, 0)
        self.label_13 = QLabel(self.widget_probe)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QSize(55, 20))
        self.label_13.setMaximumSize(QSize(55, 20))
        self.label_13.setStyleSheet(u"font: 75 12pt \"BebasKai\";")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_13)

        self.hal_led_probe = LED(self.widget_probe)
        self.hal_led_probe.setObjectName(u"hal_led_probe")
        sizePolicy.setHeightForWidth(self.hal_led_probe.sizePolicy().hasHeightForWidth())
        self.hal_led_probe.setSizePolicy(sizePolicy)
        self.hal_led_probe.setMinimumSize(QSize(16, 16))
        self.hal_led_probe.setMaximumSize(QSize(16, 16))
        self.hal_led_probe.setDiameter(15)
        self.hal_led_probe.setColor(QColor(0, 255, 0))

        self.verticalLayout_31.addWidget(self.hal_led_probe, 0, Qt.AlignHCenter)


        self.horizontalLayout_4.addWidget(self.frame_5)

        self.frame_9 = QFrame(self.page)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(780, 510, 229, 80))
        self.frame_9.setMinimumSize(QSize(229, 80))
        self.frame_9.setFrameShape(QFrame.WinPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.layoutWidget_9 = QWidget(self.frame_9)
        self.layoutWidget_9.setObjectName(u"layoutWidget_9")
        self.layoutWidget_9.setGeometry(QRect(10, 0, 211, 31))
        self.horizontalLayout_55 = QHBoxLayout(self.layoutWidget_9)
        self.horizontalLayout_55.setSpacing(4)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.layoutWidget_9)
        self.label_21.setObjectName(u"label_21")
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setMinimumSize(QSize(50, 20))
        self.label_21.setMaximumSize(QSize(50, 20))
        self.label_21.setStyleSheet(u"font: 12pt \"Sans\";")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_55.addWidget(self.label_21)

        self.label_25 = QLabel(self.layoutWidget_9)
        self.label_25.setObjectName(u"label_25")
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setMinimumSize(QSize(60, 20))
        self.label_25.setMaximumSize(QSize(60, 20))
        self.label_25.setStyleSheet(u"font: 12pt \"Sans\";")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_55.addWidget(self.label_25)

        self.label_49 = QLabel(self.layoutWidget_9)
        self.label_49.setObjectName(u"label_49")
        sizePolicy.setHeightForWidth(self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy)
        self.label_49.setMinimumSize(QSize(70, 20))
        self.label_49.setMaximumSize(QSize(70, 20))
        self.label_49.setStyleSheet(u"font: 12pt \"Sans\";")
        self.label_49.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_55.addWidget(self.label_49)

        self.layoutWidget_10 = QWidget(self.frame_9)
        self.layoutWidget_10.setObjectName(u"layoutWidget_10")
        self.layoutWidget_10.setGeometry(QRect(10, 40, 211, 32))
        self.horizontalLayout_56 = QHBoxLayout(self.layoutWidget_10)
        self.horizontalLayout_56.setSpacing(4)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.statelabel_metric = StateLabel(self.layoutWidget_10)
        self.statelabel_metric.setObjectName(u"statelabel_metric")
        sizePolicy.setHeightForWidth(self.statelabel_metric.sizePolicy().hasHeightForWidth())
        self.statelabel_metric.setSizePolicy(sizePolicy)
        self.statelabel_metric.setMinimumSize(QSize(50, 30))
        self.statelabel_metric.setMaximumSize(QSize(50, 30))
        self.statelabel_metric.setStyleSheet(u"font: 12pt \"Sans\";")
        self.statelabel_metric.setFrameShape(QFrame.WinPanel)
        self.statelabel_metric.setFrameShadow(QFrame.Sunken)
        self.statelabel_metric.setLineWidth(1)
        self.statelabel_metric.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_56.addWidget(self.statelabel_metric)

        self.status_state = StatusLabel(self.layoutWidget_10)
        self.status_state.setObjectName(u"status_state")
        sizePolicy.setHeightForWidth(self.status_state.sizePolicy().hasHeightForWidth())
        self.status_state.setSizePolicy(sizePolicy)
        self.status_state.setMinimumSize(QSize(70, 30))
        self.status_state.setMaximumSize(QSize(70, 30))
        self.status_state.setFrameShape(QFrame.WinPanel)
        self.status_state.setFrameShadow(QFrame.Sunken)
        self.status_state.setLineWidth(1)
        self.status_state.setAlignment(Qt.AlignCenter)
        self.status_state.setProperty("machine_state_status", True)

        self.horizontalLayout_56.addWidget(self.status_state)

        self.lbl_eoffset_value = QLineEdit(self.layoutWidget_10)
        self.lbl_eoffset_value.setObjectName(u"lbl_eoffset_value")
        sizePolicy.setHeightForWidth(self.lbl_eoffset_value.sizePolicy().hasHeightForWidth())
        self.lbl_eoffset_value.setSizePolicy(sizePolicy)
        self.lbl_eoffset_value.setMinimumSize(QSize(70, 30))
        self.lbl_eoffset_value.setMaximumSize(QSize(70, 30))
        self.lbl_eoffset_value.setStyleSheet(u"font: 12pt \"Sans\";")
        self.lbl_eoffset_value.setAlignment(Qt.AlignCenter)
        self.lbl_eoffset_value.setReadOnly(True)

        self.horizontalLayout_56.addWidget(self.lbl_eoffset_value)

        self.frame_status = QFrame(self.page)
        self.frame_status.setObjectName(u"frame_status")
        self.frame_status.setGeometry(QRect(0, 510, 781, 80))
        self.frame_status.setMinimumSize(QSize(591, 70))
        self.frame_status.setMaximumSize(QSize(16777215, 80))
        self.frame_status.setFrameShape(QFrame.WinPanel)
        self.frame_status.setFrameShadow(QFrame.Raised)
        self.lab_mcode_list = StatusLabel(self.frame_status)
        self.lab_mcode_list.setObjectName(u"lab_mcode_list")
        self.lab_mcode_list.setGeometry(QRect(60, 3, 350, 20))
        self.lab_mcode_list.setMinimumSize(QSize(350, 20))
        self.lab_mcode_list.setMaximumSize(QSize(318, 20))
        font2 = QFont()
        font2.setPointSize(9)
        self.lab_mcode_list.setFont(font2)
        self.lab_mcode_list.setFrameShape(QFrame.NoFrame)
        self.lab_mcode_list.setFrameShadow(QFrame.Sunken)
        self.lab_mcode_list.setProperty("mcodes_status", True)
        self.lab_gcode_list = StatusLabel(self.frame_status)
        self.lab_gcode_list.setObjectName(u"lab_gcode_list")
        self.lab_gcode_list.setGeometry(QRect(58, 25, 424, 20))
        self.lab_gcode_list.setMinimumSize(QSize(424, 20))
        self.lab_gcode_list.setMaximumSize(QSize(400, 20))
        self.lab_gcode_list.setFont(font2)
        self.lab_gcode_list.setMouseTracking(True)
        self.lab_gcode_list.setFrameShape(QFrame.NoFrame)
        self.lab_gcode_list.setFrameShadow(QFrame.Sunken)
        self.lab_gcode_list.setProperty("gcodes_status", True)
        self.lab_gcode_list.setProperty("mcodes_status", False)
        self.lab_feed_per_rev = StatusLabel(self.frame_status)
        self.lab_feed_per_rev.setObjectName(u"lab_feed_per_rev")
        self.lab_feed_per_rev.setGeometry(QRect(390, 46, 70, 30))
        self.lab_feed_per_rev.setMinimumSize(QSize(70, 30))
        self.lab_feed_per_rev.setMaximumSize(QSize(70, 30))
        font3 = QFont()
        font3.setPointSize(10)
        self.lab_feed_per_rev.setFont(font3)
        self.lab_feed_per_rev.setFrameShape(QFrame.WinPanel)
        self.lab_feed_per_rev.setFrameShadow(QFrame.Sunken)
        self.lab_feed_per_rev.setTextFormat(Qt.RichText)
        self.lab_feed_per_rev.setAlignment(Qt.AlignCenter)
        self.lab_feed_per_rev.setProperty("feed_override_status", False)
        self.lab_feed_per_rev.setProperty("spindle_override_status", False)
        self.lab_feed_per_rev.setProperty("current_feedrate_status", False)
        self.lab_feed_per_rev.setProperty("current_FPU_status", True)
        self.lab_tool_numb = StatusLabel(self.frame_status)
        self.lab_tool_numb.setObjectName(u"lab_tool_numb")
        self.lab_tool_numb.setGeometry(QRect(530, 3, 70, 30))
        self.lab_tool_numb.setMinimumSize(QSize(70, 30))
        self.lab_tool_numb.setMaximumSize(QSize(70, 30))
        self.lab_tool_numb.setFont(font1)
        self.lab_tool_numb.setStyleSheet(u"font: 15pt \"Sans\";")
        self.lab_tool_numb.setFrameShape(QFrame.WinPanel)
        self.lab_tool_numb.setFrameShadow(QFrame.Sunken)
        self.lab_tool_numb.setTextFormat(Qt.RichText)
        self.lab_tool_numb.setAlignment(Qt.AlignCenter)
        self.lab_tool_numb.setProperty("feed_override_status", False)
        self.lab_tool_numb.setProperty("spindle_override_status", False)
        self.lab_tool_numb.setProperty("current_feedrate_status", False)
        self.lab_tool_numb.setProperty("tool_number_status", True)
        self.lab_tool_diam = StatusLabel(self.frame_status)
        self.lab_tool_diam.setObjectName(u"lab_tool_diam")
        self.lab_tool_diam.setGeometry(QRect(530, 40, 70, 30))
        self.lab_tool_diam.setMinimumSize(QSize(70, 30))
        self.lab_tool_diam.setMaximumSize(QSize(70, 30))
        self.lab_tool_diam.setStyleSheet(u"font: 15pt \"Sans\";")
        self.lab_tool_diam.setFrameShape(QFrame.WinPanel)
        self.lab_tool_diam.setFrameShadow(QFrame.Sunken)
        self.lab_tool_diam.setTextFormat(Qt.RichText)
        self.lab_tool_diam.setAlignment(Qt.AlignCenter)
        self.lab_tool_diam.setProperty("feed_override_status", False)
        self.lab_tool_diam.setProperty("spindle_override_status", False)
        self.lab_tool_diam.setProperty("current_feedrate_status", False)
        self.lab_tool_diam.setProperty("tool_diameter_status", True)
        self.lab_feed_rate = StatusLabel(self.frame_status)
        self.lab_feed_rate.setObjectName(u"lab_feed_rate")
        self.lab_feed_rate.setGeometry(QRect(680, 10, 90, 30))
        self.lab_feed_rate.setMinimumSize(QSize(90, 30))
        self.lab_feed_rate.setMaximumSize(QSize(90, 30))
        self.lab_feed_rate.setFont(font1)
        self.lab_feed_rate.setStyleSheet(u"font: 15pt \"Sans\";")
        self.lab_feed_rate.setFrameShape(QFrame.WinPanel)
        self.lab_feed_rate.setFrameShadow(QFrame.Sunken)
        self.lab_feed_rate.setTextFormat(Qt.RichText)
        self.lab_feed_rate.setAlignment(Qt.AlignCenter)
        self.lab_feed_rate.setProperty("feed_override_status", False)
        self.lab_feed_rate.setProperty("spindle_override_status", False)
        self.lab_feed_rate.setProperty("current_feedrate_status", True)
        self.lab_tool_comment = StatusLabel(self.frame_status)
        self.lab_tool_comment.setObjectName(u"lab_tool_comment")
        self.lab_tool_comment.setGeometry(QRect(50, 50, 250, 20))
        self.lab_tool_comment.setMinimumSize(QSize(250, 20))
        self.lab_tool_comment.setMaximumSize(QSize(250, 20))
        self.lab_tool_comment.setFont(font3)
        self.lab_tool_comment.setFrameShape(QFrame.NoFrame)
        self.lab_tool_comment.setFrameShadow(QFrame.Sunken)
        self.lab_tool_comment.setProperty("gcodes_status", False)
        self.lab_tool_comment.setProperty("mcodes_status", False)
        self.lab_tool_comment.setProperty("tool_comment_status", True)
        self.led_eoffset_limit = LED(self.frame_status)
        self.led_eoffset_limit.setObjectName(u"led_eoffset_limit")
        self.led_eoffset_limit.setGeometry(QRect(700, 50, 21, 25))
        self.led_eoffset_limit.setFont(font2)
        self.led_eoffset_limit.setDiameter(16)
        self.lab_mcodes_label = QLabel(self.frame_status)
        self.lab_mcodes_label.setObjectName(u"lab_mcodes_label")
        self.lab_mcodes_label.setGeometry(QRect(6, 3, 52, 20))
        self.lab_mcodes_label.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.lab_gcodes_label = QLabel(self.frame_status)
        self.lab_gcodes_label.setObjectName(u"lab_gcodes_label")
        self.lab_gcodes_label.setGeometry(QRect(6, 26, 54, 17))
        self.lab_gcodes_label.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.lab_tool_label = QLabel(self.frame_status)
        self.lab_tool_label.setObjectName(u"lab_tool_label")
        self.lab_tool_label.setGeometry(QRect(6, 48, 54, 17))
        self.lab_tool_label.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.lab_in_limits_label = QLabel(self.frame_status)
        self.lab_in_limits_label.setObjectName(u"lab_in_limits_label")
        self.lab_in_limits_label.setGeometry(QRect(610, 49, 61, 21))
        self.lab_in_limits_label.setStyleSheet(u"\n"
"font: 75 12pt \"Bebas Kai\";")
        self.lab_in_limits_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lab_feed_per_rev_label = QLabel(self.frame_status)
        self.lab_feed_per_rev_label.setObjectName(u"lab_feed_per_rev_label")
        self.lab_feed_per_rev_label.setGeometry(QRect(301, 46, 81, 20))
        self.lab_feed_per_rev_label.setStyleSheet(u"\n"
"font: 75 12pt \"Bebas Kai\";")
        self.lab_feed_per_rev_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lab_tool_numb_label = QLabel(self.frame_status)
        self.lab_tool_numb_label.setObjectName(u"lab_tool_numb_label")
        self.lab_tool_numb_label.setGeometry(QRect(450, 3, 74, 20))
        self.lab_tool_numb_label.setStyleSheet(u"\n"
"font: 75 12pt \"Bebas Kai\";")
        self.lab_tool_numb_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lab_tool_diam_label = QLabel(self.frame_status)
        self.lab_tool_diam_label.setObjectName(u"lab_tool_diam_label")
        self.lab_tool_diam_label.setGeometry(QRect(467, 40, 51, 20))
        self.lab_tool_diam_label.setStyleSheet(u"\n"
"font: 75 12pt \"Bebas Kai\";")
        self.lab_tool_diam_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lab_feed_rate_label = QLabel(self.frame_status)
        self.lab_feed_rate_label.setObjectName(u"lab_feed_rate_label")
        self.lab_feed_rate_label.setGeometry(QRect(600, 10, 71, 31))
        self.lab_feed_rate_label.setStyleSheet(u"\n"
"font: 75 12pt \"Bebas Kai\";")
        self.lab_feed_rate_label.setAlignment(Qt.AlignCenter)
        self.frame_30 = QFrame(self.page)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setGeometry(QRect(1010, 510, 201, 80))
        sizePolicy1.setHeightForWidth(self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy1)
        self.frame_30.setMinimumSize(QSize(190, 60))
        self.frame_30.setFrameShape(QFrame.WinPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.widget_leds = QWidget(self.frame_30)
        self.widget_leds.setObjectName(u"widget_leds")
        self.widget_leds.setGeometry(QRect(10, 10, 171, 60))
        sizePolicy.setHeightForWidth(self.widget_leds.sizePolicy().hasHeightForWidth())
        self.widget_leds.setSizePolicy(sizePolicy)
        self.widget_leds.setMinimumSize(QSize(170, 60))
        self.widget_leds.setMaximumSize(QSize(16777215, 60))
        self.hal_led_home_z = LED(self.widget_leds)
        self.hal_led_home_z.setObjectName(u"hal_led_home_z")
        self.hal_led_home_z.setGeometry(QRect(140, 40, 16, 16))
        sizePolicy.setHeightForWidth(self.hal_led_home_z.sizePolicy().hasHeightForWidth())
        self.hal_led_home_z.setSizePolicy(sizePolicy)
        self.hal_led_home_z.setMinimumSize(QSize(16, 16))
        self.hal_led_home_z.setDiameter(15)
        self.hal_led_home_z.setColor(QColor(0, 255, 0))
        self.label_11 = QLabel(self.widget_leds)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(60, 40, 20, 16))
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QSize(20, 16))
        self.label_11.setMaximumSize(QSize(20, 16))
        self.label_11.setStyleSheet(u"font: 15pt \"Sans\";")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_10 = QLabel(self.widget_leds)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 40, 20, 16))
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QSize(20, 16))
        self.label_10.setMaximumSize(QSize(20, 16))
        self.label_10.setStyleSheet(u"font: 15pt \"Sans\";")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.hal_led_home_x = LED(self.widget_leds)
        self.hal_led_home_x.setObjectName(u"hal_led_home_x")
        self.hal_led_home_x.setGeometry(QRect(40, 40, 16, 16))
        sizePolicy.setHeightForWidth(self.hal_led_home_x.sizePolicy().hasHeightForWidth())
        self.hal_led_home_x.setSizePolicy(sizePolicy)
        self.hal_led_home_x.setMinimumSize(QSize(16, 16))
        self.hal_led_home_x.setDiameter(15)
        self.hal_led_home_x.setColor(QColor(0, 255, 0))
        self.hal_led_home_y = LED(self.widget_leds)
        self.hal_led_home_y.setObjectName(u"hal_led_home_y")
        self.hal_led_home_y.setGeometry(QRect(90, 40, 16, 16))
        sizePolicy.setHeightForWidth(self.hal_led_home_y.sizePolicy().hasHeightForWidth())
        self.hal_led_home_y.setSizePolicy(sizePolicy)
        self.hal_led_home_y.setMinimumSize(QSize(16, 16))
        self.hal_led_home_y.setDiameter(15)
        self.hal_led_home_y.setColor(QColor(0, 255, 0))
        self.label_12 = QLabel(self.widget_leds)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(110, 40, 20, 16))
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QSize(20, 16))
        self.label_12.setMaximumSize(QSize(20, 16))
        self.label_12.setStyleSheet(u"font: 15pt \"Sans\";")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_27 = QLabel(self.widget_leds)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(10, 0, 151, 20))
        sizePolicy3.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy3)
        self.label_27.setMinimumSize(QSize(0, 20))
        self.label_27.setMaximumSize(QSize(16777215, 20))
        self.label_27.setStyleSheet(u"font: 12pt \"Sans\";")
        self.label_27.setAlignment(Qt.AlignCenter)
        self.stackedWidget_4 = QStackedWidget(self.page)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        self.stackedWidget_4.setGeometry(QRect(802, 10, 408, 501))
        self.stackedWidget_4.setMinimumSize(QSize(406, 494))
        self.panel_jogging = QWidget()
        self.panel_jogging.setObjectName(u"panel_jogging")
        self.frame_jogging = QFrame(self.panel_jogging)
        self.frame_jogging.setObjectName(u"frame_jogging")
        self.frame_jogging.setGeometry(QRect(0, 0, 408, 501))
        self.frame_jogging.setMinimumSize(QSize(354, 492))
        self.frame_jogging.setMaximumSize(QSize(16777215, 16777215))
        self.frame_jogging.setFrameShape(QFrame.WinPanel)
        self.frame_jogging.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_jogging)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.stackedWidget_5 = QStackedWidget(self.frame_jogging)
        self.stackedWidget_5.setObjectName(u"stackedWidget_5")
        sizePolicy3.setHeightForWidth(self.stackedWidget_5.sizePolicy().hasHeightForWidth())
        self.stackedWidget_5.setSizePolicy(sizePolicy3)
        self.stackedWidget_5.setMinimumSize(QSize(0, 180))
        self.panel_jogging_linear = QWidget()
        self.panel_jogging_linear.setObjectName(u"panel_jogging_linear")
        self.stackedWidget_5.addWidget(self.panel_jogging_linear)
        self.panel_jogging_position = QWidget()
        self.panel_jogging_position.setObjectName(u"panel_jogging_position")
        self.frame_6 = QFrame(self.panel_jogging_position)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(-1, -1, 390, 181))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.calendarWidget = QCalendarWidget(self.frame_6)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(1, 0, 390, 171))
        self.calendarWidget.setStyleSheet(u"font: 15pt \"BebasKai\";")
        self.stackedWidget_5.addWidget(self.panel_jogging_position)
        self.panel_jogging_angular = QWidget()
        self.panel_jogging_angular.setObjectName(u"panel_jogging_angular")
        self.stackedWidget_5.addWidget(self.panel_jogging_angular)

        self.gridLayout_18.addWidget(self.stackedWidget_5, 0, 0, 1, 1)

        self.jogging_frame = QFrame(self.frame_jogging)
        self.jogging_frame.setObjectName(u"jogging_frame")
        self.jogging_frame.setMinimumSize(QSize(0, 300))
        self.jogging_frame.setFrameShape(QFrame.WinPanel)
        self.jogging_frame.setFrameShadow(QFrame.Raised)
        self.frame_jog_axis_buttons = QFrame(self.jogging_frame)
        self.frame_jog_axis_buttons.setObjectName(u"frame_jog_axis_buttons")
        self.frame_jog_axis_buttons.setGeometry(QRect(10, 10, 211, 191))
        self.frame_jog_axis_buttons.setMinimumSize(QSize(211, 191))
        self.frame_jog_axis_buttons.setMaximumSize(QSize(16777215, 16777215))
        self.frame_jog_axis_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_jog_axis_buttons.setFrameShadow(QFrame.Raised)
        self.btn_jog_neg_a = ActionButton(self.frame_jog_axis_buttons)
        self.btn_jog_neg_a.setObjectName(u"btn_jog_neg_a")
        self.btn_jog_neg_a.setGeometry(QRect(160, 130, 50, 60))
        self.btn_jog_neg_a.setMinimumSize(QSize(50, 60))
        self.btn_jog_neg_a.setMaximumSize(QSize(50, 60))
        font4 = QFont()
        font4.setFamily(u"BebasKai")
        font4.setPointSize(20)
        font4.setBold(False)
        font4.setItalic(False)
        self.btn_jog_neg_a.setFont(font4)
        self.btn_jog_neg_a.setStyleSheet(u"font: 75 20pt \"BebasKai\";")
        icon4 = QIcon()
        icon4.addFile(u"images/a_minus_jog_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_jog_neg_a.setIcon(icon4)
        self.btn_jog_neg_a.setIconSize(QSize(42, 42))
        self.btn_jog_neg_a.setProperty("estop_action", False)
        self.btn_jog_neg_a.setProperty("jog_joint_pos_action", False)
        self.btn_jog_neg_a.setProperty("jog_joint_neg_action", True)
        self.btn_jog_neg_a.setProperty("jog_selected_neg_action", False)
        self.btn_jog_neg_a.setProperty("joint_number", 3)
        self.btn_jog_neg_a.setProperty("jog_joint_number", 2)
        self.btn_jog_neg_z = ActionButton(self.frame_jog_axis_buttons)
        self.btn_jog_neg_z.setObjectName(u"btn_jog_neg_z")
        self.btn_jog_neg_z.setGeometry(QRect(0, 130, 50, 60))
        self.btn_jog_neg_z.setMinimumSize(QSize(50, 60))
        self.btn_jog_neg_z.setMaximumSize(QSize(50, 60))
        self.btn_jog_neg_z.setFont(font4)
        self.btn_jog_neg_z.setStyleSheet(u"font: 75 20pt \"BebasKai\";")
        icon5 = QIcon()
        icon5.addFile(u"images/z_minus_jog_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_jog_neg_z.setIcon(icon5)
        self.btn_jog_neg_z.setIconSize(QSize(42, 42))
        self.btn_jog_neg_z.setProperty("estop_action", False)
        self.btn_jog_neg_z.setProperty("jog_joint_pos_action", False)
        self.btn_jog_neg_z.setProperty("jog_joint_neg_action", True)
        self.btn_jog_neg_z.setProperty("jog_selected_neg_action", False)
        self.btn_jog_neg_z.setProperty("joint_number", 2)
        self.btn_jog_neg_z.setProperty("jog_joint_number", 2)
        self.btn_jog_pos_a = ActionButton(self.frame_jog_axis_buttons)
        self.btn_jog_pos_a.setObjectName(u"btn_jog_pos_a")
        self.btn_jog_pos_a.setGeometry(QRect(160, 0, 50, 60))
        self.btn_jog_pos_a.setMinimumSize(QSize(50, 60))
        self.btn_jog_pos_a.setMaximumSize(QSize(50, 60))
        self.btn_jog_pos_a.setFont(font4)
        self.btn_jog_pos_a.setStyleSheet(u"font: 75 20pt \"BebasKai\";")
        icon6 = QIcon()
        icon6.addFile(u"images/a_plus_jog_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_jog_pos_a.setIcon(icon6)
        self.btn_jog_pos_a.setIconSize(QSize(42, 42))
        self.btn_jog_pos_a.setProperty("estop_action", False)
        self.btn_jog_pos_a.setProperty("jog_joint_pos_action", True)
        self.btn_jog_pos_a.setProperty("jog_selected_pos_action", False)
        self.btn_jog_pos_a.setProperty("jog_selected_neg_action", False)
        self.btn_jog_pos_a.setProperty("joint_number", 3)
        self.btn_jog_pos_a.setProperty("jog_joint_number", 2)
        self.btn_jog_neg_x = ActionButton(self.frame_jog_axis_buttons)
        self.btn_jog_neg_x.setObjectName(u"btn_jog_neg_x")
        self.btn_jog_neg_x.setGeometry(QRect(0, 70, 70, 50))
        self.btn_jog_neg_x.setMinimumSize(QSize(70, 50))
        self.btn_jog_neg_x.setMaximumSize(QSize(70, 50))
        self.btn_jog_neg_x.setFont(font4)
        self.btn_jog_neg_x.setStyleSheet(u"background-color: rgb(252, 233, 79);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 20pt \"BebasKai\";")
        icon7 = QIcon()
        icon7.addFile(u"images/x_minus_d.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_jog_neg_x.setIcon(icon7)
        self.btn_jog_neg_x.setIconSize(QSize(50, 50))
        self.btn_jog_neg_x.setProperty("estop_action", False)
        self.btn_jog_neg_x.setProperty("jog_joint_neg_action", True)
        self.btn_jog_neg_x.setProperty("jog_selected_neg_action", False)
        self.btn_jog_neg_x.setProperty("jog_rate_action", False)
        self.btn_jog_pos_x = ActionButton(self.frame_jog_axis_buttons)
        self.btn_jog_pos_x.setObjectName(u"btn_jog_pos_x")
        self.btn_jog_pos_x.setGeometry(QRect(140, 70, 70, 50))
        self.btn_jog_pos_x.setMinimumSize(QSize(70, 50))
        self.btn_jog_pos_x.setMaximumSize(QSize(70, 50))
        self.btn_jog_pos_x.setFont(font4)
        self.btn_jog_pos_x.setStyleSheet(u"background-color: rgb(252, 233, 79);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 20pt \"BebasKai\";")
        icon8 = QIcon()
        icon8.addFile(u"images/x_plus_d.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_jog_pos_x.setIcon(icon8)
        self.btn_jog_pos_x.setIconSize(QSize(50, 50))
        self.btn_jog_pos_x.setProperty("estop_action", False)
        self.btn_jog_pos_x.setProperty("jog_joint_pos_action", True)
        self.btn_jog_pos_x.setProperty("jog_selected_pos_action", False)
        self.btn_jog_pos_z = ActionButton(self.frame_jog_axis_buttons)
        self.btn_jog_pos_z.setObjectName(u"btn_jog_pos_z")
        self.btn_jog_pos_z.setGeometry(QRect(0, 0, 50, 60))
        self.btn_jog_pos_z.setMinimumSize(QSize(50, 60))
        self.btn_jog_pos_z.setMaximumSize(QSize(50, 60))
        self.btn_jog_pos_z.setFont(font4)
        self.btn_jog_pos_z.setStyleSheet(u"font: 75 20pt \"BebasKai\";")
        icon9 = QIcon()
        icon9.addFile(u"images/z_plus_jog_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_jog_pos_z.setIcon(icon9)
        self.btn_jog_pos_z.setIconSize(QSize(42, 42))
        self.btn_jog_pos_z.setProperty("estop_action", False)
        self.btn_jog_pos_z.setProperty("jog_joint_pos_action", True)
        self.btn_jog_pos_z.setProperty("jog_selected_pos_action", False)
        self.btn_jog_pos_z.setProperty("joint_number", 2)
        self.btn_jog_pos_z.setProperty("jog_joint_number", 2)
        self.btn_jog_pos_y = ActionButton(self.frame_jog_axis_buttons)
        self.btn_jog_pos_y.setObjectName(u"btn_jog_pos_y")
        self.btn_jog_pos_y.setGeometry(QRect(80, 0, 50, 70))
        self.btn_jog_pos_y.setMinimumSize(QSize(50, 70))
        self.btn_jog_pos_y.setMaximumSize(QSize(50, 70))
        self.btn_jog_pos_y.setFont(font4)
        self.btn_jog_pos_y.setStyleSheet(u"background-color: rgb(39, 219, 219);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 20pt \"BebasKai\";")
        icon10 = QIcon()
        icon10.addFile(u"images/y_plus_d.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_jog_pos_y.setIcon(icon10)
        self.btn_jog_pos_y.setIconSize(QSize(50, 50))
        self.btn_jog_pos_y.setProperty("estop_action", False)
        self.btn_jog_pos_y.setProperty("jog_joint_pos_action", True)
        self.btn_jog_pos_y.setProperty("jog_selected_pos_action", False)
        self.btn_jog_pos_y.setProperty("jog_selected_neg_action", False)
        self.btn_jog_pos_y.setProperty("joint_number", 1)
        self.btn_jog_pos_y.setProperty("jog_joint_number", 1)
        self.btn_jog_neg_y = ActionButton(self.frame_jog_axis_buttons)
        self.btn_jog_neg_y.setObjectName(u"btn_jog_neg_y")
        self.btn_jog_neg_y.setGeometry(QRect(80, 120, 50, 70))
        self.btn_jog_neg_y.setMinimumSize(QSize(50, 70))
        self.btn_jog_neg_y.setMaximumSize(QSize(50, 70))
        self.btn_jog_neg_y.setFont(font4)
        self.btn_jog_neg_y.setStyleSheet(u"background-color: rgb(39, 219, 219);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 20pt \"BebasKai\";")
        icon11 = QIcon()
        icon11.addFile(u"images/y_minus_d.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_jog_neg_y.setIcon(icon11)
        self.btn_jog_neg_y.setIconSize(QSize(50, 50))
        self.btn_jog_neg_y.setProperty("estop_action", False)
        self.btn_jog_neg_y.setProperty("jog_joint_pos_action", False)
        self.btn_jog_neg_y.setProperty("jog_joint_neg_action", True)
        self.btn_jog_neg_y.setProperty("jog_selected_neg_action", False)
        self.btn_jog_neg_y.setProperty("joint_number", 1)
        self.btn_jog_neg_y.setProperty("jog_joint_number", 1)
        self.slider_jog_linear = StatusSlider(self.jogging_frame)
        self.slider_jog_linear.setObjectName(u"slider_jog_linear")
        self.slider_jog_linear.setGeometry(QRect(350, 50, 30, 141))
        sizePolicy.setHeightForWidth(self.slider_jog_linear.sizePolicy().hasHeightForWidth())
        self.slider_jog_linear.setSizePolicy(sizePolicy)
        self.slider_jog_linear.setMinimumSize(QSize(30, 120))
        self.slider_jog_linear.setMaximumSize(QSize(30, 210))
        self.slider_jog_linear.setStyleSheet(u"QSlider::groove:vertical {\n"
"border: 1px solid #bbb;\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"width: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"background: white;\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal  {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"width: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:vertical  {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 2"
                        "55, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"height: 30px;\n"
"margin-top: -1.3px;\n"
"margin-bottom: -1.3px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #444;\n"
"border-color: rgb(241, 239, 237);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
""
                        "}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.slider_jog_linear.setMaximum(3600)
        self.slider_jog_linear.setSingleStep(100)
        self.slider_jog_linear.setPageStep(100)
        self.slider_jog_linear.setValue(3000)
        self.slider_jog_linear.setTracking(True)
        self.slider_jog_linear.setOrientation(Qt.Vertical)
        self.slider_jog_linear.setInvertedAppearance(False)
        self.slider_jog_linear.setInvertedControls(False)
        self.slider_jog_linear.setTickPosition(QSlider.NoTicks)
        self.slider_jog_linear.setProperty("jograte_rate", True)
        self.status_jog_linear = StatusLabel(self.jogging_frame)
        self.status_jog_linear.setObjectName(u"status_jog_linear")
        self.status_jog_linear.setGeometry(QRect(240, 50, 90, 30))
        sizePolicy.setHeightForWidth(self.status_jog_linear.sizePolicy().hasHeightForWidth())
        self.status_jog_linear.setSizePolicy(sizePolicy)
        self.status_jog_linear.setMinimumSize(QSize(90, 30))
        self.status_jog_linear.setMaximumSize(QSize(90, 30))
        self.status_jog_linear.setStyleSheet(u"font: 15pt \"Sans\";")
        self.status_jog_linear.setFrameShape(QFrame.WinPanel)
        self.status_jog_linear.setFrameShadow(QFrame.Sunken)
        self.status_jog_linear.setAlignment(Qt.AlignCenter)
        self.status_jog_linear.setProperty("max_velocity_override_status", False)
        self.status_jog_linear.setProperty("jograte_status", True)
        self.lbl_jog_linear = QLabel(self.jogging_frame)
        self.lbl_jog_linear.setObjectName(u"lbl_jog_linear")
        self.lbl_jog_linear.setGeometry(QRect(240, 10, 90, 30))
        sizePolicy3.setHeightForWidth(self.lbl_jog_linear.sizePolicy().hasHeightForWidth())
        self.lbl_jog_linear.setSizePolicy(sizePolicy3)
        self.lbl_jog_linear.setMinimumSize(QSize(90, 30))
        self.lbl_jog_linear.setMaximumSize(QSize(90, 30))
        self.lbl_jog_linear.setStyleSheet(u"font: 14pt \"Sans\";")
        self.lbl_jog_linear.setAlignment(Qt.AlignCenter)
        self.btn_jog_l_slow = PushButton(self.jogging_frame)
        self.btn_jog_l_slow.setObjectName(u"btn_jog_l_slow")
        self.btn_jog_l_slow.setGeometry(QRect(250, 90, 70, 50))
        sizePolicy.setHeightForWidth(self.btn_jog_l_slow.sizePolicy().hasHeightForWidth())
        self.btn_jog_l_slow.setSizePolicy(sizePolicy)
        self.btn_jog_l_slow.setMinimumSize(QSize(70, 50))
        self.btn_jog_l_slow.setMaximumSize(QSize(70, 50))
        self.btn_jog_l_slow.setStyleSheet(u"font: 75 17pt \"Bebas Kai\";")
        self.btn_jog_l_slow.setCheckable(True)
        self.btn_jog_l_slow.setProperty("checked_state_text_option", True)
        self.pushbutton_metric = PushButton(self.jogging_frame)
        self.pushbutton_metric.setObjectName(u"pushbutton_metric")
        self.pushbutton_metric.setGeometry(QRect(250, 148, 70, 50))
        self.pushbutton_metric.setMinimumSize(QSize(70, 50))
        self.pushbutton_metric.setMaximumSize(QSize(70, 50))
        self.pushbutton_metric.setStyleSheet(u"font: 75 17pt \"Bebas Kai\";")
        self.pushbutton_metric.setCheckable(True)
        self.pushbutton_metric.setProperty("checked_state_text_option", True)
        self.verticalLayoutWidget_5 = QWidget(self.jogging_frame)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(9, 200, 371, 91))
        self.verticalLayout_20 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.verticalLayoutWidget_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 75))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.widget_increments_angular = QWidget(self.frame_10)
        self.widget_increments_angular.setObjectName(u"widget_increments_angular")
        self.widget_increments_angular.setGeometry(QRect(10, 50, 351, 30))
        self.horizontalLayout_17 = QHBoxLayout(self.widget_increments_angular)
        self.horizontalLayout_17.setSpacing(4)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.lbl_increments_angular = QLabel(self.widget_increments_angular)
        self.lbl_increments_angular.setObjectName(u"lbl_increments_angular")
        sizePolicy3.setHeightForWidth(self.lbl_increments_angular.sizePolicy().hasHeightForWidth())
        self.lbl_increments_angular.setSizePolicy(sizePolicy3)
        self.lbl_increments_angular.setMinimumSize(QSize(0, 30))
        self.lbl_increments_angular.setMaximumSize(QSize(205, 30))
        self.lbl_increments_angular.setStyleSheet(u"\n"
"font: 75 12pt \"Bebas Kai\";")
        self.lbl_increments_angular.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.lbl_increments_angular)

        self.jogincrements_angular = JogIncrements(self.widget_increments_angular)
        self.jogincrements_angular.setObjectName(u"jogincrements_angular")
        sizePolicy.setHeightForWidth(self.jogincrements_angular.sizePolicy().hasHeightForWidth())
        self.jogincrements_angular.setSizePolicy(sizePolicy)
        self.jogincrements_angular.setMinimumSize(QSize(100, 30))
        self.jogincrements_angular.setMaximumSize(QSize(100, 30))
        self.jogincrements_angular.setFocusPolicy(Qt.ClickFocus)
        self.jogincrements_angular.setMaxVisibleItems(20)
        self.jogincrements_angular.setMaxCount(20)
        self.jogincrements_angular.setProperty("linear_option", False)

        self.horizontalLayout_17.addWidget(self.jogincrements_angular)

        self.widget_increments_linear = QWidget(self.frame_10)
        self.widget_increments_linear.setObjectName(u"widget_increments_linear")
        self.widget_increments_linear.setGeometry(QRect(10, 10, 351, 30))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_increments_linear)
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lbl_increments_linear = QLabel(self.widget_increments_linear)
        self.lbl_increments_linear.setObjectName(u"lbl_increments_linear")
        sizePolicy.setHeightForWidth(self.lbl_increments_linear.sizePolicy().hasHeightForWidth())
        self.lbl_increments_linear.setSizePolicy(sizePolicy)
        self.lbl_increments_linear.setMinimumSize(QSize(160, 30))
        self.lbl_increments_linear.setMaximumSize(QSize(205, 30))
        self.lbl_increments_linear.setStyleSheet(u"\n"
"font: 75 12pt \"Bebas Kai\";")
        self.lbl_increments_linear.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.lbl_increments_linear)

        self.jogincrements_linear = JogIncrements(self.widget_increments_linear)
        self.jogincrements_linear.setObjectName(u"jogincrements_linear")
        sizePolicy.setHeightForWidth(self.jogincrements_linear.sizePolicy().hasHeightForWidth())
        self.jogincrements_linear.setSizePolicy(sizePolicy)
        self.jogincrements_linear.setMinimumSize(QSize(100, 30))
        self.jogincrements_linear.setMaximumSize(QSize(100, 30))
        self.jogincrements_linear.setFocusPolicy(Qt.ClickFocus)
        self.jogincrements_linear.setMaxVisibleItems(20)
        self.jogincrements_linear.setMaxCount(20)
        self.jogincrements_linear.setDuplicatesEnabled(False)
        self.jogincrements_linear.setFrame(True)

        self.horizontalLayout_5.addWidget(self.jogincrements_linear)


        self.verticalLayout_20.addWidget(self.frame_10)


        self.gridLayout_18.addWidget(self.jogging_frame, 1, 0, 1, 1)

        self.stackedWidget_4.addWidget(self.panel_jogging)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.frame_mpg = QFrame(self.page_7)
        self.frame_mpg.setObjectName(u"frame_mpg")
        self.frame_mpg.setGeometry(QRect(0, 0, 410, 501))
        self.frame_mpg.setFrameShape(QFrame.StyledPanel)
        self.frame_mpg.setFrameShadow(QFrame.Raised)
        self.groupBox = QGroupBox(self.frame_mpg)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(12, 290, 381, 201))
        self.groupBox.setStyleSheet(u"")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(True)
        self.frame_34 = QFrame(self.groupBox)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setGeometry(QRect(7, 30, 367, 161))
        self.frame_34.setStyleSheet(u"")
        self.frame_34.setFrameShape(QFrame.WinPanel)
        self.frame_34.setFrameShadow(QFrame.Plain)
        self.verticalLayout_42 = QVBoxLayout(self.frame_34)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.gridLayout_29 = QGridLayout()
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(0, -1, -1, -1)
        self.pushbutton_ro = PushButton(self.frame_34)
        self.pushbutton_ro.setObjectName(u"pushbutton_ro")
        self.pushbutton_ro.setMinimumSize(QSize(110, 41))
        self.pushbutton_ro.setStyleSheet(u"font: 75 12pt \"DejaVu Serif\";\n"
"color: rgb(245, 121, 0);")
        self.pushbutton_ro.setCheckable(True)
        self.pushbutton_ro.setAutoExclusive(True)
        self.pushbutton_ro.setProperty("indicator_option", True)
        self.pushbutton_ro.setProperty("indicator_HAL_pin_option", False)

        self.gridLayout_29.addWidget(self.pushbutton_ro, 2, 1, 1, 1)

        self.pushbutton_fo = PushButton(self.frame_34)
        self.pushbutton_fo.setObjectName(u"pushbutton_fo")
        self.pushbutton_fo.setMinimumSize(QSize(0, 41))
        self.pushbutton_fo.setStyleSheet(u"font: 75 12pt \"DejaVu Serif\";\n"
"color: rgb(245, 121, 0);")
        self.pushbutton_fo.setCheckable(True)
        self.pushbutton_fo.setAutoExclusive(True)
        self.pushbutton_fo.setProperty("indicator_option", True)
        self.pushbutton_fo.setProperty("indicator_HAL_pin_option", False)

        self.gridLayout_29.addWidget(self.pushbutton_fo, 2, 0, 1, 1)

        self.pushbutton_so = PushButton(self.frame_34)
        self.pushbutton_so.setObjectName(u"pushbutton_so")
        self.pushbutton_so.setMinimumSize(QSize(0, 41))
        self.pushbutton_so.setStyleSheet(u"font: 75 12pt \"DejaVu Serif\";\n"
"color: rgb(245, 121, 0);")
        self.pushbutton_so.setCheckable(True)
        self.pushbutton_so.setAutoExclusive(True)
        self.pushbutton_so.setProperty("indicator_option", True)

        self.gridLayout_29.addWidget(self.pushbutton_so, 2, 2, 1, 1)

        self.axistoolbutton = AxisToolButton(self.frame_34)
        self.axis_buttonGroup = QButtonGroup(MainWindow)
        self.axis_buttonGroup.setObjectName(u"axis_buttonGroup")
        self.axis_buttonGroup.addButton(self.axistoolbutton)
        self.axistoolbutton.setObjectName(u"axistoolbutton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.axistoolbutton.sizePolicy().hasHeightForWidth())
        self.axistoolbutton.setSizePolicy(sizePolicy5)
        self.axistoolbutton.setMinimumSize(QSize(110, 41))
        self.axistoolbutton.setStyleSheet(u"font: 75 12pt \"DejaVu Serif\";\n"
"color: rgb(245, 121, 0);")
        self.axistoolbutton.setCheckable(True)
        self.axistoolbutton.setChecked(True)
        self.axistoolbutton.setAutoExclusive(True)
        self.axistoolbutton.setPopupMode(QToolButton.MenuButtonPopup)

        self.gridLayout_29.addWidget(self.axistoolbutton, 0, 0, 1, 1)

        self.axistoolbutton_2 = AxisToolButton(self.frame_34)
        self.axis_buttonGroup.addButton(self.axistoolbutton_2)
        self.axistoolbutton_2.setObjectName(u"axistoolbutton_2")
        sizePolicy5.setHeightForWidth(self.axistoolbutton_2.sizePolicy().hasHeightForWidth())
        self.axistoolbutton_2.setSizePolicy(sizePolicy5)
        self.axistoolbutton_2.setMinimumSize(QSize(110, 41))
        self.axistoolbutton_2.setStyleSheet(u"font: 75 12pt \"DejaVu Serif\";\n"
"color: rgb(245, 121, 0);")
        self.axistoolbutton_2.setCheckable(True)
        self.axistoolbutton_2.setChecked(False)
        self.axistoolbutton_2.setAutoExclusive(True)
        self.axistoolbutton_2.setPopupMode(QToolButton.MenuButtonPopup)
        self.axistoolbutton_2.setProperty("joint_number", 1)

        self.gridLayout_29.addWidget(self.axistoolbutton_2, 0, 1, 1, 1)

        self.axistoolbutton_3 = AxisToolButton(self.frame_34)
        self.axis_buttonGroup.addButton(self.axistoolbutton_3)
        self.axistoolbutton_3.setObjectName(u"axistoolbutton_3")
        sizePolicy5.setHeightForWidth(self.axistoolbutton_3.sizePolicy().hasHeightForWidth())
        self.axistoolbutton_3.setSizePolicy(sizePolicy5)
        self.axistoolbutton_3.setMinimumSize(QSize(110, 41))
        self.axistoolbutton_3.setStyleSheet(u"font: 75 12pt \"DejaVu Serif\";\n"
"color: rgb(245, 121, 0);")
        self.axistoolbutton_3.setCheckable(True)
        self.axistoolbutton_3.setChecked(False)
        self.axistoolbutton_3.setAutoExclusive(True)
        self.axistoolbutton_3.setPopupMode(QToolButton.MenuButtonPopup)
        self.axistoolbutton_3.setProperty("joint_number", 2)

        self.gridLayout_29.addWidget(self.axistoolbutton_3, 0, 2, 1, 1)

        self.axistoolbutton_4 = AxisToolButton(self.frame_34)
        self.axis_buttonGroup.addButton(self.axistoolbutton_4)
        self.axistoolbutton_4.setObjectName(u"axistoolbutton_4")
        sizePolicy.setHeightForWidth(self.axistoolbutton_4.sizePolicy().hasHeightForWidth())
        self.axistoolbutton_4.setSizePolicy(sizePolicy)
        self.axistoolbutton_4.setMinimumSize(QSize(110, 41))
        self.axistoolbutton_4.setStyleSheet(u"font: 75 12pt \"DejaVu Serif\";\n"
"color: rgb(245, 121, 0);")
        self.axistoolbutton_4.setCheckable(True)
        self.axistoolbutton_4.setChecked(False)
        self.axistoolbutton_4.setAutoExclusive(True)
        self.axistoolbutton_4.setPopupMode(QToolButton.MenuButtonPopup)
        self.axistoolbutton_4.setProperty("joint_number", 3)

        self.gridLayout_29.addWidget(self.axistoolbutton_4, 1, 2, 1, 1)

        self.pushbutton_jog = PushButton(self.frame_34)
        self.pushbutton_jog.setObjectName(u"pushbutton_jog")
        sizePolicy.setHeightForWidth(self.pushbutton_jog.sizePolicy().hasHeightForWidth())
        self.pushbutton_jog.setSizePolicy(sizePolicy)
        self.pushbutton_jog.setMinimumSize(QSize(110, 41))
        font5 = QFont()
        font5.setFamily(u"DejaVu Serif")
        font5.setPointSize(15)
        font5.setBold(False)
        font5.setItalic(False)
        self.pushbutton_jog.setFont(font5)
        self.pushbutton_jog.setStyleSheet(u"font: 75 12pt \"DejaVu Serif\";\n"
"color: rgb(245, 121, 0);")
        self.pushbutton_jog.setCheckable(True)
        self.pushbutton_jog.setAutoExclusive(True)
        self.pushbutton_jog.setProperty("indicator_option", True)
        self.pushbutton_jog.setProperty("indicator_HAL_pin_option", False)
        self.pushbutton_jog.setProperty("indicator_status_option", False)
        self.pushbutton_jog.setProperty("python_command_option", False)
        self.pushbutton_jog.setProperty("indicator_size", 0.300000000000000)

        self.gridLayout_29.addWidget(self.pushbutton_jog, 1, 0, 1, 1)

        self.lbl_max_rapid = QLineEdit(self.frame_34)
        self.lbl_max_rapid.setObjectName(u"lbl_max_rapid")
        sizePolicy.setHeightForWidth(self.lbl_max_rapid.sizePolicy().hasHeightForWidth())
        self.lbl_max_rapid.setSizePolicy(sizePolicy)
        self.lbl_max_rapid.setMinimumSize(QSize(110, 41))
        self.lbl_max_rapid.setMaximumSize(QSize(112, 40))
        self.lbl_max_rapid.setStyleSheet(u"font: 75 12pt \"DejaVu Serif\";\n"
"color: rgb(84, 234, 7);")
        self.lbl_max_rapid.setMaxLength(4)
        self.lbl_max_rapid.setAlignment(Qt.AlignCenter)
        self.lbl_max_rapid.setReadOnly(True)

        self.gridLayout_29.addWidget(self.lbl_max_rapid, 1, 1, 1, 1)


        self.verticalLayout_42.addLayout(self.gridLayout_29)

        self.jogincrements_linear_2 = JogIncrements(self.frame_mpg)
        self.jogincrements_linear_2.setObjectName(u"jogincrements_linear_2")
        self.jogincrements_linear_2.setGeometry(QRect(260, 260, 110, 30))
        sizePolicy.setHeightForWidth(self.jogincrements_linear_2.sizePolicy().hasHeightForWidth())
        self.jogincrements_linear_2.setSizePolicy(sizePolicy)
        self.jogincrements_linear_2.setMinimumSize(QSize(110, 30))
        self.jogincrements_linear_2.setMaximumSize(QSize(110, 30))
        self.jogincrements_linear_2.setFocusPolicy(Qt.ClickFocus)
        self.jogincrements_linear_2.setStyleSheet(u"font: 75 12pt \"BebasKai\";\n"
"color: rgb(245, 121, 0);")
        self.jogincrements_linear_2.setEditable(False)
        self.jogincrements_linear_2.setMaxVisibleItems(20)
        self.jogincrements_linear_2.setMaxCount(20)
        self.jogincrements_linear_2.setDuplicatesEnabled(False)
        self.jogincrements_linear_2.setFrame(True)
        self.MPG = Dial(self.frame_mpg)
        self.MPG.setObjectName(u"MPG")
        self.MPG.setGeometry(QRect(30, 10, 261, 261))
        self.MPG.setMinimumSize(QSize(0, 200))
        self.MPG.setStyleSheet(u"QDial\n"
"       {\n"
"           background-color:QLinearGradient( \n"
"               x1: 0.177, y1: 0.004, x2: 0.831, y2: 0.911, \n"
"               stop: 0 white, \n"
"               stop: 0.061 white, \n"
"               stop: 0.066 lightgray, \n"
"               stop: 0.5 #242424, \n"
"               stop: 0.505 #000000,\n"
"               stop: 0.827 #040404,\n"
"               stop: 0.966 #292929,\n"
"               stop: 0.983 #2e2e2e\n"
"           );\n"
"       }\n"
"       ")
        self.MPG.setMaximum(100)
        self.MPG.setInvertedAppearance(False)
        self.MPG.setInvertedControls(False)
        self.MPG.setWrapping(True)
        self.MPG.setNotchesVisible(True)
        self.stackedWidget_4.addWidget(self.page_7)
        self.panel_mdi = QWidget()
        self.panel_mdi.setObjectName(u"panel_mdi")
        self.frame_mdi_history = QFrame(self.panel_mdi)
        self.frame_mdi_history.setObjectName(u"frame_mdi_history")
        self.frame_mdi_history.setGeometry(QRect(0, 0, 408, 501))
        self.frame_mdi_history.setMinimumSize(QSize(354, 470))
        self.frame_mdi_history.setMaximumSize(QSize(16777215, 16777215))
        self.frame_mdi_history.setFrameShape(QFrame.WinPanel)
        self.frame_mdi_history.setFrameShadow(QFrame.Raised)
        self.label_mdi_panel = QLabel(self.frame_mdi_history)
        self.label_mdi_panel.setObjectName(u"label_mdi_panel")
        self.label_mdi_panel.setGeometry(QRect(3, 0, 401, 31))
        font6 = QFont()
        font6.setFamily(u"Sans")
        font6.setPointSize(12)
        font6.setBold(False)
        font6.setItalic(False)
        self.label_mdi_panel.setFont(font6)
        self.label_mdi_panel.setStyleSheet(u"font: 12pt \"Sans\";")
        self.label_mdi_panel.setFrameShape(QFrame.WinPanel)
        self.label_mdi_panel.setFrameShadow(QFrame.Raised)
        self.label_mdi_panel.setAlignment(Qt.AlignCenter)
        self.mdihistory = MDIHistory(self.frame_mdi_history)
        self.mdihistory.setObjectName(u"mdihistory")
        self.mdihistory.setGeometry(QRect(3, 32, 401, 461))
        font7 = QFont()
        font7.setPointSize(11)
        self.mdihistory.setFont(font7)
        self.mdihistory.setProperty("soft_keyboard_option", True)
        self.stackedWidget_4.addWidget(self.panel_mdi)
        self.panel_gcode = QWidget()
        self.panel_gcode.setObjectName(u"panel_gcode")
        self.frame_gcode = QFrame(self.panel_gcode)
        self.frame_gcode.setObjectName(u"frame_gcode")
        self.frame_gcode.setGeometry(QRect(0, 10, 411, 481))
        self.frame_gcode.setFrameShape(QFrame.NoFrame)
        self.frame_gcode.setFrameShadow(QFrame.Plain)
        self.frame_gcode_viewer = QFrame(self.frame_gcode)
        self.frame_gcode_viewer.setObjectName(u"frame_gcode_viewer")
        self.frame_gcode_viewer.setGeometry(QRect(0, -10, 408, 491))
        self.frame_gcode_viewer.setFrameShape(QFrame.StyledPanel)
        self.frame_gcode_viewer.setFrameShadow(QFrame.Raised)
        self.gcode_viewer = GcodeEditor(self.frame_gcode_viewer)
        self.gcode_viewer.setObjectName(u"gcode_viewer")
        self.gcode_viewer.setGeometry(QRect(0, 39, 406, 450))
        self.gcode_viewer.setMinimumSize(QSize(406, 200))
        self.cmb_gcode_history = QComboBox(self.frame_gcode_viewer)
        self.cmb_gcode_history.setObjectName(u"cmb_gcode_history")
        self.cmb_gcode_history.setGeometry(QRect(0, 10, 406, 30))
        self.cmb_gcode_history.setMinimumSize(QSize(0, 30))
        self.cmb_gcode_history.setMaximumSize(QSize(16777215, 30))
        font8 = QFont()
        font8.setFamily(u"Lato Heavy")
        font8.setPointSize(10)
        font8.setBold(False)
        font8.setItalic(False)
        self.cmb_gcode_history.setFont(font8)
        self.cmb_gcode_history.setFocusPolicy(Qt.ClickFocus)
        self.cmb_gcode_history.setStyleSheet(u"    background: rgb(240,240,240);\n"
"    border: none;\n"
"    font: 10pt \"Lato Heavy\";\n"
"    color: black;\n"
"")
        self.cmb_gcode_history.setEditable(False)
        self.cmb_gcode_history.setMaxCount(10)
        self.cmb_gcode_history.setInsertPolicy(QComboBox.InsertAtTop)
        self.stackedWidget_4.addWidget(self.panel_gcode)
        self.panel_not_used = QWidget()
        self.panel_not_used.setObjectName(u"panel_not_used")
        self.frame_not_used = QFrame(self.panel_not_used)
        self.frame_not_used.setObjectName(u"frame_not_used")
        self.frame_not_used.setGeometry(QRect(0, 0, 408, 501))
        self.frame_not_used.setMinimumSize(QSize(408, 0))
        self.frame_not_used.setFrameShape(QFrame.WinPanel)
        self.frame_not_used.setFrameShadow(QFrame.Raised)
        self.frame_14 = QFrame(self.frame_not_used)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(12, 12, 385, 478))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_14)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget_work_height = QWidget(self.frame_14)
        self.widget_work_height.setObjectName(u"widget_work_height")
        self.horizontalLayout_35 = QHBoxLayout(self.widget_work_height)
        self.horizontalLayout_35.setSpacing(4)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_46 = QLabel(self.widget_work_height)
        self.label_46.setObjectName(u"label_46")
        sizePolicy3.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy3)
        self.label_46.setMinimumSize(QSize(180, 30))
        self.label_46.setMaximumSize(QSize(16777215, 30))
        self.label_46.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.label_46)

        self.lineEdit_work_height = QLineEdit(self.widget_work_height)
        self.lineEdit_work_height.setObjectName(u"lineEdit_work_height")
        sizePolicy.setHeightForWidth(self.lineEdit_work_height.sizePolicy().hasHeightForWidth())
        self.lineEdit_work_height.setSizePolicy(sizePolicy)
        self.lineEdit_work_height.setMinimumSize(QSize(80, 30))
        self.lineEdit_work_height.setMaximumSize(QSize(80, 30))
        self.lineEdit_work_height.setMaxLength(8)
        self.lineEdit_work_height.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.lineEdit_work_height)

        self.label_47 = QLabel(self.widget_work_height)
        self.label_47.setObjectName(u"label_47")
        sizePolicy.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy)
        self.label_47.setMinimumSize(QSize(40, 30))
        self.label_47.setMaximumSize(QSize(40, 30))
        self.label_47.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_35.addWidget(self.label_47)


        self.gridLayout_3.addWidget(self.widget_work_height, 0, 0, 1, 2)

        self.widget_sensor_height = QWidget(self.frame_14)
        self.widget_sensor_height.setObjectName(u"widget_sensor_height")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_sensor_height)
        self.horizontalLayout_24.setSpacing(4)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.widget_sensor_height)
        self.label_16.setObjectName(u"label_16")
        sizePolicy3.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy3)
        self.label_16.setMinimumSize(QSize(180, 30))
        self.label_16.setMaximumSize(QSize(16777215, 30))
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_16)

        self.lineEdit_sensor_height = QLineEdit(self.widget_sensor_height)
        self.lineEdit_sensor_height.setObjectName(u"lineEdit_sensor_height")
        sizePolicy.setHeightForWidth(self.lineEdit_sensor_height.sizePolicy().hasHeightForWidth())
        self.lineEdit_sensor_height.setSizePolicy(sizePolicy)
        self.lineEdit_sensor_height.setMinimumSize(QSize(80, 30))
        self.lineEdit_sensor_height.setMaximumSize(QSize(80, 30))
        self.lineEdit_sensor_height.setMaxLength(8)
        self.lineEdit_sensor_height.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.lineEdit_sensor_height)

        self.label_42 = QLabel(self.widget_sensor_height)
        self.label_42.setObjectName(u"label_42")
        sizePolicy.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy)
        self.label_42.setMinimumSize(QSize(40, 30))
        self.label_42.setMaximumSize(QSize(40, 30))
        self.label_42.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_24.addWidget(self.label_42)


        self.gridLayout_3.addWidget(self.widget_sensor_height, 1, 0, 1, 2)

        self.label_54 = QLabel(self.frame_14)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setPixmap(QPixmap(u"images/tool_probe.png"))
        self.label_54.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_54, 2, 0, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(308, 59, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_14, 3, 0, 1, 2)

        self.horizontalWidget = QWidget(self.frame_14)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        sizePolicy3.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy3)
        self.horizontalWidget.setMinimumSize(QSize(0, 30))
        self.horizontalWidget.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_52 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_52.setSpacing(4)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.label_63 = QLabel(self.horizontalWidget)
        self.label_63.setObjectName(u"label_63")
        sizePolicy.setHeightForWidth(self.label_63.sizePolicy().hasHeightForWidth())
        self.label_63.setSizePolicy(sizePolicy)
        self.label_63.setMinimumSize(QSize(180, 30))
        self.label_63.setMaximumSize(QSize(180, 30))
        self.label_63.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_52.addWidget(self.label_63)

        self.label_48 = QLabel(self.horizontalWidget)
        self.label_48.setObjectName(u"label_48")
        sizePolicy.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy)
        self.label_48.setMinimumSize(QSize(60, 30))
        self.label_48.setMaximumSize(QSize(60, 30))
        self.label_48.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_52.addWidget(self.label_48)

        self.label_68 = QLabel(self.horizontalWidget)
        self.label_68.setObjectName(u"label_68")
        sizePolicy.setHeightForWidth(self.label_68.sizePolicy().hasHeightForWidth())
        self.label_68.setSizePolicy(sizePolicy)
        self.label_68.setMinimumSize(QSize(60, 30))
        self.label_68.setMaximumSize(QSize(60, 30))
        self.label_68.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_52.addWidget(self.label_68)


        self.gridLayout_3.addWidget(self.horizontalWidget, 4, 0, 1, 2)

        self.widget_sensor_location = QWidget(self.frame_14)
        self.widget_sensor_location.setObjectName(u"widget_sensor_location")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_sensor_location)
        self.horizontalLayout_10.setSpacing(4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget_sensor_location)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QSize(180, 30))
        self.label_8.setMaximumSize(QSize(180, 30))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_8)

        self.lineEdit_sensor_x = QLineEdit(self.widget_sensor_location)
        self.lineEdit_sensor_x.setObjectName(u"lineEdit_sensor_x")
        sizePolicy.setHeightForWidth(self.lineEdit_sensor_x.sizePolicy().hasHeightForWidth())
        self.lineEdit_sensor_x.setSizePolicy(sizePolicy)
        self.lineEdit_sensor_x.setMinimumSize(QSize(80, 30))
        self.lineEdit_sensor_x.setMaximumSize(QSize(80, 30))
        self.lineEdit_sensor_x.setMaxLength(8)
        self.lineEdit_sensor_x.setAlignment(Qt.AlignCenter)
        self.lineEdit_sensor_x.setReadOnly(False)

        self.horizontalLayout_10.addWidget(self.lineEdit_sensor_x)

        self.lineEdit_sensor_y = QLineEdit(self.widget_sensor_location)
        self.lineEdit_sensor_y.setObjectName(u"lineEdit_sensor_y")
        sizePolicy.setHeightForWidth(self.lineEdit_sensor_y.sizePolicy().hasHeightForWidth())
        self.lineEdit_sensor_y.setSizePolicy(sizePolicy)
        self.lineEdit_sensor_y.setMinimumSize(QSize(80, 30))
        self.lineEdit_sensor_y.setMaximumSize(QSize(80, 30))
        self.lineEdit_sensor_y.setMaxLength(8)
        self.lineEdit_sensor_y.setAlignment(Qt.AlignCenter)
        self.lineEdit_sensor_y.setReadOnly(False)

        self.horizontalLayout_10.addWidget(self.lineEdit_sensor_y)


        self.gridLayout_3.addWidget(self.widget_sensor_location, 5, 0, 1, 2)

        self.widget_laser_offset = QWidget(self.frame_14)
        self.widget_laser_offset.setObjectName(u"widget_laser_offset")
        self.horizontalLayout_34 = QHBoxLayout(self.widget_laser_offset)
        self.horizontalLayout_34.setSpacing(4)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.widget_laser_offset)
        self.label_36.setObjectName(u"label_36")
        sizePolicy.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy)
        self.label_36.setMinimumSize(QSize(180, 30))
        self.label_36.setMaximumSize(QSize(180, 30))
        self.label_36.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_34.addWidget(self.label_36)

        self.lineEdit_laser_x = QLineEdit(self.widget_laser_offset)
        self.lineEdit_laser_x.setObjectName(u"lineEdit_laser_x")
        sizePolicy.setHeightForWidth(self.lineEdit_laser_x.sizePolicy().hasHeightForWidth())
        self.lineEdit_laser_x.setSizePolicy(sizePolicy)
        self.lineEdit_laser_x.setMinimumSize(QSize(80, 30))
        self.lineEdit_laser_x.setMaximumSize(QSize(80, 30))
        self.lineEdit_laser_x.setMaxLength(8)
        self.lineEdit_laser_x.setAlignment(Qt.AlignCenter)
        self.lineEdit_laser_x.setReadOnly(False)

        self.horizontalLayout_34.addWidget(self.lineEdit_laser_x)

        self.lineEdit_laser_y = QLineEdit(self.widget_laser_offset)
        self.lineEdit_laser_y.setObjectName(u"lineEdit_laser_y")
        sizePolicy.setHeightForWidth(self.lineEdit_laser_y.sizePolicy().hasHeightForWidth())
        self.lineEdit_laser_y.setSizePolicy(sizePolicy)
        self.lineEdit_laser_y.setMinimumSize(QSize(80, 30))
        self.lineEdit_laser_y.setMaximumSize(QSize(80, 30))
        self.lineEdit_laser_y.setMaxLength(8)
        self.lineEdit_laser_y.setAlignment(Qt.AlignCenter)
        self.lineEdit_laser_y.setReadOnly(False)

        self.horizontalLayout_34.addWidget(self.lineEdit_laser_y)


        self.gridLayout_3.addWidget(self.widget_laser_offset, 6, 0, 1, 2)

        self.widget_camera_offset_2 = QWidget(self.frame_14)
        self.widget_camera_offset_2.setObjectName(u"widget_camera_offset_2")
        sizePolicy1.setHeightForWidth(self.widget_camera_offset_2.sizePolicy().hasHeightForWidth())
        self.widget_camera_offset_2.setSizePolicy(sizePolicy1)
        self.widget_camera_offset_2.setMinimumSize(QSize(367, 0))
        self.horizontalLayout_58 = QHBoxLayout(self.widget_camera_offset_2)
        self.horizontalLayout_58.setSpacing(4)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.label_64 = QLabel(self.widget_camera_offset_2)
        self.label_64.setObjectName(u"label_64")
        sizePolicy.setHeightForWidth(self.label_64.sizePolicy().hasHeightForWidth())
        self.label_64.setSizePolicy(sizePolicy)
        self.label_64.setMinimumSize(QSize(180, 30))
        self.label_64.setMaximumSize(QSize(100, 30))
        self.label_64.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_58.addWidget(self.label_64)

        self.lineEdit_camera_x = QLineEdit(self.widget_camera_offset_2)
        self.lineEdit_camera_x.setObjectName(u"lineEdit_camera_x")
        sizePolicy.setHeightForWidth(self.lineEdit_camera_x.sizePolicy().hasHeightForWidth())
        self.lineEdit_camera_x.setSizePolicy(sizePolicy)
        self.lineEdit_camera_x.setMinimumSize(QSize(80, 30))
        self.lineEdit_camera_x.setMaximumSize(QSize(80, 30))
        self.lineEdit_camera_x.setMaxLength(8)
        self.lineEdit_camera_x.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_58.addWidget(self.lineEdit_camera_x)

        self.lineEdit_camera_y = QLineEdit(self.widget_camera_offset_2)
        self.lineEdit_camera_y.setObjectName(u"lineEdit_camera_y")
        sizePolicy.setHeightForWidth(self.lineEdit_camera_y.sizePolicy().hasHeightForWidth())
        self.lineEdit_camera_y.setSizePolicy(sizePolicy)
        self.lineEdit_camera_y.setMinimumSize(QSize(80, 30))
        self.lineEdit_camera_y.setMaximumSize(QSize(80, 30))
        self.lineEdit_camera_y.setMaxLength(8)
        self.lineEdit_camera_y.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_58.addWidget(self.lineEdit_camera_y)


        self.gridLayout_3.addWidget(self.widget_camera_offset_2, 7, 0, 1, 2)

        self.widget_offset_buttons = QWidget(self.frame_14)
        self.widget_offset_buttons.setObjectName(u"widget_offset_buttons")
        self.horizontalLayout_42 = QHBoxLayout(self.widget_offset_buttons)
        self.horizontalLayout_42.setSpacing(4)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.btn_goto_sensor = QPushButton(self.widget_offset_buttons)
        self.btn_goto_sensor.setObjectName(u"btn_goto_sensor")
        sizePolicy.setHeightForWidth(self.btn_goto_sensor.sizePolicy().hasHeightForWidth())
        self.btn_goto_sensor.setSizePolicy(sizePolicy)
        self.btn_goto_sensor.setMinimumSize(QSize(70, 40))
        self.btn_goto_sensor.setMaximumSize(QSize(70, 40))

        self.horizontalLayout_42.addWidget(self.btn_goto_sensor)

        self.btn_laser_on = PushButton(self.widget_offset_buttons)
        self.btn_laser_on.setObjectName(u"btn_laser_on")
        sizePolicy.setHeightForWidth(self.btn_laser_on.sizePolicy().hasHeightForWidth())
        self.btn_laser_on.setSizePolicy(sizePolicy)
        self.btn_laser_on.setMinimumSize(QSize(70, 40))
        self.btn_laser_on.setMaximumSize(QSize(70, 40))
        self.btn_laser_on.setCheckable(True)
        self.btn_laser_on.setChecked(False)
        self.btn_laser_on.setProperty("indicator_option", False)
        self.btn_laser_on.setProperty("checked_state_text_option", True)
        self.btn_laser_on.setProperty("python_command_option", False)
        self.btn_laser_on.setProperty("on_color", QColor(0, 255, 0))
        self.btn_laser_on.setProperty("indicator_size", 0.200000000000000)

        self.horizontalLayout_42.addWidget(self.btn_laser_on)

        self.btn_ref_laser = QPushButton(self.widget_offset_buttons)
        self.btn_ref_laser.setObjectName(u"btn_ref_laser")
        sizePolicy.setHeightForWidth(self.btn_ref_laser.sizePolicy().hasHeightForWidth())
        self.btn_ref_laser.setSizePolicy(sizePolicy)
        self.btn_ref_laser.setMinimumSize(QSize(70, 40))
        self.btn_ref_laser.setMaximumSize(QSize(70, 40))

        self.horizontalLayout_42.addWidget(self.btn_ref_laser)

        self.btn_touch_sensor = QPushButton(self.widget_offset_buttons)
        self.btn_touch_sensor.setObjectName(u"btn_touch_sensor")
        sizePolicy.setHeightForWidth(self.btn_touch_sensor.sizePolicy().hasHeightForWidth())
        self.btn_touch_sensor.setSizePolicy(sizePolicy)
        self.btn_touch_sensor.setMinimumSize(QSize(70, 40))
        self.btn_touch_sensor.setMaximumSize(QSize(70, 40))

        self.horizontalLayout_42.addWidget(self.btn_touch_sensor)


        self.gridLayout_3.addWidget(self.widget_offset_buttons, 8, 0, 1, 1)

        self.btn_ref_camera = QPushButton(self.frame_14)
        self.btn_ref_camera.setObjectName(u"btn_ref_camera")
        sizePolicy.setHeightForWidth(self.btn_ref_camera.sizePolicy().hasHeightForWidth())
        self.btn_ref_camera.setSizePolicy(sizePolicy)
        self.btn_ref_camera.setMinimumSize(QSize(70, 50))
        self.btn_ref_camera.setMaximumSize(QSize(70, 50))

        self.gridLayout_3.addWidget(self.btn_ref_camera, 8, 1, 1, 1)

        self.stackedWidget_4.addWidget(self.panel_not_used)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.frame_16 = QFrame(self.page_8)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(0, 0, 411, 501))
        sizePolicy2.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy2)
        self.frame_16.setMinimumSize(QSize(411, 0))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_16)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_69 = QLabel(self.frame_16)
        self.label_69.setObjectName(u"label_69")
        sizePolicy2.setHeightForWidth(self.label_69.sizePolicy().hasHeightForWidth())
        self.label_69.setSizePolicy(sizePolicy2)
        self.label_69.setMinimumSize(QSize(140, 0))
        self.label_69.setStyleSheet(u"font: 12pt \"Sans\";")
        self.label_69.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_69)

        self.statuslabel_5 = StatusLabel(self.frame_16)
        self.statuslabel_5.setObjectName(u"statuslabel_5")
        sizePolicy.setHeightForWidth(self.statuslabel_5.sizePolicy().hasHeightForWidth())
        self.statuslabel_5.setSizePolicy(sizePolicy)
        self.statuslabel_5.setMinimumSize(QSize(60, 30))
        self.statuslabel_5.setMaximumSize(QSize(60, 30))
        self.statuslabel_5.setFrameShape(QFrame.WinPanel)
        self.statuslabel_5.setFrameShadow(QFrame.Sunken)
        self.statuslabel_5.setAlignment(Qt.AlignCenter)
        self.statuslabel_5.setProperty("tool_diameter_status", True)

        self.horizontalLayout_7.addWidget(self.statuslabel_5)

        self.label_70 = QLabel(self.frame_16)
        self.label_70.setObjectName(u"label_70")
        sizePolicy2.setHeightForWidth(self.label_70.sizePolicy().hasHeightForWidth())
        self.label_70.setSizePolicy(sizePolicy2)
        self.label_70.setMinimumSize(QSize(140, 0))

        self.horizontalLayout_7.addWidget(self.label_70)


        self.gridLayout_9.addLayout(self.horizontalLayout_7, 3, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(298, 54, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_8, 0, 0, 1, 1)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setSpacing(4)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_71 = QLabel(self.frame_16)
        self.label_71.setObjectName(u"label_71")
        sizePolicy1.setHeightForWidth(self.label_71.sizePolicy().hasHeightForWidth())
        self.label_71.setSizePolicy(sizePolicy1)
        self.label_71.setMinimumSize(QSize(10, 0))
        self.label_71.setMaximumSize(QSize(10, 16777215))

        self.horizontalLayout_47.addWidget(self.label_71)

        self.label_72 = QLabel(self.frame_16)
        self.label_72.setObjectName(u"label_72")
        sizePolicy.setHeightForWidth(self.label_72.sizePolicy().hasHeightForWidth())
        self.label_72.setSizePolicy(sizePolicy)
        self.label_72.setMinimumSize(QSize(50, 30))
        self.label_72.setMaximumSize(QSize(120, 30))
        self.label_72.setStyleSheet(u"font: 12pt \"Sans\";")
        self.label_72.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_47.addWidget(self.label_72)

        self.statuslabel_4 = StatusLabel(self.frame_16)
        self.statuslabel_4.setObjectName(u"statuslabel_4")
        sizePolicy.setHeightForWidth(self.statuslabel_4.sizePolicy().hasHeightForWidth())
        self.statuslabel_4.setSizePolicy(sizePolicy)
        self.statuslabel_4.setMinimumSize(QSize(60, 30))
        self.statuslabel_4.setMaximumSize(QSize(60, 30))
        self.statuslabel_4.setFrameShape(QFrame.WinPanel)
        self.statuslabel_4.setFrameShadow(QFrame.Sunken)
        self.statuslabel_4.setAlignment(Qt.AlignCenter)
        self.statuslabel_4.setProperty("tool_number_status", True)

        self.horizontalLayout_47.addWidget(self.statuslabel_4)

        self.label_74 = QLabel(self.frame_16)
        self.label_74.setObjectName(u"label_74")
        sizePolicy1.setHeightForWidth(self.label_74.sizePolicy().hasHeightForWidth())
        self.label_74.setSizePolicy(sizePolicy1)
        self.label_74.setMinimumSize(QSize(140, 0))

        self.horizontalLayout_47.addWidget(self.label_74)


        self.gridLayout_9.addLayout(self.horizontalLayout_47, 1, 0, 1, 1)

        self.label_45 = QLabel(self.frame_16)
        self.label_45.setObjectName(u"label_45")
        sizePolicy.setHeightForWidth(self.label_45.sizePolicy().hasHeightForWidth())
        self.label_45.setSizePolicy(sizePolicy)
        self.label_45.setMinimumSize(QSize(377, 274))
        self.label_45.setPixmap(QPixmap(u"images/atc_spindle_tool.png"))
        self.label_45.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_45, 2, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_75 = QLabel(self.frame_16)
        self.label_75.setObjectName(u"label_75")
        sizePolicy.setHeightForWidth(self.label_75.sizePolicy().hasHeightForWidth())
        self.label_75.setSizePolicy(sizePolicy)
        self.label_75.setMinimumSize(QSize(210, 30))
        self.label_75.setMaximumSize(QSize(16777215, 30))
        self.label_75.setStyleSheet(u"font: 12pt \"Sans\";")
        self.label_75.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_75)

        self.lineEdit_touch_height = QLineEdit(self.frame_16)
        self.lineEdit_touch_height.setObjectName(u"lineEdit_touch_height")
        sizePolicy.setHeightForWidth(self.lineEdit_touch_height.sizePolicy().hasHeightForWidth())
        self.lineEdit_touch_height.setSizePolicy(sizePolicy)
        self.lineEdit_touch_height.setMinimumSize(QSize(80, 30))
        self.lineEdit_touch_height.setMaximumSize(QSize(80, 30))
        self.lineEdit_touch_height.setMaxLength(8)
        self.lineEdit_touch_height.setFrame(True)
        self.lineEdit_touch_height.setAlignment(Qt.AlignCenter)
        self.lineEdit_touch_height.setReadOnly(False)

        self.horizontalLayout_13.addWidget(self.lineEdit_touch_height)

        self.lbl_touchheight_units = QLabel(self.frame_16)
        self.lbl_touchheight_units.setObjectName(u"lbl_touchheight_units")
        sizePolicy.setHeightForWidth(self.lbl_touchheight_units.sizePolicy().hasHeightForWidth())
        self.lbl_touchheight_units.setSizePolicy(sizePolicy)
        self.lbl_touchheight_units.setMinimumSize(QSize(50, 30))
        self.lbl_touchheight_units.setMaximumSize(QSize(50, 30))
        self.lbl_touchheight_units.setAlignment(Qt.AlignCenter)
        self.lbl_touchheight_units.setWordWrap(False)
        self.lbl_touchheight_units.setIndent(0)

        self.horizontalLayout_13.addWidget(self.lbl_touchheight_units)


        self.gridLayout_9.addLayout(self.horizontalLayout_13, 4, 0, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(318, 53, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_16, 5, 0, 1, 1)

        self.widget_tool_table = QWidget(self.frame_16)
        self.widget_tool_table.setObjectName(u"widget_tool_table")
        self.horizontalLayout_51 = QHBoxLayout(self.widget_tool_table)
        self.horizontalLayout_51.setSpacing(4)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.btn_tool_add = PushButton(self.widget_tool_table)
        self.btn_tool_add.setObjectName(u"btn_tool_add")
        sizePolicy.setHeightForWidth(self.btn_tool_add.sizePolicy().hasHeightForWidth())
        self.btn_tool_add.setSizePolicy(sizePolicy)
        self.btn_tool_add.setMinimumSize(QSize(70, 40))
        self.btn_tool_add.setMaximumSize(QSize(70, 40))
        self.btn_tool_add.setStyleSheet(u"font: 12pt \"Sans\";")
        self.btn_tool_add.setProperty("python_command_option", True)

        self.horizontalLayout_51.addWidget(self.btn_tool_add)

        self.btn_tool_delete = PushButton(self.widget_tool_table)
        self.btn_tool_delete.setObjectName(u"btn_tool_delete")
        sizePolicy.setHeightForWidth(self.btn_tool_delete.sizePolicy().hasHeightForWidth())
        self.btn_tool_delete.setSizePolicy(sizePolicy)
        self.btn_tool_delete.setMinimumSize(QSize(70, 40))
        self.btn_tool_delete.setMaximumSize(QSize(70, 40))
        self.btn_tool_delete.setStyleSheet(u"font: 12pt \"Sans\";")
        self.btn_tool_delete.setProperty("python_command_option", True)

        self.horizontalLayout_51.addWidget(self.btn_tool_delete)

        self.btn_m61 = QPushButton(self.widget_tool_table)
        self.btn_m61.setObjectName(u"btn_m61")
        sizePolicy.setHeightForWidth(self.btn_m61.sizePolicy().hasHeightForWidth())
        self.btn_m61.setSizePolicy(sizePolicy)
        self.btn_m61.setMinimumSize(QSize(70, 40))
        self.btn_m61.setMaximumSize(QSize(70, 40))
        self.btn_m61.setStyleSheet(u"font: 12pt \"Sans\";")

        self.horizontalLayout_51.addWidget(self.btn_m61)

        self.btn_touchplate = QPushButton(self.widget_tool_table)
        self.btn_touchplate.setObjectName(u"btn_touchplate")
        sizePolicy.setHeightForWidth(self.btn_touchplate.sizePolicy().hasHeightForWidth())
        self.btn_touchplate.setSizePolicy(sizePolicy)
        self.btn_touchplate.setMinimumSize(QSize(70, 40))
        self.btn_touchplate.setMaximumSize(QSize(70, 40))

        self.horizontalLayout_51.addWidget(self.btn_touchplate)


        self.gridLayout_9.addWidget(self.widget_tool_table, 6, 0, 1, 1)

        self.stackedWidget_4.addWidget(self.page_8)
        self.panel_help = QWidget()
        self.panel_help.setObjectName(u"panel_help")
        self.frame_help = QFrame(self.panel_help)
        self.frame_help.setObjectName(u"frame_help")
        self.frame_help.setGeometry(QRect(0, 0, 411, 501))
        self.frame_help.setFrameShape(QFrame.WinPanel)
        self.frame_help.setFrameShadow(QFrame.Raised)
        self.frame_help_upper_panel = QFrame(self.frame_help)
        self.frame_help_upper_panel.setObjectName(u"frame_help_upper_panel")
        self.frame_help_upper_panel.setGeometry(QRect(0, 0, 408, 501))
        self.frame_help_upper_panel.setFrameShape(QFrame.WinPanel)
        self.frame_help_upper_panel.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget_8 = QWidget(self.frame_help_upper_panel)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(10, 10, 391, 421))
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widgetswitcher_2 = WidgetSwitcher(self.horizontalLayoutWidget_8)
        self.widgetswitcher_2.setObjectName(u"widgetswitcher_2")
        self.page_0 = QWidget()
        self.page_0.setObjectName(u"page_0")
        self.verticalLayout_6 = QVBoxLayout(self.page_0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widgetswitcher_2.addWidget(self.page_0)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.verticalLayout_41 = QVBoxLayout(self.page_9)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")

        self.verticalLayout_41.addLayout(self.verticalLayout_43)

        self.widgetswitcher_2.addWidget(self.page_9)

        self.horizontalLayout_8.addWidget(self.widgetswitcher_2)

        self.horizontalLayoutWidget_9 = QWidget(self.frame_help_upper_panel)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(10, 430, 391, 61))
        self.horizontalLayout_43 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.horizontalLayoutWidget_9)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.WinPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.actionbutton_view_p_2 = ActionButton(self.frame_8)
        self.actionbutton_view_p_2.setObjectName(u"actionbutton_view_p_2")
        self.actionbutton_view_p_2.setGeometry(QRect(10, 10, 50, 40))
        sizePolicy.setHeightForWidth(self.actionbutton_view_p_2.sizePolicy().hasHeightForWidth())
        self.actionbutton_view_p_2.setSizePolicy(sizePolicy)
        self.actionbutton_view_p_2.setMinimumSize(QSize(50, 40))
        self.actionbutton_view_p_2.setMaximumSize(QSize(50, 40))
        self.actionbutton_view_p_2.setBaseSize(QSize(60, 40))
        self.actionbutton_view_p_2.setCheckable(True)
        self.actionbutton_view_p_2.setChecked(True)
        self.actionbutton_view_p_2.setAutoExclusive(True)
        self.actionbutton_view_p_2.setProperty("view_change_action", True)
        self.actionbutton_view_p_2.setProperty("template_label_option", False)
        self.actionbutton_view_p_2.setProperty("joint_number", 0)
        self.actionbutton_view_p_2.setProperty("incr_imperial_number", 0.010000000000000)
        self.actionbutton_view_p_2.setProperty("incr_mm_number", 0.025000000000000)
        self.actionbutton_view_p_2.setProperty("incr_angular_number", -1.000000000000000)
        self.actionbutton_view_p_2.setProperty("toggle_float_option", False)
        self.actionbutton_view_p_2.setProperty("float_num", 100.000000000000000)
        self.actionbutton_view_p_2.setProperty("float_alt_num", 50.000000000000000)
        self.actionbutton_view_p_2.setProperty("ini_mdi_number", 0)
        self.actionbutton_view_x_2 = ActionButton(self.frame_8)
        self.actionbutton_view_x_2.setObjectName(u"actionbutton_view_x_2")
        self.actionbutton_view_x_2.setGeometry(QRect(70, 10, 50, 40))
        sizePolicy.setHeightForWidth(self.actionbutton_view_x_2.sizePolicy().hasHeightForWidth())
        self.actionbutton_view_x_2.setSizePolicy(sizePolicy)
        self.actionbutton_view_x_2.setMinimumSize(QSize(50, 40))
        self.actionbutton_view_x_2.setMaximumSize(QSize(50, 40))
        self.actionbutton_view_x_2.setBaseSize(QSize(60, 40))
        self.actionbutton_view_x_2.setCheckable(True)
        self.actionbutton_view_x_2.setAutoExclusive(True)
        self.actionbutton_view_x_2.setProperty("view_change_action", True)
        self.actionbutton_view_x_2.setProperty("template_label_option", False)
        self.actionbutton_view_x_2.setProperty("joint_number", 0)
        self.actionbutton_view_x_2.setProperty("incr_imperial_number", 0.010000000000000)
        self.actionbutton_view_x_2.setProperty("incr_mm_number", 0.025000000000000)
        self.actionbutton_view_x_2.setProperty("incr_angular_number", -1.000000000000000)
        self.actionbutton_view_x_2.setProperty("toggle_float_option", False)
        self.actionbutton_view_x_2.setProperty("float_num", 100.000000000000000)
        self.actionbutton_view_x_2.setProperty("float_alt_num", 50.000000000000000)
        self.actionbutton_view_x_2.setProperty("ini_mdi_number", 0)
        self.actionbutton_view_y_2 = ActionButton(self.frame_8)
        self.actionbutton_view_y_2.setObjectName(u"actionbutton_view_y_2")
        self.actionbutton_view_y_2.setGeometry(QRect(130, 10, 50, 40))
        sizePolicy.setHeightForWidth(self.actionbutton_view_y_2.sizePolicy().hasHeightForWidth())
        self.actionbutton_view_y_2.setSizePolicy(sizePolicy)
        self.actionbutton_view_y_2.setMinimumSize(QSize(50, 40))
        self.actionbutton_view_y_2.setMaximumSize(QSize(50, 40))
        self.actionbutton_view_y_2.setBaseSize(QSize(60, 40))
        self.actionbutton_view_y_2.setCheckable(True)
        self.actionbutton_view_y_2.setAutoExclusive(True)
        self.actionbutton_view_y_2.setProperty("view_change_action", True)
        self.actionbutton_view_y_2.setProperty("template_label_option", False)
        self.actionbutton_view_y_2.setProperty("joint_number", 0)
        self.actionbutton_view_y_2.setProperty("incr_imperial_number", 0.010000000000000)
        self.actionbutton_view_y_2.setProperty("incr_mm_number", 0.025000000000000)
        self.actionbutton_view_y_2.setProperty("incr_angular_number", -1.000000000000000)
        self.actionbutton_view_y_2.setProperty("toggle_float_option", False)
        self.actionbutton_view_y_2.setProperty("float_num", 100.000000000000000)
        self.actionbutton_view_y_2.setProperty("float_alt_num", 50.000000000000000)
        self.actionbutton_view_y_2.setProperty("ini_mdi_number", 0)
        self.actionbutton_view_z_2 = ActionButton(self.frame_8)
        self.actionbutton_view_z_2.setObjectName(u"actionbutton_view_z_2")
        self.actionbutton_view_z_2.setGeometry(QRect(190, 10, 50, 40))
        sizePolicy.setHeightForWidth(self.actionbutton_view_z_2.sizePolicy().hasHeightForWidth())
        self.actionbutton_view_z_2.setSizePolicy(sizePolicy)
        self.actionbutton_view_z_2.setMinimumSize(QSize(50, 40))
        self.actionbutton_view_z_2.setMaximumSize(QSize(50, 40))
        self.actionbutton_view_z_2.setBaseSize(QSize(60, 40))
        self.actionbutton_view_z_2.setCheckable(True)
        self.actionbutton_view_z_2.setAutoExclusive(True)
        self.actionbutton_view_z_2.setProperty("view_change_action", True)
        self.actionbutton_view_z_2.setProperty("template_label_option", False)
        self.actionbutton_view_z_2.setProperty("joint_number", 0)
        self.actionbutton_view_z_2.setProperty("incr_imperial_number", 0.010000000000000)
        self.actionbutton_view_z_2.setProperty("incr_mm_number", 0.025000000000000)
        self.actionbutton_view_z_2.setProperty("incr_angular_number", -1.000000000000000)
        self.actionbutton_view_z_2.setProperty("toggle_float_option", False)
        self.actionbutton_view_z_2.setProperty("float_num", 100.000000000000000)
        self.actionbutton_view_z_2.setProperty("float_alt_num", 50.000000000000000)
        self.actionbutton_view_z_2.setProperty("ini_mdi_number", 0)
        self.actionbutton_clear_2 = ActionButton(self.frame_8)
        self.actionbutton_clear_2.setObjectName(u"actionbutton_clear_2")
        self.actionbutton_clear_2.setGeometry(QRect(250, 10, 50, 40))
        sizePolicy.setHeightForWidth(self.actionbutton_clear_2.sizePolicy().hasHeightForWidth())
        self.actionbutton_clear_2.setSizePolicy(sizePolicy)
        self.actionbutton_clear_2.setMinimumSize(QSize(50, 40))
        self.actionbutton_clear_2.setMaximumSize(QSize(50, 40))
        self.actionbutton_clear_2.setBaseSize(QSize(60, 40))
        self.actionbutton_clear_2.setAutoFillBackground(False)
        icon12 = QIcon()
        icon12.addFile(u"images/clear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionbutton_clear_2.setIcon(icon12)
        self.actionbutton_clear_2.setIconSize(QSize(25, 25))
        self.actionbutton_clear_2.setCheckable(False)
        self.actionbutton_clear_2.setProperty("estop_action", False)
        self.actionbutton_clear_2.setProperty("view_change_action", True)
        self.actionbutton_clear_2.setProperty("template_label_option", False)
        self.actionbutton_clear_2.setProperty("joint_number", 0)
        self.actionbutton_clear_2.setProperty("incr_imperial_number", 0.010000000000000)
        self.actionbutton_clear_2.setProperty("incr_mm_number", 0.025000000000000)
        self.actionbutton_clear_2.setProperty("incr_angular_number", -1.000000000000000)
        self.actionbutton_clear_2.setProperty("toggle_float_option", False)
        self.actionbutton_clear_2.setProperty("float_num", 100.000000000000000)
        self.actionbutton_clear_2.setProperty("float_alt_num", 50.000000000000000)
        self.actionbutton_clear_2.setProperty("ini_mdi_number", 0)
        self.probesim_button = PushButton(self.frame_8)
        self.probesim_button.setObjectName(u"probesim_button")
        self.probesim_button.setGeometry(QRect(310, 10, 71, 41))
        self.probesim_button.setAutoExclusive(True)

        self.horizontalLayout_43.addWidget(self.frame_8)

        self.stackedWidget_4.addWidget(self.panel_help)
        self.verticalLayoutWidget = QWidget(self.page)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 10, 801, 501))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.verticalLayoutWidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_24 = QVBoxLayout(self.widget)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.main_tab_widget = QStackedWidget(self.widget)
        self.main_tab_widget.setObjectName(u"main_tab_widget")
        sizePolicy2.setHeightForWidth(self.main_tab_widget.sizePolicy().hasHeightForWidth())
        self.main_tab_widget.setSizePolicy(sizePolicy2)
        self.main_tab_widget.setMinimumSize(QSize(599, 399))
        self.main_tab_widget.setMaximumSize(QSize(16777215, 16777215))
        self.main_tab_widget.setFrameShape(QFrame.WinPanel)
        self.main_tab_widget.setFrameShadow(QFrame.Raised)
        self.panel_gcode_graphics = QWidget()
        self.panel_gcode_graphics.setObjectName(u"panel_gcode_graphics")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.panel_gcode_graphics.sizePolicy().hasHeightForWidth())
        self.panel_gcode_graphics.setSizePolicy(sizePolicy6)
        self.gridLayout_30 = QGridLayout(self.panel_gcode_graphics)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.frame_gcode_graphics = QFrame(self.panel_gcode_graphics)
        self.frame_gcode_graphics.setObjectName(u"frame_gcode_graphics")
        sizePolicy6.setHeightForWidth(self.frame_gcode_graphics.sizePolicy().hasHeightForWidth())
        self.frame_gcode_graphics.setSizePolicy(sizePolicy6)
        self.frame_gcode_graphics.setFrameShape(QFrame.StyledPanel)
        self.frame_gcode_graphics.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_gcode_graphics)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_graphics_btns = QFrame(self.frame_gcode_graphics)
        self.frame_graphics_btns.setObjectName(u"frame_graphics_btns")
        sizePolicy6.setHeightForWidth(self.frame_graphics_btns.sizePolicy().hasHeightForWidth())
        self.frame_graphics_btns.setSizePolicy(sizePolicy6)
        self.frame_graphics_btns.setMinimumSize(QSize(60, 400))
        self.frame_graphics_btns.setMaximumSize(QSize(60, 16777215))
        self.frame_graphics_btns.setStyleSheet(u"")
        self.frame_graphics_btns.setFrameShape(QFrame.WinPanel)
        self.frame_graphics_btns.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_graphics_btns)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.abtn_graphics_view_p = ActionButton(self.frame_graphics_btns)
        self.abtn_graphics_view_p.setObjectName(u"abtn_graphics_view_p")
        self.abtn_graphics_view_p.setMinimumSize(QSize(0, 35))
        self.abtn_graphics_view_p.setStyleSheet(u"font: 15pt \"Sans\";")
        self.abtn_graphics_view_p.setCheckable(True)
        self.abtn_graphics_view_p.setChecked(True)
        self.abtn_graphics_view_p.setAutoExclusive(True)
        self.abtn_graphics_view_p.setProperty("view_change_action", True)

        self.verticalLayout_25.addWidget(self.abtn_graphics_view_p)

        self.abtn_graphics_view_x = ActionButton(self.frame_graphics_btns)
        self.abtn_graphics_view_x.setObjectName(u"abtn_graphics_view_x")
        self.abtn_graphics_view_x.setMinimumSize(QSize(0, 35))
        self.abtn_graphics_view_x.setStyleSheet(u"font: 15pt \"Sans\";")
        self.abtn_graphics_view_x.setCheckable(True)
        self.abtn_graphics_view_x.setAutoExclusive(True)
        self.abtn_graphics_view_x.setProperty("view_change_action", True)

        self.verticalLayout_25.addWidget(self.abtn_graphics_view_x)

        self.abtn_graphics_view_y = ActionButton(self.frame_graphics_btns)
        self.abtn_graphics_view_y.setObjectName(u"abtn_graphics_view_y")
        self.abtn_graphics_view_y.setMinimumSize(QSize(0, 35))
        self.abtn_graphics_view_y.setStyleSheet(u"font: 15pt \"Sans\";")
        self.abtn_graphics_view_y.setCheckable(True)
        self.abtn_graphics_view_y.setAutoExclusive(True)
        self.abtn_graphics_view_y.setProperty("view_change_action", True)

        self.verticalLayout_25.addWidget(self.abtn_graphics_view_y)

        self.abtn_graphics_view_z = ActionButton(self.frame_graphics_btns)
        self.abtn_graphics_view_z.setObjectName(u"abtn_graphics_view_z")
        self.abtn_graphics_view_z.setMinimumSize(QSize(0, 35))
        self.abtn_graphics_view_z.setStyleSheet(u"font: 15pt \"Sans\";")
        self.abtn_graphics_view_z.setCheckable(True)
        self.abtn_graphics_view_z.setAutoExclusive(True)
        self.abtn_graphics_view_z.setProperty("view_change_action", True)

        self.verticalLayout_25.addWidget(self.abtn_graphics_view_z)

        self.abtn_graphics_view_z2 = ActionButton(self.frame_graphics_btns)
        self.abtn_graphics_view_z2.setObjectName(u"abtn_graphics_view_z2")
        self.abtn_graphics_view_z2.setMinimumSize(QSize(0, 35))
        self.abtn_graphics_view_z2.setStyleSheet(u"font: 15pt \"Sans\";")
        self.abtn_graphics_view_z2.setCheckable(True)
        self.abtn_graphics_view_z2.setAutoExclusive(True)
        self.abtn_graphics_view_z2.setProperty("view_change_action", True)

        self.verticalLayout_25.addWidget(self.abtn_graphics_view_z2)

        self.actionbutton_zoom_in = ActionButton(self.frame_graphics_btns)
        self.actionbutton_zoom_in.setObjectName(u"actionbutton_zoom_in")
        self.actionbutton_zoom_in.setMinimumSize(QSize(0, 35))
        self.actionbutton_zoom_in.setStyleSheet(u"font: 15pt \"Ubuntu\";")
        self.actionbutton_zoom_in.setProperty("view_change_action", True)

        self.verticalLayout_25.addWidget(self.actionbutton_zoom_in)

        self.actionbutton_zoom_out = ActionButton(self.frame_graphics_btns)
        self.actionbutton_zoom_out.setObjectName(u"actionbutton_zoom_out")
        self.actionbutton_zoom_out.setMinimumSize(QSize(0, 35))
        self.actionbutton_zoom_out.setStyleSheet(u"font: 15pt \"Ubuntu\";")
        self.actionbutton_zoom_out.setProperty("view_change_action", True)

        self.verticalLayout_25.addWidget(self.actionbutton_zoom_out)

        self.btn_setdro = PushButton(self.frame_graphics_btns)
        self.btn_setdro.setObjectName(u"btn_setdro")
        self.btn_setdro.setMinimumSize(QSize(0, 35))
        self.btn_setdro.setCheckable(True)

        self.verticalLayout_25.addWidget(self.btn_setdro)

        self.btn_show_offset = PushButton(self.frame_graphics_btns)
        self.btn_show_offset.setObjectName(u"btn_show_offset")
        self.btn_show_offset.setMinimumSize(QSize(0, 35))
        self.btn_show_offset.setCheckable(True)

        self.verticalLayout_25.addWidget(self.btn_show_offset)

        self.btn_dimensions = PushButton(self.frame_graphics_btns)
        self.btn_dimensions.setObjectName(u"btn_dimensions")
        sizePolicy.setHeightForWidth(self.btn_dimensions.sizePolicy().hasHeightForWidth())
        self.btn_dimensions.setSizePolicy(sizePolicy)
        self.btn_dimensions.setMinimumSize(QSize(56, 35))
        self.btn_dimensions.setMaximumSize(QSize(56, 35))
        icon13 = QIcon()
        icon13.addFile(u"images/dimensions.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_dimensions.setIcon(icon13)
        self.btn_dimensions.setIconSize(QSize(30, 30))
        self.btn_dimensions.setCheckable(True)

        self.verticalLayout_25.addWidget(self.btn_dimensions)

        self.btn_graphics_view_clear = ActionButton(self.frame_graphics_btns)
        self.btn_graphics_view_clear.setObjectName(u"btn_graphics_view_clear")
        self.btn_graphics_view_clear.setMinimumSize(QSize(0, 35))
        self.btn_graphics_view_clear.setMaximumSize(QSize(16777215, 35))
        self.btn_graphics_view_clear.setIcon(icon12)
        self.btn_graphics_view_clear.setIconSize(QSize(35, 35))
        self.btn_graphics_view_clear.setCheckable(True)
        self.btn_graphics_view_clear.setAutoExclusive(True)
        self.btn_graphics_view_clear.setProperty("view_change_action", True)
        self.btn_graphics_view_clear.setProperty("joint_number", 0)
        self.btn_graphics_view_clear.setProperty("incr_imperial_number", 0.010000000000000)
        self.btn_graphics_view_clear.setProperty("incr_mm_number", 0.025000000000000)
        self.btn_graphics_view_clear.setProperty("incr_angular_number", -1.000000000000000)
        self.btn_graphics_view_clear.setProperty("toggle_float_option", False)
        self.btn_graphics_view_clear.setProperty("float_num", 100.000000000000000)
        self.btn_graphics_view_clear.setProperty("float_alt_num", 50.000000000000000)
        self.btn_graphics_view_clear.setProperty("ini_mdi_number", 0)

        self.verticalLayout_25.addWidget(self.btn_graphics_view_clear)


        self.horizontalLayout_20.addWidget(self.frame_graphics_btns)

        self.gcodegraphics = GCodeGraphics(self.frame_gcode_graphics)
        self.gcodegraphics.setObjectName(u"gcodegraphics")
        sizePolicy6.setHeightForWidth(self.gcodegraphics.sizePolicy().hasHeightForWidth())
        self.gcodegraphics.setSizePolicy(sizePolicy6)
        self.gcodegraphics.setMinimumSize(QSize(0, 0))
        self.gcodegraphics.setMaximumSize(QSize(16777215, 16777215))
        self.gcodegraphics.setProperty("_dro", False)
        self.gcodegraphics.setProperty("_dtg", False)
        self.gcodegraphics.setProperty("background_color", QColor(100, 100, 100))
        self.gcodegraphics.setProperty("_use_gradient_background", True)

        self.horizontalLayout_20.addWidget(self.gcodegraphics)


        self.gridLayout_30.addWidget(self.frame_gcode_graphics, 0, 0, 1, 1)

        self.main_tab_widget.addWidget(self.panel_gcode_graphics)
        self.panel_filedialog = QWidget()
        self.panel_filedialog.setObjectName(u"panel_filedialog")
        sizePolicy6.setHeightForWidth(self.panel_filedialog.sizePolicy().hasHeightForWidth())
        self.panel_filedialog.setSizePolicy(sizePolicy6)
        self.verticalLayout_26 = QVBoxLayout(self.panel_filedialog)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_filedialog = QFrame(self.panel_filedialog)
        self.frame_filedialog.setObjectName(u"frame_filedialog")
        sizePolicy2.setHeightForWidth(self.frame_filedialog.sizePolicy().hasHeightForWidth())
        self.frame_filedialog.setSizePolicy(sizePolicy2)
        self.frame_filedialog.setFrameShape(QFrame.StyledPanel)
        self.frame_filedialog.setFrameShadow(QFrame.Raised)
        self.gridLayout_31 = QGridLayout(self.frame_filedialog)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.filemanager = FileManager(self.frame_filedialog)
        self.filemanager.setObjectName(u"filemanager")
        sizePolicy6.setHeightForWidth(self.filemanager.sizePolicy().hasHeightForWidth())
        self.filemanager.setSizePolicy(sizePolicy6)
        self.filemanager.setMinimumSize(QSize(0, 0))
        self.filemanager.setMaximumSize(QSize(16777215, 16777215))
        self.filemanager.setStyleSheet(u"font: 11pt \"Ubuntu\";")

        self.gridLayout_31.addWidget(self.filemanager, 0, 0, 1, 1)

        self.gcode_editor = GcodeEditor(self.frame_filedialog)
        self.gcode_editor.setObjectName(u"gcode_editor")
        sizePolicy6.setHeightForWidth(self.gcode_editor.sizePolicy().hasHeightForWidth())
        self.gcode_editor.setSizePolicy(sizePolicy6)
        self.gcode_editor.setMinimumSize(QSize(0, 0))
        self.gcode_editor.setMaximumSize(QSize(16777215, 16777215))
        self.gcode_editor.setStyleSheet(u"font: 11pt \"Ubuntu\";")
        self.gcode_editor.setProperty("auto_show_mdi_status", False)

        self.gridLayout_31.addWidget(self.gcode_editor, 0, 1, 1, 1)

        self.frm_filemanager = QFrame(self.frame_filedialog)
        self.frm_filemanager.setObjectName(u"frm_filemanager")
        sizePolicy2.setHeightForWidth(self.frm_filemanager.sizePolicy().hasHeightForWidth())
        self.frm_filemanager.setSizePolicy(sizePolicy2)
        self.frm_filemanager.setMinimumSize(QSize(0, 0))
        self.frm_filemanager.setMaximumSize(QSize(16777215, 16777215))
        self.frm_filemanager.setFrameShape(QFrame.WinPanel)
        self.frm_filemanager.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frm_filemanager)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btn_file_next = PushButton(self.frm_filemanager)
        self.btn_file_next.setObjectName(u"btn_file_next")
        sizePolicy.setHeightForWidth(self.btn_file_next.sizePolicy().hasHeightForWidth())
        self.btn_file_next.setSizePolicy(sizePolicy)
        self.btn_file_next.setMinimumSize(QSize(70, 50))
        self.btn_file_next.setMaximumSize(QSize(70, 50))
        self.btn_file_next.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.btn_file_next.setProperty("python_command_option", True)

        self.gridLayout_4.addWidget(self.btn_file_next, 1, 0, 1, 1)

        self.btn_file_prev = PushButton(self.frm_filemanager)
        self.btn_file_prev.setObjectName(u"btn_file_prev")
        sizePolicy.setHeightForWidth(self.btn_file_prev.sizePolicy().hasHeightForWidth())
        self.btn_file_prev.setSizePolicy(sizePolicy)
        self.btn_file_prev.setMinimumSize(QSize(70, 50))
        self.btn_file_prev.setMaximumSize(QSize(70, 50))
        self.btn_file_prev.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.btn_file_prev.setProperty("python_command_option", True)

        self.gridLayout_4.addWidget(self.btn_file_prev, 2, 0, 1, 1)

        self.btn_gcode_edit = PushButton(self.frm_filemanager)
        self.btn_gcode_edit.setObjectName(u"btn_gcode_edit")
        sizePolicy.setHeightForWidth(self.btn_gcode_edit.sizePolicy().hasHeightForWidth())
        self.btn_gcode_edit.setSizePolicy(sizePolicy)
        self.btn_gcode_edit.setMinimumSize(QSize(70, 50))
        self.btn_gcode_edit.setMaximumSize(QSize(70, 50))
        self.btn_gcode_edit.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.btn_gcode_edit.setCheckable(True)
        self.btn_gcode_edit.setChecked(False)
        self.btn_gcode_edit.setProperty("python_command_option", False)

        self.gridLayout_4.addWidget(self.btn_gcode_edit, 3, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_7, 4, 0, 1, 1)

        self.btn_file_load = QPushButton(self.frm_filemanager)
        self.btn_file_load.setObjectName(u"btn_file_load")
        sizePolicy.setHeightForWidth(self.btn_file_load.sizePolicy().hasHeightForWidth())
        self.btn_file_load.setSizePolicy(sizePolicy)
        self.btn_file_load.setMinimumSize(QSize(70, 50))
        self.btn_file_load.setMaximumSize(QSize(70, 50))
        self.btn_file_load.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")

        self.gridLayout_4.addWidget(self.btn_file_load, 0, 0, 1, 1)


        self.gridLayout_31.addWidget(self.frm_filemanager, 0, 2, 1, 1)


        self.verticalLayout_26.addWidget(self.frame_filedialog)

        self.main_tab_widget.addWidget(self.panel_filedialog)
        self.panel_origin_offsets = QWidget()
        self.panel_origin_offsets.setObjectName(u"panel_origin_offsets")
        sizePolicy6.setHeightForWidth(self.panel_origin_offsets.sizePolicy().hasHeightForWidth())
        self.panel_origin_offsets.setSizePolicy(sizePolicy6)
        self.verticalLayout_29 = QVBoxLayout(self.panel_origin_offsets)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_origin_offsets = QFrame(self.panel_origin_offsets)
        self.frame_origin_offsets.setObjectName(u"frame_origin_offsets")
        sizePolicy2.setHeightForWidth(self.frame_origin_offsets.sizePolicy().hasHeightForWidth())
        self.frame_origin_offsets.setSizePolicy(sizePolicy2)
        self.frame_origin_offsets.setFrameShape(QFrame.StyledPanel)
        self.frame_origin_offsets.setFrameShadow(QFrame.Raised)
        self.gridLayout_32 = QGridLayout(self.frame_origin_offsets)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.offset_table = OriginOffsetView(self.frame_origin_offsets)
        self.offset_table.setObjectName(u"offset_table")
        self.offset_table.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.offset_table.sizePolicy().hasHeightForWidth())
        self.offset_table.setSizePolicy(sizePolicy2)
        self.offset_table.setMinimumSize(QSize(0, 0))
        self.offset_table.setStyleSheet(u"font: 11pt \"Ubuntu\";")
        self.offset_table.setAlternatingRowColors(False)
        self.offset_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.offset_table.horizontalHeader().setMinimumSectionSize(75)
        self.offset_table.verticalHeader().setMinimumSectionSize(16)
        self.offset_table.verticalHeader().setDefaultSectionSize(26)

        self.gridLayout_32.addWidget(self.offset_table, 0, 0, 1, 1)

        self.frame_12 = QFrame(self.frame_origin_offsets)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy1.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy1)
        self.frame_12.setMinimumSize(QSize(81, 0))
        self.frame_12.setFrameShape(QFrame.WinPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.widget_zero_offsets = QWidget(self.frame_12)
        self.widget_zero_offsets.setObjectName(u"widget_zero_offsets")
        self.widget_zero_offsets.setGeometry(QRect(0, 0, 81, 361))
        self.verticalLayout_38 = QVBoxLayout(self.widget_zero_offsets)
        self.verticalLayout_38.setSpacing(4)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(4, 4, 4, 4)
        self.action_zero_rotation = ActionButton(self.widget_zero_offsets)
        self.action_zero_rotation.setObjectName(u"action_zero_rotation")
        sizePolicy.setHeightForWidth(self.action_zero_rotation.sizePolicy().hasHeightForWidth())
        self.action_zero_rotation.setSizePolicy(sizePolicy)
        self.action_zero_rotation.setMinimumSize(QSize(70, 50))
        self.action_zero_rotation.setMaximumSize(QSize(70, 50))
        self.action_zero_rotation.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.action_zero_rotation.setProperty("zero_zrot_action", True)

        self.verticalLayout_38.addWidget(self.action_zero_rotation)

        self.action_zero_g92 = ActionButton(self.widget_zero_offsets)
        self.action_zero_g92.setObjectName(u"action_zero_g92")
        sizePolicy.setHeightForWidth(self.action_zero_g92.sizePolicy().hasHeightForWidth())
        self.action_zero_g92.setSizePolicy(sizePolicy)
        self.action_zero_g92.setMinimumSize(QSize(70, 50))
        self.action_zero_g92.setMaximumSize(QSize(70, 50))
        self.action_zero_g92.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.action_zero_g92.setProperty("zero_g92_action", True)
        self.action_zero_g92.setProperty("template_label_option", False)
        self.action_zero_g92.setProperty("joint_number", 0)
        self.action_zero_g92.setProperty("incr_imperial_number", 0.010000000000000)
        self.action_zero_g92.setProperty("incr_mm_number", 0.025000000000000)
        self.action_zero_g92.setProperty("incr_angular_number", -1.000000000000000)
        self.action_zero_g92.setProperty("toggle_float_option", False)
        self.action_zero_g92.setProperty("float_num", 100.000000000000000)
        self.action_zero_g92.setProperty("float_alt_num", 50.000000000000000)
        self.action_zero_g92.setProperty("ini_mdi_number", 0)

        self.verticalLayout_38.addWidget(self.action_zero_g92)

        self.action_zero_g5x = ActionButton(self.widget_zero_offsets)
        self.action_zero_g5x.setObjectName(u"action_zero_g5x")
        sizePolicy.setHeightForWidth(self.action_zero_g5x.sizePolicy().hasHeightForWidth())
        self.action_zero_g5x.setSizePolicy(sizePolicy)
        self.action_zero_g5x.setMinimumSize(QSize(70, 50))
        self.action_zero_g5x.setMaximumSize(QSize(70, 50))
        self.action_zero_g5x.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.action_zero_g5x.setProperty("zero_g5x_action", True)

        self.verticalLayout_38.addWidget(self.action_zero_g5x)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_38.addItem(self.verticalSpacer_11)


        self.gridLayout_32.addWidget(self.frame_12, 0, 1, 1, 1)


        self.verticalLayout_29.addWidget(self.frame_origin_offsets)

        self.main_tab_widget.addWidget(self.panel_origin_offsets)
        self.panel_tool_offsets = QWidget()
        self.panel_tool_offsets.setObjectName(u"panel_tool_offsets")
        self.verticalLayout_39 = QVBoxLayout(self.panel_tool_offsets)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.frame_tool_offsets = QFrame(self.panel_tool_offsets)
        self.frame_tool_offsets.setObjectName(u"frame_tool_offsets")
        self.frame_tool_offsets.setFrameShape(QFrame.StyledPanel)
        self.frame_tool_offsets.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_tool_offsets)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.tooloffsetview = ToolOffsetView(self.frame_tool_offsets)
        self.tooloffsetview.setObjectName(u"tooloffsetview")
        self.tooloffsetview.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.tooloffsetview.sizePolicy().hasHeightForWidth())
        self.tooloffsetview.setSizePolicy(sizePolicy2)
        self.tooloffsetview.setStyleSheet(u"font: 11pt \"Ubuntu\";")
        self.tooloffsetview.setAlternatingRowColors(False)

        self.verticalLayout_45.addWidget(self.tooloffsetview)


        self.verticalLayout_39.addWidget(self.frame_tool_offsets)

        self.main_tab_widget.addWidget(self.panel_tool_offsets)
        self.panel_gcode_edit = QWidget()
        self.panel_gcode_edit.setObjectName(u"panel_gcode_edit")
        sizePolicy6.setHeightForWidth(self.panel_gcode_edit.sizePolicy().hasHeightForWidth())
        self.panel_gcode_edit.setSizePolicy(sizePolicy6)
        self.verticalLayout_46 = QVBoxLayout(self.panel_gcode_edit)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.panel_gcode_edit)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.gridLayout_33 = QGridLayout(self.frame_29)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.stackedWidget_log = QStackedWidget(self.frame_29)
        self.stackedWidget_log.setObjectName(u"stackedWidget_log")
        self.stackedWidget_log.setFrameShape(QFrame.WinPanel)
        self.stackedWidget_log.setFrameShadow(QFrame.Sunken)
        self.page_machine = QWidget()
        self.page_machine.setObjectName(u"page_machine")
        self.horizontalLayout_21 = QHBoxLayout(self.page_machine)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.machinelog = MachineLog(self.page_machine)
        self.machinelog.setObjectName(u"machinelog")
        sizePolicy2.setHeightForWidth(self.machinelog.sizePolicy().hasHeightForWidth())
        self.machinelog.setSizePolicy(sizePolicy2)
        self.machinelog.setFrameShape(QFrame.NoFrame)
        self.machinelog.setFrameShadow(QFrame.Plain)
        self.machinelog.setReadOnly(True)

        self.horizontalLayout_21.addWidget(self.machinelog)

        self.stackedWidget_log.addWidget(self.page_machine)
        self.page_integrator = QWidget()
        self.page_integrator.setObjectName(u"page_integrator")
        self.horizontalLayout_22 = QHBoxLayout(self.page_integrator)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.integrator_log = MachineLog(self.page_integrator)
        self.integrator_log.setObjectName(u"integrator_log")
        sizePolicy2.setHeightForWidth(self.integrator_log.sizePolicy().hasHeightForWidth())
        self.integrator_log.setSizePolicy(sizePolicy2)
        self.integrator_log.setMinimumSize(QSize(0, 0))
        self.integrator_log.setStyleSheet(u"font: 11pt \"Ubuntu\";")
        self.integrator_log.setFrameShape(QFrame.NoFrame)
        self.integrator_log.setFrameShadow(QFrame.Plain)
        self.integrator_log.setReadOnly(True)
        self.integrator_log.setProperty("integrator_log_option", True)

        self.horizontalLayout_22.addWidget(self.integrator_log)

        self.stackedWidget_log.addWidget(self.page_integrator)

        self.gridLayout_33.addWidget(self.stackedWidget_log, 0, 0, 1, 1)

        self.frame_31 = QFrame(self.frame_29)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(81, 0))
        self.frame_31.setFrameShape(QFrame.WinPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_31)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.widget_status_log = QWidget(self.frame_31)
        self.widget_status_log.setObjectName(u"widget_status_log")
        self.widget_status_log.setMinimumSize(QSize(81, 0))
        self.verticalLayout_47 = QVBoxLayout(self.widget_status_log)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(4, 0, 4, 0)
        self.btn_select_log = PushButton(self.widget_status_log)
        self.btn_select_log.setObjectName(u"btn_select_log")
        sizePolicy.setHeightForWidth(self.btn_select_log.sizePolicy().hasHeightForWidth())
        self.btn_select_log.setSizePolicy(sizePolicy)
        self.btn_select_log.setMinimumSize(QSize(70, 50))
        self.btn_select_log.setMaximumSize(QSize(60, 50))
        self.btn_select_log.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.btn_select_log.setCheckable(True)
        self.btn_select_log.setChecked(False)
        self.btn_select_log.setProperty("indicator_option", False)
        self.btn_select_log.setProperty("checked_state_text_option", True)
        self.btn_select_log.setProperty("python_command_option", True)
        self.btn_select_log.setProperty("on_color", QColor(0, 255, 0))

        self.verticalLayout_47.addWidget(self.btn_select_log)

        self.btn_clear_status = QPushButton(self.widget_status_log)
        self.btn_clear_status.setObjectName(u"btn_clear_status")
        sizePolicy.setHeightForWidth(self.btn_clear_status.sizePolicy().hasHeightForWidth())
        self.btn_clear_status.setSizePolicy(sizePolicy)
        self.btn_clear_status.setMinimumSize(QSize(70, 50))
        self.btn_clear_status.setMaximumSize(QSize(61, 50))
        self.btn_clear_status.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")

        self.verticalLayout_47.addWidget(self.btn_clear_status)

        self.btn_save_status = QPushButton(self.widget_status_log)
        self.btn_save_status.setObjectName(u"btn_save_status")
        sizePolicy.setHeightForWidth(self.btn_save_status.sizePolicy().hasHeightForWidth())
        self.btn_save_status.setSizePolicy(sizePolicy)
        self.btn_save_status.setMinimumSize(QSize(70, 50))
        self.btn_save_status.setMaximumSize(QSize(60, 50))
        self.btn_save_status.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")

        self.verticalLayout_47.addWidget(self.btn_save_status)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_47.addItem(self.verticalSpacer_13)


        self.gridLayout_5.addWidget(self.widget_status_log, 0, 0, 1, 1)


        self.gridLayout_33.addWidget(self.frame_31, 0, 1, 1, 1)


        self.verticalLayout_46.addWidget(self.frame_29)

        self.main_tab_widget.addWidget(self.panel_gcode_edit)
        self.panel_probing = QWidget()
        self.panel_probing.setObjectName(u"panel_probing")
        sizePolicy6.setHeightForWidth(self.panel_probing.sizePolicy().hasHeightForWidth())
        self.panel_probing.setSizePolicy(sizePolicy6)
        self.verticalLayout_49 = QVBoxLayout(self.panel_probing)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QFrame(self.panel_probing)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.gridLayout_34 = QGridLayout(self.frame_32)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.basicprobe = BasicProbe(self.frame_32)
        self.basicprobe.setObjectName(u"basicprobe")
        self.basicprobe.setMinimumSize(QSize(600, 397))

        self.gridLayout_34.addWidget(self.basicprobe, 0, 0, 1, 1)


        self.verticalLayout_49.addWidget(self.frame_32)

        self.main_tab_widget.addWidget(self.panel_probing)
        self.panel_macro = QWidget()
        self.panel_macro.setObjectName(u"panel_macro")
        self.verticalLayout_50 = QVBoxLayout(self.panel_macro)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.frame_macro_selection = QFrame(self.panel_macro)
        self.frame_macro_selection.setObjectName(u"frame_macro_selection")
        self.frame_macro_selection.setFrameShape(QFrame.WinPanel)
        self.frame_macro_selection.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_macro_selection)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.macrotab = MacroTab(self.frame_macro_selection)
        self.macrotab.setObjectName(u"macrotab")

        self.verticalLayout_53.addWidget(self.macrotab)


        self.verticalLayout_50.addWidget(self.frame_macro_selection)

        self.main_tab_widget.addWidget(self.panel_macro)
        self.panel_settings = QWidget()
        self.panel_settings.setObjectName(u"panel_settings")
        self.verticalLayout_52 = QVBoxLayout(self.panel_settings)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.frame_settings = QFrame(self.panel_settings)
        self.frame_settings.setObjectName(u"frame_settings")
        self.frame_settings.setFrameShape(QFrame.WinPanel)
        self.frame_settings.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_settings)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.frm_settings1 = QFrame(self.frame_settings)
        self.frm_settings1.setObjectName(u"frm_settings1")
        sizePolicy2.setHeightForWidth(self.frm_settings1.sizePolicy().hasHeightForWidth())
        self.frm_settings1.setSizePolicy(sizePolicy2)
        self.frm_settings1.setMaximumSize(QSize(16777215, 16777215))
        self.frm_settings1.setStyleSheet(u"")
        self.frm_settings1.setFrameShape(QFrame.WinPanel)
        self.frm_settings1.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frm_settings1)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_23 = QLabel(self.frm_settings1)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"font: 12pt \"Sans\";")
        self.label_23.setFrameShape(QFrame.NoFrame)
        self.label_23.setFrameShadow(QFrame.Raised)
        self.label_23.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_23, 0, 0, 1, 1)

        self.label_29 = QLabel(self.frm_settings1)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"font: 12pt \"Sans\";")

        self.gridLayout_13.addWidget(self.label_29, 1, 0, 1, 1)

        self.label_30 = QLabel(self.frm_settings1)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"font: 12pt \"Sans\";")

        self.gridLayout_13.addWidget(self.label_30, 2, 0, 1, 1)

        self.label_31 = QLabel(self.frm_settings1)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"font: 12pt \"Sans\";")

        self.gridLayout_13.addWidget(self.label_31, 3, 0, 1, 1)

        self.label_35 = QLabel(self.frm_settings1)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"font: 12pt \"Sans\";")

        self.gridLayout_13.addWidget(self.label_35, 4, 0, 1, 1)

        self.label_34 = QLabel(self.frm_settings1)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"font: 12pt \"Sans\";")

        self.gridLayout_13.addWidget(self.label_34, 5, 0, 1, 1)

        self.label_20 = QLabel(self.frm_settings1)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"font: 12pt \"Sans\";")

        self.gridLayout_13.addWidget(self.label_20, 6, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_2, 7, 0, 1, 1)

        self.chk_eoffsets = QCheckBox(self.frm_settings1)
        self.chk_eoffsets.setObjectName(u"chk_eoffsets")
        sizePolicy3.setHeightForWidth(self.chk_eoffsets.sizePolicy().hasHeightForWidth())
        self.chk_eoffsets.setSizePolicy(sizePolicy3)
        self.chk_eoffsets.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")

        self.gridLayout_13.addWidget(self.chk_eoffsets, 8, 0, 1, 1)

        self.chk_use_tool_sensor = QCheckBox(self.frm_settings1)
        self.chk_use_tool_sensor.setObjectName(u"chk_use_tool_sensor")
        sizePolicy3.setHeightForWidth(self.chk_use_tool_sensor.sizePolicy().hasHeightForWidth())
        self.chk_use_tool_sensor.setSizePolicy(sizePolicy3)
        self.chk_use_tool_sensor.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")

        self.gridLayout_13.addWidget(self.chk_use_tool_sensor, 9, 0, 1, 1)

        self.chk_use_camera = QCheckBox(self.frm_settings1)
        self.chk_use_camera.setObjectName(u"chk_use_camera")
        sizePolicy3.setHeightForWidth(self.chk_use_camera.sizePolicy().hasHeightForWidth())
        self.chk_use_camera.setSizePolicy(sizePolicy3)
        self.chk_use_camera.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")

        self.gridLayout_13.addWidget(self.chk_use_camera, 10, 0, 1, 1)

        self.chk_use_virtual = QCheckBox(self.frm_settings1)
        self.chk_use_virtual.setObjectName(u"chk_use_virtual")
        sizePolicy3.setHeightForWidth(self.chk_use_virtual.sizePolicy().hasHeightForWidth())
        self.chk_use_virtual.setSizePolicy(sizePolicy3)
        self.chk_use_virtual.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")

        self.gridLayout_13.addWidget(self.chk_use_virtual, 11, 0, 1, 1)

        self.chk_reload_tool = QCheckBox(self.frm_settings1)
        self.chk_reload_tool.setObjectName(u"chk_reload_tool")
        self.chk_reload_tool.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")

        self.gridLayout_13.addWidget(self.chk_reload_tool, 12, 0, 1, 1)

        self.chk_reload_program = QCheckBox(self.frm_settings1)
        self.chk_reload_program.setObjectName(u"chk_reload_program")
        self.chk_reload_program.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")

        self.gridLayout_13.addWidget(self.chk_reload_program, 13, 0, 1, 1)

        self.chk_use_keyboard = QCheckBox(self.frm_settings1)
        self.chk_use_keyboard.setObjectName(u"chk_use_keyboard")
        self.chk_use_keyboard.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")

        self.gridLayout_13.addWidget(self.chk_use_keyboard, 14, 0, 1, 1)

        self.chk_run_from_line = QCheckBox(self.frm_settings1)
        self.chk_run_from_line.setObjectName(u"chk_run_from_line")
        self.chk_run_from_line.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")

        self.gridLayout_13.addWidget(self.chk_run_from_line, 15, 0, 1, 1)

        self.chk_override_limits = QCheckBox(self.frm_settings1)
        self.chk_override_limits.setObjectName(u"chk_override_limits")
        self.chk_override_limits.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")

        self.gridLayout_13.addWidget(self.chk_override_limits, 16, 0, 1, 1)


        self.gridLayout_15.addWidget(self.frm_settings1, 0, 0, 1, 1)

        self.frm_settings2 = QFrame(self.frame_settings)
        self.frm_settings2.setObjectName(u"frm_settings2")
        self.frm_settings2.setFrameShape(QFrame.WinPanel)
        self.frm_settings2.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frm_settings2)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.widget_home_header = QWidget(self.frm_settings2)
        self.widget_home_header.setObjectName(u"widget_home_header")
        self.horizontalLayout_75 = QHBoxLayout(self.widget_home_header)
        self.horizontalLayout_75.setSpacing(4)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.label_73 = QLabel(self.widget_home_header)
        self.label_73.setObjectName(u"label_73")
        sizePolicy.setHeightForWidth(self.label_73.sizePolicy().hasHeightForWidth())
        self.label_73.setSizePolicy(sizePolicy)
        self.label_73.setMinimumSize(QSize(120, 30))
        self.label_73.setMaximumSize(QSize(120, 30))

        self.horizontalLayout_75.addWidget(self.label_73)

        self.label_38 = QLabel(self.widget_home_header)
        self.label_38.setObjectName(u"label_38")
        sizePolicy.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy)
        self.label_38.setMinimumSize(QSize(50, 30))
        self.label_38.setMaximumSize(QSize(50, 30))
        self.label_38.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_75.addWidget(self.label_38)

        self.label_39 = QLabel(self.widget_home_header)
        self.label_39.setObjectName(u"label_39")
        sizePolicy.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy)
        self.label_39.setMinimumSize(QSize(50, 30))
        self.label_39.setMaximumSize(QSize(50, 30))
        self.label_39.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_75.addWidget(self.label_39)


        self.gridLayout_14.addWidget(self.widget_home_header, 0, 0, 1, 1)

        self.widget_home_location = QWidget(self.frm_settings2)
        self.widget_home_location.setObjectName(u"widget_home_location")
        self.horizontalLayout_32 = QHBoxLayout(self.widget_home_location)
        self.horizontalLayout_32.setSpacing(4)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.widget_home_location)
        self.label_26.setObjectName(u"label_26")
        sizePolicy3.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy3)
        self.label_26.setMinimumSize(QSize(120, 30))
        self.label_26.setMaximumSize(QSize(120, 30))
        self.label_26.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")

        self.horizontalLayout_32.addWidget(self.label_26)

        self.lbl_home_x = QLineEdit(self.widget_home_location)
        self.lbl_home_x.setObjectName(u"lbl_home_x")
        sizePolicy.setHeightForWidth(self.lbl_home_x.sizePolicy().hasHeightForWidth())
        self.lbl_home_x.setSizePolicy(sizePolicy)
        self.lbl_home_x.setMinimumSize(QSize(70, 30))
        self.lbl_home_x.setMaximumSize(QSize(70, 30))
        self.lbl_home_x.setMaxLength(8)
        self.lbl_home_x.setAlignment(Qt.AlignCenter)
        self.lbl_home_x.setReadOnly(True)

        self.horizontalLayout_32.addWidget(self.lbl_home_x)

        self.lbl_home_y = QLineEdit(self.widget_home_location)
        self.lbl_home_y.setObjectName(u"lbl_home_y")
        sizePolicy.setHeightForWidth(self.lbl_home_y.sizePolicy().hasHeightForWidth())
        self.lbl_home_y.setSizePolicy(sizePolicy)
        self.lbl_home_y.setMinimumSize(QSize(70, 30))
        self.lbl_home_y.setMaximumSize(QSize(70, 30))
        self.lbl_home_y.setMaxLength(8)
        self.lbl_home_y.setAlignment(Qt.AlignCenter)
        self.lbl_home_y.setReadOnly(True)

        self.horizontalLayout_32.addWidget(self.lbl_home_y)


        self.gridLayout_14.addWidget(self.widget_home_location, 1, 0, 1, 1)

        self.widget_search_vel = QWidget(self.frm_settings2)
        self.widget_search_vel.setObjectName(u"widget_search_vel")
        self.horizontalLayout_76 = QHBoxLayout(self.widget_search_vel)
        self.horizontalLayout_76.setSpacing(4)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.widget_search_vel)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setMinimumSize(QSize(120, 30))
        self.label_6.setMaximumSize(QSize(120, 30))
        self.label_6.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_76.addWidget(self.label_6)

        self.lineEdit_search_vel = QLineEdit(self.widget_search_vel)
        self.lineEdit_search_vel.setObjectName(u"lineEdit_search_vel")
        sizePolicy.setHeightForWidth(self.lineEdit_search_vel.sizePolicy().hasHeightForWidth())
        self.lineEdit_search_vel.setSizePolicy(sizePolicy)
        self.lineEdit_search_vel.setMinimumSize(QSize(70, 30))
        self.lineEdit_search_vel.setMaximumSize(QSize(70, 30))
        self.lineEdit_search_vel.setMaxLength(8)
        self.lineEdit_search_vel.setAlignment(Qt.AlignCenter)
        self.lineEdit_search_vel.setReadOnly(False)

        self.horizontalLayout_76.addWidget(self.lineEdit_search_vel)

        self.lbl_search_vel_units = QLabel(self.widget_search_vel)
        self.lbl_search_vel_units.setObjectName(u"lbl_search_vel_units")
        sizePolicy.setHeightForWidth(self.lbl_search_vel_units.sizePolicy().hasHeightForWidth())
        self.lbl_search_vel_units.setSizePolicy(sizePolicy)
        self.lbl_search_vel_units.setMinimumSize(QSize(60, 30))
        self.lbl_search_vel_units.setMaximumSize(QSize(60, 30))
        self.lbl_search_vel_units.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.lbl_search_vel_units.setAlignment(Qt.AlignCenter)
        self.lbl_search_vel_units.setWordWrap(False)
        self.lbl_search_vel_units.setIndent(0)

        self.horizontalLayout_76.addWidget(self.lbl_search_vel_units)


        self.gridLayout_14.addWidget(self.widget_search_vel, 2, 0, 1, 1)

        self.widget_probe_vel = QWidget(self.frm_settings2)
        self.widget_probe_vel.setObjectName(u"widget_probe_vel")
        self.horizontalLayout_78 = QHBoxLayout(self.widget_probe_vel)
        self.horizontalLayout_78.setSpacing(4)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.widget_probe_vel)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setMinimumSize(QSize(120, 30))
        self.label_7.setMaximumSize(QSize(120, 30))
        self.label_7.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_78.addWidget(self.label_7)

        self.lineEdit_probe_vel = QLineEdit(self.widget_probe_vel)
        self.lineEdit_probe_vel.setObjectName(u"lineEdit_probe_vel")
        sizePolicy.setHeightForWidth(self.lineEdit_probe_vel.sizePolicy().hasHeightForWidth())
        self.lineEdit_probe_vel.setSizePolicy(sizePolicy)
        self.lineEdit_probe_vel.setMinimumSize(QSize(70, 30))
        self.lineEdit_probe_vel.setMaximumSize(QSize(70, 30))
        self.lineEdit_probe_vel.setMaxLength(8)
        self.lineEdit_probe_vel.setAlignment(Qt.AlignCenter)
        self.lineEdit_probe_vel.setReadOnly(False)

        self.horizontalLayout_78.addWidget(self.lineEdit_probe_vel)

        self.lbl_probe_vel_units = QLabel(self.widget_probe_vel)
        self.lbl_probe_vel_units.setObjectName(u"lbl_probe_vel_units")
        sizePolicy.setHeightForWidth(self.lbl_probe_vel_units.sizePolicy().hasHeightForWidth())
        self.lbl_probe_vel_units.setSizePolicy(sizePolicy)
        self.lbl_probe_vel_units.setMinimumSize(QSize(60, 30))
        self.lbl_probe_vel_units.setMaximumSize(QSize(60, 30))
        self.lbl_probe_vel_units.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.lbl_probe_vel_units.setAlignment(Qt.AlignCenter)
        self.lbl_probe_vel_units.setWordWrap(False)
        self.lbl_probe_vel_units.setIndent(0)

        self.horizontalLayout_78.addWidget(self.lbl_probe_vel_units)


        self.gridLayout_14.addWidget(self.widget_probe_vel, 3, 0, 1, 1)

        self.widget_max_probe = QWidget(self.frm_settings2)
        self.widget_max_probe.setObjectName(u"widget_max_probe")
        self.horizontalLayout_73 = QHBoxLayout(self.widget_max_probe)
        self.horizontalLayout_73.setSpacing(4)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_max_probe)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        self.label_4.setMinimumSize(QSize(120, 30))
        self.label_4.setMaximumSize(QSize(120, 30))
        self.label_4.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_73.addWidget(self.label_4)

        self.lineEdit_max_probe = QLineEdit(self.widget_max_probe)
        self.lineEdit_max_probe.setObjectName(u"lineEdit_max_probe")
        sizePolicy.setHeightForWidth(self.lineEdit_max_probe.sizePolicy().hasHeightForWidth())
        self.lineEdit_max_probe.setSizePolicy(sizePolicy)
        self.lineEdit_max_probe.setMinimumSize(QSize(70, 30))
        self.lineEdit_max_probe.setMaximumSize(QSize(70, 30))
        self.lineEdit_max_probe.setMaxLength(8)
        self.lineEdit_max_probe.setAlignment(Qt.AlignCenter)
        self.lineEdit_max_probe.setReadOnly(False)

        self.horizontalLayout_73.addWidget(self.lineEdit_max_probe)

        self.lbl_max_probe_units = QLabel(self.widget_max_probe)
        self.lbl_max_probe_units.setObjectName(u"lbl_max_probe_units")
        sizePolicy.setHeightForWidth(self.lbl_max_probe_units.sizePolicy().hasHeightForWidth())
        self.lbl_max_probe_units.setSizePolicy(sizePolicy)
        self.lbl_max_probe_units.setMinimumSize(QSize(60, 30))
        self.lbl_max_probe_units.setMaximumSize(QSize(60, 30))
        self.lbl_max_probe_units.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.lbl_max_probe_units.setAlignment(Qt.AlignCenter)
        self.lbl_max_probe_units.setWordWrap(False)
        self.lbl_max_probe_units.setIndent(0)

        self.horizontalLayout_73.addWidget(self.lbl_max_probe_units)


        self.gridLayout_14.addWidget(self.widget_max_probe, 4, 0, 1, 1)

        self.widget_ext_offset = QWidget(self.frm_settings2)
        self.widget_ext_offset.setObjectName(u"widget_ext_offset")
        self.horizontalLayout_77 = QHBoxLayout(self.widget_ext_offset)
        self.horizontalLayout_77.setSpacing(4)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_ext_offset)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setMinimumSize(QSize(120, 30))
        self.label_3.setMaximumSize(QSize(120, 30))
        self.label_3.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")

        self.horizontalLayout_77.addWidget(self.label_3)

        self.lineEdit_eoffset_count = QLineEdit(self.widget_ext_offset)
        self.lineEdit_eoffset_count.setObjectName(u"lineEdit_eoffset_count")
        sizePolicy.setHeightForWidth(self.lineEdit_eoffset_count.sizePolicy().hasHeightForWidth())
        self.lineEdit_eoffset_count.setSizePolicy(sizePolicy)
        self.lineEdit_eoffset_count.setMinimumSize(QSize(70, 30))
        self.lineEdit_eoffset_count.setMaximumSize(QSize(70, 30))
        self.lineEdit_eoffset_count.setMaxLength(8)
        self.lineEdit_eoffset_count.setAlignment(Qt.AlignCenter)
        self.lineEdit_eoffset_count.setReadOnly(False)

        self.horizontalLayout_77.addWidget(self.lineEdit_eoffset_count)

        self.label_33 = QLabel(self.widget_ext_offset)
        self.label_33.setObjectName(u"label_33")
        sizePolicy3.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy3)
        self.label_33.setMinimumSize(QSize(60, 30))
        self.label_33.setMaximumSize(QSize(60, 30))
        self.label_33.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.label_33.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_77.addWidget(self.label_33)


        self.gridLayout_14.addWidget(self.widget_ext_offset, 5, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_4, 6, 0, 1, 1)

        self.chk_alpha_mode = QCheckBox(self.frm_settings2)
        self.chk_alpha_mode.setObjectName(u"chk_alpha_mode")
        self.chk_alpha_mode.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")

        self.gridLayout_14.addWidget(self.chk_alpha_mode, 7, 0, 1, 1)

        self.chk_alpha_mode_2 = QCheckBox(self.frm_settings2)
        self.chk_alpha_mode_2.setObjectName(u"chk_alpha_mode_2")
        self.chk_alpha_mode_2.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")

        self.gridLayout_14.addWidget(self.chk_alpha_mode_2, 8, 0, 1, 1)


        self.gridLayout_15.addWidget(self.frm_settings2, 0, 1, 1, 1)

        self.silver_dragon = QLabel(self.frame_settings)
        self.silver_dragon.setObjectName(u"silver_dragon")
        self.silver_dragon.setMinimumSize(QSize(180, 0))
        self.silver_dragon.setFrameShape(QFrame.WinPanel)
        self.silver_dragon.setFrameShadow(QFrame.Raised)
        self.silver_dragon.setPixmap(QPixmap(u"images/woodpecker.png"))
        self.silver_dragon.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.silver_dragon, 0, 2, 1, 1)

        self.frm_settings4 = QFrame(self.frame_settings)
        self.frm_settings4.setObjectName(u"frm_settings4")
        sizePolicy1.setHeightForWidth(self.frm_settings4.sizePolicy().hasHeightForWidth())
        self.frm_settings4.setSizePolicy(sizePolicy1)
        self.frm_settings4.setMinimumSize(QSize(102, 450))
        self.frm_settings4.setFrameShape(QFrame.WinPanel)
        self.frm_settings4.setFrameShadow(QFrame.Raised)
        self.gridLayout_28 = QGridLayout(self.frm_settings4)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.actionbutton_calibration_2 = ActionButton(self.frm_settings4)
        self.actionbutton_calibration_2.setObjectName(u"actionbutton_calibration_2")
        self.actionbutton_calibration_2.setMinimumSize(QSize(90, 50))
        self.actionbutton_calibration_2.setMaximumSize(QSize(90, 50))
        self.actionbutton_calibration_2.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.actionbutton_calibration_2.setProperty("launch_calibration_action", True)

        self.gridLayout_28.addWidget(self.actionbutton_calibration_2, 3, 0, 1, 1)

        self.actionbutton_halshow_2 = ActionButton(self.frm_settings4)
        self.actionbutton_halshow_2.setObjectName(u"actionbutton_halshow_2")
        sizePolicy.setHeightForWidth(self.actionbutton_halshow_2.sizePolicy().hasHeightForWidth())
        self.actionbutton_halshow_2.setSizePolicy(sizePolicy)
        self.actionbutton_halshow_2.setMinimumSize(QSize(90, 50))
        self.actionbutton_halshow_2.setMaximumSize(QSize(90, 50))
        self.actionbutton_halshow_2.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.actionbutton_halshow_2.setProperty("launch_halshow_action", True)
        self.actionbutton_halshow_2.setProperty("template_label_option", False)
        self.actionbutton_halshow_2.setProperty("joint_number", 0)
        self.actionbutton_halshow_2.setProperty("incr_imperial_number", 0.010000000000000)
        self.actionbutton_halshow_2.setProperty("incr_mm_number", 0.025000000000000)
        self.actionbutton_halshow_2.setProperty("incr_angular_number", -1.000000000000000)
        self.actionbutton_halshow_2.setProperty("toggle_float_option", False)
        self.actionbutton_halshow_2.setProperty("float_num", 100.000000000000000)
        self.actionbutton_halshow_2.setProperty("float_alt_num", 50.000000000000000)
        self.actionbutton_halshow_2.setProperty("ini_mdi_number", 0)

        self.gridLayout_28.addWidget(self.actionbutton_halshow_2, 7, 0, 1, 1)

        self.actionbutton_halmeter_2 = ActionButton(self.frm_settings4)
        self.actionbutton_halmeter_2.setObjectName(u"actionbutton_halmeter_2")
        sizePolicy.setHeightForWidth(self.actionbutton_halmeter_2.sizePolicy().hasHeightForWidth())
        self.actionbutton_halmeter_2.setSizePolicy(sizePolicy)
        self.actionbutton_halmeter_2.setMinimumSize(QSize(90, 50))
        self.actionbutton_halmeter_2.setMaximumSize(QSize(90, 50))
        self.actionbutton_halmeter_2.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.actionbutton_halmeter_2.setProperty("launch_halmeter_action", True)
        self.actionbutton_halmeter_2.setProperty("template_label_option", False)
        self.actionbutton_halmeter_2.setProperty("joint_number", 0)
        self.actionbutton_halmeter_2.setProperty("incr_imperial_number", 0.010000000000000)
        self.actionbutton_halmeter_2.setProperty("incr_mm_number", 0.025000000000000)
        self.actionbutton_halmeter_2.setProperty("incr_angular_number", -1.000000000000000)
        self.actionbutton_halmeter_2.setProperty("toggle_float_option", False)
        self.actionbutton_halmeter_2.setProperty("float_num", 100.000000000000000)
        self.actionbutton_halmeter_2.setProperty("float_alt_num", 50.000000000000000)
        self.actionbutton_halmeter_2.setProperty("ini_mdi_number", 0)

        self.gridLayout_28.addWidget(self.actionbutton_halmeter_2, 6, 0, 1, 1)

        self.actionbutton_halscope_2 = ActionButton(self.frm_settings4)
        self.actionbutton_halscope_2.setObjectName(u"actionbutton_halscope_2")
        sizePolicy.setHeightForWidth(self.actionbutton_halscope_2.sizePolicy().hasHeightForWidth())
        self.actionbutton_halscope_2.setSizePolicy(sizePolicy)
        self.actionbutton_halscope_2.setMinimumSize(QSize(90, 50))
        self.actionbutton_halscope_2.setMaximumSize(QSize(90, 50))
        self.actionbutton_halscope_2.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.actionbutton_halscope_2.setProperty("launch_halscope_action", True)
        self.actionbutton_halscope_2.setProperty("template_label_option", False)
        self.actionbutton_halscope_2.setProperty("joint_number", 0)
        self.actionbutton_halscope_2.setProperty("incr_imperial_number", 0.010000000000000)
        self.actionbutton_halscope_2.setProperty("incr_mm_number", 0.025000000000000)
        self.actionbutton_halscope_2.setProperty("incr_angular_number", -1.000000000000000)
        self.actionbutton_halscope_2.setProperty("toggle_float_option", False)
        self.actionbutton_halscope_2.setProperty("float_num", 100.000000000000000)
        self.actionbutton_halscope_2.setProperty("float_alt_num", 50.000000000000000)
        self.actionbutton_halscope_2.setProperty("ini_mdi_number", 0)

        self.gridLayout_28.addWidget(self.actionbutton_halscope_2, 5, 0, 1, 1)

        self.widget_mb_errors = QWidget(self.frm_settings4)
        self.widget_mb_errors.setObjectName(u"widget_mb_errors")
        self.verticalLayout_37 = QVBoxLayout(self.widget_mb_errors)
        self.verticalLayout_37.setSpacing(4)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(2, 2, 2, 2)
        self.label_43 = QLabel(self.widget_mb_errors)
        self.label_43.setObjectName(u"label_43")
        sizePolicy.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy)
        self.label_43.setMinimumSize(QSize(80, 40))
        self.label_43.setMaximumSize(QSize(80, 40))
        self.label_43.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.label_43.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.label_43, 0, Qt.AlignHCenter)

        self.lbl_mb_errors = QLineEdit(self.widget_mb_errors)
        self.lbl_mb_errors.setObjectName(u"lbl_mb_errors")
        sizePolicy.setHeightForWidth(self.lbl_mb_errors.sizePolicy().hasHeightForWidth())
        self.lbl_mb_errors.setSizePolicy(sizePolicy)
        self.lbl_mb_errors.setMinimumSize(QSize(80, 30))
        self.lbl_mb_errors.setMaximumSize(QSize(80, 30))
        self.lbl_mb_errors.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_mb_errors.setReadOnly(True)

        self.verticalLayout_37.addWidget(self.lbl_mb_errors)


        self.gridLayout_28.addWidget(self.widget_mb_errors, 0, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_28.addItem(self.verticalSpacer_6, 2, 0, 1, 1)

        self.actionbutton_lcnc_status_2 = ActionButton(self.frm_settings4)
        self.actionbutton_lcnc_status_2.setObjectName(u"actionbutton_lcnc_status_2")
        sizePolicy.setHeightForWidth(self.actionbutton_lcnc_status_2.sizePolicy().hasHeightForWidth())
        self.actionbutton_lcnc_status_2.setSizePolicy(sizePolicy)
        self.actionbutton_lcnc_status_2.setMinimumSize(QSize(90, 50))
        self.actionbutton_lcnc_status_2.setMaximumSize(QSize(90, 50))
        self.actionbutton_lcnc_status_2.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.actionbutton_lcnc_status_2.setProperty("launch_status_action", True)
        self.actionbutton_lcnc_status_2.setProperty("template_label_option", False)
        self.actionbutton_lcnc_status_2.setProperty("joint_number", 0)
        self.actionbutton_lcnc_status_2.setProperty("incr_imperial_number", 0.010000000000000)
        self.actionbutton_lcnc_status_2.setProperty("incr_mm_number", 0.025000000000000)
        self.actionbutton_lcnc_status_2.setProperty("incr_angular_number", -1.000000000000000)
        self.actionbutton_lcnc_status_2.setProperty("toggle_float_option", False)
        self.actionbutton_lcnc_status_2.setProperty("float_num", 100.000000000000000)
        self.actionbutton_lcnc_status_2.setProperty("float_alt_num", 50.000000000000000)
        self.actionbutton_lcnc_status_2.setProperty("ini_mdi_number", 0)

        self.gridLayout_28.addWidget(self.actionbutton_lcnc_status_2, 4, 0, 1, 1)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setSpacing(2)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(-1, 0, -1, -1)
        self.label_59 = QLabel(self.frm_settings4)
        self.label_59.setObjectName(u"label_59")
        sizePolicy2.setHeightForWidth(self.label_59.sizePolicy().hasHeightForWidth())
        self.label_59.setSizePolicy(sizePolicy2)
        self.label_59.setMinimumSize(QSize(0, 24))
        self.label_59.setMaximumSize(QSize(16777215, 24))
        self.label_59.setStyleSheet(u"font: 75 12pt \"Bebas Kai\";")
        self.label_59.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_59)

        self.lbl_spindle_fault_2 = QLineEdit(self.frm_settings4)
        self.lbl_spindle_fault_2.setObjectName(u"lbl_spindle_fault_2")
        sizePolicy.setHeightForWidth(self.lbl_spindle_fault_2.sizePolicy().hasHeightForWidth())
        self.lbl_spindle_fault_2.setSizePolicy(sizePolicy)
        self.lbl_spindle_fault_2.setMinimumSize(QSize(80, 24))
        self.lbl_spindle_fault_2.setMaximumSize(QSize(80, 24))
        self.lbl_spindle_fault_2.setAlignment(Qt.AlignCenter)
        self.lbl_spindle_fault_2.setReadOnly(True)

        self.verticalLayout_30.addWidget(self.lbl_spindle_fault_2, 0, Qt.AlignHCenter)


        self.gridLayout_28.addLayout(self.verticalLayout_30, 1, 0, 1, 1)


        self.gridLayout_15.addWidget(self.frm_settings4, 0, 3, 1, 1)


        self.verticalLayout_52.addWidget(self.frame_settings)

        self.main_tab_widget.addWidget(self.panel_settings)
        self.panel_cam_view = QWidget()
        self.panel_cam_view.setObjectName(u"panel_cam_view")
        self.horizontalLayout_23 = QHBoxLayout(self.panel_cam_view)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_cam_view = QFrame(self.panel_cam_view)
        self.frame_cam_view.setObjectName(u"frame_cam_view")
        self.frame_cam_view.setFrameShape(QFrame.WinPanel)
        self.frame_cam_view.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_cam_view)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.camview = CamView(self.frame_cam_view)
        self.camview.setObjectName(u"camview")
        sizePolicy6.setHeightForWidth(self.camview.sizePolicy().hasHeightForWidth())
        self.camview.setSizePolicy(sizePolicy6)

        self.horizontalLayout_26.addWidget(self.camview)

        self.widget_cam_controls = QWidget(self.frame_cam_view)
        self.widget_cam_controls.setObjectName(u"widget_cam_controls")
        sizePolicy1.setHeightForWidth(self.widget_cam_controls.sizePolicy().hasHeightForWidth())
        self.widget_cam_controls.setSizePolicy(sizePolicy1)
        self.verticalLayout_54 = QVBoxLayout(self.widget_cam_controls)
        self.verticalLayout_54.setSpacing(4)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 8, 0, 8)
        self.label_95 = QLabel(self.widget_cam_controls)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setMaximumSize(QSize(16777215, 20))
        self.label_95.setAlignment(Qt.AlignCenter)

        self.verticalLayout_54.addWidget(self.label_95)

        self.cam_zoom = QSlider(self.widget_cam_controls)
        self.cam_zoom.setObjectName(u"cam_zoom")
        sizePolicy1.setHeightForWidth(self.cam_zoom.sizePolicy().hasHeightForWidth())
        self.cam_zoom.setSizePolicy(sizePolicy1)
        self.cam_zoom.setMinimumSize(QSize(30, 120))
        self.cam_zoom.setMaximumSize(QSize(30, 16777215))
        self.cam_zoom.setStyleSheet(u"QSlider::groove:vertical {\n"
"border: 1px solid #bbb;\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"width: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"background: white;\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal  {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"width: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:vertical  {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 2"
                        "55, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"height: 30px;\n"
"margin-top: -1.3px;\n"
"margin-bottom: -1.3px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #444;\n"
"border-color: rgb(241, 239, 237);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
""
                        "}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.cam_zoom.setMinimum(10)
        self.cam_zoom.setMaximum(50)
        self.cam_zoom.setOrientation(Qt.Vertical)

        self.verticalLayout_54.addWidget(self.cam_zoom, 0, Qt.AlignHCenter)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_54.addItem(self.verticalSpacer_22)

        self.label_96 = QLabel(self.widget_cam_controls)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setMaximumSize(QSize(16777215, 20))
        self.label_96.setAlignment(Qt.AlignCenter)

        self.verticalLayout_54.addWidget(self.label_96)

        self.cam_diameter = QSlider(self.widget_cam_controls)
        self.cam_diameter.setObjectName(u"cam_diameter")
        sizePolicy1.setHeightForWidth(self.cam_diameter.sizePolicy().hasHeightForWidth())
        self.cam_diameter.setSizePolicy(sizePolicy1)
        self.cam_diameter.setMinimumSize(QSize(30, 120))
        self.cam_diameter.setMaximumSize(QSize(30, 16777215))
        self.cam_diameter.setStyleSheet(u"QSlider::groove:vertical {\n"
"border: 1px solid #bbb;\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"width: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"background: white;\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal  {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"width: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:vertical  {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 2"
                        "55, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"height: 30px;\n"
"margin-top: -1.3px;\n"
"margin-bottom: -1.3px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #444;\n"
"border-color: rgb(241, 239, 237);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
""
                        "}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.cam_diameter.setMinimum(20)
        self.cam_diameter.setMaximum(100)
        self.cam_diameter.setSingleStep(2)
        self.cam_diameter.setOrientation(Qt.Vertical)

        self.verticalLayout_54.addWidget(self.cam_diameter, 0, Qt.AlignHCenter)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_54.addItem(self.verticalSpacer_23)

        self.label_97 = QLabel(self.widget_cam_controls)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setMaximumSize(QSize(16777215, 20))
        self.label_97.setAlignment(Qt.AlignCenter)

        self.verticalLayout_54.addWidget(self.label_97)

        self.cam_rotate = QSlider(self.widget_cam_controls)
        self.cam_rotate.setObjectName(u"cam_rotate")
        sizePolicy1.setHeightForWidth(self.cam_rotate.sizePolicy().hasHeightForWidth())
        self.cam_rotate.setSizePolicy(sizePolicy1)
        self.cam_rotate.setMinimumSize(QSize(30, 120))
        self.cam_rotate.setMaximumSize(QSize(30, 16777215))
        self.cam_rotate.setStyleSheet(u"QSlider::groove:vertical {\n"
"border: 1px solid #bbb;\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"width: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"background: white;\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal  {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"width: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:vertical  {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 2"
                        "55, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"height: 30px;\n"
"margin-top: -1.3px;\n"
"margin-bottom: -1.3px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #444;\n"
"border-color: rgb(241, 239, 237);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
""
                        "}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.cam_rotate.setMaximum(900)
        self.cam_rotate.setOrientation(Qt.Vertical)

        self.verticalLayout_54.addWidget(self.cam_rotate, 0, Qt.AlignHCenter)


        self.horizontalLayout_26.addWidget(self.widget_cam_controls)


        self.horizontalLayout_23.addWidget(self.frame_cam_view)

        self.main_tab_widget.addWidget(self.panel_cam_view)
        self.panel_setup = QWidget()
        self.panel_setup.setObjectName(u"panel_setup")
        self.verticalLayout_59 = QVBoxLayout(self.panel_setup)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_setup = QVBoxLayout()
        self.verticalLayout_setup.setObjectName(u"verticalLayout_setup")

        self.verticalLayout_59.addLayout(self.verticalLayout_setup)

        self.main_tab_widget.addWidget(self.panel_setup)
        self.page_mdi_touchy = QWidget()
        self.page_mdi_touchy.setObjectName(u"page_mdi_touchy")
        self.frame_mdi_touchy = QFrame(self.page_mdi_touchy)
        self.frame_mdi_touchy.setObjectName(u"frame_mdi_touchy")
        self.frame_mdi_touchy.setGeometry(QRect(10, 0, 781, 491))
        self.frame_mdi_touchy.setFrameShape(QFrame.StyledPanel)
        self.frame_mdi_touchy.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_mdi_touchy)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.mditouchy = MDITouchy(self.frame_mdi_touchy)
        self.mditouchy.setObjectName(u"mditouchy")
        sizePolicy3.setHeightForWidth(self.mditouchy.sizePolicy().hasHeightForWidth())
        self.mditouchy.setSizePolicy(sizePolicy3)
        self.mditouchy.setMinimumSize(QSize(600, 400))
        self.mditouchy.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_16.addWidget(self.mditouchy, 0, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_24 = QFrame(self.frame_mdi_touchy)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy2.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy2)
        self.frame_24.setMinimumSize(QSize(500, 0))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.state_enable_gridLayout = StateEnableGridLayout(self.frame_24)
        self.state_enable_gridLayout.setObjectName(u"state_enable_gridLayout")
        self.state_enable_gridLayout.setGeometry(QRect(170, 10, 80, 41))
        self.state_enable_gridLayout.setMinimumSize(QSize(80, 41))
        self.state_enable_gridLayout.setMaximumSize(QSize(80, 41))
        self.state_enable_gridLayout.setProperty("is_on_status", True)
        self.state_enable_gridLayout.setProperty("is_idle_status", True)
        self.runFromLineButton = PushButton(self.state_enable_gridLayout)
        self.runFromLineButton.setObjectName(u"runFromLineButton")
        self.runFromLineButton.setGeometry(QRect(0, 0, 80, 41))
        sizePolicy.setHeightForWidth(self.runFromLineButton.sizePolicy().hasHeightForWidth())
        self.runFromLineButton.setSizePolicy(sizePolicy)
        self.runFromLineButton.setMinimumSize(QSize(80, 40))
        self.line_number = QLabel(self.frame_24)
        self.line_number.setObjectName(u"line_number")
        self.line_number.setGeometry(QRect(270, 0, 108, 25))
        sizePolicy.setHeightForWidth(self.line_number.sizePolicy().hasHeightForWidth())
        self.line_number.setSizePolicy(sizePolicy)
        self.line_number.setMinimumSize(QSize(108, 25))
        self.line_number.setMaximumSize(QSize(108, 25))
        self.line_number.setStyleSheet(u"font: 12pt \"Sans\";")
        self.line_number.setAlignment(Qt.AlignCenter)
        self.runFromLineEdit = QLineEdit(self.frame_24)
        self.runFromLineEdit.setObjectName(u"runFromLineEdit")
        self.runFromLineEdit.setGeometry(QRect(270, 30, 108, 24))
        sizePolicy.setHeightForWidth(self.runFromLineEdit.sizePolicy().hasHeightForWidth())
        self.runFromLineEdit.setSizePolicy(sizePolicy)
        self.runFromLineEdit.setMinimumSize(QSize(108, 24))
        self.runFromLineEdit.setMaxLength(8)
        self.btn_rezet = PushButton(self.frame_24)
        self.btn_rezet.setObjectName(u"btn_rezet")
        self.btn_rezet.setGeometry(QRect(420, 10, 80, 41))
        sizePolicy.setHeightForWidth(self.btn_rezet.sizePolicy().hasHeightForWidth())
        self.btn_rezet.setSizePolicy(sizePolicy)
        self.btn_rezet.setMinimumSize(QSize(80, 41))
        self.btn_rezet.setStyleSheet(u"font: 12pt \"Sans\";")
        self.btn_start_macro = PushButton(self.frame_24)
        self.btn_start_macro.setObjectName(u"btn_start_macro")
        self.btn_start_macro.setGeometry(QRect(550, 10, 80, 41))
        sizePolicy.setHeightForWidth(self.btn_start_macro.sizePolicy().hasHeightForWidth())
        self.btn_start_macro.setSizePolicy(sizePolicy)
        self.btn_start_macro.setMinimumSize(QSize(80, 41))
        self.btn_start_macro.setStyleSheet(u"font: 12pt \"Sans\";")

        self.horizontalLayout_6.addWidget(self.frame_24)


        self.gridLayout_16.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)

        self.main_tab_widget.addWidget(self.page_mdi_touchy)
        self.page_gcode = QWidget()
        self.page_gcode.setObjectName(u"page_gcode")
        self.frame_33 = QFrame(self.page_gcode)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setGeometry(QRect(-1, -1, 791, 491))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.gridLayout_36 = QGridLayout(self.frame_33)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.verticalLayout_60 = QVBoxLayout()
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.gcode_list = QListWidget(self.frame_33)
        self.gcode_list.setObjectName(u"gcode_list")
        self.gcode_list.setStyleSheet(u"font: 11pt \"Ubuntu\";")
        self.gcode_list.setFrameShape(QFrame.Box)
        self.gcode_list.setFrameShadow(QFrame.Raised)
        self.gcode_list.setSelectionMode(QAbstractItemView.SingleSelection)

        self.verticalLayout_60.addWidget(self.gcode_list)


        self.gridLayout_36.addLayout(self.verticalLayout_60, 0, 0, 1, 1)

        self.verticalLayout_61 = QVBoxLayout()
        self.verticalLayout_61.setSpacing(2)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, -1, 0, -1)
        self.gcode_parameters = QLineEdit(self.frame_33)
        self.gcode_parameters.setObjectName(u"gcode_parameters")
        sizePolicy2.setHeightForWidth(self.gcode_parameters.sizePolicy().hasHeightForWidth())
        self.gcode_parameters.setSizePolicy(sizePolicy2)
        self.gcode_parameters.setMinimumSize(QSize(0, 30))
        self.gcode_parameters.setBaseSize(QSize(0, 30))
        self.gcode_parameters.setStyleSheet(u"font: 13pt \"Ubuntu\";")
        self.gcode_parameters.setAlignment(Qt.AlignCenter)
        self.gcode_parameters.setReadOnly(True)

        self.verticalLayout_61.addWidget(self.gcode_parameters)

        self.gcode_description = QPlainTextEdit(self.frame_33)
        self.gcode_description.setObjectName(u"gcode_description")
        self.gcode_description.setStyleSheet(u"font: 11pt \"Ubuntu\";")
        self.gcode_description.setFrameShape(QFrame.Box)
        self.gcode_description.setFrameShadow(QFrame.Raised)

        self.verticalLayout_61.addWidget(self.gcode_description)


        self.gridLayout_36.addLayout(self.verticalLayout_61, 0, 1, 1, 1)

        self.main_tab_widget.addWidget(self.page_gcode)
        self.main_tab_widgetPage13 = QWidget()
        self.main_tab_widgetPage13.setObjectName(u"main_tab_widgetPage13")
        self.tabWidget_utilities = QTabWidget(self.main_tab_widgetPage13)
        self.tabWidget_utilities.setObjectName(u"tabWidget_utilities")
        self.tabWidget_utilities.setGeometry(QRect(10, 0, 781, 491))
        sizePolicy2.setHeightForWidth(self.tabWidget_utilities.sizePolicy().hasHeightForWidth())
        self.tabWidget_utilities.setSizePolicy(sizePolicy2)
        self.facing = QWidget()
        self.facing.setObjectName(u"facing")
        self.layout_facing = QVBoxLayout(self.facing)
        self.layout_facing.setSpacing(0)
        self.layout_facing.setObjectName(u"layout_facing")
        self.layout_facing.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_utilities.addTab(self.facing, "")
        self.hole_circle = QWidget()
        self.hole_circle.setObjectName(u"hole_circle")
        self.layout_hole_circle = QVBoxLayout(self.hole_circle)
        self.layout_hole_circle.setSpacing(0)
        self.layout_hole_circle.setObjectName(u"layout_hole_circle")
        self.layout_hole_circle.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_utilities.addTab(self.hole_circle, "")
        self.calculator = QWidget()
        self.calculator.setObjectName(u"calculator")
        self.layout_calculator = QVBoxLayout(self.calculator)
        self.layout_calculator.setSpacing(0)
        self.layout_calculator.setObjectName(u"layout_calculator")
        self.layout_calculator.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_utilities.addTab(self.calculator, "")
        self.main_tab_widget.addWidget(self.main_tab_widgetPage13)

        self.verticalLayout_24.addWidget(self.main_tab_widget)


        self.verticalLayout_3.addWidget(self.widget)

        self.stackedWidget_0.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.widgetswitcher = WidgetSwitcher(self.page_2)
        self.widgetswitcher.setObjectName(u"widgetswitcher")
        self.widgetswitcher.setGeometry(QRect(10, 10, 1191, 841))
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_15 = QVBoxLayout(self.page_1)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")

        self.verticalLayout_15.addLayout(self.verticalLayout_17)

        self.widgetswitcher.addWidget(self.page_1)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_18 = QVBoxLayout(self.page_3)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")

        self.verticalLayout_18.addLayout(self.verticalLayout_21)

        self.widgetswitcher.addWidget(self.page_3)
        self.stackedWidget_0.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btn_full.toggled.connect(MainWindow.full_screen)
        self.spindle_pause.clicked.connect(MainWindow.disable_pause_buttons)
        self.gcodegraphics.percentLoaded.connect(MainWindow.percentLoaded)
        self.gcode_viewer.percentDone.connect(MainWindow.percentLoaded)
        self.gcode_viewer.percentDone.connect(self.progressBar.setValue)
        self.chk_use_virtual.stateChanged.connect(MainWindow.chk_use_virtual_changed)
        self.chk_use_camera.stateChanged.connect(MainWindow.chk_use_camera_changed)
        self.chk_use_tool_sensor.stateChanged.connect(MainWindow.chk_use_tool_sensor_changed)
        self.chk_override_limits.clicked.connect(MainWindow.chk_override_limits_checked)
        self.chk_alpha_mode.clicked.connect(MainWindow.chk_alpha_mode_clicked)
        self.chk_alpha_mode_2.clicked.connect(MainWindow.chk_inhibit_display_selection_clicked)
        self.cam_zoom.valueChanged.connect(MainWindow.cam_zoom_changed)
        self.cam_diameter.valueChanged.connect(MainWindow.cam_dia_changed)
        self.cam_rotate.valueChanged.connect(MainWindow.cam_rot_changed)
        self.btn_touch_sensor.clicked.connect(MainWindow.btn_touchoff_clicked)
        self.btn_touchplate.clicked.connect(MainWindow.btn_touchoff_clicked)
        self.btn_ref_camera.clicked.connect(MainWindow.btn_ref_camera_clicked)
        self.btn_ref_laser.clicked.connect(MainWindow.btn_ref_laser_clicked)
        self.btn_goto_sensor.clicked.connect(MainWindow.btn_goto_sensor_clicked)
        self.btn_m61.clicked.connect(MainWindow.btn_m61_clicked)
        self.btn_start_macro.clicked.connect(MainWindow.btn_start_macro_clicked)
        self.btn_rezet.clicked.connect(self.runFromLineEdit.clear)
        self.btn_dimensions.clicked.connect(MainWindow.btn_dimensions_clicked)
        self.btn_jog_a_slow.clicked.connect(MainWindow.slow_button_clicked)
        self.btn_jog_l_slow.clicked.connect(MainWindow.slow_button_clicked)
        self.action_step.clicked.connect(MainWindow.disable_spindle_pause)
        self.action_pause.clicked.connect(MainWindow.disable_spindle_pause)
        self.action_abort.clicked.connect(MainWindow.disable_spindle_pause)
        self.action_abort.clicked.connect(self.progressBar.reset)
        self.btn_gcode_edit.clicked.connect(MainWindow.btn_gcode_edit_clicked)
        self.btn_clear_status.clicked.connect(MainWindow.btn_clear_status_clicked)
        self.btn_save_status.clicked.connect(MainWindow.btn_save_status_clicked)
        self.btn_home_x.clicked.connect(MainWindow.btn_home_clicked)
        self.btn_home_y.clicked.connect(MainWindow.btn_home_clicked)
        self.btn_home_z.clicked.connect(MainWindow.btn_home_clicked)
        self.btn_file_load.clicked.connect(MainWindow.btn_load_file_clicked)
        self.main_tab_widget.currentChanged.connect(MainWindow.switch)
        self.slider_rapid_ovr.valueChanged.connect(MainWindow.slider_rapid_changed)
        self.slider_maxv_ovr.valueChanged.connect(MainWindow.slider_maxv_changed)
        self.pushbutton_fo.clicked.connect(MainWindow.updateJogState)
        self.pushbutton_jog.clicked.connect(MainWindow.updateJogState)
        self.pushbutton_ro.clicked.connect(MainWindow.updateJogState)
        self.pushbutton_so.clicked.connect(MainWindow.updateJogState)
        self.axistoolbutton.clicked.connect(MainWindow.updateJogState)
        self.axistoolbutton_2.clicked.connect(MainWindow.updateJogState)
        self.axistoolbutton_3.clicked.connect(MainWindow.updateJogState)
        self.axistoolbutton_4.clicked.connect(MainWindow.updateJogState)
        self.btn_spindle_slover.clicked.connect(MainWindow.spindle_slover)
        self.btn_spindle_faster.clicked.connect(MainWindow.spindle_faster)
        self.btn_setdro.clicked.connect(MainWindow.btn_setdro_clicked)
        self.btn_show_offset.clicked.connect(MainWindow.btn_show_offset_clicked)
        self.runFromLineButton.clicked.connect(MainWindow.runFromLineClicked)
        self.btn_reload_file.clicked.connect(MainWindow.btn_reload_file_clicked)

        self.stackedWidget_0.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        self.stackedWidget_4.setCurrentIndex(0)
        self.stackedWidget_5.setCurrentIndex(1)
        self.widgetswitcher_2.setCurrentIndex(0)
        self.main_tab_widget.setCurrentIndex(0)
        self.stackedWidget_log.setCurrentIndex(1)
        self.tabWidget_utilities.setCurrentIndex(0)
        self.widgetswitcher.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.screen_options.setProperty("pref_filename_string", QCoreApplication.translate("MainWindow", u"~/.qtvcp_screen_preferences", None))
        self.action_machine_on.setText(QCoreApplication.translate("MainWindow", u"POWER\n"
"OFF", None))
        self.action_machine_on.setProperty("true_state_string", QCoreApplication.translate("MainWindow", u"POWER\n"
"ON", None))
        self.action_machine_on.setProperty("false_state_string", QCoreApplication.translate("MainWindow", u"POWER\n"
"OFF", None))
        self.action_machine_on.setProperty("true_python_cmd_string", "")
        self.action_machine_on.setProperty("false_python_cmd_string", "")
        self.action_machine_on.setProperty("command_text_string", "")
        self.manual_mode_button.setText(QCoreApplication.translate("MainWindow", u"MAN", None))
        self.manual_mode_button.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"INSTANCE.stackedWidget_4.setCurrentIndex(0)", None))
        self.manual_mode_button.setProperty("false_python_cmd_string", "")
        self.abtn_mainv_mode_mdi.setText(QCoreApplication.translate("MainWindow", u"MDI", None))
        self.abtn_mainv_mode_mdi.setProperty("true_state_string", "")
        self.abtn_mainv_mode_mdi.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"INSTANCE.stackedWidget_4.setCurrentIndex(2)", None))
        self.abtn_mainv_mode_mdi.setProperty("false_python_cmd_string", "")
        self.abtn_mainv_mode_auto.setText(QCoreApplication.translate("MainWindow", u"AUTO", None))
        self.abtn_mainv_mode_auto.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"INSTANCE.stackedWidget_4.setCurrentIndex(3)", None))
        self.abtn_mainv_mode_auto.setProperty("false_python_cmd_string", "")
        self.pbtn_mainv_spare_2.setText(QCoreApplication.translate("MainWindow", u"SPARE-2", None))
        self.pbtn_mainv_spare_1.setText(QCoreApplication.translate("MainWindow", u"SPARE-1", None))
        self.btn_full.setText(QCoreApplication.translate("MainWindow", u"Full", None))
        self.btn_keyboard.setText(QCoreApplication.translate("MainWindow", u"KEY\n"
"BOARD", None))
        self.btn_keyboard.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"INSTANCE.stackedWidget_2.setCurrentIndex(1)", None))
        self.btn_keyboard.setProperty("false_python_cmd_string", QCoreApplication.translate("MainWindow", u"INSTANCE.stackedWidget_2.setCurrentIndex(0)", None))
        self.actionbutton_2.setText("")
        self.btn_accessories.setText(QCoreApplication.translate("MainWindow", u"UTILS", None))
        self.btn_handwheel_spare.setText(QCoreApplication.translate("MainWindow", u"HAND\n"
"WHEEL", None))
        self.btn_handwheel_spare.setProperty("true_state_string", QCoreApplication.translate("MainWindow", u"JOG", None))
        self.btn_handwheel_spare.setProperty("false_state_string", QCoreApplication.translate("MainWindow", u"HAND\n"
"WHEEL", None))
        self.btn_handwheel_spare.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"INSTANCE.stackedWidget_4.setCurrentIndex(1)", None))
        self.btn_handwheel_spare.setProperty("false_python_cmd_string", QCoreApplication.translate("MainWindow", u"INSTANCE.stackedWidget_4.setCurrentIndex(0)", None))
        self.action_estop.setText(QCoreApplication.translate("MainWindow", u"ESTOP\n"
"PUSH\n"
"here", None))
        self.action_estop.setProperty("true_state_string", QCoreApplication.translate("MainWindow", u"ESTOP\n"
"ACTIVE", None))
        self.action_estop.setProperty("false_state_string", QCoreApplication.translate("MainWindow", u"ESTOP\n"
"PUSH\n"
"here", None))
        self.action_estop.setProperty("true_python_cmd_string", "")
        self.action_estop.setProperty("false_python_cmd_string", "")
        self.abtn_mainh_aux_flood.setText(QCoreApplication.translate("MainWindow", u"FLOOD", None))
        self.abtn_mainh_aux_flood.setProperty("true_python_cmd_string", "")
        self.abtn_mainh_aux_flood.setProperty("false_python_cmd_string", "")
        self.abtn_mainh_aux_mist.setText(QCoreApplication.translate("MainWindow", u"MIST", None))
        self.abtn_mainh_aux_mist.setProperty("true_python_cmd_string", "")
        self.abtn_mainh_aux_mist.setProperty("false_python_cmd_string", "")
        self.statuslabel_6.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"  %a %H:%M %S", None))
        self.btn_main.setText(QCoreApplication.translate("MainWindow", u"MAIN", None))
        self.btn_file.setText(QCoreApplication.translate("MainWindow", u"FILE", None))
        self.btn_offset.setText(QCoreApplication.translate("MainWindow", u"ORIGIN\n"
"OFFSET", None))
        self.btn_tool.setText(QCoreApplication.translate("MainWindow", u"TOOL", None))
        self.btn_status.setText(QCoreApplication.translate("MainWindow", u"ALARMS", None))
        self.btn_macro.setText(QCoreApplication.translate("MainWindow", u"MACRO", None))
        self.btn_settings.setText("")
        self.btn_camera.setText(QCoreApplication.translate("MainWindow", u"CAM\n"
"VIEW", None))
        self.btn_setup.setText(QCoreApplication.translate("MainWindow", u"SETUP", None))
        self.btn_probe.setText(QCoreApplication.translate("MainWindow", u"PROBE", None))
        self.tab_mdi_touchy.setText(QCoreApplication.translate("MainWindow", u"MDI\n"
"TOUCHY", None))
        self.btn_gcode.setText(QCoreApplication.translate("MainWindow", u"GCODE", None))
        self.pbtn_axis4_select_quick_zero.setText(QCoreApplication.translate("MainWindow", u"Over\n"
"Rides", None))
        self.pbtn_axis4_select_quick_zero.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"INSTANCE.stackedWidget_3.setCurrentIndex(1)", None))
        self.pbtn_axis4_select_quick_zero.setProperty("false_python_cmd_string", "")
        self.pbtn_axis4_select_macro.setText(QCoreApplication.translate("MainWindow", u"MAX\n"
"VEL", None))
        self.pbtn_axis4_select_macro.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"INSTANCE.stackedWidget_3.setCurrentIndex(2)", None))
        self.pbtn_axis4_select_macro.setProperty("false_python_cmd_string", "")
        self.pbtn_axis4_select_overrides.setText("")
        self.pbtn_axis4_select_overrides.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"INSTANCE.stackedWidget_3.setCurrentIndex(3)", None))
        self.pbtn_axis4_select_overrides.setProperty("false_python_cmd_string", "")
        self.pbtn_axis4_select_dro.setText("")
        self.pbtn_axis4_select_dro.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"INSTANCE.stackedWidget_3.setCurrentIndex(4)", None))
        self.pbtn_axis4_select_dro.setProperty("false_python_cmd_string", "")
        self.pushbutton_5.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.pushbutton_5.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"INSTANCE.stackedWidget_3.setCurrentIndex(0)", None))
        self.lbl_cycle_start.setText(QCoreApplication.translate("MainWindow", u"CYCLE\n"
"START", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"RUN TIME", None))
        self.lbl_runtime.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.action_pause.setText(QCoreApplication.translate("MainWindow", u"PAUSE", None))
        self.action_pause.setProperty("true_state_string", QCoreApplication.translate("MainWindow", u"RESUME", None))
        self.action_pause.setProperty("false_state_string", QCoreApplication.translate("MainWindow", u"PAUSE", None))
        self.action_pause.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.action_pause.setProperty("command_text_string", "")
        self.action_pause.setProperty("textTemplate", "")
        self.action_pause.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.action_abort.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.action_abort.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.action_abort.setProperty("command_text_string", "")
        self.action_abort.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.action_abort.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.spindle_pause.setText(QCoreApplication.translate("MainWindow", u"PAUSE\n"
"SPINDLE", None))
        self.spindle_pause.setProperty("true_state_string", QCoreApplication.translate("MainWindow", u"SPINDLE\n"
"PAUSED", None))
        self.spindle_pause.setProperty("false_state_string", QCoreApplication.translate("MainWindow", u"PAUSE\n"
"SPINDLE", None))
        self.action_opt_blk.setText(QCoreApplication.translate("MainWindow", u"OPT BLK", None))
        self.action_step.setText(QCoreApplication.translate("MainWindow", u"STEP", None))
        self.action_step.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.action_step.setProperty("command_text_string", "")
        self.action_step.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.action_step.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.action_flood.setText(QCoreApplication.translate("MainWindow", u"FLOOD\n"
"OFF", None))
        self.action_flood.setProperty("true_state_string", QCoreApplication.translate("MainWindow", u"FLOOD\n"
"ON", None))
        self.action_flood.setProperty("false_state_string", QCoreApplication.translate("MainWindow", u"FLOOD\n"
"OFF", None))
        self.action_opt_stp.setText(QCoreApplication.translate("MainWindow", u"OPT STP", None))
#if QT_CONFIG(tooltip)
        self.btn_reload_file.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_reload_file.setStatusTip(QCoreApplication.translate("MainWindow", u"RELOAD PROGRAM", None))
#endif // QT_CONFIG(statustip)
        self.btn_reload_file.setText(QCoreApplication.translate("MainWindow", u"RELOAD", None))
        self.action_mist.setText(QCoreApplication.translate("MainWindow", u"MIST\n"
"OFF", None))
        self.action_mist.setProperty("true_state_string", QCoreApplication.translate("MainWindow", u"MIST\n"
"ON", None))
        self.action_mist.setProperty("false_state_string", QCoreApplication.translate("MainWindow", u"MIST\n"
"OFF", None))
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"PROGRESS %p%", None))
        self.abtn_override_spindle_rate.setText(QCoreApplication.translate("MainWindow", u"Spindle\n"
"Override", None))
        self.abtn_override_feed_rate.setText(QCoreApplication.translate("MainWindow", u"Feed\n"
"Override", None))
        self.abtn_override_rapid_rate.setText(QCoreApplication.translate("MainWindow", u"Rapid\n"
"Override", None))
        self.label_override_panel_label.setText(QCoreApplication.translate("MainWindow", u"OVERRIDE  %  ADJUSTMENT", None))
#if QT_CONFIG(tooltip)
        self.btn_jog_a_slow.setToolTip(QCoreApplication.translate("MainWindow", u"Toggle angular jog speed range", None))
#endif // QT_CONFIG(tooltip)
        self.btn_jog_a_slow.setText(QCoreApplication.translate("MainWindow", u"FAST", None))
        self.btn_jog_a_slow.setProperty("true_state_string", QCoreApplication.translate("MainWindow", u"SLOW", None))
        self.btn_jog_a_slow.setProperty("false_state_string", QCoreApplication.translate("MainWindow", u"FAST", None))
        self.btn_jog_a_slow.setProperty("slider", QCoreApplication.translate("MainWindow", u"slider_jog_angular", None))
        self.status_label_jog_angular.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.f", None))
        self.status_label_jog_angular.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.f", None))
        self.lbl_jog_angular.setText(QCoreApplication.translate("MainWindow", u"JOG - A", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"MAX VELOCITY", None))
#if QT_CONFIG(tooltip)
        self.action_max_vel_ovr_241.setToolTip(QCoreApplication.translate("MainWindow", u"Set max vel override to 0%", None))
#endif // QT_CONFIG(tooltip)
        self.action_max_vel_ovr_241.setText(QCoreApplication.translate("MainWindow", u"240", None))
#if QT_CONFIG(tooltip)
        self.action_max_vel_ovr_401.setToolTip(QCoreApplication.translate("MainWindow", u"Set max vel override to 50%", None))
#endif // QT_CONFIG(tooltip)
        self.action_max_vel_ovr_401.setText(QCoreApplication.translate("MainWindow", u"400", None))
#if QT_CONFIG(tooltip)
        self.action_max_vel_ovr_801.setToolTip(QCoreApplication.translate("MainWindow", u"Set max vel override to 100%", None))
#endif // QT_CONFIG(tooltip)
        self.action_max_vel_ovr_801.setText(QCoreApplication.translate("MainWindow", u"800", None))
#if QT_CONFIG(tooltip)
        self.action_max_vel_ovr_1601.setToolTip(QCoreApplication.translate("MainWindow", u"Set max vel override to 100%", None))
#endif // QT_CONFIG(tooltip)
        self.action_max_vel_ovr_1601.setText(QCoreApplication.translate("MainWindow", u"1600", None))
#if QT_CONFIG(tooltip)
        self.slider_maxv_ovr.setToolTip(QCoreApplication.translate("MainWindow", u"Adjust max velocity override", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.slider_maxv_ovr.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.label_max_welocity.setText(QCoreApplication.translate("MainWindow", u"200in/min", None))
        self.label_max_welocity.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.fin/min", None))
        self.label_max_welocity.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.fmm/min", None))
        self.lbl_maxv_percent.setText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.abtn_dro_dtg.setText(QCoreApplication.translate("MainWindow", u"DTG", None))
        self.actionbutton_rel.setText(QCoreApplication.translate("MainWindow", u"G54", None))
        self.actionbutton_rel.setProperty("false_state_string", QCoreApplication.translate("MainWindow", u"REL", None))
        self.abtn_dro_abs.setText(QCoreApplication.translate("MainWindow", u"ABS", None))
#if QT_CONFIG(statustip)
        self.systemtoolbutton.setStatusTip(QCoreApplication.translate("MainWindow", u"SELECT WORK COORDINATE SYSTEM", None))
#endif // QT_CONFIG(statustip)
        self.systemtoolbutton.setText(QCoreApplication.translate("MainWindow", u"WCS", None))
        self.lbl_home_all.setText(QCoreApplication.translate("MainWindow", u"HOME\n"
"ALL", None))
        self.label_axis_z.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.label_axis_a.setText(QCoreApplication.translate("MainWindow", u"A", None))
#if QT_CONFIG(tooltip)
        self.action_zero_y.setToolTip(QCoreApplication.translate("MainWindow", u"Zero axis Y", None))
#endif // QT_CONFIG(tooltip)
        self.action_zero_y.setText(QCoreApplication.translate("MainWindow", u"ZERO", None))
        self.action_zero_y.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.action_zero_y.setProperty("command_text_string", "")
        self.action_zero_y.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.action_zero_y.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
#if QT_CONFIG(tooltip)
        self.action_zero_z.setToolTip(QCoreApplication.translate("MainWindow", u"Zero axis Z", None))
#endif // QT_CONFIG(tooltip)
        self.action_zero_z.setText(QCoreApplication.translate("MainWindow", u"ZERO", None))
        self.action_zero_z.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.action_zero_z.setProperty("command_text_string", "")
        self.action_zero_z.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.action_zero_z.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
#if QT_CONFIG(tooltip)
        self.action_zero_x.setToolTip(QCoreApplication.translate("MainWindow", u"Zero axis X", None))
#endif // QT_CONFIG(tooltip)
        self.action_zero_x.setText(QCoreApplication.translate("MainWindow", u"ZERO", None))
        self.action_zero_x.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.action_zero_x.setProperty("command_text_string", "")
        self.action_zero_x.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.action_zero_x.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.axistoolbutton_z.setText(QCoreApplication.translate("MainWindow", u"REFZ", None))
        self.axistoolbutton_z.setProperty("axis_letter", QCoreApplication.translate("MainWindow", u"Z", None))
        self.axistoolbutton_z.setProperty("dialog_code_string", QCoreApplication.translate("MainWindow", u"CALCULATOR", None))
        self.axistoolbutton_x.setText(QCoreApplication.translate("MainWindow", u"REFX", None))
        self.axistoolbutton_x.setProperty("axis_letter", QCoreApplication.translate("MainWindow", u"X", None))
        self.axistoolbutton_x.setProperty("dialog_code_string", QCoreApplication.translate("MainWindow", u"CALCULATOR", None))
        self.axistoolbutton_a.setText(QCoreApplication.translate("MainWindow", u"REFA", None))
        self.axistoolbutton_a.setProperty("axis_letter", QCoreApplication.translate("MainWindow", u"A", None))
        self.axistoolbutton_a.setProperty("dialog_code_string", QCoreApplication.translate("MainWindow", u"CALCULATOR", None))
        self.action_home_a.setText(QCoreApplication.translate("MainWindow", u"GO TO\n"
"ZERO", None))
        self.action_home_a.setProperty("axis_letter", QCoreApplication.translate("MainWindow", u"A", None))
        self.action_home_a.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.action_home_a.setProperty("command_text_string", QCoreApplication.translate("MainWindow", u"G90 G0 A0", None))
        self.action_home_a.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.action_home_a.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.label_axis_y.setText(QCoreApplication.translate("MainWindow", u"Y", None))
#if QT_CONFIG(tooltip)
        self.action_zero_a.setToolTip(QCoreApplication.translate("MainWindow", u"Zero axis A", None))
#endif // QT_CONFIG(tooltip)
        self.action_zero_a.setText(QCoreApplication.translate("MainWindow", u"ZERO", None))
        self.action_zero_a.setProperty("axis_letter", QCoreApplication.translate("MainWindow", u"A", None))
        self.action_zero_a.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.action_zero_a.setProperty("command_text_string", "")
        self.action_zero_a.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.action_zero_a.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.btn_home_z.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_home_z.setProperty("true_state_string", QCoreApplication.translate("MainWindow", u"UNHOME", None))
        self.btn_home_z.setProperty("false_state_string", QCoreApplication.translate("MainWindow", u"HOME", None))
        self.axistoolbutton_y.setText(QCoreApplication.translate("MainWindow", u"REFY", None))
        self.axistoolbutton_y.setProperty("axis_letter", QCoreApplication.translate("MainWindow", u"Y", None))
        self.axistoolbutton_y.setProperty("dialog_code_string", QCoreApplication.translate("MainWindow", u"CALCULATOR", None))
        self.label_axis_x.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.btn_home_x.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_home_x.setProperty("true_state_string", QCoreApplication.translate("MainWindow", u"UNHOME", None))
        self.btn_home_x.setProperty("false_state_string", QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_home_y.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_home_y.setProperty("true_state_string", QCoreApplication.translate("MainWindow", u"UNHOME", None))
        self.btn_home_y.setProperty("false_state_string", QCoreApplication.translate("MainWindow", u"HOME", None))
        self.label_spindle.setText(QCoreApplication.translate("MainWindow", u"SPINDLE", None))
        self.spindle_reverse.setText(QCoreApplication.translate("MainWindow", u"REV", None))
        self.spindle_stop.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.spindle_forward.setText(QCoreApplication.translate("MainWindow", u"FWD", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"RPM", None))
        self.status_rpm.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.f", None))
        self.status_rpm.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.f", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"PWR", None))
        self.lbl_spindle_power.setText(QCoreApplication.translate("MainWindow", u"000", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"AMPS", None))
        self.lbl_spindle_amps.setText(QCoreApplication.translate("MainWindow", u"000", None))
        self.btn_spindle_slover.setText(QCoreApplication.translate("MainWindow", u"Spindle\n"
"Slover", None))
        self.btn_spindle_faster.setText(QCoreApplication.translate("MainWindow", u"Spindle\n"
"Faster", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"AT SPEED", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"FAULT", None))
        self.lbl_spindle_fault.setText(QCoreApplication.translate("MainWindow", u"0x0", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"PROBE", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"UNITS", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"STATE", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"EOFFSET", None))
        self.statelabel_metric.setProperty("true_textTemplate", QCoreApplication.translate("MainWindow", u"MM", None))
        self.statelabel_metric.setProperty("false_textTemplate", QCoreApplication.translate("MainWindow", u"IN", None))
        self.lbl_eoffset_value.setText(QCoreApplication.translate("MainWindow", u"000", None))
        self.lab_mcode_list.setText("")
        self.lab_gcode_list.setText("")
        self.lab_feed_per_rev.setText("")
        self.lab_tool_numb.setText("")
        self.lab_tool_diam.setText("")
        self.lab_feed_rate.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.lab_feed_rate.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.0f", None))
        self.lab_feed_rate.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.0f", None))
        self.lab_tool_comment.setText("")
        self.lab_mcodes_label.setText(QCoreApplication.translate("MainWindow", u"Mcodes:", None))
        self.lab_gcodes_label.setText(QCoreApplication.translate("MainWindow", u"Gcodes:", None))
        self.lab_tool_label.setText(QCoreApplication.translate("MainWindow", u"Tool:", None))
        self.lab_in_limits_label.setText(QCoreApplication.translate("MainWindow", u"Limits:", None))
        self.lab_feed_per_rev_label.setText(QCoreApplication.translate("MainWindow", u"Per Rev:", None))
        self.lab_tool_numb_label.setText(QCoreApplication.translate("MainWindow", u"Tool \u2116:", None))
        self.lab_tool_diam_label.setText(QCoreApplication.translate("MainWindow", u"Diam:", None))
        self.lab_feed_rate_label.setText(QCoreApplication.translate("MainWindow", u"ACT.FO.", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"HOME SWITCHES", None))
        self.btn_jog_neg_a.setText("")
        self.btn_jog_neg_a.setProperty("axis_letter", QCoreApplication.translate("MainWindow", u"A", None))
        self.btn_jog_neg_z.setText("")
        self.btn_jog_neg_z.setProperty("axis_letter", QCoreApplication.translate("MainWindow", u"Z", None))
        self.btn_jog_pos_a.setText("")
        self.btn_jog_pos_a.setProperty("axis_letter", QCoreApplication.translate("MainWindow", u"A", None))
        self.btn_jog_neg_x.setText("")
        self.btn_jog_neg_x.setProperty("axis_letter", QCoreApplication.translate("MainWindow", u"X", None))
        self.btn_jog_pos_x.setText("")
        self.btn_jog_pos_x.setProperty("axis_letter", QCoreApplication.translate("MainWindow", u"X", None))
        self.btn_jog_pos_z.setText("")
        self.btn_jog_pos_z.setProperty("axis_letter", QCoreApplication.translate("MainWindow", u"Z", None))
        self.btn_jog_pos_y.setText("")
        self.btn_jog_pos_y.setProperty("axis_letter", QCoreApplication.translate("MainWindow", u"Y", None))
        self.btn_jog_neg_y.setText("")
        self.btn_jog_neg_y.setProperty("axis_letter", QCoreApplication.translate("MainWindow", u"Y", None))
#if QT_CONFIG(tooltip)
        self.slider_jog_linear.setToolTip(QCoreApplication.translate("MainWindow", u"Adjust linear jog rate", None))
#endif // QT_CONFIG(tooltip)
        self.status_jog_linear.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.0f", None))
        self.status_jog_linear.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.0f", None))
        self.lbl_jog_linear.setText(QCoreApplication.translate("MainWindow", u"JOG RATE", None))
#if QT_CONFIG(tooltip)
        self.btn_jog_l_slow.setToolTip(QCoreApplication.translate("MainWindow", u"Toggle linear jog speed range", None))
#endif // QT_CONFIG(tooltip)
        self.btn_jog_l_slow.setText(QCoreApplication.translate("MainWindow", u"FAST", None))
        self.btn_jog_l_slow.setProperty("true_state_string", QCoreApplication.translate("MainWindow", u"SLOW", None))
        self.btn_jog_l_slow.setProperty("false_state_string", QCoreApplication.translate("MainWindow", u"FAST", None))
        self.btn_jog_l_slow.setProperty("slider", QCoreApplication.translate("MainWindow", u"slider_jog_linear", None))
        self.pushbutton_metric.setText(QCoreApplication.translate("MainWindow", u"G20", None))
        self.pushbutton_metric.setProperty("true_state_string", QCoreApplication.translate("MainWindow", u"G21", None))
        self.pushbutton_metric.setProperty("false_state_string", QCoreApplication.translate("MainWindow", u"G20", None))
        self.lbl_increments_angular.setText(QCoreApplication.translate("MainWindow", u"ANGULAR INCREMENT", None))
#if QT_CONFIG(tooltip)
        self.jogincrements_angular.setToolTip(QCoreApplication.translate("MainWindow", u"Select jog increment", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_increments_linear.setText(QCoreApplication.translate("MainWindow", u"LINEAR INCREMENT", None))
#if QT_CONFIG(tooltip)
        self.jogincrements_linear.setToolTip(QCoreApplication.translate("MainWindow", u"Select jog increment", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"HANDWHEEL", None))
        self.pushbutton_ro.setText(QCoreApplication.translate("MainWindow", u"Ro", None))
        self.pushbutton_fo.setText(QCoreApplication.translate("MainWindow", u"Fo", None))
        self.pushbutton_so.setText(QCoreApplication.translate("MainWindow", u"So", None))
        self.axistoolbutton.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.axistoolbutton.setProperty("axis_letter", QCoreApplication.translate("MainWindow", u"X", None))
        self.axistoolbutton.setProperty("dialog_code_string", QCoreApplication.translate("MainWindow", u"CALCULATOR", None))
        self.axistoolbutton_2.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.axistoolbutton_2.setProperty("axis_letter", QCoreApplication.translate("MainWindow", u"Y", None))
        self.axistoolbutton_2.setProperty("dialog_code_string", QCoreApplication.translate("MainWindow", u"CALCULATOR", None))
        self.axistoolbutton_3.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.axistoolbutton_3.setProperty("axis_letter", QCoreApplication.translate("MainWindow", u"Z", None))
        self.axistoolbutton_3.setProperty("dialog_code_string", QCoreApplication.translate("MainWindow", u"CALCULATOR", None))
        self.axistoolbutton_4.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.axistoolbutton_4.setProperty("axis_letter", QCoreApplication.translate("MainWindow", u"A", None))
        self.axistoolbutton_4.setProperty("dialog_code_string", QCoreApplication.translate("MainWindow", u"CALCULATOR", None))
        self.pushbutton_jog.setText(QCoreApplication.translate("MainWindow", u"JOG", None))
#if QT_CONFIG(tooltip)
        self.lbl_max_rapid.setToolTip(QCoreApplication.translate("MainWindow", u"Actual rapid rate", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_max_rapid.setText(QCoreApplication.translate("MainWindow", u"00", None))
#if QT_CONFIG(tooltip)
        self.jogincrements_linear_2.setToolTip(QCoreApplication.translate("MainWindow", u"Select jog increment", None))
#endif // QT_CONFIG(tooltip)
        self.label_mdi_panel.setText(QCoreApplication.translate("MainWindow", u"MDI PANEL", None))
#if QT_CONFIG(tooltip)
        self.cmb_gcode_history.setToolTip(QCoreApplication.translate("MainWindow", u"History of loaded GCODE programs", None))
#endif // QT_CONFIG(tooltip)
        self.cmb_gcode_history.setCurrentText("")
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Height from machine bed to\n"
"top of workpiece", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"MM", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Height from machine bed to\n"
"tool sensor", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_sensor_height.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"MM", None))
        self.label_54.setText("")
        self.label_63.setText("")
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"TOOL SENSOR LOCATION", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"LASER OFFSET", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"CAMERA OFFSET", None))
#if QT_CONFIG(tooltip)
        self.btn_goto_sensor.setToolTip(QCoreApplication.translate("MainWindow", u"Go to Tool Sensor location", None))
#endif // QT_CONFIG(tooltip)
        self.btn_goto_sensor.setText(QCoreApplication.translate("MainWindow", u"GO TO\n"
"SENSOR", None))
#if QT_CONFIG(tooltip)
        self.btn_laser_on.setToolTip(QCoreApplication.translate("MainWindow", u"Toggle laser crosshairs", None))
#endif // QT_CONFIG(tooltip)
        self.btn_laser_on.setText(QCoreApplication.translate("MainWindow", u"LASER\n"
"OFF", None))
        self.btn_laser_on.setProperty("true_state_string", QCoreApplication.translate("MainWindow", u"LASER\n"
"ON", None))
        self.btn_laser_on.setProperty("false_state_string", QCoreApplication.translate("MainWindow", u"LASER\n"
"OFF", None))
        self.btn_laser_on.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"print\"Laser crosshair turned on\"", None))
        self.btn_laser_on.setProperty("false_python_cmd_string", QCoreApplication.translate("MainWindow", u"print\"Laser crosshair turned off\"", None))
#if QT_CONFIG(tooltip)
        self.btn_ref_laser.setToolTip(QCoreApplication.translate("MainWindow", u"Set laser crosshair reference", None))
#endif // QT_CONFIG(tooltip)
        self.btn_ref_laser.setText(QCoreApplication.translate("MainWindow", u"REF\n"
"LASER", None))
#if QT_CONFIG(statustip)
        self.btn_touch_sensor.setStatusTip(QCoreApplication.translate("MainWindow", u"TOUCHOFF TO TOOL SENSOR", None))
#endif // QT_CONFIG(statustip)
        self.btn_touch_sensor.setText(QCoreApplication.translate("MainWindow", u"TOUCH\n"
"SENSOR", None))
        self.btn_touch_sensor.setProperty("sensor", QCoreApplication.translate("MainWindow", u"_toolsensor_", None))
        self.btn_ref_camera.setText(QCoreApplication.translate("MainWindow", u"REF\n"
"CAMERA", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"DIAMETR", None))
        self.label_70.setText("")
        self.label_71.setText("")
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"TOOL NUMBER", None))
        self.label_74.setText("")
        self.label_45.setText("")
#if QT_CONFIG(tooltip)
        self.label_75.setToolTip(QCoreApplication.translate("MainWindow", u"Height of tool touch plate", None))
#endif // QT_CONFIG(tooltip)
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"TOUCH PLATE HEIGHT ", None))
        self.lbl_touchheight_units.setText(QCoreApplication.translate("MainWindow", u"MM", None))
#if QT_CONFIG(tooltip)
        self.btn_tool_add.setToolTip(QCoreApplication.translate("MainWindow", u"Add new tool to tooltable", None))
#endif // QT_CONFIG(tooltip)
        self.btn_tool_add.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.btn_tool_add.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"INSTANCE.tooloffsetview.add_tool()", None))
        self.btn_tool_add.setProperty("false_python_cmd_string", "")
#if QT_CONFIG(tooltip)
        self.btn_tool_delete.setToolTip(QCoreApplication.translate("MainWindow", u"Delete selected tools", None))
#endif // QT_CONFIG(tooltip)
        self.btn_tool_delete.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.btn_tool_delete.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"INSTANCE.tooloffsetview.delete_tools()", None))
        self.btn_tool_delete.setProperty("false_python_cmd_string", "")
#if QT_CONFIG(tooltip)
        self.btn_m61.setToolTip(QCoreApplication.translate("MainWindow", u"Load selected tool", None))
#endif // QT_CONFIG(tooltip)
        self.btn_m61.setText(QCoreApplication.translate("MainWindow", u"M61 Qn", None))
#if QT_CONFIG(statustip)
        self.btn_touchplate.setStatusTip(QCoreApplication.translate("MainWindow", u"TOUCHOFF TO TOOL TOUCHPLATE", None))
#endif // QT_CONFIG(statustip)
        self.btn_touchplate.setText(QCoreApplication.translate("MainWindow", u"TOUCH\n"
"PLATE", None))
        self.btn_touchplate.setProperty("sensor", QCoreApplication.translate("MainWindow", u"_touchplate_", None))
        self.widgetswitcher_2.setProperty("widget_list", QStringList()
            << QCoreApplication.translate("MainWindow", u"gcodegraphics", None))
#if QT_CONFIG(tooltip)
        self.actionbutton_view_p_2.setToolTip(QCoreApplication.translate("MainWindow", u"Set view P", None))
#endif // QT_CONFIG(tooltip)
        self.actionbutton_view_p_2.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.actionbutton_view_p_2.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.actionbutton_view_p_2.setProperty("command_text_string", "")
        self.actionbutton_view_p_2.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.actionbutton_view_p_2.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
#if QT_CONFIG(tooltip)
        self.actionbutton_view_x_2.setToolTip(QCoreApplication.translate("MainWindow", u"Set view X", None))
#endif // QT_CONFIG(tooltip)
        self.actionbutton_view_x_2.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.actionbutton_view_x_2.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"X", None))
        self.actionbutton_view_x_2.setProperty("command_text_string", "")
        self.actionbutton_view_x_2.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.actionbutton_view_x_2.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
#if QT_CONFIG(tooltip)
        self.actionbutton_view_y_2.setToolTip(QCoreApplication.translate("MainWindow", u"Set view Y", None))
#endif // QT_CONFIG(tooltip)
        self.actionbutton_view_y_2.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.actionbutton_view_y_2.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"Y", None))
        self.actionbutton_view_y_2.setProperty("command_text_string", "")
        self.actionbutton_view_y_2.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.actionbutton_view_y_2.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
#if QT_CONFIG(tooltip)
        self.actionbutton_view_z_2.setToolTip(QCoreApplication.translate("MainWindow", u"Set view Z", None))
#endif // QT_CONFIG(tooltip)
        self.actionbutton_view_z_2.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.actionbutton_view_z_2.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"Z", None))
        self.actionbutton_view_z_2.setProperty("command_text_string", "")
        self.actionbutton_view_z_2.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.actionbutton_view_z_2.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
#if QT_CONFIG(tooltip)
        self.actionbutton_clear_2.setToolTip(QCoreApplication.translate("MainWindow", u"Clear display", None))
#endif // QT_CONFIG(tooltip)
        self.actionbutton_clear_2.setText("")
        self.actionbutton_clear_2.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"Clear", None))
        self.actionbutton_clear_2.setProperty("command_text_string", "")
        self.actionbutton_clear_2.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.actionbutton_clear_2.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.probesim_button.setText(QCoreApplication.translate("MainWindow", u"PROBE\n"
"SIM", None))
        self.abtn_graphics_view_p.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.abtn_graphics_view_p.setProperty("true_python_cmd_string", "")
        self.abtn_graphics_view_p.setProperty("false_python_cmd_string", "")
        self.abtn_graphics_view_x.setText(QCoreApplication.translate("MainWindow", u" X", None))
        self.abtn_graphics_view_x.setProperty("true_python_cmd_string", "")
        self.abtn_graphics_view_x.setProperty("false_python_cmd_string", "")
        self.abtn_graphics_view_x.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"x", None))
        self.abtn_graphics_view_y.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.abtn_graphics_view_y.setProperty("true_python_cmd_string", "")
        self.abtn_graphics_view_y.setProperty("false_python_cmd_string", "")
        self.abtn_graphics_view_y.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"y", None))
        self.abtn_graphics_view_z.setText(QCoreApplication.translate("MainWindow", u" Z", None))
        self.abtn_graphics_view_z.setProperty("true_python_cmd_string", "")
        self.abtn_graphics_view_z.setProperty("false_python_cmd_string", "")
        self.abtn_graphics_view_z.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"z", None))
        self.abtn_graphics_view_z2.setText(QCoreApplication.translate("MainWindow", u"Z2", None))
        self.abtn_graphics_view_z2.setProperty("true_python_cmd_string", "")
        self.abtn_graphics_view_z2.setProperty("false_python_cmd_string", "")
        self.abtn_graphics_view_z2.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"z2", None))
#if QT_CONFIG(tooltip)
        self.actionbutton_zoom_in.setToolTip(QCoreApplication.translate("MainWindow", u"Zoom in", None))
#endif // QT_CONFIG(tooltip)
        self.actionbutton_zoom_in.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.actionbutton_zoom_in.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"zoom-in", None))
#if QT_CONFIG(tooltip)
        self.actionbutton_zoom_out.setToolTip(QCoreApplication.translate("MainWindow", u"Zoom out", None))
#endif // QT_CONFIG(tooltip)
        self.actionbutton_zoom_out.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.actionbutton_zoom_out.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"zoom-out", None))
#if QT_CONFIG(tooltip)
        self.btn_setdro.setToolTip(QCoreApplication.translate("MainWindow", u"Toggle display overlay dro on", None))
#endif // QT_CONFIG(tooltip)
        self.btn_setdro.setText(QCoreApplication.translate("MainWindow", u"DRO", None))
#if QT_CONFIG(tooltip)
        self.btn_show_offset.setToolTip(QCoreApplication.translate("MainWindow", u"Toggle display setShowOffset", None))
#endif // QT_CONFIG(tooltip)
        self.btn_show_offset.setText(QCoreApplication.translate("MainWindow", u"Offset", None))
#if QT_CONFIG(tooltip)
        self.btn_dimensions.setToolTip(QCoreApplication.translate("MainWindow", u"Toggle display dimensions", None))
#endif // QT_CONFIG(tooltip)
        self.btn_dimensions.setText("")
        self.btn_graphics_view_clear.setText("")
        self.btn_graphics_view_clear.setProperty("true_python_cmd_string", "")
        self.btn_graphics_view_clear.setProperty("false_python_cmd_string", "")
        self.btn_graphics_view_clear.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"Clear", None))
        self.btn_graphics_view_clear.setProperty("command_text_string", "")
        self.btn_file_next.setText(QCoreApplication.translate("MainWindow", u"NEXT", None))
        self.btn_file_next.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"INSTANCE.filemanager.down()", None))
        self.btn_file_next.setProperty("false_python_cmd_string", "")
        self.btn_file_prev.setText(QCoreApplication.translate("MainWindow", u"PREV", None))
        self.btn_file_prev.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"INSTANCE.filemanager.up()", None))
        self.btn_file_prev.setProperty("false_python_cmd_string", "")
        self.btn_gcode_edit.setText(QCoreApplication.translate("MainWindow", u"EDIT", None))
        self.btn_gcode_edit.setProperty("true_python_cmd_string", "")
        self.btn_gcode_edit.setProperty("false_python_cmd_string", "")
        self.btn_file_load.setText(QCoreApplication.translate("MainWindow", u"LOAD", None))
        self.action_zero_rotation.setText(QCoreApplication.translate("MainWindow", u"ZERO\n"
"ROTATION", None))
        self.action_zero_g92.setText(QCoreApplication.translate("MainWindow", u"ZERO G92", None))
        self.action_zero_g92.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.action_zero_g92.setProperty("command_text_string", "")
        self.action_zero_g92.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.action_zero_g92.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.action_zero_g5x.setText(QCoreApplication.translate("MainWindow", u"ZERO G5X", None))
        self.machinelog.setDocumentTitle(QCoreApplication.translate("MainWindow", u"Machine Log", None))
        self.machinelog.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Machine Log", None))
        self.integrator_log.setDocumentTitle(QCoreApplication.translate("MainWindow", u"Integrator Log", None))
        self.integrator_log.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Integrator Log", None))
        self.btn_select_log.setProperty("true_state_string", QCoreApplication.translate("MainWindow", u"SYSTEM\n"
"LOG", None))
        self.btn_select_log.setProperty("false_state_string", QCoreApplication.translate("MainWindow", u"MACHINE\n"
"LOG", None))
        self.btn_select_log.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"INSTANCE.stackedWidget_log.setCurrentIndex(1)", None))
        self.btn_select_log.setProperty("false_python_cmd_string", QCoreApplication.translate("MainWindow", u"INSTANCE.stackedWidget_log.setCurrentIndex(0)", None))
        self.btn_clear_status.setText(QCoreApplication.translate("MainWindow", u"CLEAR\n"
"STATUS", None))
#if QT_CONFIG(tooltip)
        self.btn_save_status.setToolTip(QCoreApplication.translate("MainWindow", u"Save status to file", None))
#endif // QT_CONFIG(tooltip)
        self.btn_save_status.setText(QCoreApplication.translate("MainWindow", u"SAVE\n"
"TO FILE", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"KEYBOARD MAPPING", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"ESC - Program Abort", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"F1 - ESTOP", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"F2 - Machine OFF", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"F12 - Style Sheet Editor", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Home - HOME All", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Pause - Pause program", None))
#if QT_CONFIG(tooltip)
        self.chk_eoffsets.setToolTip(QCoreApplication.translate("MainWindow", u"Enable external offsets for spindle pause", None))
#endif // QT_CONFIG(tooltip)
        self.chk_eoffsets.setText(QCoreApplication.translate("MainWindow", u"USE EXTERNAL OFFSETS", None))
#if QT_CONFIG(tooltip)
        self.chk_use_tool_sensor.setToolTip(QCoreApplication.translate("MainWindow", u"Enable tool sensor", None))
#endif // QT_CONFIG(tooltip)
        self.chk_use_tool_sensor.setText(QCoreApplication.translate("MainWindow", u"USE TOOL SENSOR", None))
#if QT_CONFIG(tooltip)
        self.chk_use_camera.setToolTip(QCoreApplication.translate("MainWindow", u"Eanable Webcam for work offset location", None))
#endif // QT_CONFIG(tooltip)
        self.chk_use_camera.setText(QCoreApplication.translate("MainWindow", u"USE CAMERA", None))
#if QT_CONFIG(tooltip)
        self.chk_use_virtual.setToolTip(QCoreApplication.translate("MainWindow", u"Enable use of onboard virtual keyboard", None))
#endif // QT_CONFIG(tooltip)
        self.chk_use_virtual.setText(QCoreApplication.translate("MainWindow", u"USE VIRTUAL KEYBOARD", None))
        self.chk_reload_tool.setText(QCoreApplication.translate("MainWindow", u"RELOAD TOOL", None))
        self.chk_reload_program.setText(QCoreApplication.translate("MainWindow", u"RELOAD PROGRAM", None))
        self.chk_use_keyboard.setText(QCoreApplication.translate("MainWindow", u"USE KEYBOARD", None))
        self.chk_run_from_line.setText(QCoreApplication.translate("MainWindow", u"USE RUN FROM LINE", None))
        self.chk_override_limits.setText(QCoreApplication.translate("MainWindow", u"OVERRIDE LIMITS", None))
        self.label_73.setText("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"HOME LOCATION", None))
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("MainWindow", u"Probe down search velocity", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"SEARCH VELOCITY", None))
        self.lbl_search_vel_units.setText(QCoreApplication.translate("MainWindow", u"MM/MIN", None))
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(QCoreApplication.translate("MainWindow", u"Probe down final velocity", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"PROBE VELOCITY", None))
        self.lbl_probe_vel_units.setText(QCoreApplication.translate("MainWindow", u"MM/MIN", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("MainWindow", u"Max probing distance", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"MAX PROBE", None))
        self.lbl_max_probe_units.setText(QCoreApplication.translate("MainWindow", u"MM", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("MainWindow", u"Distance to raise Z axis during spindle pause", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Z EXT OFFSET", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"MM", None))
        self.chk_alpha_mode.setText(QCoreApplication.translate("MainWindow", u"Alpha Display Mode", None))
        self.chk_alpha_mode_2.setText(QCoreApplication.translate("MainWindow", u"Inhibit Display Mouse Selection", None))
        self.silver_dragon.setText("")
        self.actionbutton_calibration_2.setText(QCoreApplication.translate("MainWindow", u"CALIBRATION", None))
        self.actionbutton_halshow_2.setText(QCoreApplication.translate("MainWindow", u"HAL SHOW", None))
        self.actionbutton_halshow_2.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.actionbutton_halshow_2.setProperty("command_text_string", "")
        self.actionbutton_halshow_2.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.actionbutton_halshow_2.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.actionbutton_halshow_2.setProperty("actionName", QCoreApplication.translate("MainWindow", u"tool.halshow", None))
        self.actionbutton_halmeter_2.setText(QCoreApplication.translate("MainWindow", u"HAL METER", None))
        self.actionbutton_halmeter_2.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.actionbutton_halmeter_2.setProperty("command_text_string", "")
        self.actionbutton_halmeter_2.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.actionbutton_halmeter_2.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.actionbutton_halmeter_2.setProperty("actionName", QCoreApplication.translate("MainWindow", u"tool.halmeter", None))
        self.actionbutton_halscope_2.setText(QCoreApplication.translate("MainWindow", u"HAL SCOPE", None))
        self.actionbutton_halscope_2.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.actionbutton_halscope_2.setProperty("command_text_string", "")
        self.actionbutton_halscope_2.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.actionbutton_halscope_2.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.actionbutton_halscope_2.setProperty("actionName", QCoreApplication.translate("MainWindow", u"tool.halscope", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"MODBUS\n"
"ERRORS", None))
        self.lbl_mb_errors.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.actionbutton_lcnc_status_2.setText(QCoreApplication.translate("MainWindow", u"STATUS", None))
        self.actionbutton_lcnc_status_2.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.actionbutton_lcnc_status_2.setProperty("command_text_string", "")
        self.actionbutton_lcnc_status_2.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.actionbutton_lcnc_status_2.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.actionbutton_lcnc_status_2.setProperty("actionName", QCoreApplication.translate("MainWindow", u"tool.status", None))
#if QT_CONFIG(tooltip)
        self.label_59.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"VFD FAULT", None))
#if QT_CONFIG(tooltip)
        self.lbl_spindle_fault_2.setToolTip(QCoreApplication.translate("MainWindow", u"VFD fault code", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_spindle_fault_2.setText(QCoreApplication.translate("MainWindow", u"0x0", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"ZOOM", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"DIA", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"ROT", None))
        self.runFromLineButton.setText(QCoreApplication.translate("MainWindow", u"RUN FROM\n"
"HERE", None))
        self.line_number.setText(QCoreApplication.translate("MainWindow", u"Line Number", None))
        self.btn_rezet.setText(QCoreApplication.translate("MainWindow", u"REZET", None))
        self.btn_start_macro.setText(QCoreApplication.translate("MainWindow", u"START\n"
" MACRO", None))
        self.gcode_parameters.setText(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.gcode_parameters.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.tabWidget_utilities.setTabText(self.tabWidget_utilities.indexOf(self.facing), QCoreApplication.translate("MainWindow", u"FACING", None))
        self.tabWidget_utilities.setTabText(self.tabWidget_utilities.indexOf(self.hole_circle), QCoreApplication.translate("MainWindow", u"HOLE CIRCLE", None))
        self.tabWidget_utilities.setTabText(self.tabWidget_utilities.indexOf(self.calculator), QCoreApplication.translate("MainWindow", u"CALCULATOR", None))
        self.widgetswitcher.setProperty("widget_list", QStringList()
            << QCoreApplication.translate("MainWindow", u"main_tab_widget", None))
    # retranslateUi

