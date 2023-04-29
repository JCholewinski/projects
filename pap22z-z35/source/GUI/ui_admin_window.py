# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AdminMainWindow(object):
    def setupUi(self, AdminMainWindow):
        if not AdminMainWindow.objectName():
            AdminMainWindow.setObjectName(u"AdminMainWindow")
        AdminMainWindow.resize(718, 490)
        AdminMainWindow.setMouseTracking(False)
        AdminMainWindow.setStyleSheet(u"QMainWindow{\n"
"	border-radius: 20px;\n"
"}")
        self.centralwidget = QWidget(AdminMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color:rgb(93, 93, 93);\n"
"	color:  rgb(255, 255, 255);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")
        self.horizontalLayout_4 = QHBoxLayout(self.main_page)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_main_clients = QLabel(self.main_page)
        self.label_main_clients.setObjectName(u"label_main_clients")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_main_clients.sizePolicy().hasHeightForWidth())
        self.label_main_clients.setSizePolicy(sizePolicy)
        self.label_main_clients.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout.addWidget(self.label_main_clients)

        self.clients_listWidget = QListWidget(self.main_page)
        self.clients_listWidget.setObjectName(u"clients_listWidget")

        self.verticalLayout.addWidget(self.clients_listWidget)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.main_options__pushButton = QPushButton(self.main_page)
        self.main_options__pushButton.setObjectName(u"main_options__pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_options__pushButton.sizePolicy().hasHeightForWidth())
        self.main_options__pushButton.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(20)
        self.main_options__pushButton.setFont(font)
        self.main_options__pushButton.setStyleSheet(u"QPushButton::pressed\n"
"{\n"
"background-color : rgb(49, 49, 49);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(71, 71, 71);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"padding-left:2px;\n"
"padding-right:2px;\n"
"}\n"
"\n"
"")
        self.main_options__pushButton.setCheckable(False)
        self.main_options__pushButton.setAutoDefault(False)
        self.main_options__pushButton.setFlat(False)

        self.verticalLayout_2.addWidget(self.main_options__pushButton)

        self.main_users_pushButton = QPushButton(self.main_page)
        self.main_users_pushButton.setObjectName(u"main_users_pushButton")
        sizePolicy1.setHeightForWidth(self.main_users_pushButton.sizePolicy().hasHeightForWidth())
        self.main_users_pushButton.setSizePolicy(sizePolicy1)
        self.main_users_pushButton.setFont(font)
        self.main_users_pushButton.setStyleSheet(u"QPushButton::pressed\n"
"{\n"
"background-color : rgb(49, 49, 49);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(71, 71, 71);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding-top:5px;\n"
"padding-bottom:5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"}\n"
"\n"
"")
        self.main_users_pushButton.setCheckable(False)
        self.main_users_pushButton.setAutoDefault(False)
        self.main_users_pushButton.setFlat(False)

        self.verticalLayout_2.addWidget(self.main_users_pushButton)

        self.main_logout_pushButton = QPushButton(self.main_page)
        self.main_logout_pushButton.setObjectName(u"main_logout_pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.main_logout_pushButton.sizePolicy().hasHeightForWidth())
        self.main_logout_pushButton.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(12)
        self.main_logout_pushButton.setFont(font1)
        self.main_logout_pushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: rgb(93, 93, 93);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-radius: 10px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"padding-left:2px;\n"
"padding-right:2px;\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color : rgb(71, 71, 71);\n"
"}")

        self.verticalLayout_2.addWidget(self.main_logout_pushButton)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.stackedWidget.addWidget(self.main_page)
        self.page_options = QWidget()
        self.page_options.setObjectName(u"page_options")
        self.horizontalLayout_7 = QHBoxLayout(self.page_options)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_options = QLabel(self.page_options)
        self.label_options.setObjectName(u"label_options")
        sizePolicy.setHeightForWidth(self.label_options.sizePolicy().hasHeightForWidth())
        self.label_options.setSizePolicy(sizePolicy)
        self.label_options.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.label_options)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.options_currencies__pushButton = QPushButton(self.page_options)
        self.options_currencies__pushButton.setObjectName(u"options_currencies__pushButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.options_currencies__pushButton.sizePolicy().hasHeightForWidth())
        self.options_currencies__pushButton.setSizePolicy(sizePolicy3)
        self.options_currencies__pushButton.setFont(font)
        self.options_currencies__pushButton.setStyleSheet(u"QPushButton::pressed\n"
"{\n"
"background-color : rgb(49, 49, 49);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(71, 71, 71);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"padding-left:2px;\n"
"padding-right:2px;\n"
"}\n"
"\n"
"")
        self.options_currencies__pushButton.setCheckable(False)
        self.options_currencies__pushButton.setAutoDefault(False)
        self.options_currencies__pushButton.setFlat(False)

        self.horizontalLayout_5.addWidget(self.options_currencies__pushButton)

        self.options_deposit__pushButton = QPushButton(self.page_options)
        self.options_deposit__pushButton.setObjectName(u"options_deposit__pushButton")
        sizePolicy3.setHeightForWidth(self.options_deposit__pushButton.sizePolicy().hasHeightForWidth())
        self.options_deposit__pushButton.setSizePolicy(sizePolicy3)
        self.options_deposit__pushButton.setFont(font)
        self.options_deposit__pushButton.setStyleSheet(u"QPushButton::pressed\n"
"{\n"
"background-color : rgb(49, 49, 49);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(71, 71, 71);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"padding-left:2px;\n"
"padding-right:2px;\n"
"}\n"
"\n"
"")
        self.options_deposit__pushButton.setCheckable(False)
        self.options_deposit__pushButton.setAutoDefault(False)
        self.options_deposit__pushButton.setFlat(False)

        self.horizontalLayout_5.addWidget(self.options_deposit__pushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.options_loans__pushButton = QPushButton(self.page_options)
        self.options_loans__pushButton.setObjectName(u"options_loans__pushButton")
        sizePolicy1.setHeightForWidth(self.options_loans__pushButton.sizePolicy().hasHeightForWidth())
        self.options_loans__pushButton.setSizePolicy(sizePolicy1)
        self.options_loans__pushButton.setFont(font)
        self.options_loans__pushButton.setStyleSheet(u"QPushButton::pressed\n"
"{\n"
"background-color : rgb(49, 49, 49);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(71, 71, 71);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"padding-left:2px;\n"
"padding-right:2px;\n"
"}\n"
"\n"
"")
        self.options_loans__pushButton.setCheckable(False)
        self.options_loans__pushButton.setAutoDefault(False)
        self.options_loans__pushButton.setFlat(False)

        self.horizontalLayout_6.addWidget(self.options_loans__pushButton)

        self.options_back_pushButton = QPushButton(self.page_options)
        self.options_back_pushButton.setObjectName(u"options_back_pushButton")
        sizePolicy3.setHeightForWidth(self.options_back_pushButton.sizePolicy().hasHeightForWidth())
        self.options_back_pushButton.setSizePolicy(sizePolicy3)
        self.options_back_pushButton.setFont(font)
        self.options_back_pushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: rgb(93, 93, 93);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-radius: 5px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"padding-left:2px;\n"
"padding-right:2px;\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color : rgb(71, 71, 71);\n"
"}")

        self.horizontalLayout_6.addWidget(self.options_back_pushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_7.addLayout(self.verticalLayout_3)

        self.stackedWidget.addWidget(self.page_options)
        self.page_users = QWidget()
        self.page_users.setObjectName(u"page_users")
        self.horizontalLayout_39 = QHBoxLayout(self.page_users)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.users_left_frame = QFrame(self.page_users)
        self.users_left_frame.setObjectName(u"users_left_frame")
        self.users_left_frame.setFrameShape(QFrame.StyledPanel)
        self.users_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.users_left_frame)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_users_2 = QLabel(self.users_left_frame)
        self.label_users_2.setObjectName(u"label_users_2")
        sizePolicy2.setHeightForWidth(self.label_users_2.sizePolicy().hasHeightForWidth())
        self.label_users_2.setSizePolicy(sizePolicy2)
        self.label_users_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_5.addWidget(self.label_users_2)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_users_4 = QLabel(self.users_left_frame)
        self.label_users_4.setObjectName(u"label_users_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_users_4.sizePolicy().hasHeightForWidth())
        self.label_users_4.setSizePolicy(sizePolicy4)
        self.label_users_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_users_4)

        self.user_name_lineEdit = QLineEdit(self.users_left_frame)
        self.user_name_lineEdit.setObjectName(u"user_name_lineEdit")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.user_name_lineEdit.sizePolicy().hasHeightForWidth())
        self.user_name_lineEdit.setSizePolicy(sizePolicy5)
        self.user_name_lineEdit.setStyleSheet(u"QLineEdit\n"
"{\n"
"border: 1px solid;\n"
"border-radius: 4px;\n"
"background-color: white;\n"
"}")
        self.user_name_lineEdit.setReadOnly(True)
        self.user_name_lineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_10.addWidget(self.user_name_lineEdit)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_users_5 = QLabel(self.users_left_frame)
        self.label_users_5.setObjectName(u"label_users_5")
        sizePolicy4.setHeightForWidth(self.label_users_5.sizePolicy().hasHeightForWidth())
        self.label_users_5.setSizePolicy(sizePolicy4)
        self.label_users_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_users_5)

        self.users_num_lineEdit = QLineEdit(self.users_left_frame)
        self.users_num_lineEdit.setObjectName(u"users_num_lineEdit")
        sizePolicy5.setHeightForWidth(self.users_num_lineEdit.sizePolicy().hasHeightForWidth())
        self.users_num_lineEdit.setSizePolicy(sizePolicy5)
        self.users_num_lineEdit.setStyleSheet(u"QLineEdit\n"
"{\n"
"border: 1px solid;\n"
"border-radius: 4px;\n"
"background-color: white;\n"
"}")
        self.users_num_lineEdit.setReadOnly(True)
        self.users_num_lineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_11.addWidget(self.users_num_lineEdit)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_users_6 = QLabel(self.users_left_frame)
        self.label_users_6.setObjectName(u"label_users_6")
        sizePolicy4.setHeightForWidth(self.label_users_6.sizePolicy().hasHeightForWidth())
        self.label_users_6.setSizePolicy(sizePolicy4)
        self.label_users_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_users_6)

        self.users_password_lineEdit = QLineEdit(self.users_left_frame)
        self.users_password_lineEdit.setObjectName(u"users_password_lineEdit")
        sizePolicy5.setHeightForWidth(self.users_password_lineEdit.sizePolicy().hasHeightForWidth())
        self.users_password_lineEdit.setSizePolicy(sizePolicy5)
        self.users_password_lineEdit.setStyleSheet(u"QLineEdit\n"
"{\n"
"border: 1px solid;\n"
"border-radius: 4px;\n"
"background-color: white;\n"
"}")
        self.users_password_lineEdit.setReadOnly(True)
        self.users_password_lineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_12.addWidget(self.users_password_lineEdit)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_users_7 = QLabel(self.users_left_frame)
        self.label_users_7.setObjectName(u"label_users_7")
        sizePolicy4.setHeightForWidth(self.label_users_7.sizePolicy().hasHeightForWidth())
        self.label_users_7.setSizePolicy(sizePolicy4)
        self.label_users_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_users_7)

        self.users_money_lineEdit = QLineEdit(self.users_left_frame)
        self.users_money_lineEdit.setObjectName(u"users_money_lineEdit")
        sizePolicy5.setHeightForWidth(self.users_money_lineEdit.sizePolicy().hasHeightForWidth())
        self.users_money_lineEdit.setSizePolicy(sizePolicy5)
        self.users_money_lineEdit.setStyleSheet(u"QLineEdit\n"
"{\n"
"border: 1px solid;\n"
"border-radius: 4px;\n"
"background-color: white;\n"
"}")
        self.users_money_lineEdit.setReadOnly(True)
        self.users_money_lineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_13.addWidget(self.users_money_lineEdit)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)


        self.horizontalLayout_40.addLayout(self.verticalLayout_5)


        self.horizontalLayout_38.addWidget(self.users_left_frame)

        self.users_right_frame = QFrame(self.page_users)
        self.users_right_frame.setObjectName(u"users_right_frame")
        self.users_right_frame.setFrameShape(QFrame.StyledPanel)
        self.users_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.users_right_frame)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_users = QLabel(self.users_right_frame)
        self.label_users.setObjectName(u"label_users")
        sizePolicy4.setHeightForWidth(self.label_users.sizePolicy().hasHeightForWidth())
        self.label_users.setSizePolicy(sizePolicy4)
        self.label_users.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout_8.addWidget(self.label_users)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.users_param_comboBox = QComboBox(self.users_right_frame)
        self.users_param_comboBox.addItem("")
        self.users_param_comboBox.addItem("")
        self.users_param_comboBox.addItem("")
        self.users_param_comboBox.addItem("")
        self.users_param_comboBox.setObjectName(u"users_param_comboBox")
        sizePolicy.setHeightForWidth(self.users_param_comboBox.sizePolicy().hasHeightForWidth())
        self.users_param_comboBox.setSizePolicy(sizePolicy)
        self.users_param_comboBox.setAutoFillBackground(False)
        self.users_param_comboBox.setStyleSheet(u"QComboBox\n"
"{\n"
"border: 1px solid;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"padding-left: 1px;\n"
"padding-top: 1px;\n"
"padding-right: 1px;\n"
"padding-bottom: 1px;\n"
"}")
        self.users_param_comboBox.setMaxVisibleItems(20)
        self.users_param_comboBox.setFrame(False)

        self.verticalLayout_4.addWidget(self.users_param_comboBox)

        self.users_stackedWidget = QStackedWidget(self.users_right_frame)
        self.users_stackedWidget.setObjectName(u"users_stackedWidget")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.users_stackedWidget.sizePolicy().hasHeightForWidth())
        self.users_stackedWidget.setSizePolicy(sizePolicy6)
        self.users_stackedWidget.setFrameShadow(QFrame.Plain)
        self.page_name = QWidget()
        self.page_name.setObjectName(u"page_name")
        self.horizontalLayout_15 = QHBoxLayout(self.page_name)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.label_users_19 = QLabel(self.page_name)
        self.label_users_19.setObjectName(u"label_users_19")
        sizePolicy4.setHeightForWidth(self.label_users_19.sizePolicy().hasHeightForWidth())
        self.label_users_19.setSizePolicy(sizePolicy4)
        self.label_users_19.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_7.addWidget(self.label_users_19)

        self.edit_user_name_lineEdit = QLineEdit(self.page_name)
        self.edit_user_name_lineEdit.setObjectName(u"edit_user_name_lineEdit")
        sizePolicy5.setHeightForWidth(self.edit_user_name_lineEdit.sizePolicy().hasHeightForWidth())
        self.edit_user_name_lineEdit.setSizePolicy(sizePolicy5)
        font2 = QFont()
        font2.setPointSize(14)
        self.edit_user_name_lineEdit.setFont(font2)
        self.edit_user_name_lineEdit.setStyleSheet(u"QLineEdit\n"
"{\n"
"border: 1px solid;\n"
"border-radius: 4px;\n"
"background-color: white;\n"
"}")
        self.edit_user_name_lineEdit.setReadOnly(False)
        self.edit_user_name_lineEdit.setClearButtonEnabled(True)

        self.verticalLayout_7.addWidget(self.edit_user_name_lineEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)


        self.horizontalLayout_15.addLayout(self.verticalLayout_7)

        self.users_stackedWidget.addWidget(self.page_name)
        self.page_number = QWidget()
        self.page_number.setObjectName(u"page_number")
        self.horizontalLayout_42 = QHBoxLayout(self.page_number)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_7)

        self.label_users_20 = QLabel(self.page_number)
        self.label_users_20.setObjectName(u"label_users_20")
        sizePolicy4.setHeightForWidth(self.label_users_20.sizePolicy().hasHeightForWidth())
        self.label_users_20.setSizePolicy(sizePolicy4)
        self.label_users_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_19.addWidget(self.label_users_20)

        self.edit_user_number_spinBox = QSpinBox(self.page_number)
        self.edit_user_number_spinBox.setObjectName(u"edit_user_number_spinBox")
        sizePolicy1.setHeightForWidth(self.edit_user_number_spinBox.sizePolicy().hasHeightForWidth())
        self.edit_user_number_spinBox.setSizePolicy(sizePolicy1)
        self.edit_user_number_spinBox.setFont(font2)
        self.edit_user_number_spinBox.setStyleSheet(u"QSpinBox\n"
"{\n"
"border: 1px solid; \n"
"border-radius: 5px; \n"
"background-color: white;\n"
"padding-left: 1px;\n"
"padding-top: 1px;\n"
"padding-right: 1px;\n"
"padding-bottom: 1px;\n"
"}\n"
"\n"
"QSpinBox::up-button\n"
"{\n"
"    min-width:4px;\n"
"    min-height: 4px;\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed\n"
"{\n"
"    right : 1px\n"
"}\n"
"\n"
"QSpinBox::down-button\n"
"{\n"
"    min-width: 4px;\n"
"    min-height: 4px;\n"
"}\n"
" \n"
"QSpinBox::down-button:pressed\n"
"{\n"
"    right: 1px;\n"
"}")
        self.edit_user_number_spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.edit_user_number_spinBox.setAccelerated(False)
        self.edit_user_number_spinBox.setMaximum(999999999)

        self.verticalLayout_19.addWidget(self.edit_user_number_spinBox)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_8)


        self.horizontalLayout_42.addLayout(self.verticalLayout_19)

        self.users_stackedWidget.addWidget(self.page_number)
        self.page_password = QWidget()
        self.page_password.setObjectName(u"page_password")
        self.horizontalLayout_43 = QHBoxLayout(self.page_password)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_9)

        self.label_users_21 = QLabel(self.page_password)
        self.label_users_21.setObjectName(u"label_users_21")
        sizePolicy4.setHeightForWidth(self.label_users_21.sizePolicy().hasHeightForWidth())
        self.label_users_21.setSizePolicy(sizePolicy4)
        self.label_users_21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_20.addWidget(self.label_users_21)

        self.edit_user_password_lineEdit_4 = QLineEdit(self.page_password)
        self.edit_user_password_lineEdit_4.setObjectName(u"edit_user_password_lineEdit_4")
        sizePolicy5.setHeightForWidth(self.edit_user_password_lineEdit_4.sizePolicy().hasHeightForWidth())
        self.edit_user_password_lineEdit_4.setSizePolicy(sizePolicy5)
        self.edit_user_password_lineEdit_4.setFont(font2)
        self.edit_user_password_lineEdit_4.setStyleSheet(u"QLineEdit\n"
"{\n"
"border: 1px solid;\n"
"border-radius: 4px;\n"
"background-color: white;\n"
"}")
        self.edit_user_password_lineEdit_4.setReadOnly(False)
        self.edit_user_password_lineEdit_4.setClearButtonEnabled(True)

        self.verticalLayout_20.addWidget(self.edit_user_password_lineEdit_4)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_10)


        self.horizontalLayout_43.addLayout(self.verticalLayout_20)

        self.users_stackedWidget.addWidget(self.page_password)
        self.page_money = QWidget()
        self.page_money.setObjectName(u"page_money")
        self.horizontalLayout_44 = QHBoxLayout(self.page_money)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_11)

        self.label_users_22 = QLabel(self.page_money)
        self.label_users_22.setObjectName(u"label_users_22")
        sizePolicy4.setHeightForWidth(self.label_users_22.sizePolicy().hasHeightForWidth())
        self.label_users_22.setSizePolicy(sizePolicy4)
        self.label_users_22.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_21.addWidget(self.label_users_22)

        self.edit_user_money_doubleSpinBox = QDoubleSpinBox(self.page_money)
        self.edit_user_money_doubleSpinBox.setObjectName(u"edit_user_money_doubleSpinBox")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.edit_user_money_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.edit_user_money_doubleSpinBox.setSizePolicy(sizePolicy7)
        self.edit_user_money_doubleSpinBox.setFont(font2)
        self.edit_user_money_doubleSpinBox.setStyleSheet(u"QDoubleSpinBox\n"
"{\n"
"border: 1px solid; \n"
"border-radius: 5px; \n"
"background-color: white;\n"
"padding-left: 1px;\n"
"padding-top: 1px;\n"
"padding-right: 1px;\n"
"padding-bottom: 1px;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button\n"
"{\n"
"    min-width:4px;\n"
"    min-height: 4px;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button:pressed\n"
"{\n"
"    right : 1px\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button\n"
"{\n"
"    min-width: 4px;\n"
"    min-height: 4px;\n"
"}\n"
" \n"
"QDoubleSpinBox::down-button:pressed\n"
"{\n"
"    right: 1px;\n"
"}")
        self.edit_user_money_doubleSpinBox.setWrapping(False)
        self.edit_user_money_doubleSpinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.edit_user_money_doubleSpinBox.setAccelerated(True)
        self.edit_user_money_doubleSpinBox.setMaximum(9000000000000.000000000000000)

        self.verticalLayout_21.addWidget(self.edit_user_money_doubleSpinBox)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_12)


        self.horizontalLayout_44.addLayout(self.verticalLayout_21)

        self.users_stackedWidget.addWidget(self.page_money)

        self.verticalLayout_4.addWidget(self.users_stackedWidget)

        self.users_accept_pushButton = QPushButton(self.users_right_frame)
        self.users_accept_pushButton.setObjectName(u"users_accept_pushButton")
        self.users_accept_pushButton.setFont(font)
        self.users_accept_pushButton.setStyleSheet(u"QPushButton::pressed\n"
"{\n"
"background-color : rgb(49, 49, 49);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(71, 71, 71);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.users_accept_pushButton.setCheckable(False)
        self.users_accept_pushButton.setAutoDefault(False)
        self.users_accept_pushButton.setFlat(False)

        self.verticalLayout_4.addWidget(self.users_accept_pushButton)

        self.users_back_pushButton = QPushButton(self.users_right_frame)
        self.users_back_pushButton.setObjectName(u"users_back_pushButton")
        sizePolicy2.setHeightForWidth(self.users_back_pushButton.sizePolicy().hasHeightForWidth())
        self.users_back_pushButton.setSizePolicy(sizePolicy2)
        self.users_back_pushButton.setFont(font1)
        self.users_back_pushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: rgb(93, 93, 93);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-radius: 10px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"padding-left:2px;\n"
"padding-right:2px;\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color : rgb(71, 71, 71);\n"
"}")

        self.verticalLayout_4.addWidget(self.users_back_pushButton)


        self.horizontalLayout_41.addLayout(self.verticalLayout_4)


        self.horizontalLayout_38.addWidget(self.users_right_frame)


        self.horizontalLayout_39.addLayout(self.horizontalLayout_38)

        self.stackedWidget.addWidget(self.page_users)
        self.page_currencies = QWidget()
        self.page_currencies.setObjectName(u"page_currencies")
        self.horizontalLayout_18 = QHBoxLayout(self.page_currencies)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_currencies = QLabel(self.page_currencies)
        self.label_currencies.setObjectName(u"label_currencies")
        sizePolicy.setHeightForWidth(self.label_currencies.sizePolicy().hasHeightForWidth())
        self.label_currencies.setSizePolicy(sizePolicy)
        self.label_currencies.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_17.addWidget(self.label_currencies)

        self.currencies_back_pushButton = QPushButton(self.page_currencies)
        self.currencies_back_pushButton.setObjectName(u"currencies_back_pushButton")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.currencies_back_pushButton.sizePolicy().hasHeightForWidth())
        self.currencies_back_pushButton.setSizePolicy(sizePolicy8)
        self.currencies_back_pushButton.setFont(font2)
        self.currencies_back_pushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: rgb(93, 93, 93);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-radius: 10px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"padding-left:2px;\n"
"padding-right:2px;\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color : rgb(71, 71, 71);\n"
"}")

        self.horizontalLayout_17.addWidget(self.currencies_back_pushButton)


        self.verticalLayout_8.addLayout(self.horizontalLayout_17)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_currencies_2 = QLabel(self.page_currencies)
        self.label_currencies_2.setObjectName(u"label_currencies_2")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.label_currencies_2.sizePolicy().hasHeightForWidth())
        self.label_currencies_2.setSizePolicy(sizePolicy9)
        self.label_currencies_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_currencies_2)

        self.currency_comboBox = QComboBox(self.page_currencies)
        self.currency_comboBox.setObjectName(u"currency_comboBox")
        self.currency_comboBox.setFont(font2)
        self.currency_comboBox.setAutoFillBackground(False)
        self.currency_comboBox.setStyleSheet(u"QComboBox\n"
"{\n"
"border: 1px solid; \n"
"border-radius: 5px; \n"
"background-color: white;\n"
"padding-left: 1px;\n"
"padding-top: 1px;\n"
"padding-right: 1px;\n"
"padding-bottom: 1px;\n"
"}")
        self.currency_comboBox.setMaxVisibleItems(20)
        self.currency_comboBox.setFrame(False)

        self.horizontalLayout_9.addWidget(self.currency_comboBox)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_currencies_3 = QLabel(self.page_currencies)
        self.label_currencies_3.setObjectName(u"label_currencies_3")
        sizePolicy9.setHeightForWidth(self.label_currencies_3.sizePolicy().hasHeightForWidth())
        self.label_currencies_3.setSizePolicy(sizePolicy9)
        self.label_currencies_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_currencies_3)

        self.currency_buying_rate_doubleSpinBox = QDoubleSpinBox(self.page_currencies)
        self.currency_buying_rate_doubleSpinBox.setObjectName(u"currency_buying_rate_doubleSpinBox")
        sizePolicy7.setHeightForWidth(self.currency_buying_rate_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.currency_buying_rate_doubleSpinBox.setSizePolicy(sizePolicy7)
        self.currency_buying_rate_doubleSpinBox.setFont(font2)
        self.currency_buying_rate_doubleSpinBox.setStyleSheet(u"QDoubleSpinBox\n"
"{\n"
"border: 1px solid; \n"
"border-radius: 5px; \n"
"background-color: white;\n"
"padding-left: 1px;\n"
"padding-top: 1px;\n"
"padding-right: 1px;\n"
"padding-bottom: 1px;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button\n"
"{\n"
"    min-width:4px;\n"
"    min-height: 4px;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button:pressed\n"
"{\n"
"    right : 1px\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button\n"
"{\n"
"    min-width: 4px;\n"
"    min-height: 4px;\n"
"}\n"
" \n"
"QDoubleSpinBox::down-button:pressed\n"
"{\n"
"    right: 1px;\n"
"}")
        self.currency_buying_rate_doubleSpinBox.setWrapping(False)
        self.currency_buying_rate_doubleSpinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.currency_buying_rate_doubleSpinBox.setAccelerated(True)
        self.currency_buying_rate_doubleSpinBox.setMaximum(9000000000000.000000000000000)

        self.horizontalLayout_14.addWidget(self.currency_buying_rate_doubleSpinBox)


        self.verticalLayout_6.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_currencies_4 = QLabel(self.page_currencies)
        self.label_currencies_4.setObjectName(u"label_currencies_4")
        sizePolicy9.setHeightForWidth(self.label_currencies_4.sizePolicy().hasHeightForWidth())
        self.label_currencies_4.setSizePolicy(sizePolicy9)
        self.label_currencies_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_currencies_4)

        self.currency_selling_rate_doubleSpinBox = QDoubleSpinBox(self.page_currencies)
        self.currency_selling_rate_doubleSpinBox.setObjectName(u"currency_selling_rate_doubleSpinBox")
        sizePolicy7.setHeightForWidth(self.currency_selling_rate_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.currency_selling_rate_doubleSpinBox.setSizePolicy(sizePolicy7)
        self.currency_selling_rate_doubleSpinBox.setFont(font2)
        self.currency_selling_rate_doubleSpinBox.setStyleSheet(u"QDoubleSpinBox\n"
"{\n"
"border: 1px solid; \n"
"border-radius: 5px; \n"
"background-color: white;\n"
"padding-left: 1px;\n"
"padding-top: 1px;\n"
"padding-right: 1px;\n"
"padding-bottom: 1px;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button\n"
"{\n"
"    min-width:4px;\n"
"    min-height: 4px;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button:pressed\n"
"{\n"
"    right : 1px\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button\n"
"{\n"
"    min-width: 4px;\n"
"    min-height: 4px;\n"
"}\n"
" \n"
"QDoubleSpinBox::down-button:pressed\n"
"{\n"
"    right: 1px;\n"
"}")
        self.currency_selling_rate_doubleSpinBox.setWrapping(False)
        self.currency_selling_rate_doubleSpinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.currency_selling_rate_doubleSpinBox.setAccelerated(True)
        self.currency_selling_rate_doubleSpinBox.setMaximum(9000000000000.000000000000000)

        self.horizontalLayout_16.addWidget(self.currency_selling_rate_doubleSpinBox)


        self.verticalLayout_6.addLayout(self.horizontalLayout_16)


        self.verticalLayout_8.addLayout(self.verticalLayout_6)

        self.currency_change_pushButton = QPushButton(self.page_currencies)
        self.currency_change_pushButton.setObjectName(u"currency_change_pushButton")
        self.currency_change_pushButton.setFont(font)
        self.currency_change_pushButton.setStyleSheet(u"QPushButton::pressed\n"
"{\n"
"background-color : rgb(49, 49, 49);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(71, 71, 71);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.currency_change_pushButton.setCheckable(False)
        self.currency_change_pushButton.setAutoDefault(False)
        self.currency_change_pushButton.setFlat(False)

        self.verticalLayout_8.addWidget(self.currency_change_pushButton)


        self.horizontalLayout_18.addLayout(self.verticalLayout_8)

        self.stackedWidget.addWidget(self.page_currencies)
        self.page_deposits = QWidget()
        self.page_deposits.setObjectName(u"page_deposits")
        self.horizontalLayout_22 = QHBoxLayout(self.page_deposits)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_deposits = QLabel(self.page_deposits)
        self.label_deposits.setObjectName(u"label_deposits")
        sizePolicy.setHeightForWidth(self.label_deposits.sizePolicy().hasHeightForWidth())
        self.label_deposits.setSizePolicy(sizePolicy)
        self.label_deposits.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_21.addWidget(self.label_deposits)

        self.deposits_back_pushButton_2 = QPushButton(self.page_deposits)
        self.deposits_back_pushButton_2.setObjectName(u"deposits_back_pushButton_2")
        sizePolicy8.setHeightForWidth(self.deposits_back_pushButton_2.sizePolicy().hasHeightForWidth())
        self.deposits_back_pushButton_2.setSizePolicy(sizePolicy8)
        self.deposits_back_pushButton_2.setFont(font2)
        self.deposits_back_pushButton_2.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: rgb(93, 93, 93);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-radius: 10px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"padding-left:2px;\n"
"padding-right:2px;\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color : rgb(71, 71, 71);\n"
"}")

        self.horizontalLayout_21.addWidget(self.deposits_back_pushButton_2)


        self.verticalLayout_10.addLayout(self.horizontalLayout_21)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_deposits_2 = QLabel(self.page_deposits)
        self.label_deposits_2.setObjectName(u"label_deposits_2")
        sizePolicy9.setHeightForWidth(self.label_deposits_2.sizePolicy().hasHeightForWidth())
        self.label_deposits_2.setSizePolicy(sizePolicy9)
        self.label_deposits_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.label_deposits_2)

        self.deposit_duration_spinBox = QSpinBox(self.page_deposits)
        self.deposit_duration_spinBox.setObjectName(u"deposit_duration_spinBox")
        sizePolicy8.setHeightForWidth(self.deposit_duration_spinBox.sizePolicy().hasHeightForWidth())
        self.deposit_duration_spinBox.setSizePolicy(sizePolicy8)
        self.deposit_duration_spinBox.setFont(font2)
        self.deposit_duration_spinBox.setStyleSheet(u"QSpinBox\n"
"{\n"
"border: 1px solid; \n"
"border-radius: 5px; \n"
"background-color: white;\n"
"padding-left: 1px;\n"
"padding-top: 1px;\n"
"padding-right: 1px;\n"
"padding-bottom: 1px;\n"
"}\n"
"\n"
"QSpinBox::up-button\n"
"{\n"
"    min-width:4px;\n"
"    min-height: 4px;\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed\n"
"{\n"
"    right : 1px\n"
"}\n"
"\n"
"QSpinBox::down-button\n"
"{\n"
"    min-width: 4px;\n"
"    min-height: 4px;\n"
"}\n"
" \n"
"QSpinBox::down-button:pressed\n"
"{\n"
"    right: 1px;\n"
"}")
        self.deposit_duration_spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.deposit_duration_spinBox.setMaximum(999999999)

        self.horizontalLayout_19.addWidget(self.deposit_duration_spinBox)


        self.verticalLayout_9.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_deposits_3 = QLabel(self.page_deposits)
        self.label_deposits_3.setObjectName(u"label_deposits_3")
        sizePolicy9.setHeightForWidth(self.label_deposits_3.sizePolicy().hasHeightForWidth())
        self.label_deposits_3.setSizePolicy(sizePolicy9)
        self.label_deposits_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.label_deposits_3)

        self.deposit_interest_doubleSpinBox = QDoubleSpinBox(self.page_deposits)
        self.deposit_interest_doubleSpinBox.setObjectName(u"deposit_interest_doubleSpinBox")
        sizePolicy7.setHeightForWidth(self.deposit_interest_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.deposit_interest_doubleSpinBox.setSizePolicy(sizePolicy7)
        self.deposit_interest_doubleSpinBox.setFont(font2)
        self.deposit_interest_doubleSpinBox.setStyleSheet(u"QDoubleSpinBox\n"
"{\n"
"border: 1px solid; \n"
"border-radius: 5px; \n"
"background-color: white;\n"
"padding-left: 1px;\n"
"padding-top: 1px;\n"
"padding-right: 1px;\n"
"padding-bottom: 1px;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button\n"
"{\n"
"    min-width:4px;\n"
"    min-height: 4px;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button:pressed\n"
"{\n"
"    right : 1px\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button\n"
"{\n"
"    min-width: 4px;\n"
"    min-height: 4px;\n"
"}\n"
" \n"
"QDoubleSpinBox::down-button:pressed\n"
"{\n"
"    right: 1px;\n"
"}")
        self.deposit_interest_doubleSpinBox.setWrapping(False)
        self.deposit_interest_doubleSpinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.deposit_interest_doubleSpinBox.setAccelerated(True)
        self.deposit_interest_doubleSpinBox.setMaximum(9000000000000.000000000000000)

        self.horizontalLayout_20.addWidget(self.deposit_interest_doubleSpinBox)


        self.verticalLayout_9.addLayout(self.horizontalLayout_20)


        self.verticalLayout_10.addLayout(self.verticalLayout_9)

        self.deposit_change_pushButton = QPushButton(self.page_deposits)
        self.deposit_change_pushButton.setObjectName(u"deposit_change_pushButton")
        self.deposit_change_pushButton.setFont(font)
        self.deposit_change_pushButton.setStyleSheet(u"QPushButton::pressed\n"
"{\n"
"background-color : rgb(49, 49, 49);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(71, 71, 71);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.deposit_change_pushButton.setCheckable(False)
        self.deposit_change_pushButton.setAutoDefault(False)
        self.deposit_change_pushButton.setFlat(False)

        self.verticalLayout_10.addWidget(self.deposit_change_pushButton)


        self.horizontalLayout_22.addLayout(self.verticalLayout_10)

        self.stackedWidget.addWidget(self.page_deposits)
        self.page_loans = QWidget()
        self.page_loans.setObjectName(u"page_loans")
        self.horizontalLayout_26 = QHBoxLayout(self.page_loans)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_loans = QLabel(self.page_loans)
        self.label_loans.setObjectName(u"label_loans")
        sizePolicy.setHeightForWidth(self.label_loans.sizePolicy().hasHeightForWidth())
        self.label_loans.setSizePolicy(sizePolicy)
        self.label_loans.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_23.addWidget(self.label_loans)

        self.loans_back_pushButton = QPushButton(self.page_loans)
        self.loans_back_pushButton.setObjectName(u"loans_back_pushButton")
        sizePolicy8.setHeightForWidth(self.loans_back_pushButton.sizePolicy().hasHeightForWidth())
        self.loans_back_pushButton.setSizePolicy(sizePolicy8)
        self.loans_back_pushButton.setFont(font2)
        self.loans_back_pushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: rgb(93, 93, 93);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-radius: 10px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"padding-left:2px;\n"
"padding-right:2px;\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color : rgb(71, 71, 71);\n"
"}")

        self.horizontalLayout_23.addWidget(self.loans_back_pushButton)


        self.verticalLayout_12.addLayout(self.horizontalLayout_23)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_loans_2 = QLabel(self.page_loans)
        self.label_loans_2.setObjectName(u"label_loans_2")
        sizePolicy9.setHeightForWidth(self.label_loans_2.sizePolicy().hasHeightForWidth())
        self.label_loans_2.setSizePolicy(sizePolicy9)
        self.label_loans_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_24.addWidget(self.label_loans_2)

        self.loan_duration_spinBox = QSpinBox(self.page_loans)
        self.loan_duration_spinBox.setObjectName(u"loan_duration_spinBox")
        sizePolicy8.setHeightForWidth(self.loan_duration_spinBox.sizePolicy().hasHeightForWidth())
        self.loan_duration_spinBox.setSizePolicy(sizePolicy8)
        self.loan_duration_spinBox.setFont(font2)
        self.loan_duration_spinBox.setStyleSheet(u"QSpinBox\n"
"{\n"
"border: 1px solid; \n"
"border-radius: 5px; \n"
"background-color: white;\n"
"padding-left: 1px;\n"
"padding-top: 1px;\n"
"padding-right: 1px;\n"
"padding-bottom: 1px;\n"
"}\n"
"\n"
"QSpinBox::up-button\n"
"{\n"
"    min-width:4px;\n"
"    min-height: 4px;\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed\n"
"{\n"
"    right : 1px\n"
"}\n"
"\n"
"QSpinBox::down-button\n"
"{\n"
"    min-width: 4px;\n"
"    min-height: 4px;\n"
"}\n"
" \n"
"QSpinBox::down-button:pressed\n"
"{\n"
"    right: 1px;\n"
"}")
        self.loan_duration_spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.loan_duration_spinBox.setMaximum(999999999)

        self.horizontalLayout_24.addWidget(self.loan_duration_spinBox)


        self.verticalLayout_11.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_loans_3 = QLabel(self.page_loans)
        self.label_loans_3.setObjectName(u"label_loans_3")
        sizePolicy9.setHeightForWidth(self.label_loans_3.sizePolicy().hasHeightForWidth())
        self.label_loans_3.setSizePolicy(sizePolicy9)
        self.label_loans_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_25.addWidget(self.label_loans_3)

        self.loan_interest_doubleSpinBox = QDoubleSpinBox(self.page_loans)
        self.loan_interest_doubleSpinBox.setObjectName(u"loan_interest_doubleSpinBox")
        sizePolicy7.setHeightForWidth(self.loan_interest_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.loan_interest_doubleSpinBox.setSizePolicy(sizePolicy7)
        self.loan_interest_doubleSpinBox.setFont(font2)
        self.loan_interest_doubleSpinBox.setStyleSheet(u"QDoubleSpinBox\n"
"{\n"
"border: 1px solid; \n"
"border-radius: 5px; \n"
"background-color: white;\n"
"padding-left: 1px;\n"
"padding-top: 1px;\n"
"padding-right: 1px;\n"
"padding-bottom: 1px;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button\n"
"{\n"
"    min-width:4px;\n"
"    min-height: 4px;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button:pressed\n"
"{\n"
"    right : 1px\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button\n"
"{\n"
"    min-width: 4px;\n"
"    min-height: 4px;\n"
"}\n"
" \n"
"QDoubleSpinBox::down-button:pressed\n"
"{\n"
"    right: 1px;\n"
"}")
        self.loan_interest_doubleSpinBox.setWrapping(False)
        self.loan_interest_doubleSpinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.loan_interest_doubleSpinBox.setAccelerated(True)
        self.loan_interest_doubleSpinBox.setMaximum(9000000000000.000000000000000)

        self.horizontalLayout_25.addWidget(self.loan_interest_doubleSpinBox)


        self.verticalLayout_11.addLayout(self.horizontalLayout_25)


        self.verticalLayout_12.addLayout(self.verticalLayout_11)

        self.loan_change_pushButton = QPushButton(self.page_loans)
        self.loan_change_pushButton.setObjectName(u"loan_change_pushButton")
        self.loan_change_pushButton.setFont(font)
        self.loan_change_pushButton.setStyleSheet(u"QPushButton::pressed\n"
"{\n"
"background-color : rgb(49, 49, 49);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(71, 71, 71);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.loan_change_pushButton.setCheckable(False)
        self.loan_change_pushButton.setAutoDefault(False)
        self.loan_change_pushButton.setFlat(False)

        self.verticalLayout_12.addWidget(self.loan_change_pushButton)


        self.horizontalLayout_26.addLayout(self.verticalLayout_12)

        self.stackedWidget.addWidget(self.page_loans)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame)

        AdminMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AdminMainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.main_options__pushButton.setDefault(False)
        self.main_users_pushButton.setDefault(False)
        self.options_currencies__pushButton.setDefault(False)
        self.options_deposit__pushButton.setDefault(False)
        self.options_loans__pushButton.setDefault(False)
        self.users_stackedWidget.setCurrentIndex(3)
        self.users_accept_pushButton.setDefault(False)
        self.currency_change_pushButton.setDefault(False)
        self.deposit_change_pushButton.setDefault(False)
        self.loan_change_pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(AdminMainWindow)
    # setupUi

    def retranslateUi(self, AdminMainWindow):
        AdminMainWindow.setWindowTitle(QCoreApplication.translate("AdminMainWindow", u"Panel Administratora", None))
        self.label_main_clients.setText(QCoreApplication.translate("AdminMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Klienci:</span></p></body></html>", None))
        self.main_options__pushButton.setText(QCoreApplication.translate("AdminMainWindow", u"Opcje", None))
        self.main_users_pushButton.setText(QCoreApplication.translate("AdminMainWindow", u"Zmie\u0144 dane u\u017cytkownika", None))
        self.main_logout_pushButton.setText(QCoreApplication.translate("AdminMainWindow", u"Wyloguj si\u0119", None))
        self.label_options.setText(QCoreApplication.translate("AdminMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Opcje</span></p></body></html>", None))
        self.options_currencies__pushButton.setText(QCoreApplication.translate("AdminMainWindow", u"Waluty", None))
        self.options_deposit__pushButton.setText(QCoreApplication.translate("AdminMainWindow", u"Lokaty", None))
        self.options_loans__pushButton.setText(QCoreApplication.translate("AdminMainWindow", u"Kredyty", None))
        self.options_back_pushButton.setText(QCoreApplication.translate("AdminMainWindow", u"Powr\u00f3t", None))
        self.label_users_2.setText(QCoreApplication.translate("AdminMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Dane u\u017cytkownika</span></p></body></html>", None))
        self.label_users_4.setText(QCoreApplication.translate("AdminMainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Imi\u0119 i nazwisko</span></p></body></html>", None))
        self.label_users_5.setText(QCoreApplication.translate("AdminMainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Numer telefonu</span></p></body></html>", None))
        self.label_users_6.setText(QCoreApplication.translate("AdminMainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Has\u0142o</span></p></body></html>", None))
        self.label_users_7.setText(QCoreApplication.translate("AdminMainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Pieni\u0105dze</span></p></body></html>", None))
        self.label_users.setText(QCoreApplication.translate("AdminMainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Wybierz pole do zmiany:</span></p></body></html>", None))
        self.users_param_comboBox.setItemText(0, QCoreApplication.translate("AdminMainWindow", u"Imi\u0119 i nazwisko", None))
        self.users_param_comboBox.setItemText(1, QCoreApplication.translate("AdminMainWindow", u"Numer telefonu", None))
        self.users_param_comboBox.setItemText(2, QCoreApplication.translate("AdminMainWindow", u"Has\u0142o", None))
        self.users_param_comboBox.setItemText(3, QCoreApplication.translate("AdminMainWindow", u"Pieni\u0105dze", None))

        self.label_users_19.setText(QCoreApplication.translate("AdminMainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Nowe imi\u0119 i nazwisko</span></p></body></html>", None))
        self.label_users_20.setText(QCoreApplication.translate("AdminMainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Nowy numer telefonu</span></p></body></html>", None))
        self.label_users_21.setText(QCoreApplication.translate("AdminMainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Nowe has\u0142o</span></p></body></html>", None))
        self.label_users_22.setText(QCoreApplication.translate("AdminMainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Nowa warto\u015b\u0107 pieni\u0119dzy</span></p></body></html>", None))
        self.users_accept_pushButton.setText(QCoreApplication.translate("AdminMainWindow", u"Zatwierd\u017a", None))
        self.users_back_pushButton.setText(QCoreApplication.translate("AdminMainWindow", u"Powr\u00f3t", None))
        self.label_currencies.setText(QCoreApplication.translate("AdminMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Waluty</span></p></body></html>", None))
        self.currencies_back_pushButton.setText(QCoreApplication.translate("AdminMainWindow", u"Powr\u00f3t", None))
        self.label_currencies_2.setText(QCoreApplication.translate("AdminMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Waluta do zmiany</span></p></body></html>", None))
        self.label_currencies_3.setText(QCoreApplication.translate("AdminMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Kurs kupna</span></p></body></html>", None))
        self.label_currencies_4.setText(QCoreApplication.translate("AdminMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Kurs sprzeda\u017cy</span></p></body></html>", None))
        self.currency_change_pushButton.setText(QCoreApplication.translate("AdminMainWindow", u"Zatwierd\u017a", None))
        self.label_deposits.setText(QCoreApplication.translate("AdminMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Lokaty</span></p></body></html>", None))
        self.deposits_back_pushButton_2.setText(QCoreApplication.translate("AdminMainWindow", u"Powr\u00f3t", None))
        self.label_deposits_2.setText(QCoreApplication.translate("AdminMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">D\u0142ugo\u015b\u0107 lokaty</span></p></body></html>", None))
        self.label_deposits_3.setText(QCoreApplication.translate("AdminMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Odsetki</span></p></body></html>", None))
        self.deposit_change_pushButton.setText(QCoreApplication.translate("AdminMainWindow", u"Zatwierd\u017a", None))
        self.label_loans.setText(QCoreApplication.translate("AdminMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Kredyty</span></p></body></html>", None))
        self.loans_back_pushButton.setText(QCoreApplication.translate("AdminMainWindow", u"Powr\u00f3t", None))
        self.label_loans_2.setText(QCoreApplication.translate("AdminMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">D\u0142ugo\u015b\u0107 kredytu</span></p></body></html>", None))
        self.label_loans_3.setText(QCoreApplication.translate("AdminMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Odsetki</span></p></body></html>", None))
        self.loan_change_pushButton.setText(QCoreApplication.translate("AdminMainWindow", u"Zatwierd\u017a", None))
    # retranslateUi

