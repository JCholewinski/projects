# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'client_window_backup.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QTextBrowser,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_ClientMainWindow(object):
    def setupUi(self, ClientMainWindow):
        if not ClientMainWindow.objectName():
            ClientMainWindow.setObjectName(u"ClientMainWindow")
        ClientMainWindow.resize(652, 447)
        ClientMainWindow.setStyleSheet(u"QMainWindow{\n"
"	border-radius: 20px;\n"
"}")
        self.actionOptions = QAction(ClientMainWindow)
        self.actionOptions.setObjectName(u"actionOptions")
        self.actionHistory = QAction(ClientMainWindow)
        self.actionHistory.setObjectName(u"actionHistory")
        self.actionNew_transfer = QAction(ClientMainWindow)
        self.actionNew_transfer.setObjectName(u"actionNew_transfer")
        self.actionMain_pulpit = QAction(ClientMainWindow)
        self.actionMain_pulpit.setObjectName(u"actionMain_pulpit")
        self.centralwidget = QWidget(ClientMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_11 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame\n"
"{\n"
"background-color: rgb(167, 202, 255);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(10, 10, 10, 10)
        self.ClientStackedWidget = QStackedWidget(self.frame)
        self.ClientStackedWidget.setObjectName(u"ClientStackedWidget")
        self.page_main = QWidget()
        self.page_main.setObjectName(u"page_main")
        self.horizontalLayout_2 = QHBoxLayout(self.page_main)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_available_funds = QLabel(self.page_main)
        self.label_available_funds.setObjectName(u"label_available_funds")

        self.verticalLayout.addWidget(self.label_available_funds)

        self.Money_num_label = QLabel(self.page_main)
        self.Money_num_label.setObjectName(u"Money_num_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Money_num_label.sizePolicy().hasHeightForWidth())
        self.Money_num_label.setSizePolicy(sizePolicy)
        self.Money_num_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.Money_num_label)

        self.transfer_pushButton = QPushButton(self.page_main)
        self.transfer_pushButton.setObjectName(u"transfer_pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.transfer_pushButton.sizePolicy().hasHeightForWidth())
        self.transfer_pushButton.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(22)
        self.transfer_pushButton.setFont(font)
        self.transfer_pushButton.setStyleSheet(u"QPushButton::pressed\n"
"{\n"
"background-color : rgb(22, 22, 91);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(33, 33, 132);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding-top: 2px;\n"
"padding-bottom: 2px;\n"
"padding-left: 2px;\n"
"padding-right: 2px;\n"
"}")
        self.transfer_pushButton.setAutoDefault(False)

        self.verticalLayout.addWidget(self.transfer_pushButton)


        self.verticalLayout_8.addLayout(self.verticalLayout)

        self.label_3 = QLabel(self.page_main)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_8.addWidget(self.label_3)

        self.last_operations_textBrowser = QTextBrowser(self.page_main)
        self.last_operations_textBrowser.setObjectName(u"last_operations_textBrowser")
        sizePolicy2.setHeightForWidth(self.last_operations_textBrowser.sizePolicy().hasHeightForWidth())
        self.last_operations_textBrowser.setSizePolicy(sizePolicy2)

        self.verticalLayout_8.addWidget(self.last_operations_textBrowser)


        self.horizontalLayout.addLayout(self.verticalLayout_8)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.options_pushButton = QPushButton(self.page_main)
        self.options_pushButton.setObjectName(u"options_pushButton")
        sizePolicy1.setHeightForWidth(self.options_pushButton.sizePolicy().hasHeightForWidth())
        self.options_pushButton.setSizePolicy(sizePolicy1)
        self.options_pushButton.setFont(font)
        self.options_pushButton.setStyleSheet(u"QPushButton::pressed\n"
"{\n"
"background-color : rgb(22, 22, 91);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(33, 33, 132);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}")
        self.options_pushButton.setAutoDefault(False)

        self.verticalLayout_2.addWidget(self.options_pushButton)

        self.history_pushButton = QPushButton(self.page_main)
        self.history_pushButton.setObjectName(u"history_pushButton")
        sizePolicy1.setHeightForWidth(self.history_pushButton.sizePolicy().hasHeightForWidth())
        self.history_pushButton.setSizePolicy(sizePolicy1)
        self.history_pushButton.setFont(font)
        self.history_pushButton.setStyleSheet(u"QPushButton::pressed\n"
"{\n"
"background-color : rgb(22, 22, 91);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(33, 33, 132);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}")

        self.verticalLayout_2.addWidget(self.history_pushButton)

        self.logout_pushButton = QPushButton(self.page_main)
        self.logout_pushButton.setObjectName(u"logout_pushButton")
        font1 = QFont()
        font1.setPointSize(12)
        self.logout_pushButton.setFont(font1)
        self.logout_pushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: rgb(167, 202, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-radius: 10px;\n"
"padding-top: 2px;\n"
"padding-bottom: 2px;\n"
"padding-left: 2px;\n"
"padding-right: 2px;\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color : rgb(132, 160, 202);\n"
"}")

        self.verticalLayout_2.addWidget(self.logout_pushButton)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.ClientStackedWidget.addWidget(self.page_main)
        self.page_options = QWidget()
        self.page_options.setObjectName(u"page_options")
        self.horizontalLayout_5 = QHBoxLayout(self.page_options)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_options = QLabel(self.page_options)
        self.label_options.setObjectName(u"label_options")
        sizePolicy2.setHeightForWidth(self.label_options.sizePolicy().hasHeightForWidth())
        self.label_options.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(20)
        self.label_options.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_options)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.options_currency_pushButton = QPushButton(self.page_options)
        self.options_currency_pushButton.setObjectName(u"options_currency_pushButton")
        sizePolicy1.setHeightForWidth(self.options_currency_pushButton.sizePolicy().hasHeightForWidth())
        self.options_currency_pushButton.setSizePolicy(sizePolicy1)
        self.options_currency_pushButton.setFont(font2)
        self.options_currency_pushButton.setStyleSheet(u"QPushButton::pressed\n"
"{\n"
"background-color : rgb(22, 22, 91);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(33, 33, 132);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding-top: 2px;\n"
"padding-bottom: 2px;\n"
"padding-left: 2px;\n"
"padding-right: 2px;\n"
"}")

        self.gridLayout.addWidget(self.options_currency_pushButton, 0, 0, 1, 1)

        self.options_deposit_pushButton = QPushButton(self.page_options)
        self.options_deposit_pushButton.setObjectName(u"options_deposit_pushButton")
        sizePolicy1.setHeightForWidth(self.options_deposit_pushButton.sizePolicy().hasHeightForWidth())
        self.options_deposit_pushButton.setSizePolicy(sizePolicy1)
        self.options_deposit_pushButton.setFont(font2)
        self.options_deposit_pushButton.setStyleSheet(u"QPushButton::pressed\n"
"{\n"
"background-color : rgb(22, 22, 91);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(33, 33, 132);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding-top: 2px;\n"
"padding-bottom: 2px;\n"
"padding-left: 2px;\n"
"padding-right: 2px;\n"
"}")

        self.gridLayout.addWidget(self.options_deposit_pushButton, 0, 1, 1, 1)

        self.options_goals_pushButton = QPushButton(self.page_options)
        self.options_goals_pushButton.setObjectName(u"options_goals_pushButton")
        sizePolicy1.setHeightForWidth(self.options_goals_pushButton.sizePolicy().hasHeightForWidth())
        self.options_goals_pushButton.setSizePolicy(sizePolicy1)
        self.options_goals_pushButton.setFont(font2)
        self.options_goals_pushButton.setStyleSheet(u"QPushButton::pressed\n"
"{\n"
"background-color : rgb(22, 22, 91);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(33, 33, 132);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding-top: 2px;\n"
"padding-bottom: 2px;\n"
"padding-left: 2px;\n"
"padding-right: 2px;\n"
"}")

        self.gridLayout.addWidget(self.options_goals_pushButton, 1, 1, 1, 1)

        self.options_loan_pushButton = QPushButton(self.page_options)
        self.options_loan_pushButton.setObjectName(u"options_loan_pushButton")
        sizePolicy1.setHeightForWidth(self.options_loan_pushButton.sizePolicy().hasHeightForWidth())
        self.options_loan_pushButton.setSizePolicy(sizePolicy1)
        self.options_loan_pushButton.setFont(font2)
        self.options_loan_pushButton.setStyleSheet(u"QPushButton::pressed\n"
"{\n"
"background-color : rgb(22, 22, 91);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(33, 33, 132);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding-top: 2px;\n"
"padding-bottom: 2px;\n"
"padding-left: 2px;\n"
"padding-right: 2px;\n"
"}")

        self.gridLayout.addWidget(self.options_loan_pushButton, 1, 0, 1, 1)

        self.options_currencyAccount_pushButton = QPushButton(self.page_options)
        self.options_currencyAccount_pushButton.setObjectName(u"options_currencyAccount_pushButton")
        sizePolicy1.setHeightForWidth(self.options_currencyAccount_pushButton.sizePolicy().hasHeightForWidth())
        self.options_currencyAccount_pushButton.setSizePolicy(sizePolicy1)
        self.options_currencyAccount_pushButton.setFont(font2)
        self.options_currencyAccount_pushButton.setStyleSheet(u"QPushButton::pressed\n"
"{\n"
"background-color : rgb(22, 22, 91);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(33, 33, 132);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding-top: 2px;\n"
"padding-bottom: 2px;\n"
"padding-left: 2px;\n"
"padding-right: 2px;\n"
"}")

        self.gridLayout.addWidget(self.options_currencyAccount_pushButton, 2, 0, 1, 1)

        self.options_back_pushButton = QPushButton(self.page_options)
        self.options_back_pushButton.setObjectName(u"options_back_pushButton")
        sizePolicy1.setHeightForWidth(self.options_back_pushButton.sizePolicy().hasHeightForWidth())
        self.options_back_pushButton.setSizePolicy(sizePolicy1)
        self.options_back_pushButton.setFont(font2)
        self.options_back_pushButton.setStyleSheet(u"QPushButton::pressed\n"
"{\n"
"background-color : rgb(132, 160, 202);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(167, 202, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-radius: 10px;\n"
"padding-top: 2px;\n"
"padding-bottom: 2px;\n"
"padding-left: 2px;\n"
"padding-right: 2px;\n"
"}")

        self.gridLayout.addWidget(self.options_back_pushButton, 2, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.ClientStackedWidget.addWidget(self.page_options)
        self.page_history = QWidget()
        self.page_history.setObjectName(u"page_history")
        self.horizontalLayout_6 = QHBoxLayout(self.page_history)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_history = QLabel(self.page_history)
        self.label_history.setObjectName(u"label_history")

        self.horizontalLayout_4.addWidget(self.label_history)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.history_back_pushButton = QPushButton(self.page_history)
        self.history_back_pushButton.setObjectName(u"history_back_pushButton")
        self.history_back_pushButton.setFont(font1)
        self.history_back_pushButton.setStyleSheet(u"QPushButton::pressed\n"
"{\n"
"background-color : rgb(132, 160, 202);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(167, 202, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-radius: 10px;\n"
"padding-top: 2px;\n"
"padding-bottom: 2px;\n"
"padding-left: 2px;\n"
"padding-right: 2px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.history_back_pushButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.history_textEdit = QTextEdit(self.page_history)
        self.history_textEdit.setObjectName(u"history_textEdit")
        self.history_textEdit.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.history_textEdit)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.ClientStackedWidget.addWidget(self.page_history)
        self.page_new_transfer = QWidget()
        self.page_new_transfer.setObjectName(u"page_new_transfer")
        self.horizontalLayout_25 = QHBoxLayout(self.page_new_transfer)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_new_transfer = QLabel(self.page_new_transfer)
        self.label_new_transfer.setObjectName(u"label_new_transfer")

        self.horizontalLayout_7.addWidget(self.label_new_transfer)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.transfer_back_pushButton = QPushButton(self.page_new_transfer)
        self.transfer_back_pushButton.setObjectName(u"transfer_back_pushButton")
        self.transfer_back_pushButton.setFont(font1)
        self.transfer_back_pushButton.setStyleSheet(u"QPushButton::pressed\n"
"{\n"
"background-color : rgb(132, 160, 202);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(167, 202, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-radius: 10px;\n"
"padding-top: 2px;\n"
"padding-bottom: 2px;\n"
"padding-left: 2px;\n"
"padding-right: 2px;\n"
"}")

        self.horizontalLayout_7.addWidget(self.transfer_back_pushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_transfer_title = QLabel(self.page_new_transfer)
        self.label_transfer_title.setObjectName(u"label_transfer_title")
        font3 = QFont()
        font3.setPointSize(18)
        self.label_transfer_title.setFont(font3)

        self.horizontalLayout_8.addWidget(self.label_transfer_title)

        self.transfer_title_lineEdit = QLineEdit(self.page_new_transfer)
        self.transfer_title_lineEdit.setObjectName(u"transfer_title_lineEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.transfer_title_lineEdit.sizePolicy().hasHeightForWidth())
        self.transfer_title_lineEdit.setSizePolicy(sizePolicy3)
        self.transfer_title_lineEdit.setStyleSheet(u"QLineEdit\n"
"{\n"
"border: 1px solid; \n"
"border-radius: 4px; \n"
"background-color: white;\n"
"padding-left: 1px;\n"
"padding-top: 1px;\n"
"padding-right: 1px;\n"
"padding-bottom: 1px;\n"
"}")
        self.transfer_title_lineEdit.setClearButtonEnabled(True)

        self.horizontalLayout_8.addWidget(self.transfer_title_lineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_account_num = QLabel(self.page_new_transfer)
        self.label_account_num.setObjectName(u"label_account_num")
        self.label_account_num.setFont(font3)

        self.horizontalLayout_9.addWidget(self.label_account_num)

        self.transfer_naccount_lineEdit = QLineEdit(self.page_new_transfer)
        self.transfer_naccount_lineEdit.setObjectName(u"transfer_naccount_lineEdit")
        sizePolicy3.setHeightForWidth(self.transfer_naccount_lineEdit.sizePolicy().hasHeightForWidth())
        self.transfer_naccount_lineEdit.setSizePolicy(sizePolicy3)
        self.transfer_naccount_lineEdit.setStyleSheet(u"QLineEdit\n"
"{\n"
"border: 1px solid; \n"
"border-radius: 4px; \n"
"background-color: white;\n"
"padding-left: 1px;\n"
"padding-top: 1px;\n"
"padding-right: 1px;\n"
"padding-bottom: 1px;\n"
"}")
        self.transfer_naccount_lineEdit.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.transfer_naccount_lineEdit.setClearButtonEnabled(True)

        self.horizontalLayout_9.addWidget(self.transfer_naccount_lineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_new_transfer_2 = QLabel(self.page_new_transfer)
        self.label_new_transfer_2.setObjectName(u"label_new_transfer_2")

        self.horizontalLayout_10.addWidget(self.label_new_transfer_2)

        self.new_transfer_money_label = QLabel(self.page_new_transfer)
        self.new_transfer_money_label.setObjectName(u"new_transfer_money_label")
        sizePolicy2.setHeightForWidth(self.new_transfer_money_label.sizePolicy().hasHeightForWidth())
        self.new_transfer_money_label.setSizePolicy(sizePolicy2)
        self.new_transfer_money_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.new_transfer_money_label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_value = QLabel(self.page_new_transfer)
        self.label_value.setObjectName(u"label_value")
        sizePolicy.setHeightForWidth(self.label_value.sizePolicy().hasHeightForWidth())
        self.label_value.setSizePolicy(sizePolicy)
        self.label_value.setFont(font3)

        self.horizontalLayout_12.addWidget(self.label_value)

        self.new_transfer_doubleSpinBox = QDoubleSpinBox(self.page_new_transfer)
        self.new_transfer_doubleSpinBox.setObjectName(u"new_transfer_doubleSpinBox")
        sizePolicy3.setHeightForWidth(self.new_transfer_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.new_transfer_doubleSpinBox.setSizePolicy(sizePolicy3)
        self.new_transfer_doubleSpinBox.setStyleSheet(u"QDoubleSpinBox\n"
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
        self.new_transfer_doubleSpinBox.setWrapping(False)
        self.new_transfer_doubleSpinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.new_transfer_doubleSpinBox.setAccelerated(True)
        self.new_transfer_doubleSpinBox.setMaximum(9000000000000.000000000000000)

        self.horizontalLayout_12.addWidget(self.new_transfer_doubleSpinBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.transfer_go_pushButton = QPushButton(self.page_new_transfer)
        self.transfer_go_pushButton.setObjectName(u"transfer_go_pushButton")
        self.transfer_go_pushButton.setFont(font3)
        self.transfer_go_pushButton.setStyleSheet(u"QPushButton::pressed\n"
"{\n"
"background-color : rgb(22, 22, 91);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(33, 33, 132);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding-top: 2px;\n"
"padding-bottom: 2px;\n"
"padding-left: 2px;\n"
"padding-right: 2px;\n"
"}")

        self.verticalLayout_3.addWidget(self.transfer_go_pushButton)


        self.horizontalLayout_25.addLayout(self.verticalLayout_3)

        self.ClientStackedWidget.addWidget(self.page_new_transfer)
        self.page_currency = QWidget()
        self.page_currency.setObjectName(u"page_currency")
        self.horizontalLayout_15 = QHBoxLayout(self.page_currency)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_currency = QLabel(self.page_currency)
        self.label_currency.setObjectName(u"label_currency")

        self.horizontalLayout_14.addWidget(self.label_currency)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_6)

        self.currency_back_pushButton = QPushButton(self.page_currency)
        self.currency_back_pushButton.setObjectName(u"currency_back_pushButton")
        self.currency_back_pushButton.setFont(font1)
        self.currency_back_pushButton.setStyleSheet(u"QPushButton::pressed\n"
"{\n"
"background-color : rgb(132, 160, 202);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(167, 202, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-radius: 10px;\n"
"padding-top: 2px;\n"
"padding-bottom: 2px;\n"
"padding-left: 2px;\n"
"padding-right: 2px;\n"
"}")

        self.horizontalLayout_14.addWidget(self.currency_back_pushButton)


        self.verticalLayout_6.addLayout(self.horizontalLayout_14)

        self.currencies_textEdit = QTextEdit(self.page_currency)
        self.currencies_textEdit.setObjectName(u"currencies_textEdit")
        self.currencies_textEdit.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.currencies_textEdit)


        self.horizontalLayout_15.addLayout(self.verticalLayout_6)

        self.ClientStackedWidget.addWidget(self.page_currency)
        self.page_deposit = QWidget()
        self.page_deposit.setObjectName(u"page_deposit")
        self.horizontalLayout_34 = QHBoxLayout(self.page_deposit)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_deposit = QLabel(self.page_deposit)
        self.label_deposit.setObjectName(u"label_deposit")

        self.horizontalLayout_32.addWidget(self.label_deposit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_2)

        self.deposit_back_pushButton = QPushButton(self.page_deposit)
        self.deposit_back_pushButton.setObjectName(u"deposit_back_pushButton")
        self.deposit_back_pushButton.setFont(font1)
        self.deposit_back_pushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: rgb(167, 202, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-radius: 10px;\n"
"padding-top: 2px;\n"
"padding-bottom: 2px;\n"
"padding-left: 2px;\n"
"padding-right: 2px;\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color : rgb(132, 160, 202);\n"
"}\n"
"")

        self.horizontalLayout_32.addWidget(self.deposit_back_pushButton)


        self.verticalLayout_12.addLayout(self.horizontalLayout_32)

        self.deposit_listWidget = QListWidget(self.page_deposit)
        self.deposit_listWidget.setObjectName(u"deposit_listWidget")

        self.verticalLayout_12.addWidget(self.deposit_listWidget)

        self.deposit_textEdit = QTextEdit(self.page_deposit)
        self.deposit_textEdit.setObjectName(u"deposit_textEdit")
        self.deposit_textEdit.setReadOnly(True)

        self.verticalLayout_12.addWidget(self.deposit_textEdit)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.go_to_new_deposit_pushButton = QPushButton(self.page_deposit)
        self.go_to_new_deposit_pushButton.setObjectName(u"go_to_new_deposit_pushButton")
        font4 = QFont()
        font4.setPointSize(14)
        self.go_to_new_deposit_pushButton.setFont(font4)
        self.go_to_new_deposit_pushButton.setStyleSheet(u"QPushButton::pressed\n"
"{\n"
"background-color : rgb(22, 22, 91);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(33, 33, 132);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding-top: 2px;\n"
"padding-bottom: 2px;\n"
"padding-left: 2px;\n"
"padding-right: 2px;\n"
"}")

        self.horizontalLayout_33.addWidget(self.go_to_new_deposit_pushButton)

        self.go_to_sell_deposit_pushButton = QPushButton(self.page_deposit)
        self.go_to_sell_deposit_pushButton.setObjectName(u"go_to_sell_deposit_pushButton")
        self.go_to_sell_deposit_pushButton.setFont(font4)
        self.go_to_sell_deposit_pushButton.setStyleSheet(u"QPushButton::pressed\n"
"{\n"
"background-color : rgb(22, 22, 91);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(33, 33, 132);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding-top: 2px;\n"
"padding-bottom: 2px;\n"
"padding-left: 2px;\n"
"padding-right: 2px;\n"
"}")

        self.horizontalLayout_33.addWidget(self.go_to_sell_deposit_pushButton)


        self.verticalLayout_12.addLayout(self.horizontalLayout_33)


        self.horizontalLayout_34.addLayout(self.verticalLayout_12)

        self.ClientStackedWidget.addWidget(self.page_deposit)
        self.page_loans = QWidget()
        self.page_loans.setObjectName(u"page_loans")
        self.label_loans = QLabel(self.page_loans)
        self.label_loans.setObjectName(u"label_loans")
        self.label_loans.setGeometry(QRect(40, 20, 121, 41))
        self.loans_back_pushButton = QPushButton(self.page_loans)
        self.loans_back_pushButton.setObjectName(u"loans_back_pushButton")
        self.loans_back_pushButton.setGeometry(QRect(170, 30, 80, 27))
        self.loans_back_pushButton.setFont(font1)
        self.loans_back_pushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: rgb(167, 202, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-radius: 10px;\n"
"padding-top: 2px;\n"
"padding-bottom: 2px;\n"
"padding-left: 2px;\n"
"padding-right: 2px;\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color : rgb(132, 160, 202);\n"
"}\n"
"")
        self.ClientStackedWidget.addWidget(self.page_loans)
        self.page_goals = QWidget()
        self.page_goals.setObjectName(u"page_goals")
        self.horizontalLayout_17 = QHBoxLayout(self.page_goals)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_goals = QLabel(self.page_goals)
        self.label_goals.setObjectName(u"label_goals")

        self.horizontalLayout_16.addWidget(self.label_goals)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_7)

        self.goals_back_pushButton = QPushButton(self.page_goals)
        self.goals_back_pushButton.setObjectName(u"goals_back_pushButton")
        self.goals_back_pushButton.setFont(font1)
        self.goals_back_pushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: rgb(167, 202, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-radius: 10px;\n"
"padding-top: 2px;\n"
"padding-bottom: 2px;\n"
"padding-left: 2px;\n"
"padding-right: 2px;\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color : rgb(132, 160, 202);\n"
"}\n"
"")

        self.horizontalLayout_16.addWidget(self.goals_back_pushButton)


        self.verticalLayout_7.addLayout(self.horizontalLayout_16)

        self.goals_stackedWidget = QStackedWidget(self.page_goals)
        self.goals_stackedWidget.setObjectName(u"goals_stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.goals_stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.goals_stackedWidget.addWidget(self.page_2)

        self.verticalLayout_7.addWidget(self.goals_stackedWidget)


        self.horizontalLayout_17.addLayout(self.verticalLayout_7)

        self.ClientStackedWidget.addWidget(self.page_goals)
        self.page_currency_account = QWidget()
        self.page_currency_account.setObjectName(u"page_currency_account")
        self.horizontalLayout_19 = QHBoxLayout(self.page_currency_account)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_currency_account = QLabel(self.page_currency_account)
        self.label_currency_account.setObjectName(u"label_currency_account")

        self.horizontalLayout_3.addWidget(self.label_currency_account)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)

        self.curr_acc_back_pushButton = QPushButton(self.page_currency_account)
        self.curr_acc_back_pushButton.setObjectName(u"curr_acc_back_pushButton")
        self.curr_acc_back_pushButton.setFont(font1)
        self.curr_acc_back_pushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: rgb(167, 202, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-radius: 10px;\n"
"padding-top: 2px;\n"
"padding-bottom: 2px;\n"
"padding-left: 2px;\n"
"padding-right: 2px;\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color : rgb(132, 160, 202);\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.curr_acc_back_pushButton)


        self.verticalLayout_9.addLayout(self.horizontalLayout_3)

        self.curr_acc_listWidget = QListWidget(self.page_currency_account)
        self.curr_acc_listWidget.setObjectName(u"curr_acc_listWidget")

        self.verticalLayout_9.addWidget(self.curr_acc_listWidget)

        self.curr_accounts_textEdit = QTextEdit(self.page_currency_account)
        self.curr_accounts_textEdit.setObjectName(u"curr_accounts_textEdit")
        self.curr_accounts_textEdit.setReadOnly(True)

        self.verticalLayout_9.addWidget(self.curr_accounts_textEdit)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.go_to_new_curr_pushButton = QPushButton(self.page_currency_account)
        self.go_to_new_curr_pushButton.setObjectName(u"go_to_new_curr_pushButton")
        self.go_to_new_curr_pushButton.setFont(font4)
        self.go_to_new_curr_pushButton.setStyleSheet(u"QPushButton::pressed\n"
"{\n"
"background-color : rgb(22, 22, 91);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(33, 33, 132);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding-top: 2px;\n"
"padding-bottom: 2px;\n"
"padding-left: 2px;\n"
"padding-right: 2px;\n"
"}")

        self.horizontalLayout_18.addWidget(self.go_to_new_curr_pushButton)

        self.go_to_sell_curr_pushButton = QPushButton(self.page_currency_account)
        self.go_to_sell_curr_pushButton.setObjectName(u"go_to_sell_curr_pushButton")
        self.go_to_sell_curr_pushButton.setFont(font4)
        self.go_to_sell_curr_pushButton.setStyleSheet(u"QPushButton::pressed\n"
"{\n"
"background-color : rgb(22, 22, 91);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(33, 33, 132);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding-top: 2px;\n"
"padding-bottom: 2px;\n"
"padding-left: 2px;\n"
"padding-right: 2px;\n"
"}")

        self.horizontalLayout_18.addWidget(self.go_to_sell_curr_pushButton)


        self.verticalLayout_9.addLayout(self.horizontalLayout_18)


        self.horizontalLayout_19.addLayout(self.verticalLayout_9)

        self.ClientStackedWidget.addWidget(self.page_currency_account)
        self.page_new_currency_acc = QWidget()
        self.page_new_currency_acc.setObjectName(u"page_new_currency_acc")
        self.horizontalLayout_26 = QHBoxLayout(self.page_new_currency_acc)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_new_currency_account = QLabel(self.page_new_currency_acc)
        self.label_new_currency_account.setObjectName(u"label_new_currency_account")

        self.horizontalLayout_20.addWidget(self.label_new_currency_account)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_10)

        self.new_curr_back_pushButton = QPushButton(self.page_new_currency_acc)
        self.new_curr_back_pushButton.setObjectName(u"new_curr_back_pushButton")
        self.new_curr_back_pushButton.setFont(font1)
        self.new_curr_back_pushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: rgb(167, 202, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-radius: 10px;\n"
"padding-top: 2px;\n"
"padding-bottom: 2px;\n"
"padding-left: 2px;\n"
"padding-right: 2px;\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color : rgb(132, 160, 202);\n"
"}\n"
"")

        self.horizontalLayout_20.addWidget(self.new_curr_back_pushButton)


        self.verticalLayout_10.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_new_currency_account_2 = QLabel(self.page_new_currency_acc)
        self.label_new_currency_account_2.setObjectName(u"label_new_currency_account_2")

        self.horizontalLayout_21.addWidget(self.label_new_currency_account_2)

        self.new_curr_acc_comboBox = QComboBox(self.page_new_currency_acc)
        self.new_curr_acc_comboBox.setObjectName(u"new_curr_acc_comboBox")
        self.new_curr_acc_comboBox.setAutoFillBackground(False)
        self.new_curr_acc_comboBox.setStyleSheet(u"QComboBox\n"
"{\n"
"border: 1px solid; \n"
"border-radius: 5px; \n"
"background-color: white;\n"
"padding-left: 1px;\n"
"padding-top: 1px;\n"
"padding-right: 1px;\n"
"padding-bottom: 1px;\n"
"}")
        self.new_curr_acc_comboBox.setMaxVisibleItems(20)
        self.new_curr_acc_comboBox.setFrame(False)

        self.horizontalLayout_21.addWidget(self.new_curr_acc_comboBox)


        self.verticalLayout_10.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_new_currency_account_4 = QLabel(self.page_new_currency_acc)
        self.label_new_currency_account_4.setObjectName(u"label_new_currency_account_4")
        sizePolicy2.setHeightForWidth(self.label_new_currency_account_4.sizePolicy().hasHeightForWidth())
        self.label_new_currency_account_4.setSizePolicy(sizePolicy2)

        self.horizontalLayout_24.addWidget(self.label_new_currency_account_4)

        self.label_value_of_currency = QLabel(self.page_new_currency_acc)
        self.label_value_of_currency.setObjectName(u"label_value_of_currency")
        sizePolicy2.setHeightForWidth(self.label_value_of_currency.sizePolicy().hasHeightForWidth())
        self.label_value_of_currency.setSizePolicy(sizePolicy2)
        self.label_value_of_currency.setLayoutDirection(Qt.LeftToRight)
        self.label_value_of_currency.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_value_of_currency)


        self.verticalLayout_10.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_new_curr_acc_2 = QLabel(self.page_new_currency_acc)
        self.label_new_curr_acc_2.setObjectName(u"label_new_curr_acc_2")

        self.horizontalLayout_23.addWidget(self.label_new_curr_acc_2)

        self.new_curr_acc_money_label = QLabel(self.page_new_currency_acc)
        self.new_curr_acc_money_label.setObjectName(u"new_curr_acc_money_label")
        sizePolicy2.setHeightForWidth(self.new_curr_acc_money_label.sizePolicy().hasHeightForWidth())
        self.new_curr_acc_money_label.setSizePolicy(sizePolicy2)
        self.new_curr_acc_money_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.new_curr_acc_money_label)


        self.verticalLayout_10.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_new_currency_account_3 = QLabel(self.page_new_currency_acc)
        self.label_new_currency_account_3.setObjectName(u"label_new_currency_account_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_new_currency_account_3.sizePolicy().hasHeightForWidth())
        self.label_new_currency_account_3.setSizePolicy(sizePolicy4)

        self.horizontalLayout_22.addWidget(self.label_new_currency_account_3)

        self.new_curr_acc_doubleSpinBox = QDoubleSpinBox(self.page_new_currency_acc)
        self.new_curr_acc_doubleSpinBox.setObjectName(u"new_curr_acc_doubleSpinBox")
        self.new_curr_acc_doubleSpinBox.setStyleSheet(u"QDoubleSpinBox\n"
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
        self.new_curr_acc_doubleSpinBox.setAccelerated(True)
        self.new_curr_acc_doubleSpinBox.setMaximum(1000000000000.000000000000000)

        self.horizontalLayout_22.addWidget(self.new_curr_acc_doubleSpinBox)


        self.verticalLayout_10.addLayout(self.horizontalLayout_22)

        self.create_new_curr_pushButton = QPushButton(self.page_new_currency_acc)
        self.create_new_curr_pushButton.setObjectName(u"create_new_curr_pushButton")
        self.create_new_curr_pushButton.setFont(font4)
        self.create_new_curr_pushButton.setStyleSheet(u"QPushButton::pressed\n"
"{\n"
"background-color : rgb(22, 22, 91);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(33, 33, 132);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding-top: 2px;\n"
"padding-bottom: 2px;\n"
"padding-left: 2px;\n"
"padding-right: 2px;\n"
"}")

        self.verticalLayout_10.addWidget(self.create_new_curr_pushButton)


        self.horizontalLayout_26.addLayout(self.verticalLayout_10)

        self.ClientStackedWidget.addWidget(self.page_new_currency_acc)
        self.page_sell_curr_acc = QWidget()
        self.page_sell_curr_acc.setObjectName(u"page_sell_curr_acc")
        self.sell_curr_back_pushButton = QPushButton(self.page_sell_curr_acc)
        self.sell_curr_back_pushButton.setObjectName(u"sell_curr_back_pushButton")
        self.sell_curr_back_pushButton.setGeometry(QRect(400, 50, 64, 27))
        self.sell_curr_back_pushButton.setFont(font1)
        self.sell_curr_back_pushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: rgb(167, 202, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-radius: 10px;\n"
"padding-top: 2px;\n"
"padding-bottom: 2px;\n"
"padding-left: 2px;\n"
"padding-right: 2px;\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color : rgb(132, 160, 202);\n"
"}\n"
"")
        self.label_sell_currency_account = QLabel(self.page_sell_curr_acc)
        self.label_sell_currency_account.setObjectName(u"label_sell_currency_account")
        self.label_sell_currency_account.setGeometry(QRect(10, 10, 341, 104))
        self.tableWidget = QTableWidget(self.page_sell_curr_acc)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem8)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(160, 150, 411, 201))
        self.ClientStackedWidget.addWidget(self.page_sell_curr_acc)
        self.page_new_deposit = QWidget()
        self.page_new_deposit.setObjectName(u"page_new_deposit")
        self.horizontalLayout_27 = QHBoxLayout(self.page_new_deposit)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_new_deposit = QLabel(self.page_new_deposit)
        self.label_new_deposit.setObjectName(u"label_new_deposit")

        self.horizontalLayout_36.addWidget(self.label_new_deposit)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_4)

        self.new_deposit_back_pushButton = QPushButton(self.page_new_deposit)
        self.new_deposit_back_pushButton.setObjectName(u"new_deposit_back_pushButton")
        self.new_deposit_back_pushButton.setFont(font1)
        self.new_deposit_back_pushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: rgb(167, 202, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-radius: 10px;\n"
"padding-top: 2px;\n"
"padding-bottom: 2px;\n"
"padding-left: 2px;\n"
"padding-right: 2px;\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color : rgb(132, 160, 202);\n"
"}\n"
"")

        self.horizontalLayout_36.addWidget(self.new_deposit_back_pushButton)


        self.verticalLayout_11.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_new_deposit_2 = QLabel(self.page_new_deposit)
        self.label_new_deposit_2.setObjectName(u"label_new_deposit_2")

        self.horizontalLayout_28.addWidget(self.label_new_deposit_2)

        self.new_deposit_comboBox = QComboBox(self.page_new_deposit)
        self.new_deposit_comboBox.setObjectName(u"new_deposit_comboBox")
        self.new_deposit_comboBox.setAutoFillBackground(False)
        self.new_deposit_comboBox.setStyleSheet(u"QComboBox\n"
"{\n"
"border: 1px solid; \n"
"border-radius: 5px; \n"
"background-color: white;\n"
"padding-left: 1px;\n"
"padding-top: 1px;\n"
"padding-right: 1px;\n"
"padding-bottom: 1px;\n"
"}")
        self.new_deposit_comboBox.setMaxVisibleItems(20)
        self.new_deposit_comboBox.setFrame(False)

        self.horizontalLayout_28.addWidget(self.new_deposit_comboBox)


        self.verticalLayout_11.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_new_deposit_3 = QLabel(self.page_new_deposit)
        self.label_new_deposit_3.setObjectName(u"label_new_deposit_3")
        sizePolicy2.setHeightForWidth(self.label_new_deposit_3.sizePolicy().hasHeightForWidth())
        self.label_new_deposit_3.setSizePolicy(sizePolicy2)

        self.horizontalLayout_29.addWidget(self.label_new_deposit_3)

        self.label_new_deposit_interest_rate = QLabel(self.page_new_deposit)
        self.label_new_deposit_interest_rate.setObjectName(u"label_new_deposit_interest_rate")
        sizePolicy2.setHeightForWidth(self.label_new_deposit_interest_rate.sizePolicy().hasHeightForWidth())
        self.label_new_deposit_interest_rate.setSizePolicy(sizePolicy2)
        self.label_new_deposit_interest_rate.setLayoutDirection(Qt.LeftToRight)
        self.label_new_deposit_interest_rate.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_new_deposit_interest_rate)


        self.verticalLayout_11.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_new_deposit_4 = QLabel(self.page_new_deposit)
        self.label_new_deposit_4.setObjectName(u"label_new_deposit_4")

        self.horizontalLayout_30.addWidget(self.label_new_deposit_4)

        self.new_deposit_money_label = QLabel(self.page_new_deposit)
        self.new_deposit_money_label.setObjectName(u"new_deposit_money_label")
        sizePolicy2.setHeightForWidth(self.new_deposit_money_label.sizePolicy().hasHeightForWidth())
        self.new_deposit_money_label.setSizePolicy(sizePolicy2)
        self.new_deposit_money_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.new_deposit_money_label)


        self.verticalLayout_11.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_new_deposit_5 = QLabel(self.page_new_deposit)
        self.label_new_deposit_5.setObjectName(u"label_new_deposit_5")
        sizePolicy4.setHeightForWidth(self.label_new_deposit_5.sizePolicy().hasHeightForWidth())
        self.label_new_deposit_5.setSizePolicy(sizePolicy4)

        self.horizontalLayout_31.addWidget(self.label_new_deposit_5)

        self.new_deposit_doubleSpinBox = QDoubleSpinBox(self.page_new_deposit)
        self.new_deposit_doubleSpinBox.setObjectName(u"new_deposit_doubleSpinBox")
        self.new_deposit_doubleSpinBox.setStyleSheet(u"QDoubleSpinBox\n"
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
        self.new_deposit_doubleSpinBox.setAccelerated(True)
        self.new_deposit_doubleSpinBox.setMaximum(1000000000000.000000000000000)

        self.horizontalLayout_31.addWidget(self.new_deposit_doubleSpinBox)


        self.verticalLayout_11.addLayout(self.horizontalLayout_31)

        self.create_new_deposit_pushButton = QPushButton(self.page_new_deposit)
        self.create_new_deposit_pushButton.setObjectName(u"create_new_deposit_pushButton")
        self.create_new_deposit_pushButton.setFont(font4)
        self.create_new_deposit_pushButton.setStyleSheet(u"QPushButton::pressed\n"
"{\n"
"background-color : rgb(22, 22, 91);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(33, 33, 132);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding-top: 2px;\n"
"padding-bottom: 2px;\n"
"padding-left: 2px;\n"
"padding-right: 2px;\n"
"}")

        self.verticalLayout_11.addWidget(self.create_new_deposit_pushButton)


        self.horizontalLayout_27.addLayout(self.verticalLayout_11)

        self.ClientStackedWidget.addWidget(self.page_new_deposit)
        self.page_sell_deposit = QWidget()
        self.page_sell_deposit.setObjectName(u"page_sell_deposit")
        self.layoutWidget = QWidget(self.page_sell_deposit)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 40, 309, 35))
        self.horizontalLayout_35 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_sell_deposit_2 = QLabel(self.layoutWidget)
        self.label_sell_deposit_2.setObjectName(u"label_sell_deposit_2")

        self.horizontalLayout_35.addWidget(self.label_sell_deposit_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_3)

        self.sell_deposit_back_pushButton = QPushButton(self.layoutWidget)
        self.sell_deposit_back_pushButton.setObjectName(u"sell_deposit_back_pushButton")
        self.sell_deposit_back_pushButton.setFont(font1)
        self.sell_deposit_back_pushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: rgb(167, 202, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-radius: 10px;\n"
"padding-top: 2px;\n"
"padding-bottom: 2px;\n"
"padding-left: 2px;\n"
"padding-right: 2px;\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color : rgb(132, 160, 202);\n"
"}\n"
"")

        self.horizontalLayout_35.addWidget(self.sell_deposit_back_pushButton)

        self.ClientStackedWidget.addWidget(self.page_sell_deposit)

        self.horizontalLayout_13.addWidget(self.ClientStackedWidget)


        self.horizontalLayout_11.addWidget(self.frame)

        ClientMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ClientMainWindow)

        self.ClientStackedWidget.setCurrentIndex(5)
        self.transfer_pushButton.setDefault(False)
        self.options_pushButton.setDefault(False)
        self.transfer_go_pushButton.setDefault(False)
        self.goals_stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ClientMainWindow)
    # setupUi

    def retranslateUi(self, ClientMainWindow):
        ClientMainWindow.setWindowTitle(QCoreApplication.translate("ClientMainWindow", u"Aplikacja Banku", None))
        self.actionOptions.setText(QCoreApplication.translate("ClientMainWindow", u"Us\u0142ugi", None))
        self.actionHistory.setText(QCoreApplication.translate("ClientMainWindow", u"Historia", None))
        self.actionNew_transfer.setText(QCoreApplication.translate("ClientMainWindow", u"Nowy przelew", None))
        self.actionMain_pulpit.setText(QCoreApplication.translate("ClientMainWindow", u"Panel g\u0142\u00f3wny", None))
        self.label_available_funds.setText(QCoreApplication.translate("ClientMainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Dost\u0119pne \u015brodki:</span></p></body></html>", None))
        self.Money_num_label.setText(QCoreApplication.translate("ClientMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">200</span></p></body></html>", None))
        self.transfer_pushButton.setText(QCoreApplication.translate("ClientMainWindow", u"Nowy przelew", None))
        self.label_3.setText(QCoreApplication.translate("ClientMainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Ostatnie operacje:</span></p></body></html>", None))
        self.options_pushButton.setText(QCoreApplication.translate("ClientMainWindow", u"Us\u0142ugi", None))
        self.history_pushButton.setText(QCoreApplication.translate("ClientMainWindow", u"Historia", None))
        self.logout_pushButton.setText(QCoreApplication.translate("ClientMainWindow", u"Wyloguj si\u0119", None))
        self.label_options.setText(QCoreApplication.translate("ClientMainWindow", u"Us\u0142ugi:", None))
        self.options_currency_pushButton.setText(QCoreApplication.translate("ClientMainWindow", u"Kursy Walut", None))
        self.options_deposit_pushButton.setText(QCoreApplication.translate("ClientMainWindow", u"Lokaty", None))
        self.options_goals_pushButton.setText(QCoreApplication.translate("ClientMainWindow", u"Wydatki", None))
        self.options_loan_pushButton.setText(QCoreApplication.translate("ClientMainWindow", u"Kredyty", None))
        self.options_currencyAccount_pushButton.setText(QCoreApplication.translate("ClientMainWindow", u"Konta Walutowe", None))
        self.options_back_pushButton.setText(QCoreApplication.translate("ClientMainWindow", u"Powr\u00f3t", None))
        self.label_history.setText(QCoreApplication.translate("ClientMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Historia przelew\u00f3w:</span></p></body></html>", None))
        self.history_back_pushButton.setText(QCoreApplication.translate("ClientMainWindow", u"Powr\u00f3t", None))
        self.label_new_transfer.setText(QCoreApplication.translate("ClientMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Nowy przelew</span></p></body></html>", None))
        self.transfer_back_pushButton.setText(QCoreApplication.translate("ClientMainWindow", u"Powr\u00f3t", None))
        self.label_transfer_title.setText(QCoreApplication.translate("ClientMainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Tytu\u0142 przelewu:</span></p></body></html>", None))
        self.transfer_title_lineEdit.setText(QCoreApplication.translate("ClientMainWindow", u"Nowy przelew", None))
        self.label_account_num.setText(QCoreApplication.translate("ClientMainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Numer odbiorcy:</span></p></body></html>", None))
        self.label_new_transfer_2.setText(QCoreApplication.translate("ClientMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Dost\u0119pne \u015brodki:</span></p></body></html>", None))
        self.new_transfer_money_label.setText(QCoreApplication.translate("ClientMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">200</span></p></body></html>", None))
        self.label_value.setText(QCoreApplication.translate("ClientMainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Kwota:</span></p></body></html>", None))
        self.transfer_go_pushButton.setText(QCoreApplication.translate("ClientMainWindow", u"Wy\u015blij", None))
        self.label_currency.setText(QCoreApplication.translate("ClientMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Kursy Walut</span></p></body></html>", None))
        self.currency_back_pushButton.setText(QCoreApplication.translate("ClientMainWindow", u"Powr\u00f3t", None))
        self.label_deposit.setText(QCoreApplication.translate("ClientMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Lokaty</span></p></body></html>", None))
        self.deposit_back_pushButton.setText(QCoreApplication.translate("ClientMainWindow", u"Powr\u00f3t", None))
        self.go_to_new_deposit_pushButton.setText(QCoreApplication.translate("ClientMainWindow", u"Za\u0142\u00f3\u017c now\u0105 lokat\u0119", None))
        self.go_to_sell_deposit_pushButton.setText(QCoreApplication.translate("ClientMainWindow", u"Wyp\u0142a\u0107 lokat\u0119", None))
        self.label_loans.setText(QCoreApplication.translate("ClientMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Kredyty</span></p></body></html>", None))
        self.loans_back_pushButton.setText(QCoreApplication.translate("ClientMainWindow", u"Powr\u00f3t", None))
        self.label_goals.setText(QCoreApplication.translate("ClientMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Cele</span></p></body></html>", None))
        self.goals_back_pushButton.setText(QCoreApplication.translate("ClientMainWindow", u"Powr\u00f3t", None))
        self.label.setText(QCoreApplication.translate("ClientMainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">100</span></p></body></html>", None))
        self.label_currency_account.setText(QCoreApplication.translate("ClientMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Konta Walutowe</span></p></body></html>", None))
        self.curr_acc_back_pushButton.setText(QCoreApplication.translate("ClientMainWindow", u"Powr\u00f3t", None))
        self.go_to_new_curr_pushButton.setText(QCoreApplication.translate("ClientMainWindow", u"Za\u0142\u00f3\u017c nowe konto walutowe", None))
        self.go_to_sell_curr_pushButton.setText(QCoreApplication.translate("ClientMainWindow", u"Sprzedaj konto walutowe", None))
        self.label_new_currency_account.setText(QCoreApplication.translate("ClientMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Nowe konto walutowe</span></p></body></html>", None))
        self.new_curr_back_pushButton.setText(QCoreApplication.translate("ClientMainWindow", u"Powr\u00f3t", None))
        self.label_new_currency_account_2.setText(QCoreApplication.translate("ClientMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Waluta konta:</span></p></body></html>", None))
        self.label_new_currency_account_4.setText(QCoreApplication.translate("ClientMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Kurs wybranej waluty:</span></p></body></html>", None))
        self.label_value_of_currency.setText(QCoreApplication.translate("ClientMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">0</span></p></body></html>", None))
        self.label_new_curr_acc_2.setText(QCoreApplication.translate("ClientMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Dost\u0119pne \u015brodki:</span></p></body></html>", None))
        self.new_curr_acc_money_label.setText(QCoreApplication.translate("ClientMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">200</span></p></body></html>", None))
        self.label_new_currency_account_3.setText(QCoreApplication.translate("ClientMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Kwota:</span></p></body></html>", None))
        self.create_new_curr_pushButton.setText(QCoreApplication.translate("ClientMainWindow", u"Utw\u00f3rz konto walutowe", None))
        self.sell_curr_back_pushButton.setText(QCoreApplication.translate("ClientMainWindow", u"Powr\u00f3t", None))
        self.label_sell_currency_account.setText(QCoreApplication.translate("ClientMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Sprzedaj konto walutowe</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ClientMainWindow", u"Konto:", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ClientMainWindow", u"Waluta:", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ClientMainWindow", u"Warto\u015b\u0107", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ClientMainWindow", u"Warto\u015b\u0107 w z\u0142:", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem4 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ClientMainWindow", u"Konto 1", None));
        ___qtablewidgetitem5 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ClientMainWindow", u"dolar", None));
        ___qtablewidgetitem6 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("ClientMainWindow", u"4$", None));
        ___qtablewidgetitem7 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("ClientMainWindow", u"16z\u0142", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_new_deposit.setText(QCoreApplication.translate("ClientMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Za\u0142\u00f3\u017c lokat\u0119</span></p></body></html>", None))
        self.new_deposit_back_pushButton.setText(QCoreApplication.translate("ClientMainWindow", u"Powr\u00f3t", None))
        self.label_new_deposit_2.setText(QCoreApplication.translate("ClientMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">D\u0142ugo\u015b\u0107 lokaty:</span></p></body></html>", None))
        self.label_new_deposit_3.setText(QCoreApplication.translate("ClientMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Odsetki:</span></p></body></html>", None))
        self.label_new_deposit_interest_rate.setText(QCoreApplication.translate("ClientMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">0</span></p></body></html>", None))
        self.label_new_deposit_4.setText(QCoreApplication.translate("ClientMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Dost\u0119pne \u015brodki:</span></p></body></html>", None))
        self.new_deposit_money_label.setText(QCoreApplication.translate("ClientMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">200</span></p></body></html>", None))
        self.label_new_deposit_5.setText(QCoreApplication.translate("ClientMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Kwota:</span></p></body></html>", None))
        self.create_new_deposit_pushButton.setText(QCoreApplication.translate("ClientMainWindow", u"Utw\u00f3rz konto walutowe", None))
        self.label_sell_deposit_2.setText(QCoreApplication.translate("ClientMainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Wyp\u0142a\u0107 lokat\u0119</span></p></body></html>", None))
        self.sell_deposit_back_pushButton.setText(QCoreApplication.translate("ClientMainWindow", u"Powr\u00f3t", None))
    # retranslateUi

