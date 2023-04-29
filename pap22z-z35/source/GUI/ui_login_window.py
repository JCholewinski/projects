# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(609, 466)
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame\n"
"{\n"
"background-color: rgb(93, 93, 93);\n"
"color:  rgb(255, 255, 255);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.LoginStackedWidget = QStackedWidget(self.frame)
        self.LoginStackedWidget.setObjectName(u"LoginStackedWidget")
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.horizontalLayout_19 = QHBoxLayout(self.page_login)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.log_fake_pushButton = QPushButton(self.page_login)
        self.log_fake_pushButton.setObjectName(u"log_fake_pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.log_fake_pushButton.sizePolicy().hasHeightForWidth())
        self.log_fake_pushButton.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        self.log_fake_pushButton.setFont(font)
        self.log_fake_pushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: rgb(93, 93, 93);\n"
"color: rgb(93, 93, 93);\n"
"border: 2px rgb(93, 93, 93);\n"
"border-radius: 10px;\n"
"}\n"
"")

        self.horizontalLayout_18.addWidget(self.log_fake_pushButton)

        self.label_login = QLabel(self.page_login)
        self.label_login.setObjectName(u"label_login")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_login.sizePolicy().hasHeightForWidth())
        self.label_login.setSizePolicy(sizePolicy1)
        self.label_login.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout_18.addWidget(self.label_login)

        self.log_to_reg_pushButton = QPushButton(self.page_login)
        self.log_to_reg_pushButton.setObjectName(u"log_to_reg_pushButton")
        sizePolicy.setHeightForWidth(self.log_to_reg_pushButton.sizePolicy().hasHeightForWidth())
        self.log_to_reg_pushButton.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(14)
        self.log_to_reg_pushButton.setFont(font1)
        self.log_to_reg_pushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: rgb(93, 93, 93);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-radius: 5px;\n"
"padding-top: 2px;\n"
"padding-bottom: 2px;\n"
"padding-left: 2px;\n"
"padding-right: 2px;\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color : rgb(71, 71, 71);\n"
"}")

        self.horizontalLayout_18.addWidget(self.log_to_reg_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_18)

        self.label_log_naccount = QLabel(self.page_login)
        self.label_log_naccount.setObjectName(u"label_log_naccount")
        sizePolicy1.setHeightForWidth(self.label_log_naccount.sizePolicy().hasHeightForWidth())
        self.label_log_naccount.setSizePolicy(sizePolicy1)
        self.label_log_naccount.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout.addWidget(self.label_log_naccount)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_naccount = QLineEdit(self.page_login)
        self.lineEdit_naccount.setObjectName(u"lineEdit_naccount")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_naccount.sizePolicy().hasHeightForWidth())
        self.lineEdit_naccount.setSizePolicy(sizePolicy2)
        self.lineEdit_naccount.setFont(font1)
        self.lineEdit_naccount.setStyleSheet(u"QLineEdit\n"
"{\n"
"border: 1px solid; \n"
"border-radius: 4px; \n"
"background-color: white;\n"
"padding-left: 1px;\n"
"padding-top: 1px;\n"
"padding-right: 1px;\n"
"padding-bottom: 1px;\n"
"}")

        self.horizontalLayout.addWidget(self.lineEdit_naccount)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_log_password = QLabel(self.page_login)
        self.label_log_password.setObjectName(u"label_log_password")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_log_password.sizePolicy().hasHeightForWidth())
        self.label_log_password.setSizePolicy(sizePolicy3)
        self.label_log_password.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout.addWidget(self.label_log_password)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_password = QLineEdit(self.page_login)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setFont(font1)
        self.lineEdit_password.setStyleSheet(u"QLineEdit\n"
"{\n"
"border: 1px solid; \n"
"border-radius: 4px; \n"
"background-color: white;\n"
"padding-left: 1px;\n"
"padding-top: 1px;\n"
"padding-right: 1px;\n"
"padding-bottom: 1px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.lineEdit_password)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.Login_pushButton = QPushButton(self.page_login)
        self.Login_pushButton.setObjectName(u"Login_pushButton")
        font2 = QFont()
        font2.setPointSize(20)
        self.Login_pushButton.setFont(font2)
        self.Login_pushButton.setStyleSheet(u"QPushButton::pressed\n"
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
        self.Login_pushButton.setCheckable(False)
        self.Login_pushButton.setAutoDefault(False)
        self.Login_pushButton.setFlat(False)

        self.verticalLayout.addWidget(self.Login_pushButton)


        self.horizontalLayout_19.addLayout(self.verticalLayout)

        self.LoginStackedWidget.addWidget(self.page_login)
        self.page_register = QWidget()
        self.page_register.setObjectName(u"page_register")
        self.horizontalLayout_10 = QHBoxLayout(self.page_register)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.reg_fake_pushButton = QPushButton(self.page_register)
        self.reg_fake_pushButton.setObjectName(u"reg_fake_pushButton")
        self.reg_fake_pushButton.setFont(font)
        self.reg_fake_pushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: rgb(93, 93, 93);\n"
"color: rgb(93, 93, 93);\n"
"border: 2px rgb(93, 93, 93);\n"
"border-radius: 10px;\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.reg_fake_pushButton)

        self.label_login_2 = QLabel(self.page_register)
        self.label_login_2.setObjectName(u"label_login_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_login_2.sizePolicy().hasHeightForWidth())
        self.label_login_2.setSizePolicy(sizePolicy4)
        self.label_login_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout_9.addWidget(self.label_login_2)

        self.reg_to_log_pushButton = QPushButton(self.page_register)
        self.reg_to_log_pushButton.setObjectName(u"reg_to_log_pushButton")
        self.reg_to_log_pushButton.setFont(font1)
        self.reg_to_log_pushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: rgb(93, 93, 93);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-radius: 5px;\n"
"padding-top: 2px;\n"
"padding-bottom: 2px;\n"
"padding-left: 2px;\n"
"padding-right: 2px;\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color : rgb(71, 71, 71);\n"
"}")

        self.horizontalLayout_9.addWidget(self.reg_to_log_pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.label_reg_name = QLabel(self.page_register)
        self.label_reg_name.setObjectName(u"label_reg_name")
        sizePolicy1.setHeightForWidth(self.label_reg_name.sizePolicy().hasHeightForWidth())
        self.label_reg_name.setSizePolicy(sizePolicy1)
        self.label_reg_name.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_2.addWidget(self.label_reg_name)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.reg_name_lineEdit = QLineEdit(self.page_register)
        self.reg_name_lineEdit.setObjectName(u"reg_name_lineEdit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.reg_name_lineEdit.sizePolicy().hasHeightForWidth())
        self.reg_name_lineEdit.setSizePolicy(sizePolicy5)
        self.reg_name_lineEdit.setFont(font1)
        self.reg_name_lineEdit.setStyleSheet(u"QLineEdit\n"
"{\n"
"border: 1px solid; \n"
"border-radius: 4px; \n"
"background-color: white;\n"
"padding-left: 1px;\n"
"padding-top: 1px;\n"
"padding-right: 1px;\n"
"padding-bottom: 1px;\n"
"}")
        self.reg_name_lineEdit.setClearButtonEnabled(True)

        self.horizontalLayout_5.addWidget(self.reg_name_lineEdit)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.label_reg_surname = QLabel(self.page_register)
        self.label_reg_surname.setObjectName(u"label_reg_surname")
        sizePolicy1.setHeightForWidth(self.label_reg_surname.sizePolicy().hasHeightForWidth())
        self.label_reg_surname.setSizePolicy(sizePolicy1)
        self.label_reg_surname.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_2.addWidget(self.label_reg_surname)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.reg_surname_lineEdit = QLineEdit(self.page_register)
        self.reg_surname_lineEdit.setObjectName(u"reg_surname_lineEdit")
        self.reg_surname_lineEdit.setFont(font1)
        self.reg_surname_lineEdit.setStyleSheet(u"QLineEdit\n"
"{\n"
"border: 1px solid; \n"
"border-radius: 4px; \n"
"background-color: white;\n"
"padding-left: 1px;\n"
"padding-top: 1px;\n"
"padding-right: 1px;\n"
"padding-bottom: 1px;\n"
"}")
        self.reg_surname_lineEdit.setClearButtonEnabled(True)

        self.horizontalLayout_6.addWidget(self.reg_surname_lineEdit)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.label_reg_phone_num = QLabel(self.page_register)
        self.label_reg_phone_num.setObjectName(u"label_reg_phone_num")
        sizePolicy1.setHeightForWidth(self.label_reg_phone_num.sizePolicy().hasHeightForWidth())
        self.label_reg_phone_num.setSizePolicy(sizePolicy1)
        self.label_reg_phone_num.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_2.addWidget(self.label_reg_phone_num)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.reg_phone_lineEdit = QLineEdit(self.page_register)
        self.reg_phone_lineEdit.setObjectName(u"reg_phone_lineEdit")
        self.reg_phone_lineEdit.setFont(font1)
        self.reg_phone_lineEdit.setStyleSheet(u"QLineEdit\n"
"{\n"
"border: 1px solid; \n"
"border-radius: 4px; \n"
"background-color: white;\n"
"padding-left: 1px;\n"
"padding-top: 1px;\n"
"padding-right: 1px;\n"
"padding-bottom: 1px;\n"
"}")
        self.reg_phone_lineEdit.setClearButtonEnabled(True)

        self.horizontalLayout_7.addWidget(self.reg_phone_lineEdit)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.label_reg_password = QLabel(self.page_register)
        self.label_reg_password.setObjectName(u"label_reg_password")
        sizePolicy1.setHeightForWidth(self.label_reg_password.sizePolicy().hasHeightForWidth())
        self.label_reg_password.setSizePolicy(sizePolicy1)
        self.label_reg_password.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_2.addWidget(self.label_reg_password)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.reg_password_lineEdit = QLineEdit(self.page_register)
        self.reg_password_lineEdit.setObjectName(u"reg_password_lineEdit")
        self.reg_password_lineEdit.setFont(font1)
        self.reg_password_lineEdit.setStyleSheet(u"QLineEdit\n"
"{\n"
"border: 1px solid; \n"
"border-radius: 4px; \n"
"background-color: white;\n"
"padding-left: 1px;\n"
"padding-top: 1px;\n"
"padding-right: 1px;\n"
"padding-bottom: 1px;\n"
"}")
        self.reg_password_lineEdit.setClearButtonEnabled(True)

        self.horizontalLayout_8.addWidget(self.reg_password_lineEdit)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.Register_pushButton = QPushButton(self.page_register)
        self.Register_pushButton.setObjectName(u"Register_pushButton")
        self.Register_pushButton.setFont(font2)
        self.Register_pushButton.setStyleSheet(u"QPushButton::pressed\n"
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
        self.Register_pushButton.setCheckable(False)
        self.Register_pushButton.setAutoDefault(False)
        self.Register_pushButton.setFlat(False)

        self.verticalLayout_2.addWidget(self.Register_pushButton)


        self.horizontalLayout_10.addLayout(self.verticalLayout_2)

        self.LoginStackedWidget.addWidget(self.page_register)

        self.horizontalLayout_3.addWidget(self.LoginStackedWidget)


        self.verticalLayout_3.addWidget(self.frame)

        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)

        self.LoginStackedWidget.setCurrentIndex(1)
        self.Login_pushButton.setDefault(False)
        self.Register_pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Logowanie", None))
        self.log_fake_pushButton.setText(QCoreApplication.translate("LoginWindow", u"logowanie", None))
        self.label_login.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Logowanie</span></p></body></html>", None))
        self.log_to_reg_pushButton.setText(QCoreApplication.translate("LoginWindow", u"Rejestracja", None))
        self.label_log_naccount.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Numer Konta:</span></p></body></html>", None))
        self.label_log_password.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Has\u0142o:</span></p></body></html>", None))
        self.Login_pushButton.setText(QCoreApplication.translate("LoginWindow", u"Zaloguj si\u0119", None))
        self.reg_fake_pushButton.setText(QCoreApplication.translate("LoginWindow", u"logowanie", None))
        self.label_login_2.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Rejestracja</span></p></body></html>", None))
        self.reg_to_log_pushButton.setText(QCoreApplication.translate("LoginWindow", u"Logowanie", None))
        self.label_reg_name.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Imi\u0119:</span></p></body></html>", None))
        self.label_reg_surname.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Nazwisko:</span></p></body></html>", None))
        self.label_reg_phone_num.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Numer telefonu:</span></p></body></html>", None))
        self.label_reg_password.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Has\u0142o:</span></p></body></html>", None))
        self.Register_pushButton.setText(QCoreApplication.translate("LoginWindow", u"Zarejestruj si\u0119", None))
    # retranslateUi

