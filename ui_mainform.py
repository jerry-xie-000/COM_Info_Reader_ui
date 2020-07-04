# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainform.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainForm(object):
    def setupUi(self, MainForm):
        if not MainForm.objectName():
            MainForm.setObjectName(u"MainForm")
        MainForm.resize(471, 408)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainForm.sizePolicy().hasHeightForWidth())
        MainForm.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(MainForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 59, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_6 = QLabel(MainForm)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setPointSize(25)
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_no = QLabel(MainForm)
        self.label_no.setObjectName(u"label_no")
        self.label_no.setFont(font)

        self.gridLayout.addWidget(self.label_no, 2, 2, 1, 1)

        self.label_mac = QLabel(MainForm)
        self.label_mac.setObjectName(u"label_mac")
        self.label_mac.setFont(font)

        self.gridLayout.addWidget(self.label_mac, 1, 2, 1, 1)

        self.label = QLabel(MainForm)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.label_4 = QLabel(MainForm)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_type = QLabel(MainForm)
        self.label_type.setObjectName(u"label_type")
        self.label_type.setFont(font)

        self.gridLayout.addWidget(self.label_type, 0, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.label_tip = QLabel(MainForm)
        self.label_tip.setObjectName(u"label_tip")

        self.verticalLayout.addWidget(self.label_tip)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_7 = QLabel(MainForm)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.comboBox_com = QComboBox(MainForm)
        self.comboBox_com.setObjectName(u"comboBox_com")
        sizePolicy.setHeightForWidth(self.comboBox_com.sizePolicy().hasHeightForWidth())
        self.comboBox_com.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.comboBox_com)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 59, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_open = QPushButton(MainForm)
        self.pushButton_open.setObjectName(u"pushButton_open")
        self.pushButton_open.setFont(font)
        self.pushButton_open.setFocusPolicy(Qt.TabFocus)

        self.horizontalLayout.addWidget(self.pushButton_open)

        self.pushButton_read = QPushButton(MainForm)
        self.pushButton_read.setObjectName(u"pushButton_read")
        self.pushButton_read.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_read)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(MainForm)

        QMetaObject.connectSlotsByName(MainForm)
    # setupUi

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QCoreApplication.translate("MainForm", u"Form", None))
        self.label_6.setText(QCoreApplication.translate("MainForm", u"\u5e8f\u5217\u53f7", None))
        self.label_no.setText(QCoreApplication.translate("MainForm", u"???", None))
        self.label_mac.setText(QCoreApplication.translate("MainForm", u"???", None))
        self.label.setText(QCoreApplication.translate("MainForm", u"\u578b\u53f7", None))
        self.label_4.setText(QCoreApplication.translate("MainForm", u"MAC", None))
        self.label_type.setText(QCoreApplication.translate("MainForm", u"???", None))
        self.label_tip.setText("")
        self.label_7.setText(QCoreApplication.translate("MainForm", u"\u4e32\u53e3         ", None))
        self.pushButton_open.setText(QCoreApplication.translate("MainForm", u"\u6253\u5f00\u4e32\u53e3", None))
        self.pushButton_read.setText(QCoreApplication.translate("MainForm", u"\u8bfb\u53d6", None))
    # retranslateUi


