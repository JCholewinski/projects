# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_window_backup.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

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
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_login = QLabel(self.frame)
        self.label_login.setObjectName(u"label_login")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_login.sizePolicy().hasHeightForWidth())
        self.label_login.setSizePolicy(sizePolicy)
        self.label_login.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout.addWidget(self.label_login)

        self.label_log_naccount = QLabel(self.frame)
        self.label_log_naccount.setObjectName(u"label_log_naccount")
        sizePolicy.setHeightForWidth(self.label_log_naccount.sizePolicy().hasHeightForWidth())
        self.label_log_naccount.setSizePolicy(sizePolicy)
        self.label_log_naccount.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout.addWidget(self.label_log_naccount)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_naccount = QLineEdit(self.frame)
        self.lineEdit_naccount.setObjectName(u"lineEdit_naccount")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_naccount.sizePolicy().hasHeightForWidth())
        self.lineEdit_naccount.setSizePolicy(sizePolicy1)
        self.lineEdit_naccount.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.lineEdit_naccount)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_log_password = QLabel(self.frame)
        self.label_log_password.setObjectName(u"label_log_password")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_log_password.sizePolicy().hasHeightForWidth())
        self.label_log_password.setSizePolicy(sizePolicy2)
        self.label_log_password.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout.addWidget(self.label_log_password)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_password = QLineEdit(self.frame)
        self.lineEdit_password.setObjectName(u"lineEdit_password")

        self.horizontalLayout_2.addWidget(self.lineEdit_password)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.Login_pushButton = QPushButton(self.frame)
        self.Login_pushButton.setObjectName(u"Login_pushButton")
        font = QFont()
        font.setPointSize(20)
        self.Login_pushButton.setFont(font)
        self.Login_pushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: rgb(71, 71, 71);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}")
        self.Login_pushButton.setCheckable(False)
        self.Login_pushButton.setAutoDefault(False)
        self.Login_pushButton.setFlat(False)

        self.verticalLayout.addWidget(self.Login_pushButton)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_3.addWidget(self.frame)

        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)

        self.Login_pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"MainWindow", None))
        self.label_login.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Logowanie:</span></p></body></html>", None))
        self.label_log_naccount.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Numer Konta:</span></p></body></html>", None))
        self.label_log_password.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Has\u0142o:</span></p></body></html>", None))
        self.Login_pushButton.setText(QCoreApplication.translate("LoginWindow", u"Zaloguj si\u0119", None))
    # retranslateUi

