from PySide2.QtWidgets import QApplication, QWidget
from GUI.Bank_app_gui import ClientWindow, LoginWindow
from basic_classes.Bank import Bank

import sys


def main(args):
    bank = Bank()
    bank.read_from_file("data_base/testing_file.json")

    app = QApplication(args)
    window = LoginWindow(bank)
    window.show()
    return app.exec_()


if(__name__ == "__main__"):
    main(sys.argv)