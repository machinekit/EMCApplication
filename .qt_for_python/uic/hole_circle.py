# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hole_circle.ui'
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
        Form.resize(624, 353)
        self.horizontalLayout_5 = QHBoxLayout(Form)
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_hole_circle = QFrame(Form)
        self.frame_hole_circle.setObjectName(u"frame_hole_circle")
        self.frame_hole_circle.setMaximumSize(QSize(16777215, 16777215))
        self.frame_hole_circle.setFrameShape(QFrame.NoFrame)
        self.frame_hole_circle.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame_hole_circle)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.lbl_header = QLabel(self.frame_hole_circle)
        self.lbl_header.setObjectName(u"lbl_header")
        self.lbl_header.setMaximumSize(QSize(16777215, 30))
        self.lbl_header.setStyleSheet(u"font: 81 11pt \"Lato Heavy\";")
        self.lbl_header.setAlignment(Qt.AlignCenter)
        self.lbl_header.setMargin(4)

        self.verticalLayout.addWidget(self.lbl_header)

        self.lbl_units_info = QLabel(self.frame_hole_circle)
        self.lbl_units_info.setObjectName(u"lbl_units_info")
        self.lbl_units_info.setMaximumSize(QSize(16777215, 30))
        self.lbl_units_info.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_units_info.setMargin(4)

        self.verticalLayout.addWidget(self.lbl_units_info)

        self.widget_spindle = QWidget(self.frame_hole_circle)
        self.widget_spindle.setObjectName(u"widget_spindle")
        self.widget_spindle.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_12 = QHBoxLayout(self.widget_spindle)
        self.horizontalLayout_12.setSpacing(4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.lbl_spindle = QLabel(self.widget_spindle)
        self.lbl_spindle.setObjectName(u"lbl_spindle")
        self.lbl_spindle.setMaximumSize(QSize(160, 16777215))

        self.horizontalLayout_12.addWidget(self.lbl_spindle)

        self.lineEdit_spindle = QLineEdit(self.widget_spindle)
        self.lineEdit_spindle.setObjectName(u"lineEdit_spindle")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_spindle.sizePolicy().hasHeightForWidth())
        self.lineEdit_spindle.setSizePolicy(sizePolicy)
        self.lineEdit_spindle.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_spindle.setMaxLength(8)
        self.lineEdit_spindle.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.lineEdit_spindle)

        self.lbl_spindle_ok = QLabel(self.widget_spindle)
        self.lbl_spindle_ok.setObjectName(u"lbl_spindle_ok")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_spindle_ok.sizePolicy().hasHeightForWidth())
        self.lbl_spindle_ok.setSizePolicy(sizePolicy1)
        self.lbl_spindle_ok.setMinimumSize(QSize(24, 24))
        self.lbl_spindle_ok.setMaximumSize(QSize(24, 24))
        self.lbl_spindle_ok.setPixmap(QPixmap(u"images/unchecked.png"))
        self.lbl_spindle_ok.setScaledContents(True)
        self.lbl_spindle_ok.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.lbl_spindle_ok)


        self.verticalLayout.addWidget(self.widget_spindle)

        self.widget_num_holes = QWidget(self.frame_hole_circle)
        self.widget_num_holes.setObjectName(u"widget_num_holes")
        self.widget_num_holes.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_num_holes)
        self.horizontalLayout_6.setSpacing(4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lbl_num_holes = QLabel(self.widget_num_holes)
        self.lbl_num_holes.setObjectName(u"lbl_num_holes")
        self.lbl_num_holes.setMinimumSize(QSize(160, 0))
        self.lbl_num_holes.setMaximumSize(QSize(160, 16777215))

        self.horizontalLayout_6.addWidget(self.lbl_num_holes)

        self.lineEdit_num_holes = QLineEdit(self.widget_num_holes)
        self.lineEdit_num_holes.setObjectName(u"lineEdit_num_holes")
        sizePolicy.setHeightForWidth(self.lineEdit_num_holes.sizePolicy().hasHeightForWidth())
        self.lineEdit_num_holes.setSizePolicy(sizePolicy)
        self.lineEdit_num_holes.setMinimumSize(QSize(80, 0))
        self.lineEdit_num_holes.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_num_holes.setMaxLength(5)
        self.lineEdit_num_holes.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.lineEdit_num_holes)

        self.lbl_num_holes_ok = QLabel(self.widget_num_holes)
        self.lbl_num_holes_ok.setObjectName(u"lbl_num_holes_ok")
        sizePolicy1.setHeightForWidth(self.lbl_num_holes_ok.sizePolicy().hasHeightForWidth())
        self.lbl_num_holes_ok.setSizePolicy(sizePolicy1)
        self.lbl_num_holes_ok.setMinimumSize(QSize(24, 24))
        self.lbl_num_holes_ok.setMaximumSize(QSize(24, 24))
        self.lbl_num_holes_ok.setPixmap(QPixmap(u"images/unchecked.png"))
        self.lbl_num_holes_ok.setScaledContents(True)
        self.lbl_num_holes_ok.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.lbl_num_holes_ok)


        self.verticalLayout.addWidget(self.widget_num_holes)

        self.widget_radius = QWidget(self.frame_hole_circle)
        self.widget_radius.setObjectName(u"widget_radius")
        self.widget_radius.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_8 = QHBoxLayout(self.widget_radius)
        self.horizontalLayout_8.setSpacing(4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lbl_radius = QLabel(self.widget_radius)
        self.lbl_radius.setObjectName(u"lbl_radius")
        self.lbl_radius.setMinimumSize(QSize(160, 0))
        self.lbl_radius.setMaximumSize(QSize(160, 16777215))

        self.horizontalLayout_8.addWidget(self.lbl_radius)

        self.lineEdit_radius = QLineEdit(self.widget_radius)
        self.lineEdit_radius.setObjectName(u"lineEdit_radius")
        sizePolicy.setHeightForWidth(self.lineEdit_radius.sizePolicy().hasHeightForWidth())
        self.lineEdit_radius.setSizePolicy(sizePolicy)
        self.lineEdit_radius.setMinimumSize(QSize(80, 0))
        self.lineEdit_radius.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_radius.setMaxLength(6)
        self.lineEdit_radius.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.lineEdit_radius)

        self.lbl_radius_ok = QLabel(self.widget_radius)
        self.lbl_radius_ok.setObjectName(u"lbl_radius_ok")
        sizePolicy1.setHeightForWidth(self.lbl_radius_ok.sizePolicy().hasHeightForWidth())
        self.lbl_radius_ok.setSizePolicy(sizePolicy1)
        self.lbl_radius_ok.setMinimumSize(QSize(24, 24))
        self.lbl_radius_ok.setMaximumSize(QSize(24, 24))
        self.lbl_radius_ok.setPixmap(QPixmap(u"images/unchecked.png"))
        self.lbl_radius_ok.setScaledContents(True)
        self.lbl_radius_ok.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.lbl_radius_ok)


        self.verticalLayout.addWidget(self.widget_radius)

        self.widget_first = QWidget(self.frame_hole_circle)
        self.widget_first.setObjectName(u"widget_first")
        self.widget_first.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_7 = QHBoxLayout(self.widget_first)
        self.horizontalLayout_7.setSpacing(4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lbl_first = QLabel(self.widget_first)
        self.lbl_first.setObjectName(u"lbl_first")
        self.lbl_first.setMinimumSize(QSize(160, 0))
        self.lbl_first.setMaximumSize(QSize(160, 16777215))

        self.horizontalLayout_7.addWidget(self.lbl_first)

        self.lineEdit_first = QLineEdit(self.widget_first)
        self.lineEdit_first.setObjectName(u"lineEdit_first")
        sizePolicy.setHeightForWidth(self.lineEdit_first.sizePolicy().hasHeightForWidth())
        self.lineEdit_first.setSizePolicy(sizePolicy)
        self.lineEdit_first.setMinimumSize(QSize(80, 0))
        self.lineEdit_first.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_first.setMaxLength(6)
        self.lineEdit_first.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.lineEdit_first)

        self.lbl_first_ok = QLabel(self.widget_first)
        self.lbl_first_ok.setObjectName(u"lbl_first_ok")
        sizePolicy1.setHeightForWidth(self.lbl_first_ok.sizePolicy().hasHeightForWidth())
        self.lbl_first_ok.setSizePolicy(sizePolicy1)
        self.lbl_first_ok.setMinimumSize(QSize(24, 24))
        self.lbl_first_ok.setMaximumSize(QSize(24, 24))
        self.lbl_first_ok.setPixmap(QPixmap(u"images/unchecked.png"))
        self.lbl_first_ok.setScaledContents(True)
        self.lbl_first_ok.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.lbl_first_ok)


        self.verticalLayout.addWidget(self.widget_first)

        self.widget_safe_z = QWidget(self.frame_hole_circle)
        self.widget_safe_z.setObjectName(u"widget_safe_z")
        self.widget_safe_z.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_safe_z)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbl_safe_z = QLabel(self.widget_safe_z)
        self.lbl_safe_z.setObjectName(u"lbl_safe_z")
        self.lbl_safe_z.setMinimumSize(QSize(160, 0))
        self.lbl_safe_z.setMaximumSize(QSize(160, 16777215))

        self.horizontalLayout_2.addWidget(self.lbl_safe_z)

        self.lineEdit_safe_z = QLineEdit(self.widget_safe_z)
        self.lineEdit_safe_z.setObjectName(u"lineEdit_safe_z")
        sizePolicy.setHeightForWidth(self.lineEdit_safe_z.sizePolicy().hasHeightForWidth())
        self.lineEdit_safe_z.setSizePolicy(sizePolicy)
        self.lineEdit_safe_z.setMinimumSize(QSize(80, 0))
        self.lineEdit_safe_z.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_safe_z.setMaxLength(4)
        self.lineEdit_safe_z.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_safe_z)

        self.lbl_safe_z_ok = QLabel(self.widget_safe_z)
        self.lbl_safe_z_ok.setObjectName(u"lbl_safe_z_ok")
        sizePolicy1.setHeightForWidth(self.lbl_safe_z_ok.sizePolicy().hasHeightForWidth())
        self.lbl_safe_z_ok.setSizePolicy(sizePolicy1)
        self.lbl_safe_z_ok.setMinimumSize(QSize(24, 24))
        self.lbl_safe_z_ok.setMaximumSize(QSize(24, 24))
        self.lbl_safe_z_ok.setPixmap(QPixmap(u"images/unchecked.png"))
        self.lbl_safe_z_ok.setScaledContents(True)
        self.lbl_safe_z_ok.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lbl_safe_z_ok)


        self.verticalLayout.addWidget(self.widget_safe_z)

        self.widget_start_height = QWidget(self.frame_hole_circle)
        self.widget_start_height.setObjectName(u"widget_start_height")
        self.widget_start_height.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_start_height)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lbl_start_height = QLabel(self.widget_start_height)
        self.lbl_start_height.setObjectName(u"lbl_start_height")
        self.lbl_start_height.setMaximumSize(QSize(160, 16777215))

        self.horizontalLayout_3.addWidget(self.lbl_start_height)

        self.lineEdit_start_height = QLineEdit(self.widget_start_height)
        self.lineEdit_start_height.setObjectName(u"lineEdit_start_height")
        sizePolicy.setHeightForWidth(self.lineEdit_start_height.sizePolicy().hasHeightForWidth())
        self.lineEdit_start_height.setSizePolicy(sizePolicy)
        self.lineEdit_start_height.setMinimumSize(QSize(80, 0))
        self.lineEdit_start_height.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_start_height.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lineEdit_start_height)

        self.lbl_start_height_ok = QLabel(self.widget_start_height)
        self.lbl_start_height_ok.setObjectName(u"lbl_start_height_ok")
        sizePolicy1.setHeightForWidth(self.lbl_start_height_ok.sizePolicy().hasHeightForWidth())
        self.lbl_start_height_ok.setSizePolicy(sizePolicy1)
        self.lbl_start_height_ok.setMinimumSize(QSize(24, 24))
        self.lbl_start_height_ok.setMaximumSize(QSize(24, 24))
        self.lbl_start_height_ok.setPixmap(QPixmap(u"images/unchecked.png"))
        self.lbl_start_height_ok.setScaledContents(True)
        self.lbl_start_height_ok.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lbl_start_height_ok)


        self.verticalLayout.addWidget(self.widget_start_height)

        self.widget_depth = QWidget(self.frame_hole_circle)
        self.widget_depth.setObjectName(u"widget_depth")
        self.widget_depth.setMinimumSize(QSize(0, 0))
        self.widget_depth.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_depth)
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lbl_depth = QLabel(self.widget_depth)
        self.lbl_depth.setObjectName(u"lbl_depth")
        self.lbl_depth.setMinimumSize(QSize(160, 0))
        self.lbl_depth.setMaximumSize(QSize(160, 16777215))

        self.horizontalLayout_4.addWidget(self.lbl_depth)

        self.lineEdit_depth = QLineEdit(self.widget_depth)
        self.lineEdit_depth.setObjectName(u"lineEdit_depth")
        sizePolicy.setHeightForWidth(self.lineEdit_depth.sizePolicy().hasHeightForWidth())
        self.lineEdit_depth.setSizePolicy(sizePolicy)
        self.lineEdit_depth.setMinimumSize(QSize(80, 0))
        self.lineEdit_depth.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_depth.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lineEdit_depth)

        self.lbl_depth_ok = QLabel(self.widget_depth)
        self.lbl_depth_ok.setObjectName(u"lbl_depth_ok")
        sizePolicy1.setHeightForWidth(self.lbl_depth_ok.sizePolicy().hasHeightForWidth())
        self.lbl_depth_ok.setSizePolicy(sizePolicy1)
        self.lbl_depth_ok.setMinimumSize(QSize(24, 24))
        self.lbl_depth_ok.setMaximumSize(QSize(24, 24))
        self.lbl_depth_ok.setPixmap(QPixmap(u"images/unchecked.png"))
        self.lbl_depth_ok.setScaledContents(True)
        self.lbl_depth_ok.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lbl_depth_ok)


        self.verticalLayout.addWidget(self.widget_depth)

        self.widget_drill_feedrate = QWidget(self.frame_hole_circle)
        self.widget_drill_feedrate.setObjectName(u"widget_drill_feedrate")
        self.widget_drill_feedrate.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_10 = QHBoxLayout(self.widget_drill_feedrate)
        self.horizontalLayout_10.setSpacing(4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.lbl_drill_feed = QLabel(self.widget_drill_feedrate)
        self.lbl_drill_feed.setObjectName(u"lbl_drill_feed")
        self.lbl_drill_feed.setMaximumSize(QSize(160, 16777215))

        self.horizontalLayout_10.addWidget(self.lbl_drill_feed)

        self.lineEdit_drill_feed = QLineEdit(self.widget_drill_feedrate)
        self.lineEdit_drill_feed.setObjectName(u"lineEdit_drill_feed")
        sizePolicy.setHeightForWidth(self.lineEdit_drill_feed.sizePolicy().hasHeightForWidth())
        self.lineEdit_drill_feed.setSizePolicy(sizePolicy)
        self.lineEdit_drill_feed.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_drill_feed.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lineEdit_drill_feed)

        self.lbl_drill_feed_ok = QLabel(self.widget_drill_feedrate)
        self.lbl_drill_feed_ok.setObjectName(u"lbl_drill_feed_ok")
        sizePolicy1.setHeightForWidth(self.lbl_drill_feed_ok.sizePolicy().hasHeightForWidth())
        self.lbl_drill_feed_ok.setSizePolicy(sizePolicy1)
        self.lbl_drill_feed_ok.setMinimumSize(QSize(24, 24))
        self.lbl_drill_feed_ok.setMaximumSize(QSize(24, 24))
        self.lbl_drill_feed_ok.setPixmap(QPixmap(u"images/unchecked.png"))
        self.lbl_drill_feed_ok.setScaledContents(True)
        self.lbl_drill_feed_ok.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lbl_drill_feed_ok)


        self.verticalLayout.addWidget(self.widget_drill_feedrate)

        self.widget_units = QWidget(self.frame_hole_circle)
        self.widget_units.setObjectName(u"widget_units")
        self.widget_units.setMinimumSize(QSize(0, 30))
        self.widget_units.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_9 = QHBoxLayout(self.widget_units)
        self.horizontalLayout_9.setSpacing(4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.lbl_units = QLabel(self.widget_units)
        self.lbl_units.setObjectName(u"lbl_units")
        self.lbl_units.setMinimumSize(QSize(80, 0))
        self.lbl_units.setMaximumSize(QSize(80, 16777215))
        self.lbl_units.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.lbl_units)

        self.btn_inch = QPushButton(self.widget_units)
        self.btn_inch.setObjectName(u"btn_inch")
        sizePolicy.setHeightForWidth(self.btn_inch.sizePolicy().hasHeightForWidth())
        self.btn_inch.setSizePolicy(sizePolicy)
        self.btn_inch.setMinimumSize(QSize(60, 0))
        self.btn_inch.setMaximumSize(QSize(60, 16777215))
        self.btn_inch.setCheckable(True)
        self.btn_inch.setAutoExclusive(True)

        self.horizontalLayout_9.addWidget(self.btn_inch)

        self.btn_mm = QPushButton(self.widget_units)
        self.btn_mm.setObjectName(u"btn_mm")
        sizePolicy.setHeightForWidth(self.btn_mm.sizePolicy().hasHeightForWidth())
        self.btn_mm.setSizePolicy(sizePolicy)
        self.btn_mm.setMinimumSize(QSize(60, 0))
        self.btn_mm.setMaximumSize(QSize(60, 16777215))
        self.btn_mm.setCheckable(True)
        self.btn_mm.setChecked(True)
        self.btn_mm.setAutoExclusive(True)

        self.horizontalLayout_9.addWidget(self.btn_mm)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.widget_units)

        self.widget_comment = QWidget(self.frame_hole_circle)
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
        self.lbl_comment.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.lbl_comment)

        self.lineEdit_comment = QLineEdit(self.widget_comment)
        self.lineEdit_comment.setObjectName(u"lineEdit_comment")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_comment.sizePolicy().hasHeightForWidth())
        self.lineEdit_comment.setSizePolicy(sizePolicy2)

        self.horizontalLayout_11.addWidget(self.lineEdit_comment)


        self.verticalLayout.addWidget(self.widget_comment)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.layout_preview = QVBoxLayout()
        self.layout_preview.setSpacing(6)
        self.layout_preview.setObjectName(u"layout_preview")
        self.layout_preview.setSizeConstraint(QLayout.SetMaximumSize)
        self.layout_preview.setContentsMargins(2, 2, 2, 2)
        self.widget_macro = QWidget(self.frame_hole_circle)
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


        self.layout_preview.addWidget(self.widget_macro)


        self.horizontalLayout.addLayout(self.layout_preview)


        self.horizontalLayout_5.addWidget(self.frame_hole_circle)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_header.setText(QCoreApplication.translate("Form", u"HOLE CIRCLE PROGRAM", None))
        self.lbl_spindle.setText(QCoreApplication.translate("Form", u"SPINDLE RPM", None))
        self.lbl_spindle_ok.setText("")
        self.lbl_num_holes.setText(QCoreApplication.translate("Form", u"NUMBER OF HOLES", None))
        self.lbl_num_holes_ok.setText("")
        self.lbl_radius.setText(QCoreApplication.translate("Form", u"CIRCLE RADIUS", None))
        self.lbl_radius_ok.setText("")
#if QT_CONFIG(tooltip)
        self.lbl_first.setToolTip(QCoreApplication.translate("Form", u"Tool to use for facing", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_first.setText(QCoreApplication.translate("Form", u"ANGLE OF FIRST HOLE", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_first.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lbl_first_ok.setText("")
        self.lbl_safe_z.setText(QCoreApplication.translate("Form", u"SAFE Z TRAVEL HEIGHT", None))
        self.lbl_safe_z_ok.setText("")
        self.lbl_start_height.setText(QCoreApplication.translate("Form", u"HOLE START HEIGHT", None))
        self.lbl_start_height_ok.setText("")
        self.lbl_depth.setText(QCoreApplication.translate("Form", u"HOLE DRILL DEPTH", None))
        self.lbl_depth_ok.setText("")
        self.lbl_drill_feed.setText(QCoreApplication.translate("Form", u"DRILL FEEDRATE", None))
        self.lbl_drill_feed_ok.setText("")
#if QT_CONFIG(tooltip)
        self.lbl_units.setToolTip(QCoreApplication.translate("Form", u"Select machine units", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_units.setText(QCoreApplication.translate("Form", u"UNITS", None))
        self.btn_inch.setText(QCoreApplication.translate("Form", u"INCH", None))
        self.btn_mm.setText(QCoreApplication.translate("Form", u"MM", None))
#if QT_CONFIG(tooltip)
        self.lbl_comment.setToolTip(QCoreApplication.translate("Form", u"Comment for gcode file", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_comment.setText(QCoreApplication.translate("Form", u"COMMENT", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_comment.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btn_validate.setToolTip(QCoreApplication.translate("Form", u"Check if all inputs are valid", None))
#endif // QT_CONFIG(tooltip)
        self.btn_validate.setText(QCoreApplication.translate("Form", u"VALIDATE\n"
"INPUTS", None))
#if QT_CONFIG(tooltip)
        self.btn_create.setToolTip(QCoreApplication.translate("Form", u"Create program and save to file", None))
#endif // QT_CONFIG(tooltip)
        self.btn_create.setText(QCoreApplication.translate("Form", u"SAVE AS\n"
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

