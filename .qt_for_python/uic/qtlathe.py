# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qtlathe.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from qtvcp.widgets.simple_widgets import LCDNumber
from qtvcp.widgets.gcode_graphics import GCodeGraphics
from qtvcp.widgets.macro_widget import MacroTab
from qtvcp.widgets.origin_offsetview import OriginOffsetView
from qtvcp.widgets.status_slider import StatusSlider
from qtvcp.widgets.state_label import StateLabel
from qtvcp.widgets.axis_tool_button import AxisToolButton
from qtvcp.widgets.led_widget import LED
from qtvcp.widgets.state_led import StateLED
from qtvcp.widgets.jog_increments import JogIncrements
from qtvcp.widgets.screen_options import ScreenOptions
from qtvcp.widgets.simple_widgets import PushButton
from qtvcp.widgets.status_label import StatusLabel
from qtvcp.widgets.image_switcher import ImageSwitcher
from qtvcp.widgets.tool_offsetview import ToolOffsetView
from qtvcp.widgets.dro_widget import DROLabel
from qtvcp.widgets.widget_switcher import WidgetSwitcher
from qtvcp.widgets.file_manager import FileManager
from qtvcp.widgets.system_tool_button import SystemToolButton
from qtvcp.widgets.gcode_editor import GcodeEditor
from qtvcp.widgets.mdi_history import MDIHistory
from qtvcp.widgets.image_switcher import StatusImageSwitcher
from qtvcp.widgets.action_button import ActionButton
from qtvcp.widgets.mdi_touchy import MDITouchy

import qtlathe_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1500, 985)
        MainWindow.setMinimumSize(QSize(1500, 985))
        MainWindow.setMaximumSize(QSize(1500, 985))
        self.actionCalculatorDialog = QAction(MainWindow)
        self.actionCalculatorDialog.setObjectName(u"actionCalculatorDialog")
        self.actionToolOffsetDialog = QAction(MainWindow)
        self.actionToolOffsetDialog.setObjectName(u"actionToolOffsetDialog")
        self.actionReload = QAction(MainWindow)
        self.actionReload.setObjectName(u"actionReload")
        self.actionStep = QAction(MainWindow)
        self.actionStep.setObjectName(u"actionStep")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_8 = QFrame(self.centralwidget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.WinPanel)
        self.frame_8.setFrameShadow(QFrame.Plain)
        self.gridLayout_12 = QGridLayout(self.frame_8)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.actionbutton = ActionButton(self.frame_8)
        self.actionbutton.setObjectName(u"actionbutton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton.sizePolicy().hasHeightForWidth())
        self.actionbutton.setSizePolicy(sizePolicy)
        self.actionbutton.setMinimumSize(QSize(80, 60))
        self.actionbutton.setCheckable(True)
        self.actionbutton.setAutoRepeatDelay(317)
        self.actionbutton.setProperty("indicator_option", False)
        self.actionbutton.setProperty("indicator_HAL_pin_option", False)
        self.actionbutton.setProperty("checked_state_text_option", False)
        self.actionbutton.setProperty("on_color", QColor(255, 0, 0))
        self.actionbutton.setProperty("off_color", QColor(0, 0, 0))
        self.actionbutton.setProperty("estop_action", True)
        self.actionbutton.setProperty("template_label_option", False)
        self.actionbutton.setProperty("joint_number", 0)
        self.actionbutton.setProperty("incr_imperial_number", 0.010000000000000)
        self.actionbutton.setProperty("incr_mm_number", 0.025000000000000)
        self.actionbutton.setProperty("incr_angular_number", -1.000000000000000)
        self.actionbutton.setProperty("toggle_float_option", False)
        self.actionbutton.setProperty("float_num", 100.000000000000000)
        self.actionbutton.setProperty("float_alt_num", 50.000000000000000)
        self.actionbutton.setProperty("ini_mdi_number", 0)

        self.gridLayout_12.addWidget(self.actionbutton, 0, 0, 2, 1)

        self.actionbutton_2 = ActionButton(self.frame_8)
        self.actionbutton_2.setObjectName(u"actionbutton_2")
        sizePolicy.setHeightForWidth(self.actionbutton_2.sizePolicy().hasHeightForWidth())
        self.actionbutton_2.setSizePolicy(sizePolicy)
        self.actionbutton_2.setMinimumSize(QSize(80, 60))
        self.actionbutton_2.setCheckable(True)
        self.actionbutton_2.setProperty("indicator_option", False)
        self.actionbutton_2.setProperty("indicator_HAL_pin_option", False)
        self.actionbutton_2.setProperty("checked_state_text_option", False)
        self.actionbutton_2.setProperty("on_color", QColor(255, 0, 0))
        self.actionbutton_2.setProperty("off_color", QColor(0, 0, 0))
        self.actionbutton_2.setProperty("machine_on_action", True)
        self.actionbutton_2.setProperty("template_label_option", False)
        self.actionbutton_2.setProperty("joint_number", 0)
        self.actionbutton_2.setProperty("incr_imperial_number", 0.010000000000000)
        self.actionbutton_2.setProperty("incr_mm_number", 0.025000000000000)
        self.actionbutton_2.setProperty("incr_angular_number", -1.000000000000000)
        self.actionbutton_2.setProperty("toggle_float_option", False)
        self.actionbutton_2.setProperty("float_num", 100.000000000000000)
        self.actionbutton_2.setProperty("float_alt_num", 50.000000000000000)
        self.actionbutton_2.setProperty("ini_mdi_number", 0)

        self.gridLayout_12.addWidget(self.actionbutton_2, 0, 1, 2, 1)

        self.action_pause = ActionButton(self.frame_8)
        self.action_pause.setObjectName(u"action_pause")
        sizePolicy.setHeightForWidth(self.action_pause.sizePolicy().hasHeightForWidth())
        self.action_pause.setSizePolicy(sizePolicy)
        self.action_pause.setMinimumSize(QSize(80, 41))
        self.action_pause.setMaximumSize(QSize(80, 41))
        self.action_pause.setProperty("indicator_option", True)
        self.action_pause.setProperty("indicator_HAL_pin_option", True)
        self.action_pause.setProperty("on_color", QColor(255, 255, 0))
        self.action_pause.setProperty("indicator_size", 0.200000000000000)
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

        self.gridLayout_12.addWidget(self.action_pause, 0, 3, 2, 1)

        self.actionbutton_13 = ActionButton(self.frame_8)
        self.actionbutton_13.setObjectName(u"actionbutton_13")
        self.actionbutton_13.setMinimumSize(QSize(80, 40))
        self.actionbutton_13.setProperty("abort_action", True)

        self.gridLayout_12.addWidget(self.actionbutton_13, 0, 4, 2, 1)

        self.widget_runtime = QWidget(self.frame_8)
        self.widget_runtime.setObjectName(u"widget_runtime")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_runtime.sizePolicy().hasHeightForWidth())
        self.widget_runtime.setSizePolicy(sizePolicy1)
        self.widget_runtime.setMinimumSize(QSize(90, 55))
        self.widget_runtime.setMaximumSize(QSize(90, 55))
        self.verticalLayout_47 = QVBoxLayout(self.widget_runtime)
        self.verticalLayout_47.setSpacing(2)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 2)
        self.label_50 = QLabel(self.widget_runtime)
        self.label_50.setObjectName(u"label_50")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy2)
        self.label_50.setMinimumSize(QSize(0, 0))
        self.label_50.setMaximumSize(QSize(16777215, 16777215))
        self.label_50.setAlignment(Qt.AlignCenter)

        self.verticalLayout_47.addWidget(self.label_50)

        self.lbl_runtime = QLineEdit(self.widget_runtime)
        self.lbl_runtime.setObjectName(u"lbl_runtime")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lbl_runtime.sizePolicy().hasHeightForWidth())
        self.lbl_runtime.setSizePolicy(sizePolicy3)
        self.lbl_runtime.setMinimumSize(QSize(0, 28))
        self.lbl_runtime.setMaximumSize(QSize(16777215, 28))
        font = QFont()
        font.setPointSize(13)
        self.lbl_runtime.setFont(font)
        self.lbl_runtime.setAlignment(Qt.AlignCenter)
        self.lbl_runtime.setReadOnly(True)

        self.verticalLayout_47.addWidget(self.lbl_runtime)


        self.gridLayout_12.addWidget(self.widget_runtime, 0, 6, 2, 1)

        self.pushbutton_3 = PushButton(self.frame_8)
        self.pushbutton_3.setObjectName(u"pushbutton_3")
        sizePolicy.setHeightForWidth(self.pushbutton_3.sizePolicy().hasHeightForWidth())
        self.pushbutton_3.setSizePolicy(sizePolicy)
        self.pushbutton_3.setMinimumSize(QSize(80, 41))
        self.pushbutton_3.setProperty("python_command_option", True)

        self.gridLayout_12.addWidget(self.pushbutton_3, 0, 8, 2, 1)

        self.pushbutton_2 = PushButton(self.frame_8)
        self.pushbutton_2.setObjectName(u"pushbutton_2")
        sizePolicy.setHeightForWidth(self.pushbutton_2.sizePolicy().hasHeightForWidth())
        self.pushbutton_2.setSizePolicy(sizePolicy)
        self.pushbutton_2.setMinimumSize(QSize(80, 41))
        self.pushbutton_2.setProperty("indicator_option", False)
        self.pushbutton_2.setProperty("indicator_HAL_pin_option", False)
        self.pushbutton_2.setProperty("python_command_option", True)

        self.gridLayout_12.addWidget(self.pushbutton_2, 0, 9, 2, 1)

        self.pushbutton_5 = PushButton(self.frame_8)
        self.pushbutton_5.setObjectName(u"pushbutton_5")
        sizePolicy.setHeightForWidth(self.pushbutton_5.sizePolicy().hasHeightForWidth())
        self.pushbutton_5.setSizePolicy(sizePolicy)
        self.pushbutton_5.setMinimumSize(QSize(80, 41))
        self.pushbutton_5.setProperty("python_command_option", True)

        self.gridLayout_12.addWidget(self.pushbutton_5, 0, 10, 2, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_2, 0, 11, 2, 1)

        self.actionbutton_view_y2 = ActionButton(self.frame_8)
        self.actionbutton_view_y2.setObjectName(u"actionbutton_view_y2")
        sizePolicy.setHeightForWidth(self.actionbutton_view_y2.sizePolicy().hasHeightForWidth())
        self.actionbutton_view_y2.setSizePolicy(sizePolicy)
        self.actionbutton_view_y2.setMinimumSize(QSize(50, 40))
        self.actionbutton_view_y2.setMaximumSize(QSize(50, 40))
        self.actionbutton_view_y2.setProperty("view_change_action", True)

        self.gridLayout_12.addWidget(self.actionbutton_view_y2, 0, 12, 2, 1)

        self.actionbutton_view_y = ActionButton(self.frame_8)
        self.actionbutton_view_y.setObjectName(u"actionbutton_view_y")
        sizePolicy.setHeightForWidth(self.actionbutton_view_y.sizePolicy().hasHeightForWidth())
        self.actionbutton_view_y.setSizePolicy(sizePolicy)
        self.actionbutton_view_y.setMinimumSize(QSize(50, 40))
        self.actionbutton_view_y.setMaximumSize(QSize(50, 40))
        self.actionbutton_view_y.setBaseSize(QSize(60, 40))
        self.actionbutton_view_y.setCheckable(True)
        self.actionbutton_view_y.setAutoExclusive(True)
        self.actionbutton_view_y.setProperty("view_change_action", True)
        self.actionbutton_view_y.setProperty("template_label_option", False)
        self.actionbutton_view_y.setProperty("joint_number", 0)
        self.actionbutton_view_y.setProperty("incr_imperial_number", 0.010000000000000)
        self.actionbutton_view_y.setProperty("incr_mm_number", 0.025000000000000)
        self.actionbutton_view_y.setProperty("incr_angular_number", -1.000000000000000)
        self.actionbutton_view_y.setProperty("toggle_float_option", False)
        self.actionbutton_view_y.setProperty("float_num", 100.000000000000000)
        self.actionbutton_view_y.setProperty("float_alt_num", 50.000000000000000)
        self.actionbutton_view_y.setProperty("ini_mdi_number", 0)

        self.gridLayout_12.addWidget(self.actionbutton_view_y, 0, 13, 2, 1)

        self.actionbutton_clear = ActionButton(self.frame_8)
        self.actionbutton_clear.setObjectName(u"actionbutton_clear")
        sizePolicy.setHeightForWidth(self.actionbutton_clear.sizePolicy().hasHeightForWidth())
        self.actionbutton_clear.setSizePolicy(sizePolicy)
        self.actionbutton_clear.setMinimumSize(QSize(50, 40))
        self.actionbutton_clear.setMaximumSize(QSize(50, 40))
        self.actionbutton_clear.setBaseSize(QSize(60, 40))
        self.actionbutton_clear.setAutoFillBackground(False)
        self.actionbutton_clear.setCheckable(False)
        self.actionbutton_clear.setProperty("estop_action", False)
        self.actionbutton_clear.setProperty("view_change_action", True)
        self.actionbutton_clear.setProperty("template_label_option", False)
        self.actionbutton_clear.setProperty("joint_number", 0)
        self.actionbutton_clear.setProperty("incr_imperial_number", 0.010000000000000)
        self.actionbutton_clear.setProperty("incr_mm_number", 0.025000000000000)
        self.actionbutton_clear.setProperty("incr_angular_number", -1.000000000000000)
        self.actionbutton_clear.setProperty("toggle_float_option", False)
        self.actionbutton_clear.setProperty("float_num", 100.000000000000000)
        self.actionbutton_clear.setProperty("float_alt_num", 50.000000000000000)
        self.actionbutton_clear.setProperty("ini_mdi_number", 0)

        self.gridLayout_12.addWidget(self.actionbutton_clear, 0, 14, 2, 1)

        self.pushbutton_6 = PushButton(self.frame_8)
        self.pushbutton_6.setObjectName(u"pushbutton_6")
        sizePolicy.setHeightForWidth(self.pushbutton_6.sizePolicy().hasHeightForWidth())
        self.pushbutton_6.setSizePolicy(sizePolicy)
        self.pushbutton_6.setMinimumSize(QSize(80, 41))
        self.pushbutton_6.setProperty("python_command_option", True)

        self.gridLayout_12.addWidget(self.pushbutton_6, 0, 15, 2, 1)

        self.pushbutton_4 = PushButton(self.frame_8)
        self.pushbutton_4.setObjectName(u"pushbutton_4")
        sizePolicy.setHeightForWidth(self.pushbutton_4.sizePolicy().hasHeightForWidth())
        self.pushbutton_4.setSizePolicy(sizePolicy)
        self.pushbutton_4.setMinimumSize(QSize(80, 41))
        self.pushbutton_4.setProperty("python_command_option", True)
        self.pushbutton_4.setProperty("on_color", QColor(0, 255, 0))

        self.gridLayout_12.addWidget(self.pushbutton_4, 0, 16, 2, 1)

        self.pushbutton = PushButton(self.frame_8)
        self.pushbutton.setObjectName(u"pushbutton")
        sizePolicy.setHeightForWidth(self.pushbutton.sizePolicy().hasHeightForWidth())
        self.pushbutton.setSizePolicy(sizePolicy)
        self.pushbutton.setMinimumSize(QSize(80, 41))
        self.pushbutton.setProperty("python_command_option", True)

        self.gridLayout_12.addWidget(self.pushbutton, 0, 17, 2, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer, 1, 7, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.progressBar = QProgressBar(self.frame_8)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QSize(189, 25))
        self.progressBar.setMaximumSize(QSize(16777215, 20))
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setMaximum(99)
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setInvertedAppearance(False)

        self.horizontalLayout_14.addWidget(self.progressBar)


        self.gridLayout_12.addLayout(self.horizontalLayout_14, 0, 5, 2, 1)

        self.btn_start = ActionButton(self.frame_8)
        self.btn_start.setObjectName(u"btn_start")
        sizePolicy.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy)
        self.btn_start.setMinimumSize(QSize(80, 41))
        self.btn_start.setCheckable(True)
        self.btn_start.setProperty("indicator_option", True)
        self.btn_start.setProperty("indicator_HAL_pin_option", True)
        self.btn_start.setProperty("on_color", QColor(51, 255, 0))
        self.btn_start.setProperty("run_action", True)
        self.btn_start.setProperty("abort_action", False)
        self.btn_start.setProperty("template_label_option", False)
        self.btn_start.setProperty("joint_number", 0)
        self.btn_start.setProperty("incr_imperial_number", 0.010000000000000)
        self.btn_start.setProperty("incr_mm_number", 0.025000000000000)
        self.btn_start.setProperty("incr_angular_number", -1.000000000000000)
        self.btn_start.setProperty("toggle_float_option", False)
        self.btn_start.setProperty("float_num", 100.000000000000000)
        self.btn_start.setProperty("float_alt_num", 50.000000000000000)
        self.btn_start.setProperty("ini_mdi_number", 0)

        self.gridLayout_12.addWidget(self.btn_start, 0, 2, 2, 1)


        self.gridLayout_6.addWidget(self.frame_8, 2, 0, 1, 1)

        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setMinimumSize(QSize(0, 160))
        self.frame.setFrameShape(QFrame.WinPanel)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_spindle = QWidget(self.frame)
        self.widget_spindle.setObjectName(u"widget_spindle")
        self.gridLayout_17 = QGridLayout(self.widget_spindle)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_25 = QLabel(self.widget_spindle)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font)
        self.label_25.setStyleSheet(u"")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.label_25, 0, 0, 1, 1)

        self.widget_spindle_control = QWidget(self.widget_spindle)
        self.widget_spindle_control.setObjectName(u"widget_spindle_control")
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
        self.spindle_reverse.setMinimumSize(QSize(52, 41))
        self.spindle_reverse.setMaximumSize(QSize(50, 40))
        self.spindle_reverse.setFocusPolicy(Qt.NoFocus)
        self.spindle_reverse.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"images/spindle_fwd.png", QSize(), QIcon.Normal, QIcon.Off)
        self.spindle_reverse.setIcon(icon)
        self.spindle_reverse.setIconSize(QSize(18, 18))
        self.spindle_reverse.setCheckable(False)
        self.spindle_reverse.setAutoExclusive(False)
        self.spindle_reverse.setProperty("indicator_option", True)
        self.spindle_reverse.setProperty("indicator_HAL_pin_option", False)
        self.spindle_reverse.setProperty("indicator_status_option", True)
        self.spindle_reverse.setProperty("checked_state_text_option", False)
        self.spindle_reverse.setProperty("python_command_option", False)
        self.spindle_reverse.setProperty("on_color", QColor(255, 255, 0))
        self.spindle_reverse.setProperty("shape_option", 0)
        self.spindle_reverse.setProperty("off_color", QColor(0, 0, 0))
        self.spindle_reverse.setProperty("indicator_size", 0.200000000000000)
        self.spindle_reverse.setProperty("circle_diameter", 10.000000000000000)
        self.spindle_reverse.setProperty("right_edge_offset", 0.000000000000000)
        self.spindle_reverse.setProperty("top_edge_offset", 0.000000000000000)
        self.spindle_reverse.setProperty("corner_radius", 5.000000000000000)
        self.spindle_reverse.setProperty("height_fraction", 0.300000000000000)
        self.spindle_reverse.setProperty("width_fraction", 0.900000000000000)
        self.spindle_reverse.setProperty("invert_the_status", False)
        self.spindle_reverse.setProperty("is_paused_status", False)
        self.spindle_reverse.setProperty("is_estopped_status", False)
        self.spindle_reverse.setProperty("is_on_status", False)
        self.spindle_reverse.setProperty("is_idle_status", False)
        self.spindle_reverse.setProperty("is_homed_status", False)
        self.spindle_reverse.setProperty("is_flood_status", False)
        self.spindle_reverse.setProperty("is_mist_status", False)
        self.spindle_reverse.setProperty("is_block_delete_status", False)
        self.spindle_reverse.setProperty("is_optional_stop_status", False)
        self.spindle_reverse.setProperty("is_joint_homed_status", False)
        self.spindle_reverse.setProperty("is_limits_overridden_status", False)
        self.spindle_reverse.setProperty("is_manual_status", False)
        self.spindle_reverse.setProperty("is_mdi_status", False)
        self.spindle_reverse.setProperty("is_auto_status", False)
        self.spindle_reverse.setProperty("is_spindle_stopped_status", False)
        self.spindle_reverse.setProperty("is_spindle_fwd_status", False)
        self.spindle_reverse.setProperty("is_spindle_rev_status", True)
        self.spindle_reverse.setProperty("joint_number_status", 0)
        self.spindle_reverse.setProperty("spindle_fwd_action", False)
        self.spindle_reverse.setProperty("spindle_rev_action", True)
        self.spindle_reverse.setProperty("template_label_option", False)
        self.spindle_reverse.setProperty("joint_number", 0)
        self.spindle_reverse.setProperty("incr_imperial_number", 0.010000000000000)
        self.spindle_reverse.setProperty("incr_mm_number", 0.025000000000000)
        self.spindle_reverse.setProperty("incr_angular_number", -1.000000000000000)
        self.spindle_reverse.setProperty("toggle_float_option", False)
        self.spindle_reverse.setProperty("float_num", 0.200000000000000)
        self.spindle_reverse.setProperty("float_alt_num", 50.000000000000000)
        self.spindle_reverse.setProperty("ini_mdi_number", 0)

        self.horizontalLayout_16.addWidget(self.spindle_reverse)

        self.spindle_stop = ActionButton(self.widget_spindle_control)
        self.spindle_stop.setObjectName(u"spindle_stop")
        sizePolicy.setHeightForWidth(self.spindle_stop.sizePolicy().hasHeightForWidth())
        self.spindle_stop.setSizePolicy(sizePolicy)
        self.spindle_stop.setMinimumSize(QSize(50, 41))
        self.spindle_stop.setMaximumSize(QSize(50, 40))
        self.spindle_stop.setFocusPolicy(Qt.NoFocus)
        self.spindle_stop.setCheckable(False)
        self.spindle_stop.setChecked(False)
        self.spindle_stop.setAutoExclusive(False)
        self.spindle_stop.setProperty("indicator_option", True)
        self.spindle_stop.setProperty("indicator_HAL_pin_option", False)
        self.spindle_stop.setProperty("indicator_status_option", True)
        self.spindle_stop.setProperty("checked_state_text_option", False)
        self.spindle_stop.setProperty("python_command_option", False)
        self.spindle_stop.setProperty("on_color", QColor(0, 0, 0))
        self.spindle_stop.setProperty("shape_option", 0)
        self.spindle_stop.setProperty("off_color", QColor(255, 0, 0))
        self.spindle_stop.setProperty("indicator_size", 0.200000000000000)
        self.spindle_stop.setProperty("circle_diameter", 10.000000000000000)
        self.spindle_stop.setProperty("right_edge_offset", 0.000000000000000)
        self.spindle_stop.setProperty("top_edge_offset", 0.000000000000000)
        self.spindle_stop.setProperty("corner_radius", 5.000000000000000)
        self.spindle_stop.setProperty("height_fraction", 0.300000000000000)
        self.spindle_stop.setProperty("width_fraction", 0.900000000000000)
        self.spindle_stop.setProperty("invert_the_status", False)
        self.spindle_stop.setProperty("is_paused_status", False)
        self.spindle_stop.setProperty("is_estopped_status", False)
        self.spindle_stop.setProperty("is_on_status", False)
        self.spindle_stop.setProperty("is_idle_status", False)
        self.spindle_stop.setProperty("is_homed_status", False)
        self.spindle_stop.setProperty("is_flood_status", False)
        self.spindle_stop.setProperty("is_mist_status", False)
        self.spindle_stop.setProperty("is_block_delete_status", False)
        self.spindle_stop.setProperty("is_optional_stop_status", False)
        self.spindle_stop.setProperty("is_joint_homed_status", False)
        self.spindle_stop.setProperty("is_limits_overridden_status", False)
        self.spindle_stop.setProperty("is_manual_status", False)
        self.spindle_stop.setProperty("is_mdi_status", False)
        self.spindle_stop.setProperty("is_auto_status", False)
        self.spindle_stop.setProperty("is_spindle_stopped_status", True)
        self.spindle_stop.setProperty("is_spindle_fwd_status", False)
        self.spindle_stop.setProperty("is_spindle_rev_status", False)
        self.spindle_stop.setProperty("joint_number_status", 0)
        self.spindle_stop.setProperty("spindle_stop_action", True)
        self.spindle_stop.setProperty("template_label_option", False)
        self.spindle_stop.setProperty("joint_number", 0)
        self.spindle_stop.setProperty("incr_imperial_number", 0.010000000000000)
        self.spindle_stop.setProperty("incr_mm_number", 0.025000000000000)
        self.spindle_stop.setProperty("incr_angular_number", -1.000000000000000)
        self.spindle_stop.setProperty("toggle_float_option", False)
        self.spindle_stop.setProperty("float_num", 0.200000000000000)
        self.spindle_stop.setProperty("float_alt_num", 50.000000000000000)
        self.spindle_stop.setProperty("ini_mdi_number", 0)

        self.horizontalLayout_16.addWidget(self.spindle_stop)

        self.spindle_forward = ActionButton(self.widget_spindle_control)
        self.spindle_forward.setObjectName(u"spindle_forward")
        sizePolicy.setHeightForWidth(self.spindle_forward.sizePolicy().hasHeightForWidth())
        self.spindle_forward.setSizePolicy(sizePolicy)
        self.spindle_forward.setMinimumSize(QSize(52, 41))
        self.spindle_forward.setMaximumSize(QSize(50, 40))
        self.spindle_forward.setFocusPolicy(Qt.NoFocus)
        self.spindle_forward.setLayoutDirection(Qt.LeftToRight)
        icon1 = QIcon()
        icon1.addFile(u"images/spindle_rev.png", QSize(), QIcon.Normal, QIcon.Off)
        self.spindle_forward.setIcon(icon1)
        self.spindle_forward.setIconSize(QSize(18, 18))
        self.spindle_forward.setCheckable(False)
        self.spindle_forward.setAutoExclusive(False)
        self.spindle_forward.setProperty("indicator_option", True)
        self.spindle_forward.setProperty("indicator_HAL_pin_option", False)
        self.spindle_forward.setProperty("indicator_status_option", True)
        self.spindle_forward.setProperty("checked_state_text_option", False)
        self.spindle_forward.setProperty("python_command_option", False)
        self.spindle_forward.setProperty("on_color", QColor(0, 255, 0))
        self.spindle_forward.setProperty("shape_option", 0)
        self.spindle_forward.setProperty("off_color", QColor(0, 0, 0))
        self.spindle_forward.setProperty("indicator_size", 0.200000000000000)
        self.spindle_forward.setProperty("circle_diameter", 10.000000000000000)
        self.spindle_forward.setProperty("right_edge_offset", 0.000000000000000)
        self.spindle_forward.setProperty("top_edge_offset", 0.000000000000000)
        self.spindle_forward.setProperty("corner_radius", 5.000000000000000)
        self.spindle_forward.setProperty("height_fraction", 0.300000000000000)
        self.spindle_forward.setProperty("width_fraction", 0.900000000000000)
        self.spindle_forward.setProperty("invert_the_status", False)
        self.spindle_forward.setProperty("is_paused_status", False)
        self.spindle_forward.setProperty("is_estopped_status", False)
        self.spindle_forward.setProperty("is_on_status", False)
        self.spindle_forward.setProperty("is_idle_status", False)
        self.spindle_forward.setProperty("is_homed_status", False)
        self.spindle_forward.setProperty("is_flood_status", False)
        self.spindle_forward.setProperty("is_mist_status", False)
        self.spindle_forward.setProperty("is_block_delete_status", False)
        self.spindle_forward.setProperty("is_optional_stop_status", False)
        self.spindle_forward.setProperty("is_joint_homed_status", False)
        self.spindle_forward.setProperty("is_limits_overridden_status", False)
        self.spindle_forward.setProperty("is_manual_status", False)
        self.spindle_forward.setProperty("is_mdi_status", False)
        self.spindle_forward.setProperty("is_auto_status", False)
        self.spindle_forward.setProperty("is_spindle_stopped_status", False)
        self.spindle_forward.setProperty("is_spindle_fwd_status", True)
        self.spindle_forward.setProperty("is_spindle_rev_status", False)
        self.spindle_forward.setProperty("joint_number_status", 0)
        self.spindle_forward.setProperty("spindle_fwd_action", True)
        self.spindle_forward.setProperty("spindle_rev_action", False)
        self.spindle_forward.setProperty("template_label_option", False)
        self.spindle_forward.setProperty("joint_number", 0)
        self.spindle_forward.setProperty("incr_imperial_number", 0.010000000000000)
        self.spindle_forward.setProperty("incr_mm_number", 0.025000000000000)
        self.spindle_forward.setProperty("incr_angular_number", -1.000000000000000)
        self.spindle_forward.setProperty("toggle_float_option", False)
        self.spindle_forward.setProperty("float_num", 0.200000000000000)
        self.spindle_forward.setProperty("float_alt_num", 50.000000000000000)
        self.spindle_forward.setProperty("ini_mdi_number", 0)

        self.horizontalLayout_16.addWidget(self.spindle_forward)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setSpacing(4)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(-1, 0, -1, -1)
        self.label_18 = QLabel(self.widget_spindle_control)
        self.label_18.setObjectName(u"label_18")
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setMinimumSize(QSize(70, 16))
        self.label_18.setMaximumSize(QSize(60, 16))
        self.label_18.setStyleSheet(u"")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_35.addWidget(self.label_18, 0, Qt.AlignHCenter)

        self.stateled = StateLED(self.widget_spindle_control)
        self.stateled.setObjectName(u"stateled")
        self.stateled.setColor(QColor(0, 255, 0))
        self.stateled.setProperty("is_spindle_at_speed_status", True)

        self.verticalLayout_35.addWidget(self.stateled)


        self.horizontalLayout_16.addLayout(self.verticalLayout_35)


        self.gridLayout_17.addWidget(self.widget_spindle_control, 1, 0, 1, 2)

        self.lcdnumber = LCDNumber(self.widget_spindle)
        self.lcdnumber.setObjectName(u"lcdnumber")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lcdnumber.sizePolicy().hasHeightForWidth())
        self.lcdnumber.setSizePolicy(sizePolicy4)
        self.lcdnumber.setMinimumSize(QSize(165, 45))
        self.lcdnumber.setStyleSheet(u"color: rgb(51, 255, 0);\n"
"background-color: rgb(46, 52, 54);")

        self.gridLayout_17.addWidget(self.lcdnumber, 2, 0, 1, 1)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.actionbutton_11 = ActionButton(self.widget_spindle)
        self.actionbutton_11.setObjectName(u"actionbutton_11")
        sizePolicy.setHeightForWidth(self.actionbutton_11.sizePolicy().hasHeightForWidth())
        self.actionbutton_11.setSizePolicy(sizePolicy)
        self.actionbutton_11.setMinimumSize(QSize(70, 41))
        self.actionbutton_11.setMaximumSize(QSize(70, 16777215))
        self.actionbutton_11.setProperty("spindle_down_action", True)
        self.actionbutton_11.setProperty("float_num", 100.000000000000000)

        self.horizontalLayout_46.addWidget(self.actionbutton_11)

        self.actionbutton_12 = ActionButton(self.widget_spindle)
        self.actionbutton_12.setObjectName(u"actionbutton_12")
        sizePolicy.setHeightForWidth(self.actionbutton_12.sizePolicy().hasHeightForWidth())
        self.actionbutton_12.setSizePolicy(sizePolicy)
        self.actionbutton_12.setMinimumSize(QSize(70, 41))
        self.actionbutton_12.setMaximumSize(QSize(70, 16777215))
        self.actionbutton_12.setProperty("spindle_up_action", True)

        self.horizontalLayout_46.addWidget(self.actionbutton_12)


        self.gridLayout_17.addLayout(self.horizontalLayout_46, 2, 1, 1, 1)


        self.horizontalLayout_6.addWidget(self.widget_spindle)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_spindle_ovr = QFrame(self.frame)
        self.frame_spindle_ovr.setObjectName(u"frame_spindle_ovr")
        sizePolicy2.setHeightForWidth(self.frame_spindle_ovr.sizePolicy().hasHeightForWidth())
        self.frame_spindle_ovr.setSizePolicy(sizePolicy2)
        self.frame_spindle_ovr.setMinimumSize(QSize(0, 0))
        self.frame_spindle_ovr.setFrameShape(QFrame.WinPanel)
        self.frame_spindle_ovr.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_spindle_ovr)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.widget_spindle_ovr = QWidget(self.frame_spindle_ovr)
        self.widget_spindle_ovr.setObjectName(u"widget_spindle_ovr")
        self.verticalLayout_26 = QVBoxLayout(self.widget_spindle_ovr)
        self.verticalLayout_26.setSpacing(4)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(4, 0, 0, 0)
        self.label_4 = QLabel(self.widget_spindle_ovr)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        self.label_4.setMinimumSize(QSize(0, 30))
        self.label_4.setStyleSheet(u"")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_4)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setSpacing(4)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(-1, 1, -1, 5)
        self.action_spindle_ovr_50 = ActionButton(self.widget_spindle_ovr)
        self.action_spindle_ovr_50.setObjectName(u"action_spindle_ovr_50")
        sizePolicy2.setHeightForWidth(self.action_spindle_ovr_50.sizePolicy().hasHeightForWidth())
        self.action_spindle_ovr_50.setSizePolicy(sizePolicy2)
        self.action_spindle_ovr_50.setMinimumSize(QSize(50, 27))
        self.action_spindle_ovr_50.setMaximumSize(QSize(40, 27))
        self.action_spindle_ovr_50.setProperty("rapid_over_action", False)
        self.action_spindle_ovr_50.setProperty("spindle_over_action", True)
        self.action_spindle_ovr_50.setProperty("float_num", 50.000000000000000)

        self.horizontalLayout_34.addWidget(self.action_spindle_ovr_50, 0, Qt.AlignLeft)

        self.action_spindle_ovr_100 = ActionButton(self.widget_spindle_ovr)
        self.action_spindle_ovr_100.setObjectName(u"action_spindle_ovr_100")
        sizePolicy2.setHeightForWidth(self.action_spindle_ovr_100.sizePolicy().hasHeightForWidth())
        self.action_spindle_ovr_100.setSizePolicy(sizePolicy2)
        self.action_spindle_ovr_100.setMinimumSize(QSize(50, 27))
        self.action_spindle_ovr_100.setMaximumSize(QSize(40, 27))
        self.action_spindle_ovr_100.setProperty("rapid_over_action", False)
        self.action_spindle_ovr_100.setProperty("spindle_over_action", True)

        self.horizontalLayout_34.addWidget(self.action_spindle_ovr_100, 0, Qt.AlignHCenter)

        self.action_spindle_ovr_120 = ActionButton(self.widget_spindle_ovr)
        self.action_spindle_ovr_120.setObjectName(u"action_spindle_ovr_120")
        sizePolicy2.setHeightForWidth(self.action_spindle_ovr_120.sizePolicy().hasHeightForWidth())
        self.action_spindle_ovr_120.setSizePolicy(sizePolicy2)
        self.action_spindle_ovr_120.setMinimumSize(QSize(50, 27))
        self.action_spindle_ovr_120.setMaximumSize(QSize(50, 27))
        self.action_spindle_ovr_120.setProperty("rapid_over_action", False)
        self.action_spindle_ovr_120.setProperty("spindle_over_action", True)
        self.action_spindle_ovr_120.setProperty("float_num", 120.000000000000000)

        self.horizontalLayout_34.addWidget(self.action_spindle_ovr_120, 0, Qt.AlignRight)


        self.verticalLayout_26.addLayout(self.horizontalLayout_34)


        self.gridLayout_8.addWidget(self.widget_spindle_ovr, 0, 0, 1, 1)

        self.widget_spindle_info = QWidget(self.frame_spindle_ovr)
        self.widget_spindle_info.setObjectName(u"widget_spindle_info")
        sizePolicy1.setHeightForWidth(self.widget_spindle_info.sizePolicy().hasHeightForWidth())
        self.widget_spindle_info.setSizePolicy(sizePolicy1)
        self.verticalLayout_34 = QVBoxLayout(self.widget_spindle_info)
        self.verticalLayout_34.setSpacing(4)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 4, 0)
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setSpacing(4)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(-1, 0, 4, 0)
        self.label_22 = QLabel(self.widget_spindle_info)
        self.label_22.setObjectName(u"label_22")
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setMinimumSize(QSize(60, 35))
        self.label_22.setMaximumSize(QSize(60, 16777215))
        self.label_22.setFont(font)
        self.label_22.setStyleSheet(u"")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.label_22)

        self.status_spindle_ovr = StatusLabel(self.widget_spindle_info)
        self.status_spindle_ovr.setObjectName(u"status_spindle_ovr")
        sizePolicy.setHeightForWidth(self.status_spindle_ovr.sizePolicy().hasHeightForWidth())
        self.status_spindle_ovr.setSizePolicy(sizePolicy)
        self.status_spindle_ovr.setMinimumSize(QSize(60, 28))
        self.status_spindle_ovr.setMaximumSize(QSize(60, 35))
        self.status_spindle_ovr.setFont(font)
        self.status_spindle_ovr.setFrameShape(QFrame.WinPanel)
        self.status_spindle_ovr.setFrameShadow(QFrame.Sunken)
        self.status_spindle_ovr.setAlignment(Qt.AlignCenter)
        self.status_spindle_ovr.setProperty("feed_override_status", False)
        self.status_spindle_ovr.setProperty("rapid_override_status", False)
        self.status_spindle_ovr.setProperty("spindle_override_status", True)
        self.status_spindle_ovr.setProperty("jograte_status", False)

        self.horizontalLayout_32.addWidget(self.status_spindle_ovr)


        self.verticalLayout_34.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setSpacing(4)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(-1, 0, 4, 0)
        self.label_5 = QLabel(self.widget_spindle_info)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(60, 35))
        self.label_5.setMaximumSize(QSize(60, 16777215))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.label_5)

        self.label_spindle_set = StatusLabel(self.widget_spindle_info)
        self.label_spindle_set.setObjectName(u"label_spindle_set")
        sizePolicy.setHeightForWidth(self.label_spindle_set.sizePolicy().hasHeightForWidth())
        self.label_spindle_set.setSizePolicy(sizePolicy)
        self.label_spindle_set.setMinimumSize(QSize(60, 24))
        self.label_spindle_set.setMaximumSize(QSize(60, 35))
        self.label_spindle_set.setFont(font)
        self.label_spindle_set.setStyleSheet(u"")
        self.label_spindle_set.setFrameShape(QFrame.WinPanel)
        self.label_spindle_set.setFrameShadow(QFrame.Sunken)
        self.label_spindle_set.setLineWidth(2)
        self.label_spindle_set.setAlignment(Qt.AlignCenter)
        self.label_spindle_set.setProperty("requested_spindle_speed_status", True)
        self.label_spindle_set.setProperty("actual_spindle_speed_status", False)
        self.label_spindle_set.setProperty("overspeed", False)

        self.horizontalLayout_30.addWidget(self.label_spindle_set)


        self.verticalLayout_34.addLayout(self.horizontalLayout_30)


        self.gridLayout_8.addWidget(self.widget_spindle_info, 0, 1, 2, 1)

        self.slider_spindle_ovr = StatusSlider(self.frame_spindle_ovr)
        self.slider_spindle_ovr.setObjectName(u"slider_spindle_ovr")
        sizePolicy3.setHeightForWidth(self.slider_spindle_ovr.sizePolicy().hasHeightForWidth())
        self.slider_spindle_ovr.setSizePolicy(sizePolicy3)
        self.slider_spindle_ovr.setMinimumSize(QSize(180, 51))
        self.slider_spindle_ovr.setStyleSheet(u"QSlider::groove:horizontal {\n"
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
"QSlider::add-page:horizontal {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255,"
                        " 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"width: 40px;\n"
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
        self.slider_spindle_ovr.setMinimum(50)
        self.slider_spindle_ovr.setMaximum(120)
        self.slider_spindle_ovr.setSingleStep(1)
        self.slider_spindle_ovr.setValue(100)
        self.slider_spindle_ovr.setOrientation(Qt.Horizontal)
        self.slider_spindle_ovr.setProperty("rapid_rate", False)
        self.slider_spindle_ovr.setProperty("feed_rate", False)
        self.slider_spindle_ovr.setProperty("spindle_rate", True)
        self.slider_spindle_ovr.setProperty("jograte_rate", False)

        self.gridLayout_8.addWidget(self.slider_spindle_ovr, 1, 0, 1, 1)


        self.horizontalLayout_8.addWidget(self.frame_spindle_ovr)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_8)

        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy3.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy3)
        self.frame_9.setMinimumSize(QSize(0, 100))
        self.frame_9.setFrameShape(QFrame.WinPanel)
        self.frame_9.setFrameShadow(QFrame.Plain)
        self.gridLayout_9 = QGridLayout(self.frame_9)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_26 = QLabel(self.frame_9)
        self.label_26.setObjectName(u"label_26")
        sizePolicy2.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy2)
        self.label_26.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_26.setFont(font1)

        self.gridLayout_9.addWidget(self.label_26, 0, 0, 1, 1)

        self.label_9 = QLabel(self.frame_9)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setMinimumSize(QSize(0, 0))
        self.label_9.setFont(font1)

        self.gridLayout_9.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_28 = QLabel(self.frame_9)
        self.label_28.setObjectName(u"label_28")
        sizePolicy2.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy2)
        self.label_28.setMinimumSize(QSize(0, 0))
        self.label_28.setFont(font)

        self.gridLayout_9.addWidget(self.label_28, 3, 0, 1, 1)

        self.label_12 = QLabel(self.frame_9)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_9.addWidget(self.label_12, 2, 0, 1, 1)

        self.statuslabel_6 = StatusLabel(self.frame_9)
        self.statuslabel_6.setObjectName(u"statuslabel_6")
        sizePolicy3.setHeightForWidth(self.statuslabel_6.sizePolicy().hasHeightForWidth())
        self.statuslabel_6.setSizePolicy(sizePolicy3)
        self.statuslabel_6.setMinimumSize(QSize(70, 30))
        self.statuslabel_6.setFont(font1)
        self.statuslabel_6.setFrameShape(QFrame.WinPanel)
        self.statuslabel_6.setFrameShadow(QFrame.Sunken)
        self.statuslabel_6.setAlignment(Qt.AlignCenter)
        self.statuslabel_6.setProperty("feed_override_status", False)
        self.statuslabel_6.setProperty("actual_surface_speed_status", True)

        self.gridLayout_9.addWidget(self.statuslabel_6, 1, 1, 1, 2)

        self.statuslabel_14 = StatusLabel(self.frame_9)
        self.statuslabel_14.setObjectName(u"statuslabel_14")
        sizePolicy3.setHeightForWidth(self.statuslabel_14.sizePolicy().hasHeightForWidth())
        self.statuslabel_14.setSizePolicy(sizePolicy3)
        self.statuslabel_14.setMinimumSize(QSize(0, 30))
        self.statuslabel_14.setFrameShape(QFrame.WinPanel)
        self.statuslabel_14.setFrameShadow(QFrame.Sunken)
        self.statuslabel_14.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextEditable)
        self.statuslabel_14.setProperty("feed_override_status", False)

        self.gridLayout_9.addWidget(self.statuslabel_14, 0, 1, 1, 2)

        self.statuslabel_11 = StatusLabel(self.frame_9)
        self.statuslabel_11.setObjectName(u"statuslabel_11")
        sizePolicy3.setHeightForWidth(self.statuslabel_11.sizePolicy().hasHeightForWidth())
        self.statuslabel_11.setSizePolicy(sizePolicy3)
        self.statuslabel_11.setMinimumSize(QSize(60, 30))
        self.statuslabel_11.setFrameShape(QFrame.WinPanel)
        self.statuslabel_11.setFrameShadow(QFrame.Sunken)
        self.statuslabel_11.setAlignment(Qt.AlignCenter)
        self.statuslabel_11.setProperty("current_feedrate_status", False)
        self.statuslabel_11.setProperty("current_FPU_status", True)

        self.gridLayout_9.addWidget(self.statuslabel_11, 2, 1, 1, 2)

        self.label_27 = QLabel(self.frame_9)
        self.label_27.setObjectName(u"label_27")
        sizePolicy3.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy3)
        self.label_27.setMinimumSize(QSize(0, 30))
        self.label_27.setFont(font)
        self.label_27.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_27.setFrameShape(QFrame.WinPanel)
        self.label_27.setFrameShadow(QFrame.Sunken)
        self.label_27.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_27, 3, 1, 1, 2)


        self.horizontalLayout_2.addWidget(self.frame_9)


        self.gridLayout_19.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setMinimumSize(QSize(0, 160))
        self.frame_2.setMaximumSize(QSize(400, 16777215))
        self.frame_2.setFrameShape(QFrame.WinPanel)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.droPaneStack = QStackedWidget(self.frame_2)
        self.droPaneStack.setObjectName(u"droPaneStack")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.droPaneStack.sizePolicy().hasHeightForWidth())
        self.droPaneStack.setSizePolicy(sizePolicy5)
        self.droPaneStack.setStyleSheet(u"DROLabel {\n"
"    background-color: black;\n"
"/*    border: 2px solid black;*/\n"
"    font: 20pt \"Lato Heavy\";\n"
"    color: #00FF00;\n"
"}\n"
"\n"
"DROLabel[homed=false] {\n"
"    color: red;\n"
"}\n"
"")
        self.machine_page = QWidget()
        self.machine_page.setObjectName(u"machine_page")
        self.gridLayout = QGridLayout(self.machine_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_dro_title = QLabel(self.machine_page)
        self.label_dro_title.setObjectName(u"label_dro_title")
        sizePolicy5.setHeightForWidth(self.label_dro_title.sizePolicy().hasHeightForWidth())
        self.label_dro_title.setSizePolicy(sizePolicy5)
        self.label_dro_title.setMaximumSize(QSize(16777215, 20))
        self.label_dro_title.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 138, 0);")

        self.gridLayout.addWidget(self.label_dro_title, 0, 0, 1, 1)

        self.label_x = QLabel(self.machine_page)
        self.label_x.setObjectName(u"label_x")
        self.label_x.setMinimumSize(QSize(0, 44))
        self.label_x.setAlignment(Qt.AlignCenter)
        self.label_x.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextEditable)

        self.gridLayout.addWidget(self.label_x, 1, 0, 1, 1)

        self.dro_label_x = DROLabel(self.machine_page)
        self.dro_label_x.setObjectName(u"dro_label_x")
        self.dro_label_x.setMinimumSize(QSize(0, 40))
        self.dro_label_x.setStyleSheet(u"DROLabel {\n"
"    background-color: black;\n"
"/*    border: 2px solid black;*/\n"
"    font: 20pt \"Lato Heavy\";\n"
"    color: #00FF00;\n"
"}\n"
"\n"
"DROLabel[homed=false] {\n"
"    color:  rgb(255, 138, 0);\n"
"}")
        self.dro_label_x.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dro_label_x.setProperty("always_display_radius", True)
        self.dro_label_x.setProperty("homed", False)

        self.gridLayout.addWidget(self.dro_label_x, 1, 1, 1, 1)

        self.label_x_diametr = QLabel(self.machine_page)
        self.label_x_diametr.setObjectName(u"label_x_diametr")
        self.label_x_diametr.setMinimumSize(QSize(0, 44))
        self.label_x_diametr.setStyleSheet(u"color: rgb(204, 0, 255);")
        self.label_x_diametr.setAlignment(Qt.AlignCenter)
        self.label_x_diametr.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextEditable)

        self.gridLayout.addWidget(self.label_x_diametr, 2, 0, 1, 1)

        self.dro_label = DROLabel(self.machine_page)
        self.dro_label.setObjectName(u"dro_label")
        self.dro_label.setMinimumSize(QSize(0, 40))
        self.dro_label.setStyleSheet(u"DROLabel {	\n"
"    background-color: black;\n"
"/*    border: 2px solid black;*/\n"
"    font: 20pt \"Lato Heavy\";\n"
"    color: #00FF00;\n"
"}\n"
"\n"
"DROLabel[homed=false] {\n"
"   color: rgb(204, 0, 255);\n"
"}")
        self.dro_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dro_label.setProperty("always_display_diameter", True)
        self.dro_label.setProperty("homed", False)

        self.gridLayout.addWidget(self.dro_label, 2, 1, 1, 1)

        self.label_z = QLabel(self.machine_page)
        self.label_z.setObjectName(u"label_z")
        self.label_z.setMinimumSize(QSize(0, 44))
        self.label_z.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_z, 3, 0, 1, 1)

        self.dro_label_z = DROLabel(self.machine_page)
        self.dro_label_z.setObjectName(u"dro_label_z")
        self.dro_label_z.setMinimumSize(QSize(0, 40))
        self.dro_label_z.setStyleSheet(u"DROLabel {\n"
"    background-color: black;\n"
"/*    border: 2px solid black;*/\n"
"    font: 20pt \"Lato Heavy\";\n"
"    color: #00FF00;\n"
"}\n"
"\n"
"DROLabel[homed=false] {\n"
"    color: rgb(255, 138, 0);\n"
"}\n"
"")
        self.dro_label_z.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dro_label_z.setProperty("Qjoint_number", 2)
        self.dro_label_z.setProperty("homed", False)

        self.gridLayout.addWidget(self.dro_label_z, 3, 1, 1, 1)

        self.droPaneStack.addWidget(self.machine_page)
        self.user_page = QWidget()
        self.user_page.setObjectName(u"user_page")
        self.gridLayout_5 = QGridLayout(self.user_page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_dro_title_3 = StatusLabel(self.user_page)
        self.label_dro_title_3.setObjectName(u"label_dro_title_3")
        sizePolicy5.setHeightForWidth(self.label_dro_title_3.sizePolicy().hasHeightForWidth())
        self.label_dro_title_3.setSizePolicy(sizePolicy5)
        self.label_dro_title_3.setMaximumSize(QSize(16777215, 20))
        self.label_dro_title_3.setStyleSheet(u"color: rgb(51, 255, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.label_dro_title_3.setProperty("user_system_status", True)

        self.gridLayout_5.addWidget(self.label_dro_title_3, 0, 0, 1, 1)

        self.label_x_2 = QLabel(self.user_page)
        self.label_x_2.setObjectName(u"label_x_2")
        self.label_x_2.setMinimumSize(QSize(0, 44))
        self.label_x_2.setStyleSheet(u"color: rgb(51, 255, 0);")
        self.label_x_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_x_2, 1, 0, 1, 1)

        self.dro_label_x_2 = DROLabel(self.user_page)
        self.dro_label_x_2.setObjectName(u"dro_label_x_2")
        self.dro_label_x_2.setMinimumSize(QSize(0, 40))
        self.dro_label_x_2.setStyleSheet(u"DROLabel {\n"
"    background-color: black;\n"
"/*    border: 2px solid black;*/\n"
"    font: 20pt \"Lato Heavy\";\n"
"    color: #00FF00;\n"
"}\n"
"\n"
"DROLabel[homed=false] {\n"
"    color: red;\n"
"}")
        self.dro_label_x_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dro_label_x_2.setProperty("always_display_radius", True)
        self.dro_label_x_2.setProperty("Qreference_type", 1)
        self.dro_label_x_2.setProperty("homed", True)

        self.gridLayout_5.addWidget(self.dro_label_x_2, 1, 1, 1, 1)

        self.label_x_diametr_2 = QLabel(self.user_page)
        self.label_x_diametr_2.setObjectName(u"label_x_diametr_2")
        self.label_x_diametr_2.setMinimumSize(QSize(0, 44))
        self.label_x_diametr_2.setStyleSheet(u"color: rgb(204, 0, 255);")
        self.label_x_diametr_2.setAlignment(Qt.AlignCenter)
        self.label_x_diametr_2.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextEditable)

        self.gridLayout_5.addWidget(self.label_x_diametr_2, 2, 0, 1, 1)

        self.dro_label_2 = DROLabel(self.user_page)
        self.dro_label_2.setObjectName(u"dro_label_2")
        self.dro_label_2.setMinimumSize(QSize(0, 40))
        self.dro_label_2.setStyleSheet(u"DROLabel {	\n"
"    background-color: black;\n"
"/*    border: 2px solid black;*/\n"
"    font: 20pt \"Lato Heavy\";\n"
"    color: #00FF00;\n"
"}\n"
"\n"
"DROLabel[homed=false] {\n"
"   color: rgb(204, 0, 255);\n"
"}")
        self.dro_label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dro_label_2.setProperty("always_display_diameter", True)
        self.dro_label_2.setProperty("Qreference_type", 1)
        self.dro_label_2.setProperty("homed", False)

        self.gridLayout_5.addWidget(self.dro_label_2, 2, 1, 1, 1)

        self.label_z_2 = QLabel(self.user_page)
        self.label_z_2.setObjectName(u"label_z_2")
        self.label_z_2.setMinimumSize(QSize(0, 44))
        self.label_z_2.setStyleSheet(u"color: rgb(51, 255, 0);")
        self.label_z_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_z_2, 3, 0, 1, 1)

        self.dro_label_z_2 = DROLabel(self.user_page)
        self.dro_label_z_2.setObjectName(u"dro_label_z_2")
        self.dro_label_z_2.setMinimumSize(QSize(0, 40))
        self.dro_label_z_2.setStyleSheet(u"DROLabel {\n"
"    background-color: black;\n"
"/*    border: 2px solid black;*/\n"
"    font: 20pt \"Lato Heavy\";\n"
"    color: #00FF00;\n"
"}\n"
"\n"
"DROLabel[homed=false] {\n"
"    color: red;\n"
"}")
        self.dro_label_z_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dro_label_z_2.setProperty("Qjoint_number", 2)
        self.dro_label_z_2.setProperty("Qreference_type", 1)
        self.dro_label_z_2.setProperty("homed", True)

        self.gridLayout_5.addWidget(self.dro_label_z_2, 3, 1, 1, 1)

        self.droPaneStack.addWidget(self.user_page)
        self.dtg_page = QWidget()
        self.dtg_page.setObjectName(u"dtg_page")
        self.gridLayout_21 = QGridLayout(self.dtg_page)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label_dro_title_2 = QLabel(self.dtg_page)
        self.label_dro_title_2.setObjectName(u"label_dro_title_2")
        sizePolicy5.setHeightForWidth(self.label_dro_title_2.sizePolicy().hasHeightForWidth())
        self.label_dro_title_2.setSizePolicy(sizePolicy5)
        self.label_dro_title_2.setMaximumSize(QSize(16777215, 20))
        self.label_dro_title_2.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(252, 233, 79);")

        self.gridLayout_21.addWidget(self.label_dro_title_2, 0, 0, 1, 1)

        self.label_x_3 = QLabel(self.dtg_page)
        self.label_x_3.setObjectName(u"label_x_3")
        self.label_x_3.setMinimumSize(QSize(0, 44))
        self.label_x_3.setStyleSheet(u"color: rgb(252, 233, 79);")
        self.label_x_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.label_x_3, 1, 0, 1, 1)

        self.dro_label_x_3 = DROLabel(self.dtg_page)
        self.dro_label_x_3.setObjectName(u"dro_label_x_3")
        self.dro_label_x_3.setMinimumSize(QSize(0, 40))
        self.dro_label_x_3.setStyleSheet(u"DROLabel {\n"
"    background-color: black;\n"
"/*    border: 2px solid black;*/\n"
"    font: 20pt \"Lato Heavy\";\n"
"    color: #00FF00;\n"
"}\n"
"\n"
"DROLabel[homed=false] {\n"
"    color: red;\n"
"}")
        self.dro_label_x_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dro_label_x_3.setProperty("always_display_radius", True)
        self.dro_label_x_3.setProperty("Qjoint_number", 0)
        self.dro_label_x_3.setProperty("Qreference_type", 2)
        self.dro_label_x_3.setProperty("homed", True)

        self.gridLayout_21.addWidget(self.dro_label_x_3, 1, 1, 1, 1)

        self.label_x_diametr_3 = QLabel(self.dtg_page)
        self.label_x_diametr_3.setObjectName(u"label_x_diametr_3")
        self.label_x_diametr_3.setMinimumSize(QSize(0, 44))
        self.label_x_diametr_3.setStyleSheet(u"color: rgb(204, 0, 255);")
        self.label_x_diametr_3.setAlignment(Qt.AlignCenter)
        self.label_x_diametr_3.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextEditable)

        self.gridLayout_21.addWidget(self.label_x_diametr_3, 2, 0, 1, 1)

        self.dro_label_3 = DROLabel(self.dtg_page)
        self.dro_label_3.setObjectName(u"dro_label_3")
        self.dro_label_3.setMinimumSize(QSize(0, 40))
        self.dro_label_3.setStyleSheet(u"DROLabel {	\n"
"    background-color: black;\n"
"/*    border: 2px solid black;*/\n"
"    font: 20pt \"Lato Heavy\";\n"
"    color: #00FF00;\n"
"}\n"
"\n"
"DROLabel[homed=false] {\n"
"   color: rgb(204, 0, 255);\n"
"}")
        self.dro_label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dro_label_3.setProperty("always_display_diameter", True)
        self.dro_label_3.setProperty("Qreference_type", 2)
        self.dro_label_3.setProperty("homed", False)

        self.gridLayout_21.addWidget(self.dro_label_3, 2, 1, 1, 1)

        self.label_z_3 = QLabel(self.dtg_page)
        self.label_z_3.setObjectName(u"label_z_3")
        self.label_z_3.setMinimumSize(QSize(0, 44))
        self.label_z_3.setStyleSheet(u"color: rgb(252, 233, 79);")
        self.label_z_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.label_z_3, 3, 0, 1, 1)

        self.dro_label_z_3 = DROLabel(self.dtg_page)
        self.dro_label_z_3.setObjectName(u"dro_label_z_3")
        self.dro_label_z_3.setMinimumSize(QSize(0, 40))
        self.dro_label_z_3.setStyleSheet(u"DROLabel {\n"
"    background-color: black;\n"
"/*    border: 2px solid black;*/\n"
"    font: 20pt \"Lato Heavy\";\n"
"    color: #00FF00;\n"
"}\n"
"\n"
"DROLabel[homed=false] {\n"
"    color: red;\n"
"}")
        self.dro_label_z_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dro_label_z_3.setProperty("Qjoint_number", 2)
        self.dro_label_z_3.setProperty("Qreference_type", 2)
        self.dro_label_z_3.setProperty("homed", True)

        self.gridLayout_21.addWidget(self.dro_label_z_3, 3, 1, 1, 1)

        self.droPaneStack.addWidget(self.dtg_page)

        self.verticalLayout_2.addWidget(self.droPaneStack)


        self.gridLayout_19.addWidget(self.frame_2, 0, 1, 1, 1)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QSize(200, 160))
        self.frame_3.setMaximumSize(QSize(16777215, 160))
        self.frame_3.setFrameShape(QFrame.WinPanel)
        self.gridLayout_10 = QGridLayout(self.frame_3)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.action_exit = ActionButton(self.frame_3)
        self.action_exit.setObjectName(u"action_exit")
        sizePolicy.setHeightForWidth(self.action_exit.sizePolicy().hasHeightForWidth())
        self.action_exit.setSizePolicy(sizePolicy)
        self.action_exit.setMinimumSize(QSize(100, 48))
        self.action_exit.setMaximumSize(QSize(16777215, 48))
        self.action_exit.setBaseSize(QSize(90, 50))
        self.action_exit.setProperty("exit_action", True)
        self.action_exit.setProperty("template_label_option", False)
        self.action_exit.setProperty("joint_number", 0)
        self.action_exit.setProperty("incr_imperial_number", 0.010000000000000)
        self.action_exit.setProperty("incr_mm_number", 0.025000000000000)
        self.action_exit.setProperty("incr_angular_number", -1.000000000000000)
        self.action_exit.setProperty("toggle_float_option", False)
        self.action_exit.setProperty("float_num", 100.000000000000000)
        self.action_exit.setProperty("float_alt_num", 50.000000000000000)
        self.action_exit.setProperty("ini_mdi_number", 0)

        self.horizontalLayout_17.addWidget(self.action_exit)


        self.gridLayout_10.addLayout(self.horizontalLayout_17, 0, 0, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setMinimumSize(QSize(179, 79))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.statuslabel_3 = StatusLabel(self.frame_10)
        self.statuslabel_3.setObjectName(u"statuslabel_3")
        sizePolicy3.setHeightForWidth(self.statuslabel_3.sizePolicy().hasHeightForWidth())
        self.statuslabel_3.setSizePolicy(sizePolicy3)
        self.statuslabel_3.setMinimumSize(QSize(0, 35))
        self.statuslabel_3.setMaximumSize(QSize(16777215, 35))
        font2 = QFont()
        font2.setPointSize(12)
        self.statuslabel_3.setFont(font2)
        self.statuslabel_3.setAlignment(Qt.AlignCenter)
        self.statuslabel_3.setProperty("time_stamp_status", True)

        self.gridLayout_2.addWidget(self.statuslabel_3, 2, 0, 1, 1)

        self.label_17 = QLabel(self.frame_10)
        self.label_17.setObjectName(u"label_17")
        sizePolicy2.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy2)
        self.label_17.setMinimumSize(QSize(0, 30))
        self.label_17.setMaximumSize(QSize(16777215, 30))
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_17, 1, 0, 1, 1)


        self.horizontalLayout_15.addWidget(self.frame_10)


        self.gridLayout_10.addLayout(self.horizontalLayout_15, 1, 0, 1, 1)


        self.gridLayout_19.addWidget(self.frame_3, 0, 2, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_19, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.mainLeftStack = QStackedWidget(self.centralwidget)
        self.mainLeftStack.setObjectName(u"mainLeftStack")
        sizePolicy6 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.mainLeftStack.sizePolicy().hasHeightForWidth())
        self.mainLeftStack.setSizePolicy(sizePolicy6)
        self.mainLeftStack.setFrameShape(QFrame.WinPanel)
        self.programPage = QWidget()
        self.programPage.setObjectName(u"programPage")
        self.verticalLayout_24 = QVBoxLayout(self.programPage)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_mode = QLabel(self.programPage)
        self.label_mode.setObjectName(u"label_mode")

        self.verticalLayout_24.addWidget(self.label_mode)

        self.statuslabel_13 = StatusLabel(self.programPage)
        self.statuslabel_13.setObjectName(u"statuslabel_13")
        self.statuslabel_13.setProperty("filename_status", True)

        self.verticalLayout_24.addWidget(self.statuslabel_13)

        self.gcode_viewer = GcodeEditor(self.programPage)
        self.gcode_viewer.setObjectName(u"gcode_viewer")
        self.gcode_viewer.setProperty("auto_show_mdi_status", False)

        self.verticalLayout_24.addWidget(self.gcode_viewer)

        self.mainLeftStack.addWidget(self.programPage)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        sizePolicy1.setHeightForWidth(self.page_3.sizePolicy().hasHeightForWidth())
        self.page_3.setSizePolicy(sizePolicy1)
        self.page_3.setMaximumSize(QSize(730, 16777215))
        self.verticalLayout = QVBoxLayout(self.page_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_setup = QVBoxLayout()
        self.verticalLayout_setup.setObjectName(u"verticalLayout_setup")
        self.verticalLayout_setup.setSizeConstraint(QLayout.SetFixedSize)

        self.verticalLayout.addLayout(self.verticalLayout_setup)

        self.mainLeftStack.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_29 = QVBoxLayout(self.page_2)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.gcodegraphics = GCodeGraphics(self.page_2)
        self.gcodegraphics.setObjectName(u"gcodegraphics")
        self.gcodegraphics.setProperty("background_color", QColor(0, 0, 0, 150))
        self.gcodegraphics.setProperty("_use_gradient_background", False)

        self.verticalLayout_28.addWidget(self.gcodegraphics)


        self.verticalLayout_29.addLayout(self.verticalLayout_28)

        self.mainLeftStack.addWidget(self.page_2)

        self.verticalLayout_3.addWidget(self.mainLeftStack)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.mainPaneStack = QStackedWidget(self.centralwidget)
        self.mainPaneStack.setObjectName(u"mainPaneStack")
        self.mainPaneStack.setStyleSheet(u"")
        self.mainPaneStack.setFrameShape(QFrame.NoFrame)
        self.operationPage = QWidget()
        self.operationPage.setObjectName(u"operationPage")
        self.verticalLayout_4 = QVBoxLayout(self.operationPage)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_4 = QFrame(self.operationPage)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.WinPanel)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.statuslabel = StatusLabel(self.frame_4)
        self.statuslabel.setObjectName(u"statuslabel")
        font3 = QFont()
        font3.setBold(True)
        self.statuslabel.setFont(font3)
        self.statuslabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.statuslabel.setProperty("gcodes_status", True)

        self.verticalLayout_5.addWidget(self.statuslabel)


        self.horizontalLayout_5.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.operationPage)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.WinPanel)
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.statelabel = StateLabel(self.frame_5)
        self.statelabel.setObjectName(u"statelabel")

        self.verticalLayout_6.addWidget(self.statelabel)


        self.horizontalLayout_5.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.operationPage)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.WinPanel)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.statuslabel_2 = StatusLabel(self.frame_6)
        self.statuslabel_2.setObjectName(u"statuslabel_2")
        self.statuslabel_2.setProperty("tool_number_status", True)

        self.verticalLayout_7.addWidget(self.statuslabel_2)


        self.horizontalLayout_5.addWidget(self.frame_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.widgetswitcher = WidgetSwitcher(self.operationPage)
        self.widgetswitcher.setObjectName(u"widgetswitcher")
        self.tooloffsetsPage = QWidget()
        self.tooloffsetsPage.setObjectName(u"tooloffsetsPage")
        self.verticalLayout_30 = QVBoxLayout(self.tooloffsetsPage)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.toffsetspage = QFrame(self.tooloffsetsPage)
        self.toffsetspage.setObjectName(u"toffsetspage")
        self.toffsetspage.setFrameShape(QFrame.WinPanel)
        self.toffsetspage.setFrameShadow(QFrame.Plain)
        self.gridLayout_13 = QGridLayout(self.toffsetspage)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_20 = QLabel(self.toffsetspage)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_13.addWidget(self.label_20, 0, 0, 1, 1)

        self.tooloffsetview = ToolOffsetView(self.toffsetspage)
        self.tooloffsetview.setObjectName(u"tooloffsetview")
        sizePolicy2.setHeightForWidth(self.tooloffsetview.sizePolicy().hasHeightForWidth())
        self.tooloffsetview.setSizePolicy(sizePolicy2)
        self.tooloffsetview.setMinimumSize(QSize(0, 0))

        self.gridLayout_13.addWidget(self.tooloffsetview, 1, 0, 1, 1)

        self.frm_tooledit = QFrame(self.toffsetspage)
        self.frm_tooledit.setObjectName(u"frm_tooledit")
        sizePolicy1.setHeightForWidth(self.frm_tooledit.sizePolicy().hasHeightForWidth())
        self.frm_tooledit.setSizePolicy(sizePolicy1)
        self.frm_tooledit.setMinimumSize(QSize(92, 0))
        self.frm_tooledit.setFrameShape(QFrame.WinPanel)
        self.frm_tooledit.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frm_tooledit)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(4, 4, 4, 4)
        self.btn_tool_add = PushButton(self.frm_tooledit)
        self.btn_tool_add.setObjectName(u"btn_tool_add")
        sizePolicy.setHeightForWidth(self.btn_tool_add.sizePolicy().hasHeightForWidth())
        self.btn_tool_add.setSizePolicy(sizePolicy)
        self.btn_tool_add.setMinimumSize(QSize(80, 50))
        self.btn_tool_add.setMaximumSize(QSize(80, 50))
        self.btn_tool_add.setProperty("python_command_option", True)

        self.gridLayout_14.addWidget(self.btn_tool_add, 0, 0, 1, 1)

        self.btn_tool_delete = PushButton(self.frm_tooledit)
        self.btn_tool_delete.setObjectName(u"btn_tool_delete")
        sizePolicy.setHeightForWidth(self.btn_tool_delete.sizePolicy().hasHeightForWidth())
        self.btn_tool_delete.setSizePolicy(sizePolicy)
        self.btn_tool_delete.setMinimumSize(QSize(80, 50))
        self.btn_tool_delete.setMaximumSize(QSize(80, 50))
        self.btn_tool_delete.setProperty("python_command_option", True)

        self.gridLayout_14.addWidget(self.btn_tool_delete, 1, 0, 1, 1)

        self.btn_m61 = QPushButton(self.frm_tooledit)
        self.btn_m61.setObjectName(u"btn_m61")
        sizePolicy.setHeightForWidth(self.btn_m61.sizePolicy().hasHeightForWidth())
        self.btn_m61.setSizePolicy(sizePolicy)
        self.btn_m61.setMinimumSize(QSize(80, 50))
        self.btn_m61.setMaximumSize(QSize(80, 50))

        self.gridLayout_14.addWidget(self.btn_m61, 2, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_8, 3, 0, 1, 1)


        self.gridLayout_13.addWidget(self.frm_tooledit, 1, 1, 1, 1)


        self.verticalLayout_30.addWidget(self.toffsetspage)

        self.widgetswitcher.addWidget(self.tooloffsetsPage)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_23 = QVBoxLayout(self.page)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")

        self.verticalLayout_23.addLayout(self.verticalLayout_18)

        self.widgetswitcher.addWidget(self.page)
        self.workoffsetsPage = QWidget()
        self.workoffsetsPage.setObjectName(u"workoffsetsPage")
        self.verticalLayout_31 = QVBoxLayout(self.workoffsetsPage)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.woffsetspage = QFrame(self.workoffsetsPage)
        self.woffsetspage.setObjectName(u"woffsetspage")
        self.woffsetspage.setFrameShape(QFrame.WinPanel)
        self.woffsetspage.setFrameShadow(QFrame.Plain)
        self.gridLayout_16 = QGridLayout(self.woffsetspage)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.frm_zero_offsets = QFrame(self.woffsetspage)
        self.frm_zero_offsets.setObjectName(u"frm_zero_offsets")
        sizePolicy1.setHeightForWidth(self.frm_zero_offsets.sizePolicy().hasHeightForWidth())
        self.frm_zero_offsets.setSizePolicy(sizePolicy1)
        self.frm_zero_offsets.setMinimumSize(QSize(92, 542))
        self.frm_zero_offsets.setFrameShape(QFrame.WinPanel)
        self.frm_zero_offsets.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frm_zero_offsets)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(4, 4, 4, 4)
        self.action_zero_g92 = ActionButton(self.frm_zero_offsets)
        self.action_zero_g92.setObjectName(u"action_zero_g92")
        sizePolicy.setHeightForWidth(self.action_zero_g92.sizePolicy().hasHeightForWidth())
        self.action_zero_g92.setSizePolicy(sizePolicy)
        self.action_zero_g92.setMinimumSize(QSize(80, 50))
        self.action_zero_g92.setMaximumSize(QSize(80, 50))
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

        self.gridLayout_15.addWidget(self.action_zero_g92, 0, 0, 1, 1)

        self.action_zero_g5x = ActionButton(self.frm_zero_offsets)
        self.action_zero_g5x.setObjectName(u"action_zero_g5x")
        sizePolicy.setHeightForWidth(self.action_zero_g5x.sizePolicy().hasHeightForWidth())
        self.action_zero_g5x.setSizePolicy(sizePolicy)
        self.action_zero_g5x.setMinimumSize(QSize(80, 50))
        self.action_zero_g5x.setMaximumSize(QSize(80, 50))
        self.action_zero_g5x.setProperty("zero_g5x_action", True)

        self.gridLayout_15.addWidget(self.action_zero_g5x, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_3, 2, 0, 1, 1)


        self.gridLayout_16.addWidget(self.frm_zero_offsets, 1, 1, 1, 1)

        self.label_19 = QLabel(self.woffsetspage)
        self.label_19.setObjectName(u"label_19")
        sizePolicy5.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy5)
        self.label_19.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_16.addWidget(self.label_19, 0, 0, 1, 1)

        self.originoffsetview_2 = OriginOffsetView(self.woffsetspage)
        self.originoffsetview_2.setObjectName(u"originoffsetview_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.originoffsetview_2.sizePolicy().hasHeightForWidth())
        self.originoffsetview_2.setSizePolicy(sizePolicy7)
        self.originoffsetview_2.setMinimumSize(QSize(0, 0))
        self.originoffsetview_2.verticalHeader().setDefaultSectionSize(36)

        self.gridLayout_16.addWidget(self.originoffsetview_2, 1, 0, 1, 1)


        self.verticalLayout_31.addWidget(self.woffsetspage)

        self.widgetswitcher.addWidget(self.workoffsetsPage)
        self.setupPage = QWidget()
        self.setupPage.setObjectName(u"setupPage")
        self.verticalLayout_32 = QVBoxLayout(self.setupPage)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.setupPage)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.WinPanel)
        self.frame_12.setFrameShadow(QFrame.Plain)
        self.verticalLayout_19 = QVBoxLayout(self.frame_12)
        self.verticalLayout_19.setSpacing(3)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(2, 0, 2, 2)
        self.label_23 = QLabel(self.frame_12)
        self.label_23.setObjectName(u"label_23")
        sizePolicy5.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy5)
        self.label_23.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_19.addWidget(self.label_23)

        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.WinPanel)
        self.frame_14.setFrameShadow(QFrame.Plain)
        self.action_home_all = ActionButton(self.frame_14)
        self.action_home_all.setObjectName(u"action_home_all")
        self.action_home_all.setGeometry(QRect(179, 120, 80, 41))
        sizePolicy.setHeightForWidth(self.action_home_all.sizePolicy().hasHeightForWidth())
        self.action_home_all.setSizePolicy(sizePolicy)
        self.action_home_all.setMinimumSize(QSize(80, 41))
        self.action_home_all.setProperty("indicator_status_option", False)
        self.action_home_all.setProperty("checked_state_text_option", True)
        self.action_home_all.setProperty("on_color", QColor(0, 255, 0))
        self.action_home_all.setProperty("off_color", QColor(255, 0, 0))
        self.action_home_all.setProperty("home_action", True)
        self.action_home_all.setProperty("template_label_option", False)
        self.action_home_all.setProperty("joint_number", -1)
        self.action_home_all.setProperty("incr_imperial_number", 0.010000000000000)
        self.action_home_all.setProperty("incr_mm_number", 0.025000000000000)
        self.action_home_all.setProperty("incr_angular_number", -1.000000000000000)
        self.action_home_all.setProperty("toggle_float_option", False)
        self.action_home_all.setProperty("float_num", 100.000000000000000)
        self.action_home_all.setProperty("float_alt_num", 50.000000000000000)
        self.action_home_all.setProperty("ini_mdi_number", 0)
        self.horizontalLayoutWidget = QWidget(self.frame_14)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(302, 209, 411, 53))
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.horizontalLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        self.label_11.setMinimumSize(QSize(70, 0))
        self.label_11.setMaximumSize(QSize(70, 16777215))
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_11)

        self.statuslabel_8 = StatusLabel(self.horizontalLayoutWidget)
        self.statuslabel_8.setObjectName(u"statuslabel_8")
        sizePolicy3.setHeightForWidth(self.statuslabel_8.sizePolicy().hasHeightForWidth())
        self.statuslabel_8.setSizePolicy(sizePolicy3)
        self.statuslabel_8.setMinimumSize(QSize(0, 41))
        self.statuslabel_8.setMaximumSize(QSize(100, 16777215))
        self.statuslabel_8.setAlignment(Qt.AlignCenter)
        self.statuslabel_8.setProperty("index_number", 0)
        self.statuslabel_8.setProperty("max_velocity_override_status", True)
        self.statuslabel_8.setProperty("current_feedrate_status", False)
        self.statuslabel_8.setProperty("gcode_selected_status", False)

        self.horizontalLayout_9.addWidget(self.statuslabel_8)

        self.statusslider_4 = StatusSlider(self.horizontalLayoutWidget)
        self.statusslider_4.setObjectName(u"statusslider_4")
        sizePolicy.setHeightForWidth(self.statusslider_4.sizePolicy().hasHeightForWidth())
        self.statusslider_4.setSizePolicy(sizePolicy)
        self.statusslider_4.setMinimumSize(QSize(191, 51))
        self.statusslider_4.setStyleSheet(u"QSlider::groove:horizontal {\n"
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
"QSlider::add-page:horizontal {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255,"
                        " 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"width: 40px;\n"
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
        self.statusslider_4.setMaximum(199)
        self.statusslider_4.setSingleStep(1)
        self.statusslider_4.setPageStep(1)
        self.statusslider_4.setValue(100)
        self.statusslider_4.setOrientation(Qt.Horizontal)
        self.statusslider_4.setProperty("feed_rate", False)
        self.statusslider_4.setProperty("jograte_rate", False)
        self.statusslider_4.setProperty("max_velocity_rate", True)

        self.horizontalLayout_9.addWidget(self.statusslider_4)

        self.horizontalLayoutWidget_2 = QWidget(self.frame_14)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(302, 145, 411, 53))
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.horizontalLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setMinimumSize(QSize(70, 0))
        self.label_10.setMaximumSize(QSize(70, 16777215))
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_10)

        self.statuslabel_7 = StatusLabel(self.horizontalLayoutWidget_2)
        self.statuslabel_7.setObjectName(u"statuslabel_7")
        sizePolicy3.setHeightForWidth(self.statuslabel_7.sizePolicy().hasHeightForWidth())
        self.statuslabel_7.setSizePolicy(sizePolicy3)
        self.statuslabel_7.setMinimumSize(QSize(0, 41))
        self.statuslabel_7.setMaximumSize(QSize(100, 16777215))
        self.statuslabel_7.setAlignment(Qt.AlignCenter)
        self.statuslabel_7.setProperty("jograte_status", True)
        self.statuslabel_7.setProperty("current_feedrate_status", False)

        self.horizontalLayout_10.addWidget(self.statuslabel_7)

        self.slider_jog_linear = StatusSlider(self.horizontalLayoutWidget_2)
        self.slider_jog_linear.setObjectName(u"slider_jog_linear")
        sizePolicy.setHeightForWidth(self.slider_jog_linear.sizePolicy().hasHeightForWidth())
        self.slider_jog_linear.setSizePolicy(sizePolicy)
        self.slider_jog_linear.setMinimumSize(QSize(191, 51))
        self.slider_jog_linear.setStyleSheet(u"QSlider::groove:horizontal {\n"
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
"QSlider::add-page:horizontal {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255,"
                        " 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"width: 40px;\n"
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
        self.slider_jog_linear.setMaximum(199)
        self.slider_jog_linear.setPageStep(1)
        self.slider_jog_linear.setValue(150)
        self.slider_jog_linear.setOrientation(Qt.Horizontal)
        self.slider_jog_linear.setProperty("feed_rate", False)
        self.slider_jog_linear.setProperty("jograte_rate", True)

        self.horizontalLayout_10.addWidget(self.slider_jog_linear)

        self.horizontalLayoutWidget_3 = QWidget(self.frame_14)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(302, 80, 411, 53))
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.horizontalLayoutWidget_3)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)
        self.label_14.setMinimumSize(QSize(100, 0))
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_14)

        self.statuslabel_12 = StatusLabel(self.horizontalLayoutWidget_3)
        self.statuslabel_12.setObjectName(u"statuslabel_12")
        sizePolicy.setHeightForWidth(self.statuslabel_12.sizePolicy().hasHeightForWidth())
        self.statuslabel_12.setSizePolicy(sizePolicy)
        self.statuslabel_12.setMinimumSize(QSize(70, 41))
        self.statuslabel_12.setMaximumSize(QSize(70, 16777215))
        self.statuslabel_12.setAlignment(Qt.AlignCenter)
        self.statuslabel_12.setProperty("rapid_override_status", True)

        self.horizontalLayout_11.addWidget(self.statuslabel_12)

        self.statusslider_2 = StatusSlider(self.horizontalLayoutWidget_3)
        self.statusslider_2.setObjectName(u"statusslider_2")
        sizePolicy.setHeightForWidth(self.statusslider_2.sizePolicy().hasHeightForWidth())
        self.statusslider_2.setSizePolicy(sizePolicy)
        self.statusslider_2.setMinimumSize(QSize(191, 51))
        self.statusslider_2.setStyleSheet(u"QSlider::groove:horizontal {\n"
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
"QSlider::add-page:horizontal {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255,"
                        " 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"width: 40px;\n"
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
        self.statusslider_2.setValue(99)
        self.statusslider_2.setOrientation(Qt.Horizontal)

        self.horizontalLayout_11.addWidget(self.statusslider_2)

        self.horizontalLayoutWidget_4 = QWidget(self.frame_14)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(302, 10, 411, 53))
        self.horizontalLayout_12 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.horizontalLayoutWidget_4)
        self.label_16.setObjectName(u"label_16")
        sizePolicy1.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy1)
        self.label_16.setMinimumSize(QSize(100, 0))
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_16)

        self.statuslabel_10 = StatusLabel(self.horizontalLayoutWidget_4)
        self.statuslabel_10.setObjectName(u"statuslabel_10")
        sizePolicy.setHeightForWidth(self.statuslabel_10.sizePolicy().hasHeightForWidth())
        self.statuslabel_10.setSizePolicy(sizePolicy)
        self.statuslabel_10.setMinimumSize(QSize(70, 41))
        self.statuslabel_10.setMaximumSize(QSize(70, 16777215))
        self.statuslabel_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.statuslabel_10)

        self.statusslider = StatusSlider(self.horizontalLayoutWidget_4)
        self.statusslider.setObjectName(u"statusslider")
        sizePolicy.setHeightForWidth(self.statusslider.sizePolicy().hasHeightForWidth())
        self.statusslider.setSizePolicy(sizePolicy)
        self.statusslider.setMinimumSize(QSize(191, 51))
        self.statusslider.setStyleSheet(u"QSlider::groove:horizontal {\n"
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
"QSlider::add-page:horizontal {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255,"
                        " 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"width: 40px;\n"
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
        self.statusslider.setMaximum(120)
        self.statusslider.setValue(100)
        self.statusslider.setOrientation(Qt.Horizontal)
        self.statusslider.setProperty("feed_rate", True)

        self.horizontalLayout_12.addWidget(self.statusslider)

        self.y_plus_jogbutton = ActionButton(self.frame_14)
        self.y_plus_jogbutton.setObjectName(u"y_plus_jogbutton")
        self.y_plus_jogbutton.setGeometry(QRect(50, 120, 50, 50))
        self.y_plus_jogbutton.setMinimumSize(QSize(50, 50))
        self.y_plus_jogbutton.setMaximumSize(QSize(50, 50))
        icon2 = QIcon()
        icon2.addFile(u"images/x_minus_jog_button.3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.y_plus_jogbutton.setIcon(icon2)
        self.y_plus_jogbutton.setIconSize(QSize(48, 48))
        self.y_plus_jogbutton.setProperty("jog_joint_pos_action", False)
        self.y_plus_jogbutton.setProperty("jog_joint_neg_action", True)
        self.y_plus_jogbutton.setProperty("template_label_option", False)
        self.y_plus_jogbutton.setProperty("joint_number", 0)
        self.y_plus_jogbutton.setProperty("incr_imperial_number", 0.010000000000000)
        self.y_plus_jogbutton.setProperty("incr_mm_number", 0.025000000000000)
        self.y_plus_jogbutton.setProperty("incr_angular_number", -1.000000000000000)
        self.y_plus_jogbutton.setProperty("toggle_float_option", False)
        self.y_plus_jogbutton.setProperty("float_num", 100.000000000000000)
        self.y_plus_jogbutton.setProperty("float_alt_num", 50.000000000000000)
        self.y_plus_jogbutton.setProperty("ini_mdi_number", 0)
        self.y_minus_jogbutton = ActionButton(self.frame_14)
        self.y_minus_jogbutton.setObjectName(u"y_minus_jogbutton")
        self.y_minus_jogbutton.setGeometry(QRect(50, 220, 50, 50))
        sizePolicy.setHeightForWidth(self.y_minus_jogbutton.sizePolicy().hasHeightForWidth())
        self.y_minus_jogbutton.setSizePolicy(sizePolicy)
        self.y_minus_jogbutton.setMinimumSize(QSize(50, 50))
        self.y_minus_jogbutton.setMaximumSize(QSize(50, 50))
        icon3 = QIcon()
        icon3.addFile(u"images/x_plus_jog_button.3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.y_minus_jogbutton.setIcon(icon3)
        self.y_minus_jogbutton.setIconSize(QSize(48, 48))
        self.y_minus_jogbutton.setProperty("jog_joint_pos_action", True)
        self.y_minus_jogbutton.setProperty("jog_joint_neg_action", False)
        self.y_minus_jogbutton.setProperty("template_label_option", False)
        self.y_minus_jogbutton.setProperty("joint_number", 0)
        self.y_minus_jogbutton.setProperty("incr_imperial_number", 0.010000000000000)
        self.y_minus_jogbutton.setProperty("incr_mm_number", 0.025000000000000)
        self.y_minus_jogbutton.setProperty("incr_angular_number", -1.000000000000000)
        self.y_minus_jogbutton.setProperty("toggle_float_option", False)
        self.y_minus_jogbutton.setProperty("float_num", 100.000000000000000)
        self.y_minus_jogbutton.setProperty("float_alt_num", 50.000000000000000)
        self.y_minus_jogbutton.setProperty("ini_mdi_number", 0)
        self.a_minus_jogbutton = ActionButton(self.frame_14)
        self.a_minus_jogbutton.setObjectName(u"a_minus_jogbutton")
        self.a_minus_jogbutton.setGeometry(QRect(10, 170, 50, 50))
        self.a_minus_jogbutton.setMinimumSize(QSize(50, 50))
        self.a_minus_jogbutton.setMaximumSize(QSize(50, 50))
        icon4 = QIcon()
        icon4.addFile(u"images/z_minus_jog_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.a_minus_jogbutton.setIcon(icon4)
        self.a_minus_jogbutton.setIconSize(QSize(48, 48))
        self.a_minus_jogbutton.setProperty("joint_number_status", 2)
        self.a_minus_jogbutton.setProperty("jog_joint_pos_action", False)
        self.a_minus_jogbutton.setProperty("jog_joint_neg_action", True)
        self.a_minus_jogbutton.setProperty("joint_number", 1)
        self.a_plus_jogbutton = ActionButton(self.frame_14)
        self.a_plus_jogbutton.setObjectName(u"a_plus_jogbutton")
        self.a_plus_jogbutton.setGeometry(QRect(90, 170, 50, 50))
        self.a_plus_jogbutton.setMinimumSize(QSize(50, 50))
        self.a_plus_jogbutton.setMaximumSize(QSize(50, 50))
        icon5 = QIcon()
        icon5.addFile(u"images/z_plus_jog_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.a_plus_jogbutton.setIcon(icon5)
        self.a_plus_jogbutton.setIconSize(QSize(48, 48))
        self.a_plus_jogbutton.setProperty("joint_number_status", 2)
        self.a_plus_jogbutton.setProperty("jog_joint_pos_action", True)
        self.a_plus_jogbutton.setProperty("joint_number", 1)
        self.jogincrements_linear = JogIncrements(self.frame_14)
        self.jogincrements_linear.setObjectName(u"jogincrements_linear")
        self.jogincrements_linear.setGeometry(QRect(180, 170, 107, 30))
        sizePolicy.setHeightForWidth(self.jogincrements_linear.sizePolicy().hasHeightForWidth())
        self.jogincrements_linear.setSizePolicy(sizePolicy)
        self.jogincrements_linear.setMinimumSize(QSize(107, 30))
        self.jogincrements_linear.setMaximumSize(QSize(100, 30))
        self.jogincrements_linear.setFrame(True)
        self.horizontalLayoutWidget_5 = QWidget(self.frame_14)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 10, 254, 51))
        self.gridLayout_7 = QGridLayout(self.horizontalLayoutWidget_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.axistoolbutton = AxisToolButton(self.horizontalLayoutWidget_5)
        self.axistoolbutton.setObjectName(u"axistoolbutton")
        self.axistoolbutton.setMinimumSize(QSize(80, 41))

        self.gridLayout_7.addWidget(self.axistoolbutton, 0, 0, 1, 1)

        self.action_zero_x = ActionButton(self.horizontalLayoutWidget_5)
        self.action_zero_x.setObjectName(u"action_zero_x")
        sizePolicy.setHeightForWidth(self.action_zero_x.sizePolicy().hasHeightForWidth())
        self.action_zero_x.setSizePolicy(sizePolicy)
        self.action_zero_x.setMinimumSize(QSize(80, 41))
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

        self.gridLayout_7.addWidget(self.action_zero_x, 0, 1, 1, 1)

        self.action_home_x = ActionButton(self.horizontalLayoutWidget_5)
        self.action_home_x.setObjectName(u"action_home_x")
        sizePolicy.setHeightForWidth(self.action_home_x.sizePolicy().hasHeightForWidth())
        self.action_home_x.setSizePolicy(sizePolicy)
        self.action_home_x.setMinimumSize(QSize(80, 41))
        self.action_home_x.setCheckable(True)
        self.action_home_x.setProperty("indicator_option", True)
        self.action_home_x.setProperty("indicator_HAL_pin_option", True)
        self.action_home_x.setProperty("on_color", QColor(0, 255, 0))
        self.action_home_x.setProperty("off_color", QColor(255, 0, 0))
        self.action_home_x.setProperty("home_action", True)
        self.action_home_x.setProperty("template_label_option", False)
        self.action_home_x.setProperty("joint_number", 0)
        self.action_home_x.setProperty("incr_imperial_number", 0.010000000000000)
        self.action_home_x.setProperty("incr_mm_number", 0.025000000000000)
        self.action_home_x.setProperty("incr_angular_number", -1.000000000000000)
        self.action_home_x.setProperty("toggle_float_option", False)
        self.action_home_x.setProperty("float_num", 100.000000000000000)
        self.action_home_x.setProperty("float_alt_num", 50.000000000000000)
        self.action_home_x.setProperty("ini_mdi_number", 0)

        self.gridLayout_7.addWidget(self.action_home_x, 0, 2, 1, 1)

        self.horizontalLayoutWidget_6 = QWidget(self.frame_14)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 58, 254, 51))
        self.gridLayout_4 = QGridLayout(self.horizontalLayoutWidget_6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.axistoolbutton_2 = AxisToolButton(self.horizontalLayoutWidget_6)
        self.axistoolbutton_2.setObjectName(u"axistoolbutton_2")
        self.axistoolbutton_2.setMinimumSize(QSize(80, 41))
        self.axistoolbutton_2.setProperty("joint_number", 2)

        self.gridLayout_4.addWidget(self.axistoolbutton_2, 0, 0, 1, 1)

        self.action_zero_z = ActionButton(self.horizontalLayoutWidget_6)
        self.action_zero_z.setObjectName(u"action_zero_z")
        sizePolicy.setHeightForWidth(self.action_zero_z.sizePolicy().hasHeightForWidth())
        self.action_zero_z.setSizePolicy(sizePolicy)
        self.action_zero_z.setMinimumSize(QSize(80, 41))
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

        self.gridLayout_4.addWidget(self.action_zero_z, 0, 1, 1, 1)

        self.action_home_z = ActionButton(self.horizontalLayoutWidget_6)
        self.action_home_z.setObjectName(u"action_home_z")
        sizePolicy.setHeightForWidth(self.action_home_z.sizePolicy().hasHeightForWidth())
        self.action_home_z.setSizePolicy(sizePolicy)
        self.action_home_z.setMinimumSize(QSize(80, 41))
        self.action_home_z.setCheckable(True)
        self.action_home_z.setProperty("indicator_option", True)
        self.action_home_z.setProperty("indicator_HAL_pin_option", True)
        self.action_home_z.setProperty("on_color", QColor(0, 255, 0))
        self.action_home_z.setProperty("off_color", QColor(255, 0, 0))
        self.action_home_z.setProperty("home_action", True)
        self.action_home_z.setProperty("template_label_option", False)
        self.action_home_z.setProperty("joint_number", 1)
        self.action_home_z.setProperty("incr_imperial_number", 0.010000000000000)
        self.action_home_z.setProperty("incr_mm_number", 0.025000000000000)
        self.action_home_z.setProperty("incr_angular_number", -1.000000000000000)
        self.action_home_z.setProperty("toggle_float_option", False)
        self.action_home_z.setProperty("float_num", 100.000000000000000)
        self.action_home_z.setProperty("float_alt_num", 50.000000000000000)
        self.action_home_z.setProperty("ini_mdi_number", 0)

        self.gridLayout_4.addWidget(self.action_home_z, 0, 2, 1, 1)

        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(0, 280, 721, 230))
        sizePolicy2.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy2)
        self.frame_15.setMinimumSize(QSize(0, 230))
        self.frame_15.setMaximumSize(QSize(16777215, 230))
        self.frame_15.setFrameShape(QFrame.WinPanel)
        self.frame_15.setFrameShadow(QFrame.Plain)
        self.gridLayout_18 = QGridLayout(self.frame_15)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.actionbutton_3 = ActionButton(self.frame_15)
        self.actionbutton_3.setObjectName(u"actionbutton_3")
        self.actionbutton_3.setMinimumSize(QSize(41, 41))
        self.actionbutton_3.setMaximumSize(QSize(80, 16777215))
        self.actionbutton_3.setProperty("indicator_option", True)
        self.actionbutton_3.setProperty("indicator_HAL_pin_option", False)
        self.actionbutton_3.setProperty("indicator_status_option", True)
        self.actionbutton_3.setProperty("checked_state_text_option", False)
        self.actionbutton_3.setProperty("python_command_option", False)
        self.actionbutton_3.setProperty("on_color", QColor(255, 0, 0))
        self.actionbutton_3.setProperty("shape_option", 0)
        self.actionbutton_3.setProperty("off_color", QColor(0, 0, 0))
        self.actionbutton_3.setProperty("indicator_size", 0.300000000000000)
        self.actionbutton_3.setProperty("circle_diameter", 10.000000000000000)
        self.actionbutton_3.setProperty("right_edge_offset", 0.000000000000000)
        self.actionbutton_3.setProperty("top_edge_offset", 0.000000000000000)
        self.actionbutton_3.setProperty("corner_radius", 5.000000000000000)
        self.actionbutton_3.setProperty("height_fraction", 0.300000000000000)
        self.actionbutton_3.setProperty("width_fraction", 0.900000000000000)
        self.actionbutton_3.setProperty("invert_the_status", False)
        self.actionbutton_3.setProperty("is_paused_status", False)
        self.actionbutton_3.setProperty("is_estopped_status", False)
        self.actionbutton_3.setProperty("is_on_status", False)
        self.actionbutton_3.setProperty("is_idle_status", False)
        self.actionbutton_3.setProperty("is_homed_status", False)
        self.actionbutton_3.setProperty("is_flood_status", False)
        self.actionbutton_3.setProperty("is_mist_status", False)
        self.actionbutton_3.setProperty("is_block_delete_status", False)
        self.actionbutton_3.setProperty("is_optional_stop_status", False)
        self.actionbutton_3.setProperty("is_joint_homed_status", False)
        self.actionbutton_3.setProperty("is_limits_overridden_status", False)
        self.actionbutton_3.setProperty("is_manual_status", True)
        self.actionbutton_3.setProperty("is_mdi_status", False)
        self.actionbutton_3.setProperty("is_auto_status", False)
        self.actionbutton_3.setProperty("is_spindle_stopped_status", False)
        self.actionbutton_3.setProperty("is_spindle_fwd_status", False)
        self.actionbutton_3.setProperty("is_spindle_rev_status", False)
        self.actionbutton_3.setProperty("joint_number_status", 0)
        self.actionbutton_3.setProperty("manual_action", True)
        self.actionbutton_3.setProperty("template_label_option", False)
        self.actionbutton_3.setProperty("joint_number", 0)
        self.actionbutton_3.setProperty("incr_imperial_number", 0.010000000000000)
        self.actionbutton_3.setProperty("incr_mm_number", 0.025000000000000)
        self.actionbutton_3.setProperty("incr_angular_number", -1.000000000000000)
        self.actionbutton_3.setProperty("toggle_float_option", False)
        self.actionbutton_3.setProperty("float_num", 0.300000000000000)
        self.actionbutton_3.setProperty("float_alt_num", 50.000000000000000)
        self.actionbutton_3.setProperty("ini_mdi_number", 0)

        self.gridLayout_18.addWidget(self.actionbutton_3, 2, 0, 1, 1)

        self.action_mist = ActionButton(self.frame_15)
        self.action_mist.setObjectName(u"action_mist")
        sizePolicy.setHeightForWidth(self.action_mist.sizePolicy().hasHeightForWidth())
        self.action_mist.setSizePolicy(sizePolicy)
        self.action_mist.setMinimumSize(QSize(80, 41))
        self.action_mist.setMaximumSize(QSize(80, 41))
        self.action_mist.setCheckable(True)
        self.action_mist.setChecked(False)
        self.action_mist.setProperty("indicator_option", True)
        self.action_mist.setProperty("indicator_HAL_pin_option", False)
        self.action_mist.setProperty("indicator_status_option", True)
        self.action_mist.setProperty("checked_state_text_option", True)
        self.action_mist.setProperty("python_command_option", False)
        self.action_mist.setProperty("on_color", QColor(0, 255, 0))
        self.action_mist.setProperty("shape_option", 0)
        self.action_mist.setProperty("off_color", QColor(0, 0, 0))
        self.action_mist.setProperty("indicator_size", 0.200000000000000)
        self.action_mist.setProperty("circle_diameter", 10.000000000000000)
        self.action_mist.setProperty("right_edge_offset", 0.000000000000000)
        self.action_mist.setProperty("top_edge_offset", 0.000000000000000)
        self.action_mist.setProperty("corner_radius", 5.000000000000000)
        self.action_mist.setProperty("height_fraction", 0.300000000000000)
        self.action_mist.setProperty("width_fraction", 0.900000000000000)
        self.action_mist.setProperty("invert_the_status", False)
        self.action_mist.setProperty("is_paused_status", False)
        self.action_mist.setProperty("is_estopped_status", False)
        self.action_mist.setProperty("is_on_status", False)
        self.action_mist.setProperty("is_idle_status", False)
        self.action_mist.setProperty("is_homed_status", False)
        self.action_mist.setProperty("is_flood_status", False)
        self.action_mist.setProperty("is_mist_status", True)
        self.action_mist.setProperty("is_block_delete_status", False)
        self.action_mist.setProperty("is_optional_stop_status", False)
        self.action_mist.setProperty("is_joint_homed_status", False)
        self.action_mist.setProperty("is_limits_overridden_status", False)
        self.action_mist.setProperty("is_manual_status", False)
        self.action_mist.setProperty("is_mdi_status", False)
        self.action_mist.setProperty("is_auto_status", False)
        self.action_mist.setProperty("is_spindle_stopped_status", False)
        self.action_mist.setProperty("is_spindle_fwd_status", False)
        self.action_mist.setProperty("is_spindle_rev_status", False)
        self.action_mist.setProperty("joint_number_status", 0)
        self.action_mist.setProperty("mist_action", True)
        self.action_mist.setProperty("template_label_option", False)
        self.action_mist.setProperty("joint_number", 0)
        self.action_mist.setProperty("incr_imperial_number", 0.010000000000000)
        self.action_mist.setProperty("incr_mm_number", 0.025000000000000)
        self.action_mist.setProperty("incr_angular_number", -1.000000000000000)
        self.action_mist.setProperty("toggle_float_option", False)
        self.action_mist.setProperty("float_num", 0.200000000000000)
        self.action_mist.setProperty("float_alt_num", 50.000000000000000)
        self.action_mist.setProperty("ini_mdi_number", 0)

        self.gridLayout_18.addWidget(self.action_mist, 1, 3, 1, 1)

        self.statusimageswitcher = StatusImageSwitcher(self.frame_15)
        self.statusimageswitcher.setObjectName(u"statusimageswitcher")
        self.statusimageswitcher.setPixmap(QPixmap(u":/images/images/stop_on.gif"))
        self.statusimageswitcher.setScaledContents(False)
        self.statusimageswitcher.setAlignment(Qt.AlignCenter)
        self.statusimageswitcher.setProperty("image_number", 0)

        self.gridLayout_18.addWidget(self.statusimageswitcher, 1, 1, 1, 1)

        self.action_flood = ActionButton(self.frame_15)
        self.action_flood.setObjectName(u"action_flood")
        sizePolicy.setHeightForWidth(self.action_flood.sizePolicy().hasHeightForWidth())
        self.action_flood.setSizePolicy(sizePolicy)
        self.action_flood.setMinimumSize(QSize(80, 41))
        self.action_flood.setMaximumSize(QSize(80, 41))
        self.action_flood.setCheckable(True)
        self.action_flood.setProperty("indicator_option", True)
        self.action_flood.setProperty("indicator_HAL_pin_option", False)
        self.action_flood.setProperty("indicator_status_option", True)
        self.action_flood.setProperty("checked_state_text_option", True)
        self.action_flood.setProperty("python_command_option", False)
        self.action_flood.setProperty("on_color", QColor(0, 255, 0))
        self.action_flood.setProperty("shape_option", 0)
        self.action_flood.setProperty("off_color", QColor(0, 0, 0))
        self.action_flood.setProperty("indicator_size", 0.200000000000000)
        self.action_flood.setProperty("circle_diameter", 10.000000000000000)
        self.action_flood.setProperty("right_edge_offset", 0.000000000000000)
        self.action_flood.setProperty("top_edge_offset", 0.000000000000000)
        self.action_flood.setProperty("corner_radius", 5.000000000000000)
        self.action_flood.setProperty("height_fraction", 0.300000000000000)
        self.action_flood.setProperty("width_fraction", 0.900000000000000)
        self.action_flood.setProperty("invert_the_status", False)
        self.action_flood.setProperty("is_paused_status", False)
        self.action_flood.setProperty("is_estopped_status", False)
        self.action_flood.setProperty("is_on_status", False)
        self.action_flood.setProperty("is_idle_status", False)
        self.action_flood.setProperty("is_homed_status", False)
        self.action_flood.setProperty("is_flood_status", True)
        self.action_flood.setProperty("is_mist_status", False)
        self.action_flood.setProperty("is_block_delete_status", False)
        self.action_flood.setProperty("is_optional_stop_status", False)
        self.action_flood.setProperty("is_joint_homed_status", False)
        self.action_flood.setProperty("is_limits_overridden_status", False)
        self.action_flood.setProperty("is_manual_status", False)
        self.action_flood.setProperty("is_mdi_status", False)
        self.action_flood.setProperty("is_auto_status", False)
        self.action_flood.setProperty("is_spindle_stopped_status", False)
        self.action_flood.setProperty("is_spindle_fwd_status", False)
        self.action_flood.setProperty("is_spindle_rev_status", False)
        self.action_flood.setProperty("joint_number_status", 0)
        self.action_flood.setProperty("flood_action", True)
        self.action_flood.setProperty("template_label_option", False)
        self.action_flood.setProperty("joint_number", 0)
        self.action_flood.setProperty("incr_imperial_number", 0.010000000000000)
        self.action_flood.setProperty("incr_mm_number", 0.025000000000000)
        self.action_flood.setProperty("incr_angular_number", -1.000000000000000)
        self.action_flood.setProperty("toggle_float_option", False)
        self.action_flood.setProperty("float_num", 0.200000000000000)
        self.action_flood.setProperty("float_alt_num", 50.000000000000000)
        self.action_flood.setProperty("ini_mdi_number", 0)

        self.gridLayout_18.addWidget(self.action_flood, 0, 3, 1, 1)

        self.actionbutton_8 = ActionButton(self.frame_15)
        self.actionbutton_8.setObjectName(u"actionbutton_8")
        sizePolicy.setHeightForWidth(self.actionbutton_8.sizePolicy().hasHeightForWidth())
        self.actionbutton_8.setSizePolicy(sizePolicy)
        self.actionbutton_8.setMinimumSize(QSize(80, 41))
        self.actionbutton_8.setProperty("limits_override_action", True)
        self.actionbutton_8.setProperty("template_label_option", False)
        self.actionbutton_8.setProperty("joint_number", 0)
        self.actionbutton_8.setProperty("incr_imperial_number", 0.010000000000000)
        self.actionbutton_8.setProperty("incr_mm_number", 0.025000000000000)
        self.actionbutton_8.setProperty("incr_angular_number", -1.000000000000000)
        self.actionbutton_8.setProperty("toggle_float_option", False)
        self.actionbutton_8.setProperty("float_num", 100.000000000000000)
        self.actionbutton_8.setProperty("float_alt_num", 50.000000000000000)
        self.actionbutton_8.setProperty("ini_mdi_number", 0)

        self.gridLayout_18.addWidget(self.actionbutton_8, 0, 1, 1, 1)

        self.actionbutton_16 = ActionButton(self.frame_15)
        self.actionbutton_16.setObjectName(u"actionbutton_16")
        self.actionbutton_16.setMinimumSize(QSize(80, 41))
        self.actionbutton_16.setProperty("load_dialog_action", True)

        self.gridLayout_18.addWidget(self.actionbutton_16, 3, 3, 1, 1)

        self.actionbutton_camview = ActionButton(self.frame_15)
        self.actionbutton_camview.setObjectName(u"actionbutton_camview")
        sizePolicy.setHeightForWidth(self.actionbutton_camview.sizePolicy().hasHeightForWidth())
        self.actionbutton_camview.setSizePolicy(sizePolicy)
        self.actionbutton_camview.setMinimumSize(QSize(80, 41))
        self.actionbutton_camview.setProperty("camview_dialog_action", True)

        self.gridLayout_18.addWidget(self.actionbutton_camview, 3, 0, 1, 1)

        self.btn_clear_alarms = QPushButton(self.frame_15)
        self.btn_clear_alarms.setObjectName(u"btn_clear_alarms")
        sizePolicy.setHeightForWidth(self.btn_clear_alarms.sizePolicy().hasHeightForWidth())
        self.btn_clear_alarms.setSizePolicy(sizePolicy)
        self.btn_clear_alarms.setMinimumSize(QSize(80, 41))
        self.btn_clear_alarms.setMaximumSize(QSize(80, 41))

        self.gridLayout_18.addWidget(self.btn_clear_alarms, 1, 2, 1, 1)

        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy8)
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_16)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_29 = QLabel(self.frame_16)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFrameShape(QFrame.NoFrame)
        self.label_29.setFrameShadow(QFrame.Raised)
        self.label_29.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_29)

        self.label_34 = QLabel(self.frame_16)
        self.label_34.setObjectName(u"label_34")

        self.verticalLayout_8.addWidget(self.label_34)

        self.label_30 = QLabel(self.frame_16)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_8.addWidget(self.label_30)

        self.label_31 = QLabel(self.frame_16)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_8.addWidget(self.label_31)

        self.label_32 = QLabel(self.frame_16)
        self.label_32.setObjectName(u"label_32")

        self.verticalLayout_8.addWidget(self.label_32)

        self.label_6 = QLabel(self.frame_16)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_8.addWidget(self.label_6)

        self.label_35 = QLabel(self.frame_16)
        self.label_35.setObjectName(u"label_35")

        self.verticalLayout_8.addWidget(self.label_35)

        self.label_33 = QLabel(self.frame_16)
        self.label_33.setObjectName(u"label_33")

        self.verticalLayout_8.addWidget(self.label_33)

        self.label_36 = QLabel(self.frame_16)
        self.label_36.setObjectName(u"label_36")

        self.verticalLayout_8.addWidget(self.label_36)


        self.gridLayout_18.addWidget(self.frame_16, 0, 4, 5, 1)

        self.systemtoolbutton = SystemToolButton(self.frame_15)
        self.systemtoolbutton.setObjectName(u"systemtoolbutton")
        self.systemtoolbutton.setMinimumSize(QSize(80, 41))

        self.gridLayout_18.addWidget(self.systemtoolbutton, 0, 0, 1, 1)

        self.actionbutton_10 = ActionButton(self.frame_15)
        self.actionbutton_10.setObjectName(u"actionbutton_10")
        sizePolicy.setHeightForWidth(self.actionbutton_10.sizePolicy().hasHeightForWidth())
        self.actionbutton_10.setSizePolicy(sizePolicy)
        self.actionbutton_10.setMinimumSize(QSize(80, 41))
        self.actionbutton_10.setProperty("machine_log_dialog_action", True)
        self.actionbutton_10.setProperty("template_label_option", False)
        self.actionbutton_10.setProperty("joint_number", 0)
        self.actionbutton_10.setProperty("incr_imperial_number", 0.010000000000000)
        self.actionbutton_10.setProperty("incr_mm_number", 0.025000000000000)
        self.actionbutton_10.setProperty("incr_angular_number", -1.000000000000000)
        self.actionbutton_10.setProperty("toggle_float_option", False)
        self.actionbutton_10.setProperty("float_num", 100.000000000000000)
        self.actionbutton_10.setProperty("float_alt_num", 50.000000000000000)
        self.actionbutton_10.setProperty("ini_mdi_number", 0)

        self.gridLayout_18.addWidget(self.actionbutton_10, 0, 2, 1, 1)

        self.btn_save_alarms = QPushButton(self.frame_15)
        self.btn_save_alarms.setObjectName(u"btn_save_alarms")
        sizePolicy.setHeightForWidth(self.btn_save_alarms.sizePolicy().hasHeightForWidth())
        self.btn_save_alarms.setSizePolicy(sizePolicy)
        self.btn_save_alarms.setMinimumSize(QSize(80, 41))
        self.btn_save_alarms.setMaximumSize(QSize(80, 41))

        self.gridLayout_18.addWidget(self.btn_save_alarms, 3, 2, 1, 1)

        self.actionbutton_4 = ActionButton(self.frame_15)
        self.actionbutton_4.setObjectName(u"actionbutton_4")
        self.actionbutton_4.setMinimumSize(QSize(41, 41))
        self.actionbutton_4.setMaximumSize(QSize(80, 16777215))
        self.actionbutton_4.setProperty("indicator_option", True)
        self.actionbutton_4.setProperty("indicator_HAL_pin_option", False)
        self.actionbutton_4.setProperty("indicator_status_option", True)
        self.actionbutton_4.setProperty("checked_state_text_option", False)
        self.actionbutton_4.setProperty("python_command_option", False)
        self.actionbutton_4.setProperty("on_color", QColor(255, 0, 0))
        self.actionbutton_4.setProperty("shape_option", 0)
        self.actionbutton_4.setProperty("off_color", QColor(0, 0, 0))
        self.actionbutton_4.setProperty("indicator_size", 0.300000000000000)
        self.actionbutton_4.setProperty("circle_diameter", 10.000000000000000)
        self.actionbutton_4.setProperty("right_edge_offset", 0.000000000000000)
        self.actionbutton_4.setProperty("top_edge_offset", 0.000000000000000)
        self.actionbutton_4.setProperty("corner_radius", 5.000000000000000)
        self.actionbutton_4.setProperty("height_fraction", 0.300000000000000)
        self.actionbutton_4.setProperty("width_fraction", 0.900000000000000)
        self.actionbutton_4.setProperty("invert_the_status", False)
        self.actionbutton_4.setProperty("is_paused_status", False)
        self.actionbutton_4.setProperty("is_estopped_status", False)
        self.actionbutton_4.setProperty("is_on_status", False)
        self.actionbutton_4.setProperty("is_idle_status", False)
        self.actionbutton_4.setProperty("is_homed_status", False)
        self.actionbutton_4.setProperty("is_flood_status", False)
        self.actionbutton_4.setProperty("is_mist_status", False)
        self.actionbutton_4.setProperty("is_block_delete_status", False)
        self.actionbutton_4.setProperty("is_optional_stop_status", False)
        self.actionbutton_4.setProperty("is_joint_homed_status", False)
        self.actionbutton_4.setProperty("is_limits_overridden_status", False)
        self.actionbutton_4.setProperty("is_manual_status", False)
        self.actionbutton_4.setProperty("is_mdi_status", True)
        self.actionbutton_4.setProperty("is_auto_status", False)
        self.actionbutton_4.setProperty("is_spindle_stopped_status", False)
        self.actionbutton_4.setProperty("is_spindle_fwd_status", False)
        self.actionbutton_4.setProperty("is_spindle_rev_status", False)
        self.actionbutton_4.setProperty("joint_number_status", 0)
        self.actionbutton_4.setProperty("mdi_action", True)
        self.actionbutton_4.setProperty("template_label_option", False)
        self.actionbutton_4.setProperty("joint_number", 0)
        self.actionbutton_4.setProperty("incr_imperial_number", 0.010000000000000)
        self.actionbutton_4.setProperty("incr_mm_number", 0.025000000000000)
        self.actionbutton_4.setProperty("incr_angular_number", -1.000000000000000)
        self.actionbutton_4.setProperty("toggle_float_option", False)
        self.actionbutton_4.setProperty("float_num", 0.300000000000000)
        self.actionbutton_4.setProperty("float_alt_num", 50.000000000000000)
        self.actionbutton_4.setProperty("ini_mdi_number", 0)

        self.gridLayout_18.addWidget(self.actionbutton_4, 2, 1, 1, 1)

        self.actionbutton_5 = ActionButton(self.frame_15)
        self.actionbutton_5.setObjectName(u"actionbutton_5")
        self.actionbutton_5.setMinimumSize(QSize(41, 41))
        self.actionbutton_5.setMaximumSize(QSize(80, 16777215))
        self.actionbutton_5.setProperty("indicator_option", True)
        self.actionbutton_5.setProperty("indicator_HAL_pin_option", False)
        self.actionbutton_5.setProperty("indicator_status_option", True)
        self.actionbutton_5.setProperty("checked_state_text_option", False)
        self.actionbutton_5.setProperty("python_command_option", False)
        self.actionbutton_5.setProperty("on_color", QColor(255, 0, 0))
        self.actionbutton_5.setProperty("shape_option", 0)
        self.actionbutton_5.setProperty("off_color", QColor(0, 0, 0))
        self.actionbutton_5.setProperty("indicator_size", 0.300000000000000)
        self.actionbutton_5.setProperty("circle_diameter", 10.000000000000000)
        self.actionbutton_5.setProperty("right_edge_offset", 0.000000000000000)
        self.actionbutton_5.setProperty("top_edge_offset", 0.000000000000000)
        self.actionbutton_5.setProperty("corner_radius", 5.000000000000000)
        self.actionbutton_5.setProperty("height_fraction", 0.300000000000000)
        self.actionbutton_5.setProperty("width_fraction", 0.900000000000000)
        self.actionbutton_5.setProperty("invert_the_status", False)
        self.actionbutton_5.setProperty("is_paused_status", False)
        self.actionbutton_5.setProperty("is_estopped_status", False)
        self.actionbutton_5.setProperty("is_on_status", False)
        self.actionbutton_5.setProperty("is_idle_status", False)
        self.actionbutton_5.setProperty("is_homed_status", False)
        self.actionbutton_5.setProperty("is_flood_status", False)
        self.actionbutton_5.setProperty("is_mist_status", False)
        self.actionbutton_5.setProperty("is_block_delete_status", False)
        self.actionbutton_5.setProperty("is_optional_stop_status", False)
        self.actionbutton_5.setProperty("is_joint_homed_status", False)
        self.actionbutton_5.setProperty("is_limits_overridden_status", False)
        self.actionbutton_5.setProperty("is_manual_status", False)
        self.actionbutton_5.setProperty("is_mdi_status", False)
        self.actionbutton_5.setProperty("is_auto_status", True)
        self.actionbutton_5.setProperty("is_spindle_stopped_status", False)
        self.actionbutton_5.setProperty("is_spindle_fwd_status", False)
        self.actionbutton_5.setProperty("is_spindle_rev_status", False)
        self.actionbutton_5.setProperty("joint_number_status", 0)
        self.actionbutton_5.setProperty("auto_action", True)
        self.actionbutton_5.setProperty("template_label_option", False)
        self.actionbutton_5.setProperty("joint_number", 0)
        self.actionbutton_5.setProperty("incr_imperial_number", 0.010000000000000)
        self.actionbutton_5.setProperty("incr_mm_number", 0.025000000000000)
        self.actionbutton_5.setProperty("incr_angular_number", -1.000000000000000)
        self.actionbutton_5.setProperty("toggle_float_option", False)
        self.actionbutton_5.setProperty("float_num", 0.300000000000000)
        self.actionbutton_5.setProperty("float_alt_num", 50.000000000000000)
        self.actionbutton_5.setProperty("ini_mdi_number", 0)

        self.gridLayout_18.addWidget(self.actionbutton_5, 2, 2, 1, 1)

        self.actionbutton_6 = ActionButton(self.frame_15)
        self.actionbutton_6.setObjectName(u"actionbutton_6")
        sizePolicy.setHeightForWidth(self.actionbutton_6.sizePolicy().hasHeightForWidth())
        self.actionbutton_6.setSizePolicy(sizePolicy)
        self.actionbutton_6.setMinimumSize(QSize(80, 40))
        self.actionbutton_6.setProperty("indicator_option", False)
        self.actionbutton_6.setProperty("indicator_HAL_pin_option", False)
        self.actionbutton_6.setProperty("indicator_status_option", False)
        self.actionbutton_6.setProperty("checked_state_text_option", False)
        self.actionbutton_6.setProperty("python_command_option", False)
        self.actionbutton_6.setProperty("on_color", QColor(255, 0, 0))
        self.actionbutton_6.setProperty("shape_option", 0)
        self.actionbutton_6.setProperty("off_color", QColor(0, 0, 0))
        self.actionbutton_6.setProperty("indicator_size", 0.300000000000000)
        self.actionbutton_6.setProperty("circle_diameter", 10.000000000000000)
        self.actionbutton_6.setProperty("right_edge_offset", 0.000000000000000)
        self.actionbutton_6.setProperty("top_edge_offset", 0.000000000000000)
        self.actionbutton_6.setProperty("corner_radius", 5.000000000000000)
        self.actionbutton_6.setProperty("height_fraction", 0.300000000000000)
        self.actionbutton_6.setProperty("width_fraction", 0.900000000000000)
        self.actionbutton_6.setProperty("invert_the_status", False)
        self.actionbutton_6.setProperty("is_paused_status", False)
        self.actionbutton_6.setProperty("is_estopped_status", False)
        self.actionbutton_6.setProperty("is_on_status", False)
        self.actionbutton_6.setProperty("is_idle_status", False)
        self.actionbutton_6.setProperty("is_homed_status", False)
        self.actionbutton_6.setProperty("is_flood_status", False)
        self.actionbutton_6.setProperty("is_mist_status", False)
        self.actionbutton_6.setProperty("is_block_delete_status", False)
        self.actionbutton_6.setProperty("is_optional_stop_status", False)
        self.actionbutton_6.setProperty("is_joint_homed_status", False)
        self.actionbutton_6.setProperty("is_limits_overridden_status", False)
        self.actionbutton_6.setProperty("is_manual_status", False)
        self.actionbutton_6.setProperty("is_mdi_status", False)
        self.actionbutton_6.setProperty("is_auto_status", False)
        self.actionbutton_6.setProperty("is_spindle_stopped_status", False)
        self.actionbutton_6.setProperty("is_spindle_fwd_status", False)
        self.actionbutton_6.setProperty("is_spindle_rev_status", False)
        self.actionbutton_6.setProperty("joint_number_status", 0)
        self.actionbutton_6.setProperty("launch_halmeter_action", True)
        self.actionbutton_6.setProperty("template_label_option", False)
        self.actionbutton_6.setProperty("joint_number", 0)
        self.actionbutton_6.setProperty("incr_imperial_number", 0.010000000000000)
        self.actionbutton_6.setProperty("incr_mm_number", 0.025000000000000)
        self.actionbutton_6.setProperty("incr_angular_number", -1.000000000000000)
        self.actionbutton_6.setProperty("toggle_float_option", False)
        self.actionbutton_6.setProperty("float_num", 0.300000000000000)
        self.actionbutton_6.setProperty("float_alt_num", 50.000000000000000)
        self.actionbutton_6.setProperty("ini_mdi_number", 0)

        self.gridLayout_18.addWidget(self.actionbutton_6, 0, 5, 1, 1)

        self.actionbutton_7 = ActionButton(self.frame_15)
        self.actionbutton_7.setObjectName(u"actionbutton_7")
        sizePolicy.setHeightForWidth(self.actionbutton_7.sizePolicy().hasHeightForWidth())
        self.actionbutton_7.setSizePolicy(sizePolicy)
        self.actionbutton_7.setMinimumSize(QSize(80, 40))
        self.actionbutton_7.setProperty("indicator_option", False)
        self.actionbutton_7.setProperty("indicator_HAL_pin_option", False)
        self.actionbutton_7.setProperty("indicator_status_option", False)
        self.actionbutton_7.setProperty("checked_state_text_option", False)
        self.actionbutton_7.setProperty("python_command_option", False)
        self.actionbutton_7.setProperty("on_color", QColor(255, 0, 0))
        self.actionbutton_7.setProperty("shape_option", 0)
        self.actionbutton_7.setProperty("off_color", QColor(0, 0, 0))
        self.actionbutton_7.setProperty("indicator_size", 0.300000000000000)
        self.actionbutton_7.setProperty("circle_diameter", 10.000000000000000)
        self.actionbutton_7.setProperty("right_edge_offset", 0.000000000000000)
        self.actionbutton_7.setProperty("top_edge_offset", 0.000000000000000)
        self.actionbutton_7.setProperty("corner_radius", 5.000000000000000)
        self.actionbutton_7.setProperty("height_fraction", 0.300000000000000)
        self.actionbutton_7.setProperty("width_fraction", 0.900000000000000)
        self.actionbutton_7.setProperty("invert_the_status", False)
        self.actionbutton_7.setProperty("is_paused_status", False)
        self.actionbutton_7.setProperty("is_estopped_status", False)
        self.actionbutton_7.setProperty("is_on_status", False)
        self.actionbutton_7.setProperty("is_idle_status", False)
        self.actionbutton_7.setProperty("is_homed_status", False)
        self.actionbutton_7.setProperty("is_flood_status", False)
        self.actionbutton_7.setProperty("is_mist_status", False)
        self.actionbutton_7.setProperty("is_block_delete_status", False)
        self.actionbutton_7.setProperty("is_optional_stop_status", False)
        self.actionbutton_7.setProperty("is_joint_homed_status", False)
        self.actionbutton_7.setProperty("is_limits_overridden_status", False)
        self.actionbutton_7.setProperty("is_manual_status", False)
        self.actionbutton_7.setProperty("is_mdi_status", False)
        self.actionbutton_7.setProperty("is_auto_status", False)
        self.actionbutton_7.setProperty("is_spindle_stopped_status", False)
        self.actionbutton_7.setProperty("is_spindle_fwd_status", False)
        self.actionbutton_7.setProperty("is_spindle_rev_status", False)
        self.actionbutton_7.setProperty("joint_number_status", 0)
        self.actionbutton_7.setProperty("launch_status_action", True)
        self.actionbutton_7.setProperty("template_label_option", False)
        self.actionbutton_7.setProperty("joint_number", 0)
        self.actionbutton_7.setProperty("incr_imperial_number", 0.010000000000000)
        self.actionbutton_7.setProperty("incr_mm_number", 0.025000000000000)
        self.actionbutton_7.setProperty("incr_angular_number", -1.000000000000000)
        self.actionbutton_7.setProperty("toggle_float_option", False)
        self.actionbutton_7.setProperty("float_num", 0.300000000000000)
        self.actionbutton_7.setProperty("float_alt_num", 50.000000000000000)
        self.actionbutton_7.setProperty("ini_mdi_number", 0)

        self.gridLayout_18.addWidget(self.actionbutton_7, 1, 5, 1, 1)

        self.btn_jog_l_slow = PushButton(self.frame_14)
        self.btn_jog_l_slow.setObjectName(u"btn_jog_l_slow")
        self.btn_jog_l_slow.setGeometry(QRect(120, 120, 50, 40))
        sizePolicy.setHeightForWidth(self.btn_jog_l_slow.sizePolicy().hasHeightForWidth())
        self.btn_jog_l_slow.setSizePolicy(sizePolicy)
        self.btn_jog_l_slow.setMinimumSize(QSize(50, 30))
        self.btn_jog_l_slow.setMaximumSize(QSize(63, 40))
        self.btn_jog_l_slow.setCheckable(True)
        self.btn_jog_l_slow.setProperty("checked_state_text_option", True)
        self.frame_17 = QFrame(self.frame_14)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(150, 210, 141, 69))
        self.frame_17.setFrameShape(QFrame.WinPanel)
        self.frame_17.setFrameShadow(QFrame.Plain)
        self.gridLayout_20 = QGridLayout(self.frame_17)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.label_37 = QLabel(self.frame_17)
        self.label_37.setObjectName(u"label_37")
        sizePolicy.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy)
        self.label_37.setMinimumSize(QSize(50, 20))
        self.label_37.setMaximumSize(QSize(50, 20))
        self.label_37.setStyleSheet(u"")
        self.label_37.setAlignment(Qt.AlignCenter)

        self.gridLayout_20.addWidget(self.label_37, 0, 1, 1, 1)

        self.statelabel_metric = StateLabel(self.frame_17)
        self.statelabel_metric.setObjectName(u"statelabel_metric")
        sizePolicy.setHeightForWidth(self.statelabel_metric.sizePolicy().hasHeightForWidth())
        self.statelabel_metric.setSizePolicy(sizePolicy)
        self.statelabel_metric.setMinimumSize(QSize(50, 24))
        self.statelabel_metric.setMaximumSize(QSize(50, 24))
        self.statelabel_metric.setFrameShape(QFrame.WinPanel)
        self.statelabel_metric.setFrameShadow(QFrame.Sunken)
        self.statelabel_metric.setLineWidth(1)
        self.statelabel_metric.setAlignment(Qt.AlignCenter)

        self.gridLayout_20.addWidget(self.statelabel_metric, 1, 1, 1, 1)

        self.pushbutton_metric = PushButton(self.frame_17)
        self.pushbutton_metric.setObjectName(u"pushbutton_metric")
        self.pushbutton_metric.setMinimumSize(QSize(0, 41))
        self.pushbutton_metric.setCheckable(True)
        self.pushbutton_metric.setProperty("checked_state_text_option", True)

        self.gridLayout_20.addWidget(self.pushbutton_metric, 0, 0, 2, 1)


        self.verticalLayout_19.addWidget(self.frame_14)


        self.verticalLayout_32.addWidget(self.frame_12)

        self.widgetswitcher.addWidget(self.setupPage)
        self.mdiPage = QWidget()
        self.mdiPage.setObjectName(u"mdiPage")
        self.verticalLayout_33 = QVBoxLayout(self.mdiPage)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.mdiPage)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.WinPanel)
        self.frame_7.setFrameShadow(QFrame.Plain)
        self.verticalLayout_11 = QVBoxLayout(self.frame_7)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.mdi_tab = QTabWidget(self.frame_7)
        self.mdi_tab.setObjectName(u"mdi_tab")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_22 = QVBoxLayout(self.tab)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.mdihistory = MDIHistory(self.tab)
        self.mdihistory.setObjectName(u"mdihistory")
        self.mdihistory.setMinimumSize(QSize(100, 100))
        self.mdihistory.setProperty("soft_keyboard_option", True)

        self.verticalLayout_22.addWidget(self.mdihistory)

        self.mdi_tab.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_27 = QVBoxLayout(self.tab_2)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_13 = QFrame(self.tab_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.WinPanel)
        self.frame_13.setFrameShadow(QFrame.Plain)
        self.verticalLayout_25 = QVBoxLayout(self.frame_13)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_24 = QLabel(self.frame_13)
        self.label_24.setObjectName(u"label_24")
        sizePolicy5.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy5)
        self.label_24.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_25.addWidget(self.label_24)

        self.macrotab = MacroTab(self.frame_13)
        self.macrotab.setObjectName(u"macrotab")
        sizePolicy2.setHeightForWidth(self.macrotab.sizePolicy().hasHeightForWidth())
        self.macrotab.setSizePolicy(sizePolicy2)
        self.macrotab.setMinimumSize(QSize(400, 300))
        self.macrotab.setMaximumSize(QSize(600, 40000))

        self.verticalLayout_25.addWidget(self.macrotab)


        self.verticalLayout_27.addWidget(self.frame_13)

        self.mdi_tab.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.mditouchy = MDITouchy(self.tab_3)
        self.mditouchy.setObjectName(u"mditouchy")
        self.mditouchy.setGeometry(QRect(10, 9, 691, 451))
        self.mditouchy.setStyleSheet(u"")
        self.btn_start_macro = PushButton(self.tab_3)
        self.btn_start_macro.setObjectName(u"btn_start_macro")
        self.btn_start_macro.setGeometry(QRect(130, 470, 101, 51))
        self.mdi_tab.addTab(self.tab_3, "")
        self.tab_gcode = QWidget()
        self.tab_gcode.setObjectName(u"tab_gcode")
        self.horizontalLayout_7 = QHBoxLayout(self.tab_gcode)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_56 = QVBoxLayout()
        self.verticalLayout_56.setSpacing(4)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.gcode_list = QListWidget(self.tab_gcode)
        self.gcode_list.setObjectName(u"gcode_list")
        self.gcode_list.setFrameShape(QFrame.WinPanel)
        self.gcode_list.setFrameShadow(QFrame.Raised)

        self.verticalLayout_56.addWidget(self.gcode_list)


        self.horizontalLayout_7.addLayout(self.verticalLayout_56)

        self.verticalLayout_55 = QVBoxLayout()
        self.verticalLayout_55.setSpacing(4)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(4, -1, 4, -1)
        self.gcode_parameters = QLabel(self.tab_gcode)
        self.gcode_parameters.setObjectName(u"gcode_parameters")
        self.gcode_parameters.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.gcode_parameters.setFrameShape(QFrame.WinPanel)
        self.gcode_parameters.setFrameShadow(QFrame.Raised)

        self.verticalLayout_55.addWidget(self.gcode_parameters)

        self.gcode_description = QPlainTextEdit(self.tab_gcode)
        self.gcode_description.setObjectName(u"gcode_description")
        self.gcode_description.setFrameShape(QFrame.WinPanel)
        self.gcode_description.setFrameShadow(QFrame.Raised)

        self.verticalLayout_55.addWidget(self.gcode_description)


        self.horizontalLayout_7.addLayout(self.verticalLayout_55)

        self.mdi_tab.addTab(self.tab_gcode, "")

        self.verticalLayout_11.addWidget(self.mdi_tab)


        self.verticalLayout_33.addWidget(self.frame_7)

        self.widgetswitcher.addWidget(self.mdiPage)

        self.verticalLayout_4.addWidget(self.widgetswitcher)

        self.mainPaneStack.addWidget(self.operationPage)
        self.loadPage = QWidget()
        self.loadPage.setObjectName(u"loadPage")
        self.verticalLayout_12 = QVBoxLayout(self.loadPage)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.screen_options = ScreenOptions(self.loadPage)
        self.screen_options.setObjectName(u"screen_options")
        self.screen_options.setProperty("focusOverlay_option", True)
        self.screen_options.setProperty("entryDialog_option", True)
        self.screen_options.setProperty("toolDialog_option", True)
        self.screen_options.setProperty("fileDialog_option", True)
        self.screen_options.setProperty("versaProbeDialog_option", False)
        self.screen_options.setProperty("macroTabDialog_option", False)
        self.screen_options.setProperty("camViewDialog_option", True)
        self.screen_options.setProperty("toolOffsetDialog_option", True)
        self.screen_options.setProperty("originOffsetDialog_option", True)
        self.screen_options.setProperty("calculatorDialog_option", True)
        self.screen_options.setProperty("machineLogDialog_option", True)
        self.screen_options.setProperty("runFromLineDialog_option", True)
        self.verticalLayout_15 = QVBoxLayout(self.screen_options)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.screen_options)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.WinPanel)
        self.frame_11.setFrameShadow(QFrame.Plain)
        self.gridLayout_11 = QGridLayout(self.frame_11)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_21 = QLabel(self.frame_11)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_11.addWidget(self.label_21, 0, 0, 1, 2)

        self.frm_filemanager = QFrame(self.frame_11)
        self.frm_filemanager.setObjectName(u"frm_filemanager")
        sizePolicy1.setHeightForWidth(self.frm_filemanager.sizePolicy().hasHeightForWidth())
        self.frm_filemanager.setSizePolicy(sizePolicy1)
        self.frm_filemanager.setMinimumSize(QSize(92, 0))
        self.frm_filemanager.setFrameShape(QFrame.WinPanel)
        self.frm_filemanager.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frm_filemanager)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_13, 6, 0, 1, 1)

        self.btn_file_prev = PushButton(self.frm_filemanager)
        self.btn_file_prev.setObjectName(u"btn_file_prev")
        sizePolicy.setHeightForWidth(self.btn_file_prev.sizePolicy().hasHeightForWidth())
        self.btn_file_prev.setSizePolicy(sizePolicy)
        self.btn_file_prev.setMinimumSize(QSize(80, 50))
        self.btn_file_prev.setMaximumSize(QSize(80, 50))
        self.btn_file_prev.setProperty("python_command_option", True)

        self.gridLayout_3.addWidget(self.btn_file_prev, 4, 0, 1, 1)

        self.btn_gcode_edit = PushButton(self.frm_filemanager)
        self.btn_gcode_edit.setObjectName(u"btn_gcode_edit")
        sizePolicy.setHeightForWidth(self.btn_gcode_edit.sizePolicy().hasHeightForWidth())
        self.btn_gcode_edit.setSizePolicy(sizePolicy)
        self.btn_gcode_edit.setMinimumSize(QSize(80, 50))
        self.btn_gcode_edit.setMaximumSize(QSize(80, 50))
        self.btn_gcode_edit.setCheckable(True)
        self.btn_gcode_edit.setChecked(False)
        self.btn_gcode_edit.setProperty("python_command_option", False)

        self.gridLayout_3.addWidget(self.btn_gcode_edit, 5, 0, 1, 1)

        self.btn_file_next = PushButton(self.frm_filemanager)
        self.btn_file_next.setObjectName(u"btn_file_next")
        sizePolicy.setHeightForWidth(self.btn_file_next.sizePolicy().hasHeightForWidth())
        self.btn_file_next.setSizePolicy(sizePolicy)
        self.btn_file_next.setMinimumSize(QSize(80, 50))
        self.btn_file_next.setMaximumSize(QSize(80, 50))
        self.btn_file_next.setProperty("python_command_option", True)

        self.gridLayout_3.addWidget(self.btn_file_next, 2, 0, 1, 1)

        self.btn_file_load = PushButton(self.frm_filemanager)
        self.btn_file_load.setObjectName(u"btn_file_load")
        sizePolicy.setHeightForWidth(self.btn_file_load.sizePolicy().hasHeightForWidth())
        self.btn_file_load.setSizePolicy(sizePolicy)
        self.btn_file_load.setMinimumSize(QSize(80, 50))
        self.btn_file_load.setMaximumSize(QSize(80, 50))
        self.btn_file_load.setProperty("python_command_option", False)

        self.gridLayout_3.addWidget(self.btn_file_load, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.frm_filemanager, 0, 2, 2, 1)

        self.filemanager = FileManager(self.frame_11)
        self.filemanager.setObjectName(u"filemanager")
        sizePolicy2.setHeightForWidth(self.filemanager.sizePolicy().hasHeightForWidth())
        self.filemanager.setSizePolicy(sizePolicy2)
        self.filemanager.setMinimumSize(QSize(0, 0))

        self.gridLayout_11.addWidget(self.filemanager, 1, 0, 1, 1)

        self.gcode_editor = GcodeEditor(self.frame_11)
        self.gcode_editor.setObjectName(u"gcode_editor")
        self.gcode_editor.setMinimumSize(QSize(0, 0))
        self.gcode_editor.setProperty("auto_show_mdi_status", False)

        self.gridLayout_11.addWidget(self.gcode_editor, 1, 1, 1, 1)


        self.verticalLayout_15.addWidget(self.frame_11)


        self.verticalLayout_12.addWidget(self.screen_options)

        self.mainPaneStack.addWidget(self.loadPage)

        self.horizontalLayout_4.addWidget(self.mainPaneStack)


        self.horizontalLayout.addLayout(self.horizontalLayout_4)


        self.gridLayout_6.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.homeIcon = StatusImageSwitcher(self.centralwidget)
        self.homeIcon.setObjectName(u"homeIcon")
        self.homeIcon.setPixmap(QPixmap(u":/images/images/ref_z_not.png"))
        self.homeIcon.setProperty("image_number", 0)
        self.homeIcon.setProperty("watch_all_homed", False)
        self.homeIcon.setProperty("watch_axis_homed", True)

        self.horizontalLayout_3.addWidget(self.homeIcon)

        self.homeIcon_x = StatusImageSwitcher(self.centralwidget)
        self.homeIcon_x.setObjectName(u"homeIcon_x")
        self.homeIcon_x.setPixmap(QPixmap(u":/images/images/clear.png"))
        self.homeIcon_x.setProperty("watch_all_homed", False)
        self.homeIcon_x.setProperty("watch_axis_homed", True)

        self.horizontalLayout_3.addWidget(self.homeIcon_x)

        self.HardLimitIcon = StatusImageSwitcher(self.centralwidget)
        self.HardLimitIcon.setObjectName(u"HardLimitIcon")
        self.HardLimitIcon.setPixmap(QPixmap(u"../../images/clear.png"))
        self.HardLimitIcon.setProperty("watch_hard_limits", True)

        self.horizontalLayout_3.addWidget(self.HardLimitIcon)

        self.hardLimit2Icon = StatusImageSwitcher(self.centralwidget)
        self.hardLimit2Icon.setObjectName(u"hardLimit2Icon")
        self.hardLimit2Icon.setPixmap(QPixmap(u"../../images/clear.png"))
        self.hardLimit2Icon.setProperty("watch_hard_limits", True)

        self.horizontalLayout_3.addWidget(self.hardLimit2Icon)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy9)
        self.label_2.setMinimumSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy9.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy9)
        self.label.setMinimumSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy9.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy9)
        self.label_3.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.gridLayout_6.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1500, 27))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuMachine = QMenu(self.menubar)
        self.menuMachine.setObjectName(u"menuMachine")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuGridSize = QMenu(self.menuView)
        self.menuGridSize.setObjectName(u"menuGridSize")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuSystem = QMenu(self.menubar)
        self.menuSystem.setObjectName(u"menuSystem")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuMachine.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuSystem.menuAction())
        self.menuFile.addAction(self.actionReload)
        self.menuMachine.addAction(self.actionStep)
        self.menuView.addAction(self.menuGridSize.menuAction())
        self.menuView.addAction(self.actionCalculatorDialog)
        self.menuView.addAction(self.actionToolOffsetDialog)

        self.retranslateUi(MainWindow)
        self.btn_m61.clicked.connect(MainWindow.btn_m61_clicked)
        self.gcodegraphics.percentLoaded.connect(MainWindow.percentLoaded)
        self.gcode_viewer.percentDone.connect(MainWindow.percentLoaded)
        self.gcode_viewer.percentDone.connect(self.progressBar.setValue)
        self.btn_clear_alarms.clicked.connect(MainWindow.btn_clear_alarms_clicked)
        self.btn_save_alarms.clicked.connect(MainWindow.btn_save_alarms_clicked)
        self.btn_start_macro.clicked.connect(MainWindow.btn_start_macro_clicked)
        self.btn_jog_l_slow.clicked.connect(MainWindow.slow_jog_clicked)
        self.btn_gcode_edit.clicked.connect(MainWindow.btn_gcode_edit_clicked)
        self.btn_file_load.clicked.connect(MainWindow.btn_load_file_clicked)

        self.droPaneStack.setCurrentIndex(1)
        self.mainLeftStack.setCurrentIndex(1)
        self.mainPaneStack.setCurrentIndex(0)
        self.widgetswitcher.setCurrentIndex(3)
        self.mdi_tab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionCalculatorDialog.setText(QCoreApplication.translate("MainWindow", u"Calculator", None))
#if QT_CONFIG(shortcut)
        self.actionCalculatorDialog.setShortcut(QCoreApplication.translate("MainWindow", u"F9", None))
#endif // QT_CONFIG(shortcut)
        self.actionToolOffsetDialog.setText(QCoreApplication.translate("MainWindow", u"Edit Tooltable", None))
#if QT_CONFIG(shortcut)
        self.actionToolOffsetDialog.setShortcut(QCoreApplication.translate("MainWindow", u"F6", None))
#endif // QT_CONFIG(shortcut)
        self.actionReload.setText(QCoreApplication.translate("MainWindow", u"Reload", None))
        self.actionStep.setText(QCoreApplication.translate("MainWindow", u"Step", None))
        self.actionbutton.setText(QCoreApplication.translate("MainWindow", u"Estop", None))
        self.actionbutton.setProperty("true_state_string", QCoreApplication.translate("MainWindow", u"True", None))
        self.actionbutton.setProperty("false_state_string", QCoreApplication.translate("MainWindow", u"False", None))
        self.actionbutton.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.actionbutton.setProperty("command_text_string", "")
        self.actionbutton.setProperty("textTemplate", "")
        self.actionbutton.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.actionbutton_2.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.actionbutton_2.setProperty("true_state_string", QCoreApplication.translate("MainWindow", u"True", None))
        self.actionbutton_2.setProperty("false_state_string", QCoreApplication.translate("MainWindow", u"False", None))
        self.actionbutton_2.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.actionbutton_2.setProperty("command_text_string", "")
        self.actionbutton_2.setProperty("textTemplate", "")
        self.actionbutton_2.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.action_pause.setText(QCoreApplication.translate("MainWindow", u"PAUSE", None))
        self.action_pause.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.action_pause.setProperty("command_text_string", "")
        self.action_pause.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.action_pause.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.actionbutton_13.setText(QCoreApplication.translate("MainWindow", u"Abort", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"RUN TIME", None))
        self.lbl_runtime.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.pushbutton_3.setText(QCoreApplication.translate("MainWindow", u"Prog", None))
        self.pushbutton_3.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"INSTANCE.toggle_prog()", None))
        self.pushbutton_3.setProperty("false_python_cmd_string", "")
        self.pushbutton_2.setText(QCoreApplication.translate("MainWindow", u"Setup", None))
        self.pushbutton_2.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"INSTANCE.toggle_setup()", None))
        self.pushbutton_2.setProperty("false_python_cmd_string", "")
        self.pushbutton_5.setText(QCoreApplication.translate("MainWindow", u"MDI", None))
        self.pushbutton_5.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"INSTANCE.toggle_MDI()", None))
        self.pushbutton_5.setProperty("false_python_cmd_string", "")
        self.actionbutton_view_y2.setText(QCoreApplication.translate("MainWindow", u"Y2", None))
        self.actionbutton_view_y2.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"Y2", None))
#if QT_CONFIG(tooltip)
        self.actionbutton_view_y.setToolTip(QCoreApplication.translate("MainWindow", u"Set view Y", None))
#endif // QT_CONFIG(tooltip)
        self.actionbutton_view_y.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.actionbutton_view_y.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"Y", None))
        self.actionbutton_view_y.setProperty("command_text_string", "")
        self.actionbutton_view_y.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.actionbutton_view_y.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
#if QT_CONFIG(tooltip)
        self.actionbutton_clear.setToolTip(QCoreApplication.translate("MainWindow", u"Clear display", None))
#endif // QT_CONFIG(tooltip)
        self.actionbutton_clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.actionbutton_clear.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"Clear", None))
        self.actionbutton_clear.setProperty("command_text_string", "")
        self.actionbutton_clear.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.actionbutton_clear.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.pushbutton_6.setText(QCoreApplication.translate("MainWindow", u"Graphics", None))
        self.pushbutton_6.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"INSTANCE.toggle_graphics()", None))
        self.pushbutton_6.setProperty("false_python_cmd_string", "")
        self.pushbutton_4.setText(QCoreApplication.translate("MainWindow", u"Dro", None))
        self.pushbutton_4.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"INSTANCE.toggle_dro()", None))
        self.pushbutton_4.setProperty("false_python_cmd_string", "")
        self.pushbutton.setText(QCoreApplication.translate("MainWindow", u"Offsets", None))
        self.pushbutton.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"INSTANCE.toggle_offsets()", None))
        self.pushbutton.setProperty("false_python_cmd_string", "")
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"PROGRESS %p%", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.btn_start.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.btn_start.setProperty("command_text_string", "")
        self.btn_start.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.btn_start.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"SPINDLE", None))
        self.spindle_reverse.setText(QCoreApplication.translate("MainWindow", u"REV", None))
        self.spindle_reverse.setProperty("true_state_string", QCoreApplication.translate("MainWindow", u"True", None))
        self.spindle_reverse.setProperty("false_state_string", QCoreApplication.translate("MainWindow", u"False", None))
        self.spindle_reverse.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"print\"true command\"", None))
        self.spindle_reverse.setProperty("false_python_cmd_string", QCoreApplication.translate("MainWindow", u"print\"false command\"", None))
        self.spindle_reverse.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.spindle_reverse.setProperty("command_text_string", "")
        self.spindle_reverse.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.spindle_reverse.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.spindle_stop.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.spindle_stop.setProperty("true_state_string", QCoreApplication.translate("MainWindow", u"True", None))
        self.spindle_stop.setProperty("false_state_string", QCoreApplication.translate("MainWindow", u"False", None))
        self.spindle_stop.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"print\"true command\"", None))
        self.spindle_stop.setProperty("false_python_cmd_string", QCoreApplication.translate("MainWindow", u"print\"false command\"", None))
        self.spindle_stop.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.spindle_stop.setProperty("command_text_string", "")
        self.spindle_stop.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.spindle_stop.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.spindle_forward.setText(QCoreApplication.translate("MainWindow", u"FWD", None))
        self.spindle_forward.setProperty("true_state_string", QCoreApplication.translate("MainWindow", u"True", None))
        self.spindle_forward.setProperty("false_state_string", QCoreApplication.translate("MainWindow", u"False", None))
        self.spindle_forward.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"print\"true command\"", None))
        self.spindle_forward.setProperty("false_python_cmd_string", QCoreApplication.translate("MainWindow", u"print\"false command\"", None))
        self.spindle_forward.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.spindle_forward.setProperty("command_text_string", "")
        self.spindle_forward.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.spindle_forward.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"AT SPEED", None))
        self.actionbutton_11.setText(QCoreApplication.translate("MainWindow", u"Spindle\n"
"Slover", None))
        self.actionbutton_12.setText(QCoreApplication.translate("MainWindow", u"Spindle\n"
"Faster", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"SPINDLE OVERRIDE", None))
#if QT_CONFIG(tooltip)
        self.action_spindle_ovr_50.setToolTip(QCoreApplication.translate("MainWindow", u"Set spindle override to 50%", None))
#endif // QT_CONFIG(tooltip)
        self.action_spindle_ovr_50.setText(QCoreApplication.translate("MainWindow", u"50", None))
#if QT_CONFIG(tooltip)
        self.action_spindle_ovr_100.setToolTip(QCoreApplication.translate("MainWindow", u"Set spindle override to 100%", None))
#endif // QT_CONFIG(tooltip)
        self.action_spindle_ovr_100.setText(QCoreApplication.translate("MainWindow", u"100", None))
#if QT_CONFIG(tooltip)
        self.action_spindle_ovr_120.setToolTip(QCoreApplication.translate("MainWindow", u"Set spindle override to 120%", None))
#endif // QT_CONFIG(tooltip)
        self.action_spindle_ovr_120.setText(QCoreApplication.translate("MainWindow", u"120", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"OVR", None))
#if QT_CONFIG(tooltip)
        self.status_spindle_ovr.setToolTip(QCoreApplication.translate("MainWindow", u"Spindle speed override", None))
#endif // QT_CONFIG(tooltip)
        self.status_spindle_ovr.setText(QCoreApplication.translate("MainWindow", u"100 %", None))
        self.status_spindle_ovr.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%d %%", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"REQ", None))
#if QT_CONFIG(tooltip)
        self.label_spindle_set.setToolTip(QCoreApplication.translate("MainWindow", u"Requested spindle speed", None))
#endif // QT_CONFIG(tooltip)
        self.label_spindle_set.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.label_spindle_set.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%d", None))
        self.label_spindle_set.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%d", None))
#if QT_CONFIG(tooltip)
        self.slider_spindle_ovr.setToolTip(QCoreApplication.translate("MainWindow", u"Adjust spindle override", None))
#endif // QT_CONFIG(tooltip)
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Spindle\n"
" Load", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Surface\n"
" Speed", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Gear", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Active\n"
" Feed", None))
        self.statuslabel_6.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%d", None))
        self.statuslabel_6.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%d", None))
        self.statuslabel_11.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%.3fin/rev", None))
        self.statuslabel_11.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%.2fmm/rev", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"low", None))
        self.label_dro_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Position </span>- Machine</p></body></html>", None))
        self.label_x.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">X </span><span style=\" font-size:18pt;\">RADIUS</span></p></body></html>", None))
        self.dro_label_x.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">%10.3f</span><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">in</span></p></body></html>", None))
        self.dro_label_x.setProperty("metric_template", QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">%10.3f</span><span style=\" font-size:10pt; font-weight:600; font-style:italic;\"> mm</span></p></body></html>", None))
        self.dro_label_x.setProperty("imperial_template", QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">%9.4f</span><span style=\" font-size:10pt; font-weight:600; font-style:italic;\"> in</span></p></body></html>", None))
        self.label_x_diametr.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">DIAMETER</span></p></body></html>", None))
        self.dro_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">%10.3f</span><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">in</span></p></body></html>", None))
        self.dro_label.setProperty("metric_template", QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">%10.3f</span><span style=\" font-size:10pt; font-weight:600; font-style:italic;\"> mm</span></p></body></html>", None))
        self.dro_label.setProperty("imperial_template", QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">%9.4f</span><span style=\" font-size:10pt; font-weight:600; font-style:italic;\"> in</span></p></body></html>", None))
        self.label_z.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">Z</span></p></body></html>", None))
        self.dro_label_z.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">%9.3f</span><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">in</span></p></body></html>", None))
        self.dro_label_z.setProperty("metric_template", QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">%10.3f</span><span style=\" font-size:10pt; font-weight:600; font-style:italic;\"> mm</span></p></body></html>", None))
        self.dro_label_z.setProperty("imperial_template", QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">%9.4f</span><span style=\" font-size:10pt; font-weight:600; font-style:italic;\"> in</span></p></body></html>", None))
        self.label_dro_title_3.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Position </span>- G%s</p></body></html>", None))
        self.label_x_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">X </span><span style=\" font-size:18pt;\">RADIUS</span></p></body></html>", None))
        self.dro_label_x_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">%10.3f</span><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">in</span></p></body></html>", None))
        self.dro_label_x_2.setProperty("metric_template", QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">%10.3f</span><span style=\" font-size:10pt; font-weight:600; font-style:italic;\"> mm</span></p></body></html>", None))
        self.dro_label_x_2.setProperty("imperial_template", QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">%9.4f</span><span style=\" font-size:10pt; font-weight:600; font-style:italic;\"> in</span></p></body></html>", None))
        self.label_x_diametr_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">DIAMETER</span></p></body></html>", None))
        self.dro_label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">%10.3f</span><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">in</span></p></body></html>", None))
        self.dro_label_2.setProperty("metric_template", QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">%10.3f</span><span style=\" font-size:10pt; font-weight:600; font-style:italic;\"> mm</span></p></body></html>", None))
        self.dro_label_2.setProperty("imperial_template", QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">%9.4f</span><span style=\" font-size:10pt; font-weight:600; font-style:italic;\"> in</span></p></body></html>", None))
        self.label_z_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">Z</span></p></body></html>", None))
        self.dro_label_z_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">%9.3f</span><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">in</span></p></body></html>", None))
        self.dro_label_z_2.setProperty("metric_template", QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">%10.3f</span><span style=\" font-size:10pt; font-weight:600; font-style:italic;\"> mm</span></p></body></html>", None))
        self.dro_label_z_2.setProperty("imperial_template", QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">%9.4f</span><span style=\" font-size:10pt; font-weight:600; font-style:italic;\"> in</span></p></body></html>", None))
        self.label_dro_title_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Position </span>- DTG</p></body></html>", None))
        self.label_x_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">X </span><span style=\" font-size:18pt;\">RADIUS</span></p></body></html>", None))
        self.dro_label_x_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">%10.3f</span><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">in</span></p></body></html>", None))
        self.dro_label_x_3.setProperty("metric_template", QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">%10.3f</span><span style=\" font-size:10pt; font-weight:600; font-style:italic;\"> mm</span></p></body></html>", None))
        self.dro_label_x_3.setProperty("imperial_template", QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">%9.4f</span><span style=\" font-size:10pt; font-weight:600; font-style:italic;\"> in</span></p></body></html>", None))
        self.label_x_diametr_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">DIAMETER</span></p></body></html>", None))
        self.dro_label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">%10.3f</span><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">in</span></p></body></html>", None))
        self.dro_label_3.setProperty("metric_template", QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">%10.3f</span><span style=\" font-size:10pt; font-weight:600; font-style:italic;\"> mm</span></p></body></html>", None))
        self.dro_label_3.setProperty("imperial_template", QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">%9.4f</span><span style=\" font-size:10pt; font-weight:600; font-style:italic;\"> in</span></p></body></html>", None))
        self.label_z_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">Z</span></p></body></html>", None))
        self.dro_label_z_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">%9.3f</span><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">in</span></p></body></html>", None))
        self.dro_label_z_3.setProperty("metric_template", QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">%10.3f</span><span style=\" font-size:10pt; font-weight:600; font-style:italic;\"> mm</span></p></body></html>", None))
        self.dro_label_z_3.setProperty("imperial_template", QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">%9.4f</span><span style=\" font-size:10pt; font-weight:600; font-style:italic;\"> in</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.action_exit.setStatusTip(QCoreApplication.translate("MainWindow", u"EXIT LINUXCNC", None))
#endif // QT_CONFIG(statustip)
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
        self.action_exit.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.action_exit.setProperty("command_text_string", "")
        self.action_exit.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.action_exit.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.statuslabel_3.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"Time:   %a %H:%M %S", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Timers &amp; Counters</span></p></body></html>", None))
        self.label_mode.setText(QCoreApplication.translate("MainWindow", u"Operation", None))
        self.statuslabel_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Active Program: </span>100.0</p></body></html>", None))
        self.statuslabel_13.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Active Program: </span>%s</p></body></html>", None))
        self.gcodegraphics.setProperty("_view", QCoreApplication.translate("MainWindow", u"y", None))
        self.statuslabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Active Gcode</span></p><p>   100.0</p></body></html>", None))
        self.statuslabel.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Active Gcode</span></p><p>   %s</p></body></html>", None))
        self.statelabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Coolant</span></p><p>Off</p></body></html>", None))
        self.statelabel.setProperty("true_textTemplate", QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Coolant</span></p><p>On</p></body></html>", None))
        self.statelabel.setProperty("false_textTemplate", QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Coolant</span></p><p>Off</p></body></html>", None))
        self.statuslabel_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Active Tool</span></p><p>   100.0</p></body></html>", None))
        self.statuslabel_2.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Active Tool</span></p><p>   %s</p></body></html>", None))
        self.widgetswitcher.setProperty("widget_list", QStringList()
            << QCoreApplication.translate("MainWindow", u"gcodegraphics", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Offsets Tool</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.btn_tool_add.setStatusTip(QCoreApplication.translate("MainWindow", u"ADD TOOL TO TOOLTABLE", None))
#endif // QT_CONFIG(statustip)
        self.btn_tool_add.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.btn_tool_add.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"INSTANCE.tooloffsetview.add_tool()", None))
        self.btn_tool_add.setProperty("false_python_cmd_string", "")
#if QT_CONFIG(statustip)
        self.btn_tool_delete.setStatusTip(QCoreApplication.translate("MainWindow", u"DELETE SELECTED TOOLS", None))
#endif // QT_CONFIG(statustip)
        self.btn_tool_delete.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.btn_tool_delete.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"INSTANCE.tooloffsetview.delete_tools()", None))
#if QT_CONFIG(statustip)
        self.btn_m61.setStatusTip(QCoreApplication.translate("MainWindow", u"LOAD SELECTED TOOL", None))
#endif // QT_CONFIG(statustip)
        self.btn_m61.setText(QCoreApplication.translate("MainWindow", u"M61 Qn", None))
        self.action_zero_g92.setText(QCoreApplication.translate("MainWindow", u"ZERO G92", None))
        self.action_zero_g92.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.action_zero_g92.setProperty("command_text_string", "")
        self.action_zero_g92.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.action_zero_g92.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
#if QT_CONFIG(statustip)
        self.action_zero_g5x.setStatusTip(QCoreApplication.translate("MainWindow", u"ZERO CURRENT WCS", None))
#endif // QT_CONFIG(statustip)
        self.action_zero_g5x.setText(QCoreApplication.translate("MainWindow", u"ZERO G5X", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Offset Work</span></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Manual Setup</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.action_home_all.setStatusTip(QCoreApplication.translate("MainWindow", u"HOME ALL AXES", None))
#endif // QT_CONFIG(statustip)
        self.action_home_all.setText(QCoreApplication.translate("MainWindow", u"HOME ALL", None))
        self.action_home_all.setProperty("true_state_string", QCoreApplication.translate("MainWindow", u"ALL HOMED", None))
        self.action_home_all.setProperty("false_state_string", QCoreApplication.translate("MainWindow", u"HOME ALL", None))
        self.action_home_all.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.action_home_all.setProperty("command_text_string", "")
        self.action_home_all.setProperty("textTemplate", "")
        self.action_home_all.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"MAX VEL", None))
        self.statuslabel_8.setText(QCoreApplication.translate("MainWindow", u"200.0in/min", None))
        self.statuslabel_8.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%.1fin/min", None))
        self.statuslabel_8.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%.1fmm/min", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"JOG RATE", None))
        self.statuslabel_7.setText(QCoreApplication.translate("MainWindow", u"200.0in/min", None))
        self.statuslabel_7.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%.1fin/min", None))
        self.statuslabel_7.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%.1fmm/min", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"RAPID OVERRIDE", None))
        self.statuslabel_12.setText(QCoreApplication.translate("MainWindow", u"100 %", None))
        self.statuslabel_12.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%d %%", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"FEED OVERRIDE", None))
        self.statuslabel_10.setText(QCoreApplication.translate("MainWindow", u"100 %", None))
        self.statuslabel_10.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%d %%", None))
        self.y_plus_jogbutton.setText("")
        self.y_plus_jogbutton.setProperty("axis_letter", QCoreApplication.translate("MainWindow", u"X", None))
        self.y_plus_jogbutton.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.y_plus_jogbutton.setProperty("command_text_string", "")
        self.y_plus_jogbutton.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.y_plus_jogbutton.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.y_minus_jogbutton.setText("")
        self.y_minus_jogbutton.setProperty("axis_letter", QCoreApplication.translate("MainWindow", u"X", None))
        self.y_minus_jogbutton.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.y_minus_jogbutton.setProperty("command_text_string", "")
        self.y_minus_jogbutton.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.y_minus_jogbutton.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.a_minus_jogbutton.setText("")
        self.a_minus_jogbutton.setProperty("axis_letter", QCoreApplication.translate("MainWindow", u"Z", None))
        self.a_plus_jogbutton.setText("")
        self.a_plus_jogbutton.setProperty("axis_letter", QCoreApplication.translate("MainWindow", u"Z", None))
#if QT_CONFIG(tooltip)
        self.jogincrements_linear.setToolTip(QCoreApplication.translate("MainWindow", u"Select jog increment", None))
#endif // QT_CONFIG(tooltip)
        self.axistoolbutton.setText(QCoreApplication.translate("MainWindow", u"Set X", None))
        self.axistoolbutton.setProperty("axis_letter", QCoreApplication.translate("MainWindow", u"X", None))
#if QT_CONFIG(statustip)
        self.action_zero_x.setStatusTip(QCoreApplication.translate("MainWindow", u"ZERO AXIS X", None))
#endif // QT_CONFIG(statustip)
        self.action_zero_x.setText(QCoreApplication.translate("MainWindow", u"Zero X", None))
        self.action_zero_x.setProperty("axis_letter", QCoreApplication.translate("MainWindow", u"X", None))
        self.action_zero_x.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.action_zero_x.setProperty("command_text_string", "")
        self.action_zero_x.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.action_zero_x.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.action_home_x.setText(QCoreApplication.translate("MainWindow", u"Home X", None))
        self.action_home_x.setProperty("axis_letter", QCoreApplication.translate("MainWindow", u"X", None))
        self.action_home_x.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.action_home_x.setProperty("command_text_string", "")
        self.action_home_x.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.action_home_x.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.axistoolbutton_2.setText(QCoreApplication.translate("MainWindow", u"Set Z", None))
        self.axistoolbutton_2.setProperty("axis_letter", QCoreApplication.translate("MainWindow", u"Z", None))
#if QT_CONFIG(statustip)
        self.action_zero_z.setStatusTip(QCoreApplication.translate("MainWindow", u"ZERO AXIS Z", None))
#endif // QT_CONFIG(statustip)
        self.action_zero_z.setText(QCoreApplication.translate("MainWindow", u"Zero Z", None))
        self.action_zero_z.setProperty("axis_letter", QCoreApplication.translate("MainWindow", u"Z", None))
        self.action_zero_z.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.action_zero_z.setProperty("command_text_string", "")
        self.action_zero_z.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.action_zero_z.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.action_home_z.setText(QCoreApplication.translate("MainWindow", u"Home Z", None))
        self.action_home_z.setProperty("axis_letter", QCoreApplication.translate("MainWindow", u"Z", None))
        self.action_home_z.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.action_home_z.setProperty("command_text_string", "")
        self.action_home_z.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.action_home_z.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.actionbutton_3.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.actionbutton_3.setProperty("true_state_string", QCoreApplication.translate("MainWindow", u"True", None))
        self.actionbutton_3.setProperty("false_state_string", QCoreApplication.translate("MainWindow", u"False", None))
        self.actionbutton_3.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"print\"true command\"", None))
        self.actionbutton_3.setProperty("false_python_cmd_string", QCoreApplication.translate("MainWindow", u"print\"false command\"", None))
        self.actionbutton_3.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.actionbutton_3.setProperty("command_text_string", "")
        self.actionbutton_3.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.actionbutton_3.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.action_mist.setText(QCoreApplication.translate("MainWindow", u"MIST\n"
"OFF", None))
        self.action_mist.setProperty("true_state_string", QCoreApplication.translate("MainWindow", u"MIST\n"
"ON", None))
        self.action_mist.setProperty("false_state_string", QCoreApplication.translate("MainWindow", u"MIST\n"
"OFF", None))
        self.action_mist.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"print\"true command\"", None))
        self.action_mist.setProperty("false_python_cmd_string", QCoreApplication.translate("MainWindow", u"print\"false command\"", None))
        self.action_mist.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.action_mist.setProperty("command_text_string", "")
        self.action_mist.setProperty("textTemplate", "")
        self.action_mist.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.statusimageswitcher.setProperty("image_list", QStringList()
            << QCoreApplication.translate("MainWindow", u":/images/images/stop_on.gif", None)
            << QCoreApplication.translate("MainWindow", u":/images/images/forward_on.gif", None)
            << QCoreApplication.translate("MainWindow", u":/images/images/reverse_on.gif", None))
        self.action_flood.setText(QCoreApplication.translate("MainWindow", u"FLOOD\n"
"OFF", None))
        self.action_flood.setProperty("true_state_string", QCoreApplication.translate("MainWindow", u"FLOOD\n"
"ON", None))
        self.action_flood.setProperty("false_state_string", QCoreApplication.translate("MainWindow", u"FLOOD\n"
"OFF", None))
        self.action_flood.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"print\"true command\"", None))
        self.action_flood.setProperty("false_python_cmd_string", QCoreApplication.translate("MainWindow", u"print\"false command\"", None))
        self.action_flood.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.action_flood.setProperty("command_text_string", "")
        self.action_flood.setProperty("textTemplate", "")
        self.action_flood.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.actionbutton_8.setText(QCoreApplication.translate("MainWindow", u"Override\n"
"Limits", None))
        self.actionbutton_8.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.actionbutton_8.setProperty("command_text_string", "")
        self.actionbutton_8.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.actionbutton_8.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.actionbutton_16.setText(QCoreApplication.translate("MainWindow", u"Load File", None))
        self.actionbutton_camview.setText(QCoreApplication.translate("MainWindow", u"Cam View", None))
        self.btn_clear_alarms.setText(QCoreApplication.translate("MainWindow", u"CLEAR\n"
"ALARMS", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">KEYBOARD MAPPING</span></p></body></html>", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Home - HOME ALL", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"ESC - Program Abort", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"F1 - ESTOP", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"F2 - POWER OFF", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"F3 - ORIGINOFFSET", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"F12 - Style Sheet Editor", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"F6 - TOOL OFFSET", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"F9 - CALCULATOR", None))
        self.systemtoolbutton.setText(QCoreApplication.translate("MainWindow", u"Coodinate\n"
"System", None))
        self.actionbutton_10.setText(QCoreApplication.translate("MainWindow", u"Machine\n"
" Log", None))
        self.actionbutton_10.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.actionbutton_10.setProperty("command_text_string", "")
        self.actionbutton_10.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.actionbutton_10.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
#if QT_CONFIG(statustip)
        self.btn_save_alarms.setStatusTip(QCoreApplication.translate("MainWindow", u"SAVE ALARMS TO FILE", None))
#endif // QT_CONFIG(statustip)
        self.btn_save_alarms.setText(QCoreApplication.translate("MainWindow", u"SAVE\n"
"TO FILE", None))
        self.actionbutton_4.setText(QCoreApplication.translate("MainWindow", u"MDI", None))
        self.actionbutton_4.setProperty("true_state_string", QCoreApplication.translate("MainWindow", u"True", None))
        self.actionbutton_4.setProperty("false_state_string", QCoreApplication.translate("MainWindow", u"False", None))
        self.actionbutton_4.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"print\"true command\"", None))
        self.actionbutton_4.setProperty("false_python_cmd_string", QCoreApplication.translate("MainWindow", u"print\"false command\"", None))
        self.actionbutton_4.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.actionbutton_4.setProperty("command_text_string", "")
        self.actionbutton_4.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.actionbutton_4.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.actionbutton_5.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.actionbutton_5.setProperty("true_state_string", QCoreApplication.translate("MainWindow", u"True", None))
        self.actionbutton_5.setProperty("false_state_string", QCoreApplication.translate("MainWindow", u"False", None))
        self.actionbutton_5.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"print\"true command\"", None))
        self.actionbutton_5.setProperty("false_python_cmd_string", QCoreApplication.translate("MainWindow", u"print\"false command\"", None))
        self.actionbutton_5.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.actionbutton_5.setProperty("command_text_string", "")
        self.actionbutton_5.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.actionbutton_5.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.actionbutton_6.setText(QCoreApplication.translate("MainWindow", u"Halmeter", None))
        self.actionbutton_6.setProperty("true_state_string", QCoreApplication.translate("MainWindow", u"True", None))
        self.actionbutton_6.setProperty("false_state_string", QCoreApplication.translate("MainWindow", u"False", None))
        self.actionbutton_6.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"print\"true command\"", None))
        self.actionbutton_6.setProperty("false_python_cmd_string", QCoreApplication.translate("MainWindow", u"print\"false command\"", None))
        self.actionbutton_6.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.actionbutton_6.setProperty("command_text_string", "")
        self.actionbutton_6.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.actionbutton_6.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
        self.actionbutton_7.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.actionbutton_7.setProperty("true_state_string", QCoreApplication.translate("MainWindow", u"True", None))
        self.actionbutton_7.setProperty("false_state_string", QCoreApplication.translate("MainWindow", u"False", None))
        self.actionbutton_7.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"print\"true command\"", None))
        self.actionbutton_7.setProperty("false_python_cmd_string", QCoreApplication.translate("MainWindow", u"print\"false command\"", None))
        self.actionbutton_7.setProperty("view_type_string", QCoreApplication.translate("MainWindow", u"P", None))
        self.actionbutton_7.setProperty("command_text_string", "")
        self.actionbutton_7.setProperty("textTemplate", QCoreApplication.translate("MainWindow", u"%1.3f in", None))
        self.actionbutton_7.setProperty("alt_textTemplate", QCoreApplication.translate("MainWindow", u"%1.2f mm", None))
#if QT_CONFIG(tooltip)
        self.btn_jog_l_slow.setToolTip(QCoreApplication.translate("MainWindow", u"Toggle linear jog speed range", None))
#endif // QT_CONFIG(tooltip)
        self.btn_jog_l_slow.setText(QCoreApplication.translate("MainWindow", u"FAST", None))
        self.btn_jog_l_slow.setProperty("true_state_string", QCoreApplication.translate("MainWindow", u"SLOW", None))
        self.btn_jog_l_slow.setProperty("false_state_string", QCoreApplication.translate("MainWindow", u"FAST", None))
        self.btn_jog_l_slow.setProperty("slider", QCoreApplication.translate("MainWindow", u"slider_jog_linear", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"UNITS", None))
        self.statelabel_metric.setProperty("true_textTemplate", QCoreApplication.translate("MainWindow", u"MM", None))
        self.statelabel_metric.setProperty("false_textTemplate", QCoreApplication.translate("MainWindow", u"IN", None))
        self.pushbutton_metric.setProperty("true_state_string", QCoreApplication.translate("MainWindow", u"G21", None))
        self.pushbutton_metric.setProperty("false_state_string", QCoreApplication.translate("MainWindow", u"G20", None))
        self.mdi_tab.setTabText(self.mdi_tab.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"MDI", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Macro</span></p></body></html>", None))
        self.mdi_tab.setTabText(self.mdi_tab.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Macro", None))
        self.btn_start_macro.setText(QCoreApplication.translate("MainWindow", u"START MACRO", None))
        self.mdi_tab.setTabText(self.mdi_tab.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"MDITouchy", None))
        self.gcode_parameters.setText(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.mdi_tab.setTabText(self.mdi_tab.indexOf(self.tab_gcode), QCoreApplication.translate("MainWindow", u"Gcode List", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Program Manager</span></p></body></html>", None))
        self.btn_file_prev.setText(QCoreApplication.translate("MainWindow", u"PREV", None))
        self.btn_file_prev.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"INSTANCE.filemanager.up()", None))
        self.btn_file_prev.setProperty("false_python_cmd_string", "")
        self.btn_gcode_edit.setText(QCoreApplication.translate("MainWindow", u"EDIT", None))
        self.btn_gcode_edit.setProperty("true_python_cmd_string", "")
        self.btn_gcode_edit.setProperty("false_python_cmd_string", "")
        self.btn_file_next.setText(QCoreApplication.translate("MainWindow", u"NEXT", None))
        self.btn_file_next.setProperty("true_python_cmd_string", QCoreApplication.translate("MainWindow", u"INSTANCE.filemanager.down()", None))
        self.btn_file_next.setProperty("false_python_cmd_string", "")
        self.btn_file_load.setText(QCoreApplication.translate("MainWindow", u"LOAD", None))
        self.btn_file_load.setProperty("true_python_cmd_string", "")
        self.btn_file_load.setProperty("false_python_cmd_string", "")
        self.homeIcon.setProperty("image_list", QStringList()
            << QCoreApplication.translate("MainWindow", u":/images/images/ref_z_not.png", None)
            << QCoreApplication.translate("MainWindow", u":/images/images/clear.png", None))
        self.homeIcon.setProperty("axis_letter", QCoreApplication.translate("MainWindow", u"Z", None))
        self.homeIcon_x.setProperty("image_list", QStringList()
            << QCoreApplication.translate("MainWindow", u":/images/images/ref_x_not.png", None)
            << QCoreApplication.translate("MainWindow", u":/images/images/clear.png", None))
        self.HardLimitIcon.setProperty("image_list", QStringList()
            << QCoreApplication.translate("MainWindow", u"/home/chris/emc-dev/share/qtvcp/images/clear.png", None)
            << QCoreApplication.translate("MainWindow", u"/home/chris/emc-dev/share/qtvcp/images/limit_error.png", None))
        self.hardLimit2Icon.setProperty("image_list", QStringList()
            << QCoreApplication.translate("MainWindow", u"/home/chris/emc-dev/share/qtvcp/images/clear.png", None)
            << QCoreApplication.translate("MainWindow", u"None", None)
            << QCoreApplication.translate("MainWindow", u"/home/chris/emc-dev/share/qtvcp/images/applet-critical.png", None))
        self.label_2.setText("")
        self.label.setText("")
        self.label_3.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuMachine.setTitle(QCoreApplication.translate("MainWindow", u"Machine", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuGridSize.setTitle(QCoreApplication.translate("MainWindow", u"Grid Size", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuSystem.setTitle(QCoreApplication.translate("MainWindow", u"System", None))
    # retranslateUi

