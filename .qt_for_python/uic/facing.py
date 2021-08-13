# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'facing.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(610, 370)
        self.horizontalLayout_5 = QHBoxLayout(Form)
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_facing = QFrame(Form)
        self.frame_facing.setObjectName(u"frame_facing")
        self.horizontalLayout = QHBoxLayout(self.frame_facing)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, -1, 2, -1)
        self.lbl_header = QLabel(self.frame_facing)
        self.lbl_header.setObjectName(u"lbl_header")
        self.lbl_header.setMaximumSize(QSize(16777215, 30))
        self.lbl_header.setStyleSheet(u"font: 81 11pt \"Lato Heavy\";")
        self.lbl_header.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_header)

        self.lbl_units_info = QLabel(self.frame_facing)
        self.lbl_units_info.setObjectName(u"lbl_units_info")
        self.lbl_units_info.setMaximumSize(QSize(16777215, 30))
        self.lbl_units_info.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_units_info.setMargin(4)

        self.verticalLayout.addWidget(self.lbl_units_info)

        self.widget_xy_header = QWidget(self.frame_facing)
        self.widget_xy_header.setObjectName(u"widget_xy_header")
        self.widget_xy_header.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_10 = QHBoxLayout(self.widget_xy_header)
        self.horizontalLayout_10.setSpacing(4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.lbl_blank = QLabel(self.widget_xy_header)
        self.lbl_blank.setObjectName(u"lbl_blank")
        self.lbl_blank.setMinimumSize(QSize(60, 0))
        self.lbl_blank.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_10.addWidget(self.lbl_blank)

        self.lbl_x = QLabel(self.widget_xy_header)
        self.lbl_x.setObjectName(u"lbl_x")
        self.lbl_x.setMinimumSize(QSize(70, 0))
        self.lbl_x.setMaximumSize(QSize(70, 16777215))
        self.lbl_x.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lbl_x)

        self.lbl_y = QLabel(self.widget_xy_header)
        self.lbl_y.setObjectName(u"lbl_y")
        self.lbl_y.setMinimumSize(QSize(70, 0))
        self.lbl_y.setMaximumSize(QSize(70, 16777215))
        self.lbl_y.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lbl_y)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.widget_xy_header)

        self.widget_size = QWidget(self.frame_facing)
        self.widget_size.setObjectName(u"widget_size")
        self.widget_size.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_size)
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lbl_size = QLabel(self.widget_size)
        self.lbl_size.setObjectName(u"lbl_size")
        self.lbl_size.setMinimumSize(QSize(60, 0))
        self.lbl_size.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_4.addWidget(self.lbl_size)

        self.lineEdit_size_x = QLineEdit(self.widget_size)
        self.lineEdit_size_x.setObjectName(u"lineEdit_size_x")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_size_x.sizePolicy().hasHeightForWidth())
        self.lineEdit_size_x.setSizePolicy(sizePolicy)
        self.lineEdit_size_x.setMinimumSize(QSize(70, 0))
        self.lineEdit_size_x.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_size_x.setMaxLength(8)
        self.lineEdit_size_x.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lineEdit_size_x)

        self.lineEdit_size_y = QLineEdit(self.widget_size)
        self.lineEdit_size_y.setObjectName(u"lineEdit_size_y")
        sizePolicy.setHeightForWidth(self.lineEdit_size_y.sizePolicy().hasHeightForWidth())
        self.lineEdit_size_y.setSizePolicy(sizePolicy)
        self.lineEdit_size_y.setMinimumSize(QSize(70, 0))
        self.lineEdit_size_y.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_size_y.setMaxLength(8)
        self.lineEdit_size_y.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lineEdit_size_y)

        self.lbl_size_unit = QLabel(self.widget_size)
        self.lbl_size_unit.setObjectName(u"lbl_size_unit")
        self.lbl_size_unit.setMinimumSize(QSize(0, 0))
        self.lbl_size_unit.setMaximumSize(QSize(16777215, 16777215))
        self.lbl_size_unit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lbl_size_unit)

        self.lbl_size_ok = QLabel(self.widget_size)
        self.lbl_size_ok.setObjectName(u"lbl_size_ok")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_size_ok.sizePolicy().hasHeightForWidth())
        self.lbl_size_ok.setSizePolicy(sizePolicy1)
        self.lbl_size_ok.setMinimumSize(QSize(24, 24))
        self.lbl_size_ok.setMaximumSize(QSize(24, 24))
        self.lbl_size_ok.setPixmap(QPixmap(u"images/unchecked.png"))
        self.lbl_size_ok.setScaledContents(True)
        self.lbl_size_ok.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lbl_size_ok)


        self.verticalLayout.addWidget(self.widget_size)

        self.widget_spindle = QWidget(self.frame_facing)
        self.widget_spindle.setObjectName(u"widget_spindle")
        self.widget_spindle.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_spindle)
        self.horizontalLayout_6.setSpacing(4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lbl_spindle_rpm = QLabel(self.widget_spindle)
        self.lbl_spindle_rpm.setObjectName(u"lbl_spindle_rpm")
        self.lbl_spindle_rpm.setMinimumSize(QSize(80, 0))
        self.lbl_spindle_rpm.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_6.addWidget(self.lbl_spindle_rpm)

        self.lineEdit_spindle = QLineEdit(self.widget_spindle)
        self.lineEdit_spindle.setObjectName(u"lineEdit_spindle")
        sizePolicy.setHeightForWidth(self.lineEdit_spindle.sizePolicy().hasHeightForWidth())
        self.lineEdit_spindle.setSizePolicy(sizePolicy)
        self.lineEdit_spindle.setMinimumSize(QSize(80, 0))
        self.lineEdit_spindle.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_spindle.setMaxLength(5)
        self.lineEdit_spindle.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.lineEdit_spindle)

        self.lbl_rpm = QLabel(self.widget_spindle)
        self.lbl_rpm.setObjectName(u"lbl_rpm")

        self.horizontalLayout_6.addWidget(self.lbl_rpm)

        self.lbl_spindle_ok = QLabel(self.widget_spindle)
        self.lbl_spindle_ok.setObjectName(u"lbl_spindle_ok")
        sizePolicy1.setHeightForWidth(self.lbl_spindle_ok.sizePolicy().hasHeightForWidth())
        self.lbl_spindle_ok.setSizePolicy(sizePolicy1)
        self.lbl_spindle_ok.setMinimumSize(QSize(24, 24))
        self.lbl_spindle_ok.setMaximumSize(QSize(24, 24))
        self.lbl_spindle_ok.setPixmap(QPixmap(u"images/unchecked.png"))
        self.lbl_spindle_ok.setScaledContents(True)
        self.lbl_spindle_ok.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.lbl_spindle_ok)


        self.verticalLayout.addWidget(self.widget_spindle)

        self.widget_feedrate = QWidget(self.frame_facing)
        self.widget_feedrate.setObjectName(u"widget_feedrate")
        self.widget_feedrate.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_8 = QHBoxLayout(self.widget_feedrate)
        self.horizontalLayout_8.setSpacing(4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lbl_feedrate = QLabel(self.widget_feedrate)
        self.lbl_feedrate.setObjectName(u"lbl_feedrate")
        self.lbl_feedrate.setMinimumSize(QSize(80, 0))
        self.lbl_feedrate.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_8.addWidget(self.lbl_feedrate)

        self.lineEdit_feedrate = QLineEdit(self.widget_feedrate)
        self.lineEdit_feedrate.setObjectName(u"lineEdit_feedrate")
        sizePolicy.setHeightForWidth(self.lineEdit_feedrate.sizePolicy().hasHeightForWidth())
        self.lineEdit_feedrate.setSizePolicy(sizePolicy)
        self.lineEdit_feedrate.setMinimumSize(QSize(80, 0))
        self.lineEdit_feedrate.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_feedrate.setMaxLength(6)
        self.lineEdit_feedrate.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.lineEdit_feedrate)

        self.lbl_feed_unit = QLabel(self.widget_feedrate)
        self.lbl_feed_unit.setObjectName(u"lbl_feed_unit")

        self.horizontalLayout_8.addWidget(self.lbl_feed_unit)

        self.lbl_feed_ok = QLabel(self.widget_feedrate)
        self.lbl_feed_ok.setObjectName(u"lbl_feed_ok")
        sizePolicy1.setHeightForWidth(self.lbl_feed_ok.sizePolicy().hasHeightForWidth())
        self.lbl_feed_ok.setSizePolicy(sizePolicy1)
        self.lbl_feed_ok.setMinimumSize(QSize(24, 24))
        self.lbl_feed_ok.setMaximumSize(QSize(24, 24))
        self.lbl_feed_ok.setPixmap(QPixmap(u"images/unchecked.png"))
        self.lbl_feed_ok.setScaledContents(True)
        self.lbl_feed_ok.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.lbl_feed_ok)


        self.verticalLayout.addWidget(self.widget_feedrate)

        self.widget_tool = QWidget(self.frame_facing)
        self.widget_tool.setObjectName(u"widget_tool")
        self.widget_tool.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_7 = QHBoxLayout(self.widget_tool)
        self.horizontalLayout_7.setSpacing(4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lbl_tool = QLabel(self.widget_tool)
        self.lbl_tool.setObjectName(u"lbl_tool")
        self.lbl_tool.setMinimumSize(QSize(80, 0))
        self.lbl_tool.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_7.addWidget(self.lbl_tool)

        self.lineEdit_tool = QLineEdit(self.widget_tool)
        self.lineEdit_tool.setObjectName(u"lineEdit_tool")
        sizePolicy.setHeightForWidth(self.lineEdit_tool.sizePolicy().hasHeightForWidth())
        self.lineEdit_tool.setSizePolicy(sizePolicy)
        self.lineEdit_tool.setMinimumSize(QSize(80, 0))
        self.lineEdit_tool.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_tool.setMaxLength(6)
        self.lineEdit_tool.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.lineEdit_tool)

        self.lbl_tool_unit = QLabel(self.widget_tool)
        self.lbl_tool_unit.setObjectName(u"lbl_tool_unit")

        self.horizontalLayout_7.addWidget(self.lbl_tool_unit)

        self.lbl_tool_ok = QLabel(self.widget_tool)
        self.lbl_tool_ok.setObjectName(u"lbl_tool_ok")
        sizePolicy1.setHeightForWidth(self.lbl_tool_ok.sizePolicy().hasHeightForWidth())
        self.lbl_tool_ok.setSizePolicy(sizePolicy1)
        self.lbl_tool_ok.setMinimumSize(QSize(24, 24))
        self.lbl_tool_ok.setMaximumSize(QSize(24, 24))
        self.lbl_tool_ok.setPixmap(QPixmap(u"images/unchecked.png"))
        self.lbl_tool_ok.setScaledContents(True)
        self.lbl_tool_ok.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.lbl_tool_ok)


        self.verticalLayout.addWidget(self.widget_tool)

        self.widget_stepover = QWidget(self.frame_facing)
        self.widget_stepover.setObjectName(u"widget_stepover")
        self.widget_stepover.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_stepover)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.lbl_stepover = QLabel(self.widget_stepover)
        self.lbl_stepover.setObjectName(u"lbl_stepover")
        self.lbl_stepover.setMinimumSize(QSize(80, 0))
        self.lbl_stepover.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_2.addWidget(self.lbl_stepover)

        self.lineEdit_stepover = QLineEdit(self.widget_stepover)
        self.lineEdit_stepover.setObjectName(u"lineEdit_stepover")
        sizePolicy.setHeightForWidth(self.lineEdit_stepover.sizePolicy().hasHeightForWidth())
        self.lineEdit_stepover.setSizePolicy(sizePolicy)
        self.lineEdit_stepover.setMinimumSize(QSize(80, 0))
        self.lineEdit_stepover.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_stepover.setMaxLength(4)
        self.lineEdit_stepover.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_stepover)

        self.lbl_stepover_unit = QLabel(self.widget_stepover)
        self.lbl_stepover_unit.setObjectName(u"lbl_stepover_unit")

        self.horizontalLayout_2.addWidget(self.lbl_stepover_unit)

        self.lbl_stepover_ok = QLabel(self.widget_stepover)
        self.lbl_stepover_ok.setObjectName(u"lbl_stepover_ok")
        sizePolicy1.setHeightForWidth(self.lbl_stepover_ok.sizePolicy().hasHeightForWidth())
        self.lbl_stepover_ok.setSizePolicy(sizePolicy1)
        self.lbl_stepover_ok.setMinimumSize(QSize(24, 24))
        self.lbl_stepover_ok.setMaximumSize(QSize(24, 24))
        self.lbl_stepover_ok.setPixmap(QPixmap(u"images/unchecked.png"))
        self.lbl_stepover_ok.setScaledContents(True)
        self.lbl_stepover_ok.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lbl_stepover_ok)


        self.verticalLayout.addWidget(self.widget_stepover)

        self.widget_units = QWidget(self.frame_facing)
        self.widget_units.setObjectName(u"widget_units")
        self.widget_units.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_9 = QHBoxLayout(self.widget_units)
        self.horizontalLayout_9.setSpacing(4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.lbl_units = QLabel(self.widget_units)
        self.lbl_units.setObjectName(u"lbl_units")
        self.lbl_units.setMinimumSize(QSize(80, 0))
        self.lbl_units.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_9.addWidget(self.lbl_units)

        self.rbtn_inch = QPushButton(self.widget_units)
        self.rbtn_inch.setObjectName(u"rbtn_inch")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.rbtn_inch.sizePolicy().hasHeightForWidth())
        self.rbtn_inch.setSizePolicy(sizePolicy2)
        self.rbtn_inch.setMinimumSize(QSize(60, 0))
        self.rbtn_inch.setMaximumSize(QSize(60, 16777215))
        self.rbtn_inch.setCheckable(True)
        self.rbtn_inch.setAutoExclusive(True)

        self.horizontalLayout_9.addWidget(self.rbtn_inch)

        self.rbtn_mm = QPushButton(self.widget_units)
        self.rbtn_mm.setObjectName(u"rbtn_mm")
        sizePolicy2.setHeightForWidth(self.rbtn_mm.sizePolicy().hasHeightForWidth())
        self.rbtn_mm.setSizePolicy(sizePolicy2)
        self.rbtn_mm.setMinimumSize(QSize(60, 0))
        self.rbtn_mm.setMaximumSize(QSize(60, 16777215))
        self.rbtn_mm.setCheckable(True)
        self.rbtn_mm.setChecked(True)
        self.rbtn_mm.setAutoExclusive(True)

        self.horizontalLayout_9.addWidget(self.rbtn_mm)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.widget_units)

        self.widget_raster = QWidget(self.frame_facing)
        self.widget_raster.setObjectName(u"widget_raster")
        self.widget_raster.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_12 = QHBoxLayout(self.widget_raster)
        self.horizontalLayout_12.setSpacing(4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.lbl_raster = QLabel(self.widget_raster)
        self.lbl_raster.setObjectName(u"lbl_raster")
        self.lbl_raster.setMinimumSize(QSize(80, 0))
        self.lbl_raster.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_12.addWidget(self.lbl_raster)

        self.rbtn_raster_0 = QPushButton(self.widget_raster)
        self.rbtn_raster_0.setObjectName(u"rbtn_raster_0")
        sizePolicy2.setHeightForWidth(self.rbtn_raster_0.sizePolicy().hasHeightForWidth())
        self.rbtn_raster_0.setSizePolicy(sizePolicy2)
        self.rbtn_raster_0.setMinimumSize(QSize(50, 0))
        self.rbtn_raster_0.setMaximumSize(QSize(50, 16777215))
        self.rbtn_raster_0.setCheckable(True)
        self.rbtn_raster_0.setChecked(True)
        self.rbtn_raster_0.setAutoExclusive(True)

        self.horizontalLayout_12.addWidget(self.rbtn_raster_0)

        self.rbtn_raster_45 = QPushButton(self.widget_raster)
        self.rbtn_raster_45.setObjectName(u"rbtn_raster_45")
        sizePolicy2.setHeightForWidth(self.rbtn_raster_45.sizePolicy().hasHeightForWidth())
        self.rbtn_raster_45.setSizePolicy(sizePolicy2)
        self.rbtn_raster_45.setMinimumSize(QSize(50, 0))
        self.rbtn_raster_45.setMaximumSize(QSize(50, 16777215))
        self.rbtn_raster_45.setCheckable(True)
        self.rbtn_raster_45.setAutoExclusive(True)

        self.horizontalLayout_12.addWidget(self.rbtn_raster_45)

        self.rbtn_raster_90 = QPushButton(self.widget_raster)
        self.rbtn_raster_90.setObjectName(u"rbtn_raster_90")
        sizePolicy2.setHeightForWidth(self.rbtn_raster_90.sizePolicy().hasHeightForWidth())
        self.rbtn_raster_90.setSizePolicy(sizePolicy2)
        self.rbtn_raster_90.setMinimumSize(QSize(50, 0))
        self.rbtn_raster_90.setMaximumSize(QSize(50, 16777215))
        self.rbtn_raster_90.setCheckable(True)
        self.rbtn_raster_90.setAutoExclusive(True)

        self.horizontalLayout_12.addWidget(self.rbtn_raster_90)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.widget_raster)

        self.widget_comment = QWidget(self.frame_facing)
        self.widget_comment.setObjectName(u"widget_comment")
        self.widget_comment.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_11 = QHBoxLayout(self.widget_comment)
        self.horizontalLayout_11.setSpacing(4)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.lbl_comment = QLabel(self.widget_comment)
        self.lbl_comment.setObjectName(u"lbl_comment")
        self.lbl_comment.setMinimumSize(QSize(80, 0))
        self.lbl_comment.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_11.addWidget(self.lbl_comment)

        self.lineEdit_comment = QLineEdit(self.widget_comment)
        self.lineEdit_comment.setObjectName(u"lineEdit_comment")
        sizePolicy.setHeightForWidth(self.lineEdit_comment.sizePolicy().hasHeightForWidth())
        self.lineEdit_comment.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.lineEdit_comment)


        self.verticalLayout.addWidget(self.widget_comment)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, -1, 2, -1)
        self.lbl_image = QLabel(self.frame_facing)
        self.lbl_image.setObjectName(u"lbl_image")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lbl_image.sizePolicy().hasHeightForWidth())
        self.lbl_image.setSizePolicy(sizePolicy3)
        self.lbl_image.setPixmap(QPixmap(u"images/raster_0.png"))
        self.lbl_image.setScaledContents(True)
        self.lbl_image.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_image)

        self.widget_macro = QWidget(self.frame_facing)
        self.widget_macro.setObjectName(u"widget_macro")
        self.widget_macro.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_13 = QHBoxLayout(self.widget_macro)
        self.horizontalLayout_13.setSpacing(4)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.btn_validate = QPushButton(self.widget_macro)
        self.btn_validate.setObjectName(u"btn_validate")
        sizePolicy1.setHeightForWidth(self.btn_validate.sizePolicy().hasHeightForWidth())
        self.btn_validate.setSizePolicy(sizePolicy1)
        self.btn_validate.setMinimumSize(QSize(80, 50))
        self.btn_validate.setMaximumSize(QSize(80, 50))

        self.horizontalLayout_13.addWidget(self.btn_validate)

        self.btn_create = QPushButton(self.widget_macro)
        self.btn_create.setObjectName(u"btn_create")
        sizePolicy1.setHeightForWidth(self.btn_create.sizePolicy().hasHeightForWidth())
        self.btn_create.setSizePolicy(sizePolicy1)
        self.btn_create.setMinimumSize(QSize(80, 50))
        self.btn_create.setMaximumSize(QSize(80, 50))

        self.horizontalLayout_13.addWidget(self.btn_create)

        self.btn_send = QPushButton(self.widget_macro)
        self.btn_send.setObjectName(u"btn_send")
        sizePolicy1.setHeightForWidth(self.btn_send.sizePolicy().hasHeightForWidth())
        self.btn_send.setSizePolicy(sizePolicy1)
        self.btn_send.setMinimumSize(QSize(80, 50))
        self.btn_send.setMaximumSize(QSize(80, 50))

        self.horizontalLayout_13.addWidget(self.btn_send)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)

        self.btn_help = QPushButton(self.widget_macro)
        self.btn_help.setObjectName(u"btn_help")
        sizePolicy1.setHeightForWidth(self.btn_help.sizePolicy().hasHeightForWidth())
        self.btn_help.setSizePolicy(sizePolicy1)
        self.btn_help.setMinimumSize(QSize(80, 50))
        self.btn_help.setMaximumSize(QSize(80, 50))
        self.btn_help.setCheckable(False)

        self.horizontalLayout_13.addWidget(self.btn_help, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.widget_macro, 0, Qt.AlignBottom)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.horizontalLayout_5.addWidget(self.frame_facing)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_header.setText(QCoreApplication.translate("Form", u"RECTANGULAR FACING PROGRAM", None))
        self.lbl_blank.setText("")
        self.lbl_x.setText(QCoreApplication.translate("Form", u"X", None))
        self.lbl_y.setText(QCoreApplication.translate("Form", u"Y", None))
#if QT_CONFIG(tooltip)
        self.lbl_size.setToolTip(QCoreApplication.translate("Form", u"Start point of rectangle in relative workspace", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_size.setText(QCoreApplication.translate("Form", u"SIZE", None))
        self.lbl_size_unit.setText(QCoreApplication.translate("Form", u"MM", None))
        self.lbl_size_ok.setText("")
        self.lbl_spindle_rpm.setText(QCoreApplication.translate("Form", u"SPINDLE", None))
        self.lbl_rpm.setText(QCoreApplication.translate("Form", u"RPM", None))
        self.lbl_spindle_ok.setText("")
        self.lbl_feedrate.setText(QCoreApplication.translate("Form", u"FEED RATE", None))
        self.lbl_feed_unit.setText(QCoreApplication.translate("Form", u"MM/MIN", None))
        self.lbl_feed_ok.setText("")
#if QT_CONFIG(tooltip)
        self.lbl_tool.setToolTip(QCoreApplication.translate("Form", u"Tool to use for facing", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_tool.setText(QCoreApplication.translate("Form", u"TOOL DIA", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_tool.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lbl_tool_unit.setText(QCoreApplication.translate("Form", u"MM", None))
        self.lbl_tool_ok.setText("")
        self.lbl_stepover.setText(QCoreApplication.translate("Form", u"STEPOVER", None))
        self.lbl_stepover_unit.setText(QCoreApplication.translate("Form", u"MM", None))
        self.lbl_stepover_ok.setText("")
#if QT_CONFIG(tooltip)
        self.lbl_units.setToolTip(QCoreApplication.translate("Form", u"Select machine units", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_units.setText(QCoreApplication.translate("Form", u"UNITS", None))
        self.rbtn_inch.setText(QCoreApplication.translate("Form", u"INCH", None))
        self.rbtn_mm.setText(QCoreApplication.translate("Form", u"MM", None))
#if QT_CONFIG(tooltip)
        self.lbl_raster.setToolTip(QCoreApplication.translate("Form", u"Select raster angle", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_raster.setText(QCoreApplication.translate("Form", u"ANGLE", None))
        self.rbtn_raster_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.rbtn_raster_45.setText(QCoreApplication.translate("Form", u"45", None))
        self.rbtn_raster_90.setText(QCoreApplication.translate("Form", u"90", None))
#if QT_CONFIG(tooltip)
        self.lbl_comment.setToolTip(QCoreApplication.translate("Form", u"Comment for gcode file", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_comment.setText(QCoreApplication.translate("Form", u"COMMENT", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_comment.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lbl_image.setText("")
#if QT_CONFIG(tooltip)
        self.btn_validate.setToolTip(QCoreApplication.translate("Form", u"Check if all inputs are valid", None))
#endif // QT_CONFIG(tooltip)
        self.btn_validate.setText(QCoreApplication.translate("Form", u"VALIDATE\n"
"INPUTS", None))
#if QT_CONFIG(tooltip)
        self.btn_create.setToolTip(QCoreApplication.translate("Form", u"Create macro and save to file", None))
#endif // QT_CONFIG(tooltip)
        self.btn_create.setText(QCoreApplication.translate("Form", u"CREATE\n"
"PROGRAM", None))
#if QT_CONFIG(tooltip)
        self.btn_send.setToolTip(QCoreApplication.translate("Form", u"Create temporary macro and load in linuxcnc", None))
#endif // QT_CONFIG(tooltip)
        self.btn_send.setText(QCoreApplication.translate("Form", u"SEND AS\n"
"MACRO", None))
#if QT_CONFIG(tooltip)
        self.btn_help.setToolTip(QCoreApplication.translate("Form", u"Opens a help dialog box", None))
#endif // QT_CONFIG(tooltip)
        self.btn_help.setText(QCoreApplication.translate("Form", u"HELP", None))
    # retranslateUi

