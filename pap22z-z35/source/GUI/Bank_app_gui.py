from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
from PySide2.QtGui import *
from basic_classes.Bank import *

from GUI.ui_client_window import Ui_ClientMainWindow
from GUI.ui_admin_window import Ui_AdminMainWindow
from GUI.ui_login_window import Ui_LoginWindow
from basic_classes.Errors import *

import sys

class ClientWindow(QMainWindow):
    def __init__(self, bank: Bank, parent=None):
        super().__init__(parent)
        self.bank = bank
        self.file_path = "data_base/testing_file.json"

        self.ui = Ui_ClientMainWindow()
        self.ui.setupUi(self)

        self.ui.ClientStackedWidget.setCurrentIndex(0)

        # main
        self.ui.options_pushButton.clicked.connect(self.go_to_options)
        self.ui.history_pushButton.clicked.connect(self.go_to_history)
        self.ui.transfer_pushButton.clicked.connect(self.go_to_new_transfer)

        self.ui.options_back_pushButton.clicked.connect(self.go_to_main)
        self.ui.history_back_pushButton.clicked.connect(self.go_to_main)
        self.ui.transfer_back_pushButton.clicked.connect(self.go_to_main)

        self.ui.logout_pushButton.clicked.connect(self.logout)

        # transfer
        self.ui.transfer_go_pushButton.clicked.connect(self.transfer)
        self.ui.new_transfer_doubleSpinBox.setSuffix(self.bank.currencies[0].sign)

        # options
        self.ui.options_currency_pushButton.clicked.connect(self.go_to_currency)
        self.ui.options_deposit_pushButton.clicked.connect(self.go_to_deposit)
        self.ui.options_loan_pushButton.clicked.connect(self.go_to_loans)
        self.ui.options_currencyAccount_pushButton.clicked.connect(self.go_to_currency_account)
        self.ui.options_goals_pushButton.clicked.connect(self.go_to_spendings)

        self.ui.loans_back_pushButton.clicked.connect(self.go_to_options)
        self.ui.deposit_back_pushButton.clicked.connect(self.go_to_options)
        self.ui.currency_back_pushButton.clicked.connect(self.go_to_options)
        self.ui.curr_acc_back_pushButton.clicked.connect(self.go_to_options)
        self.ui.spendings_back_pushButton.clicked.connect(self.go_to_options)

        # curr_acc
        self.ui.new_curr_back_pushButton.clicked.connect(self.go_to_currency_account)
        self.ui.go_to_new_curr_pushButton.clicked.connect(self.go_to_new_curr_acc)
        self.ui.sell_curr_pushButton.clicked.connect(self.sell_curr_acc)

        self.fill_new_curr_combobox()
        self.show_exchange_rate()
        self.ui.new_curr_acc_comboBox.activated.connect(self.show_exchange_rate)
        self.ui.curr_acc_listWidget.setSpacing(7)
        self.set_up_curr_acc_listWidget()

        self.ui.create_new_curr_pushButton.clicked.connect(self.create_curr_acc)

        # deposit
        self.ui.go_to_new_deposit_pushButton.clicked.connect(self.go_to_new_deposit)
        self.ui.sell_deposit_pushButton.clicked.connect(self.sell_deposit)

        self.ui.new_deposit_back_pushButton.clicked.connect(self.go_to_deposit)

        self.fill_deposit_combobox()
        self.show_deposit_interest_rate()
        self.ui.new_deposit_comboBox.activated.connect(self.show_deposit_interest_rate)
        self.ui.new_deposit_doubleSpinBox.setSuffix(self.bank.currencies[0].sign)
        self.ui.deposit_listWidget.setSpacing(7)
        self.set_up_deposit_listWidget()

        self.ui.create_new_deposit_pushButton.clicked.connect(self.create_new_deposit)

        # loan
        self.ui.go_to_new_loan_pushButton.clicked.connect(self.go_to_new_loan)
        self.ui.new_loan_back_pushButton.clicked.connect(self.go_to_loans)

        self.ui.loan_pay_off_doubleSpinBox.setValue(0.00)
        self.ui.loan_pay_off_doubleSpinBox.setSuffix(self.bank.currencies[0].sign)
        self.ui.new_loan_doubleSpinBox.setValue(0.00)
        self.ui.new_loan_doubleSpinBox.setSuffix(self.bank.currencies[0].sign)

        self.fill_loan_combobox()
        self.show_loan_interest_rate()
        self.ui.label_new_loan_interest_per_month.setFont(QFont('SansSerif', 20))
        self.ui.label_new_loan_interest_per_month.setText("0.00 zł")

        self.ui.new_loan_comboBox.activated.connect(self.show_loan_interest_rate)
        self.ui.new_loan_comboBox.activated.connect(self.show_loan_monthly_cost)
        self.ui.new_loan_doubleSpinBox.valueChanged.connect(self.show_loan_monthly_cost)

        self.ui.take_loan_pushButton.clicked.connect(self.create_new_loan)
        self.ui.loan_pay_off_instalment_pushButton.clicked.connect(self.pay_off_instalment)

        # refresh
        self.refresh()

    def go_to_main(self):
        self.ui.ClientStackedWidget.setCurrentIndex(0)
        self.refresh()

    def go_to_options(self):
        self.ui.ClientStackedWidget.setCurrentIndex(1)
        self.refresh()

    def go_to_history(self):
        self.ui.ClientStackedWidget.setCurrentIndex(2)
        self.refresh()

    def go_to_new_transfer(self):
        self.ui.ClientStackedWidget.setCurrentIndex(3)
        self.ui.transfer_title_lineEdit.setText("Nowy przelew")
        self.ui.new_transfer_doubleSpinBox.setValue(0.00)
        self.ui.transfer_naccount_lineEdit.clear()
        self.refresh()

    def go_to_currency(self):
        self.ui.ClientStackedWidget.setCurrentIndex(4)
        self.refresh()

    def go_to_deposit(self):
        self.ui.ClientStackedWidget.setCurrentIndex(5)
        self.refresh()

    def go_to_loans(self):
        self.ui.ClientStackedWidget.setCurrentIndex(6)
        self.ui.loan_pay_off_doubleSpinBox.setValue(0.00)
        self.refresh()

    def go_to_spendings(self):
        self.ui.ClientStackedWidget.setCurrentIndex(7)
        self.refresh()

    def go_to_currency_account(self):
        self.ui.ClientStackedWidget.setCurrentIndex(8)
        self.refresh()

    def go_to_new_curr_acc(self):
        self.ui.ClientStackedWidget.setCurrentIndex(9)
        self.ui.new_curr_acc_comboBox.setCurrentIndex(0)
        self.ui.new_curr_acc_doubleSpinBox.setValue(0.00)
        self.refresh()

    def go_to_new_deposit(self):
        self.ui.ClientStackedWidget.setCurrentIndex(10)
        self.ui.new_deposit_comboBox.setCurrentIndex(0)
        self.ui.new_deposit_doubleSpinBox.setValue(0.00)
        self.refresh()

    def go_to_new_loan(self):
        self.ui.ClientStackedWidget.setCurrentIndex(11)
        self.ui.new_loan_comboBox.setCurrentIndex(0)
        self.ui.new_loan_doubleSpinBox.setValue(0.00)
        self.refresh()

    def refresh(self):
        self.show_money(self.ui.Money_num_label)
        self.show_money(self.ui.new_transfer_money_label)
        self.show_money(self.ui.new_curr_acc_money_label)
        self.show_money(self.ui.new_deposit_money_label)
        self.bank.write_to_file(self.file_path)
        self.show_last_operations()
        self.show_history()
        self.print_curr()
        self.print_loans()
        self.show_instalment_to_pay()
        self.show_spendings()

    def show_money(self, label):
        label.setFont(QFont('SansSerif', 20))
        label.setText(self.bank.get_user_money().__repr__())

    def show_last_operations(self):
        self.ui.last_operations_textBrowser.setFont(QFont('SansSerif', 10))
        self.ui.last_operations_textBrowser.setText(self.bank.current_user.get_account().get_history().__str__())

    def show_history(self):
        self.ui.history_textEdit.setFont(QFont('SansSerif', 12))
        self.ui.history_textEdit.setText(self.bank.current_user.get_account().get_history().__repr__())

    def transfer(self):
        try:
            if (self.ui.new_transfer_doubleSpinBox.value() == 0 ):
                raise ValueError
            if (self.ui.new_transfer_doubleSpinBox.value()*100 > self.bank.get_user_money().amount ):
                raise TooLittleMoneyToTransfer
            money_to_transfer = Money(self.bank.currencies[0], int(self.ui.new_transfer_doubleSpinBox.value()*100))
            self.bank.user_transfer(money_to_transfer , int(self.ui.transfer_naccount_lineEdit.text()), self.ui.transfer_title_lineEdit.text())
            self.message("Przelew przebiegł pomyślnie", None)
            self.go_to_main()
        except ValueError:
            self.message("Błąd", 'Wartość przelewu musi być większa niż 0')
        except InvalidMoneyNumber:
            self.message("Błąd", 'Wartość przelewu musi być większa niż 0')
        except InvalidUserId:
            self.message("Błąd", "Nie istnieje osoba o podanym numerze")
        except TooLittleMoneyToTransfer:
            self.message("Błąd", "Wartość przelewu nie może przekraczać posiadanych pieniędzy")
        self.refresh()

    def message(self, Title, InformativeText):
        msg = QMessageBox()
        msg.setText(Title)
        msg.setInformativeText(InformativeText)
        msg.setWindowTitle(Title)
        msg.exec_()

    def logout(self):
        self.refresh()
        self.bank.logout()
        self.show_login_window()

    def show_login_window(self):
        if(not self.bank.current_user):
            self.login_window = LoginWindow(self.bank)
            self.login_window.show()
            self.close()

    # currencies
    def print_curr(self):
        # bez zlotowki indeks -> 0
        text = ""
        for curr in self.bank.get_currencies()[1:]:
            text += curr.__repr__() + "\n"
        self.ui.currencies_textEdit.setFont(QFont('SansSerif', 20))
        self.ui.currencies_textEdit.setText(text)

    # currencies accounts
    def fill_new_curr_combobox(self):
        for curr in self.bank.get_currencies()[1:]:
            self.ui.new_curr_acc_comboBox.addItem(curr.name)

    def show_exchange_rate(self):
        exchange_rate = 0.00
        suffix = ""
        for curr in self.bank.get_currencies()[1:]:
            if(curr.name == self.ui.new_curr_acc_comboBox.currentText()):
                exchange_rate = curr.exchange_rate
                suffix = curr.sign
        self.ui.label_value_of_currency.setFont(QFont('SansSerif', 20))
        self.ui.label_value_of_currency.setText(str(exchange_rate))
        # setting suffix in spinbox
        self.ui.new_curr_acc_doubleSpinBox.setSuffix(suffix)

    def set_up_curr_acc_listWidget(self):
        self.ui.curr_acc_listWidget.setFont(QFont('SansSerif', 12))
        for curr_acc in self.bank.current_user.get_account().return_all_active_currency_accounts():
            self.ui.curr_acc_listWidget.addItem(curr_acc.__repr__())

    def create_curr_acc(self):
        try:
            if self.ui.new_curr_acc_doubleSpinBox.value() != 0:
                self.bank.create_currency_account(int(self.ui.new_curr_acc_doubleSpinBox.value()*100), self.ui.new_curr_acc_comboBox.currentText())
                self.message("Konto utworzone pomyślnie", None)
                self.add_new_curr_acc()
                self.go_to_currency_account()
            else:
                raise ValueError
        except ValueError:
            self.message("Błąd", "Wartość kupowanej waluty musi być większa niż 0")
        except TooLittleMoneyToExchange:
            self.message("Błąd", "Wartość kupowanej waluty nie może przekraczać posiadanych pieniędzy")
        self.refresh()

    def add_new_curr_acc(self):
        self.ui.curr_acc_listWidget.addItem(self.bank.current_user.get_account().return_all_active_currency_accounts()[-1].__repr__())

    def sell_curr_acc(self):
        if(self.ui.curr_acc_listWidget.currentRow() != -1):
            self.bank.transfer_currency_to_main_account(self.ui.curr_acc_listWidget.currentItem().text())
            self.ui.curr_acc_listWidget.takeItem(self.ui.curr_acc_listWidget.currentRow())
            self.message("Pomyślnie wypłacono środki z konta walutowego", None)
        else:
            self.message("Błąd", "Wybierz konto walutowe, z którego chcesz wypłacić")

    # deposits
    def set_up_deposit_listWidget(self):
        self.ui.deposit_listWidget.setFont(QFont('SansSerif', 12))
        for deposit in self.bank.current_user.get_account().all_active_deposits():
            self.ui.deposit_listWidget.addItem(deposit.__repr__())

    def fill_deposit_combobox(self):
        for option in self.bank.deposits:
            self.ui.new_deposit_comboBox.addItem(str(option))

    def show_deposit_interest_rate(self):
        self.ui.label_new_deposit_interest_rate.setFont(QFont('SansSerif', 20))
        self.ui.label_new_deposit_interest_rate.setText(str(self.bank.deposits[int(self.ui.new_deposit_comboBox.currentText())])+"%")

    def create_new_deposit(self):
        try:
            if(self.ui.new_deposit_doubleSpinBox.value() != 0):
                self.bank.create_deposit(int(self.ui.new_deposit_comboBox.currentText()), int(self.ui.new_deposit_doubleSpinBox.value()*100))
                self.message("Pomyślnie utworzono lokatę", None)
                self.add_new_deposit()
                self.go_to_deposit()
            else:
                raise ValueError
        except ValueError:
            self.message("Błąd", "Pieniądze przeznaczone na lokatę muszą być większe niż 0")
        except TooLittleMoneyToCreateDeposit:
            self.message("Błąd", "Zbyt mało pieniędzy, by założyć podaną lokatę")

    def add_new_deposit(self):
        self.ui.deposit_listWidget.addItem(self.bank.current_user.get_account().deposits[-1].__repr__())

    def sell_deposit(self):
        if(self.ui.deposit_listWidget.currentRow() != -1):
            self.ui.deposit_listWidget.currentRow()
            self.bank.withdrawal_deposit(self.ui.deposit_listWidget.currentItem().text())
            self.ui.deposit_listWidget.takeItem(self.ui.deposit_listWidget.currentRow())
            self.message("Pomyślnie wypłacono środki z lokaty", None)
        else:
            self.message("Błąd", "Wybierz lokatę, którą chcesz wyplacić")

    # loans
    def fill_loan_combobox(self):
        for option in self.bank.credits:
            self.ui.new_loan_comboBox.addItem(str(option))

    def show_loan_interest_rate(self):
        self.ui.label_new_loan_percentage.setFont(QFont('SansSerif', 20))
        self.ui.label_new_loan_percentage.setText(str(self.bank.credits[int(self.ui.new_loan_comboBox.currentText())]))

    def show_loan_monthly_cost(self):
        self.ui.label_new_loan_interest_per_month.setFont(QFont('SansSerif', 20))
        self.ui.label_new_loan_interest_per_month.setText(str(self.bank.get_installment_without_credit(int(self.ui.new_loan_doubleSpinBox.value()*100), int(self.ui.new_loan_comboBox.currentText()))))

    def show_instalment_to_pay(self):
        self.ui.label_loans_instalment_to_pay.setFont(QFont('SansSerif', 20))
        self.ui.label_loans_instalment_to_pay.setText(f'{self.bank.current_user.get_account().get_overdue_credit_instalments()/100} zł')

    def create_new_loan(self):
        try:
            if(self.ui.new_loan_doubleSpinBox.value()!=0):
                self.bank.create_credit(int(self.ui.new_loan_comboBox.currentText()), int(self.ui.new_loan_doubleSpinBox.value()*100))
                self.message("Pomyślnie wziąłeś kredyt", None)
                self.go_to_loans()
            else:
                raise ValueError
        except ValueError:
            self.message("Błąd", "Wartość kredytu musi być większa niż 0")
        except TooLittleMoneyToTakeaLoan:
            self.message("Błąd", "Wartość kredytu nie może przekraczać dwukrotności twoich pieniędzy")

    def print_loans(self):
        text = ""
        for loan in self.bank.current_user.get_account().return_all_active_credits():
            text += loan.__repr__() + "\n"
        self.ui.loans_textEdit.setFont(QFont("SansSerif", 12))
        self.ui.loans_textEdit.setText(text)

    def pay_off_instalment(self):
        try:
            if (self.bank.current_user.get_account().get_overdue_credit_instalments()):
                self.bank.pay_off_overdue_credit_installments(int(self.ui.loan_pay_off_doubleSpinBox.value()*100))
                self.refresh()
            else:
                self.message("Błąd", "Brak odsetek do opłacenia")
        except TooMuchMoney:
            self.message("Błąd", "Nie możesz spłaćić więcej odsetek, niż jest wyświetlone na ekranie")

    # spendings
    def show_spendings(self):
        text = ""
        for spending in self.bank.get_expenses():
            text += spending.__repr__() + "\n"
        self.ui.spendings_textEdit.setFont(QFont("SansSerif", 20))
        self.ui.spendings_textEdit.setText(text)


class AdminWindow(QMainWindow):
    def __init__(self, bank : Bank, parent=None):
        super().__init__(parent)
        self.bank = bank
        self.ui = Ui_AdminMainWindow()
        self.ui.setupUi(self)

        self.file_path = "data_base/testing_file.json"

        self.ui.stackedWidget.setCurrentIndex(0)
        # main
        self.ui.main_options__pushButton.clicked.connect(self.go_to_options)
        self.ui.main_users_pushButton.clicked.connect(self.go_to_users)
        self.ui.main_logout_pushButton.clicked.connect(self.logout)

        self.ui.clients_listWidget.setSpacing(7)
        self.set_up_users_listWidget()
        self.ui.clients_listWidget.setCurrentRow(0)

        # options
        self.ui.options_back_pushButton.clicked.connect(self.go_to_main)

        self.ui.options_currencies__pushButton.clicked.connect(self.go_to_currencies)
        self.ui.options_deposit__pushButton.clicked.connect(self.go_to_deposits)
        self.ui.options_loans__pushButton.clicked.connect(self.go_to_loans)

        # users
        self.ui.users_back_pushButton.clicked.connect(self.go_to_main)
        self.ui.users_accept_pushButton.clicked.connect(self.change_user_params)

        self.ui.users_stackedWidget.setCurrentIndex(0)
        self.ui.users_param_comboBox.activated.connect(self.show_user_param_to_edit)

        # currencies
        self.ui.currencies_back_pushButton.clicked.connect(self.go_to_options)
        self.ui.currency_change_pushButton.clicked.connect(self.change_currency)

        self.fill_currency_comboBox()

        # deposits
        self.ui.deposits_back_pushButton_2.clicked.connect(self.go_to_options)
        self.ui.deposit_change_pushButton.clicked.connect(self.change_deposit_rate)

        self.ui.deposit_duration_spinBox.setSuffix("m.")
        self.ui.deposit_interest_doubleSpinBox.setSuffix("%")

        # loans
        self.ui.loans_back_pushButton.clicked.connect(self.go_to_options)
        self.ui.loan_change_pushButton.clicked.connect(self.change_loan_rate)

        self.ui.loan_duration_spinBox.setSuffix("m.")
        self.ui.loan_interest_doubleSpinBox.setSuffix("%")

    def go_to_main(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.clients_listWidget.setCurrentRow(0)
        self.refresh()

    def go_to_options(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.refresh()

    def go_to_users(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.bank.set_modified_client_by_repr(self.ui.clients_listWidget.currentItem().text())
        self.set_up_users_lineEdits()
        self.refresh()

    def go_to_currencies(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.currency_buying_rate_doubleSpinBox.setValue(0.00)
        self.ui.currency_selling_rate_doubleSpinBox.setValue(0.00)
        self.refresh()

    def go_to_deposits(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.deposit_duration_spinBox.setValue(0)
        self.ui.deposit_interest_doubleSpinBox.setValue(0.00)
        self.refresh()

    def go_to_loans(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        self.ui.loan_duration_spinBox.setValue(0)
        self.ui.loan_interest_doubleSpinBox.setValue(0.00)
        self.refresh()

    def refresh(self):
        self.bank.write_to_file(self.file_path)

    def message(self, Title, InformativeText):
        msg = QMessageBox()
        msg.setText(Title)
        msg.setInformativeText(InformativeText)
        msg.setWindowTitle(Title)
        msg.exec_()

    def logout(self):
        self.refresh()
        self.bank.logout()
        self.show_login_window()

    def show_login_window(self):
        if(not self.bank.current_user):
            self.login_window = LoginWindow(self.bank)
            self.login_window.show()
            self.close()

    def set_up_users_listWidget(self):
        self.ui.clients_listWidget.clear()
        for client in self.bank.clients:
            if type(client) == Client:
                self.ui.clients_listWidget.addItem(client.__repr__())

    def set_up_users_lineEdits(self):
        self.ui.user_name_lineEdit.setText(self.bank.current_user.client_modify.name)
        self.ui.users_num_lineEdit.setText(str(self.bank.current_user.client_modify.phone))
        self.ui.users_password_lineEdit.setText(self.bank.current_user.client_modify.password)
        self.ui.users_money_lineEdit.setText(self.bank.current_user.client_modify.get_account().main_banking_account.__repr__())

    # user
    def show_user_param_to_edit(self):
        self.ui.users_stackedWidget.setCurrentIndex(self.ui.users_param_comboBox.currentIndex())

    def change_user_params(self):
        if(self.ui.users_param_comboBox.currentIndex()==0):
            if(self.ui.edit_user_name_lineEdit.text()):
                self.bank.current_user.change_client_name(self.ui.edit_user_name_lineEdit.text())
                self.message("Pomyślnie zmieniono imię i nazwisko", None)
                self.refresh()
                self.set_up_users_lineEdits()
                self.set_up_users_listWidget()
            else:
                self.message("Błąd", "Wpisz nowe imię i nazwisko użytkownika")
        elif(self.ui.users_param_comboBox.currentIndex()==1):
            if(self.ui.edit_user_number_spinBox.value()):
                self.bank.current_user.change_client_phone(self.ui.edit_user_number_spinBox.value())
                self.message("Pomyślnie zmieniono numer telefonu", None)
                self.refresh()
                self.set_up_users_lineEdits()
                self.set_up_users_listWidget()
            else:
                self.message("Błąd", "Wpisz nowy numer telefonu")
        elif(self.ui.users_param_comboBox.currentIndex()==2):
            if(self.ui.edit_user_password_lineEdit_4.text()):
                self.bank.current_user.change_client_password(self.ui.edit_user_password_lineEdit_4.text())
                self.message("Pomyślnie zmieniono hasło", None)
                self.refresh()
                self.set_up_users_lineEdits()
                self.set_up_users_listWidget()
            else:
                self.message("Błąd", "Wpisz nowe hasło")
        elif(self.ui.users_param_comboBox.currentIndex()==3):
            if(self.ui.edit_user_money_doubleSpinBox.value()):
                self.bank.current_user.change_client_main_account_money(int(self.ui.edit_user_money_doubleSpinBox.value()*100))
                self.message("Pomyślnie zmieniono wartość pieniędzy", None)
                self.refresh()
                self.set_up_users_lineEdits()
                self.set_up_users_listWidget()
            else:
                self.message("Błąd", "Wpisz nową wartość pieniędzy")

    # currencies
    def fill_currency_comboBox(self):
        self.ui.currency_comboBox.clear()
        for currency in self.bank.currencies[1:]:
            self.ui.currency_comboBox.addItem(currency.__repr__())

    def change_currency(self):
        try:
            if (self.ui.currency_buying_rate_doubleSpinBox.value() != 0 and self.ui.currency_selling_rate_doubleSpinBox.value() != 0):
                self.bank.change_currency_rate(self.ui.currency_comboBox.currentText(), self.ui.currency_buying_rate_doubleSpinBox.value(), self.ui.currency_selling_rate_doubleSpinBox.value())
                self.message("Pomyślnie zmieniono wartości waluty", None)
                self.refresh()
                self.fill_currency_comboBox()
                self.go_to_options()
            else:
                raise ValueError
        except ValueError:
            self.message("Błąd", "Wartość kupna i sprzedaży waluty musi być większa od 0")

    # deposits
    def change_deposit_rate(self):
        try:
            self.bank.change_deposit_rate(int(self.ui.deposit_duration_spinBox.value()), float(self.ui.deposit_interest_doubleSpinBox.value()))
            if(self.ui.deposit_interest_doubleSpinBox.value() != 0.00):
                self.message("Oprocentowanie lokaty zmienione pomyślnie", None)
            else:
                self.message(f'Lokata o długości {self.ui.deposit_duration_spinBox.value()} usunięta pomyślnie', None)
            self.refresh()
            self.go_to_options()
        except KeyError:
            self.message("Podana długość lokaty już i tak nie istnieje", None)

    # loans
    def change_loan_rate(self):
        try:
            self.bank.change_credit_rate(int(self.ui.loan_duration_spinBox.value()), float(self.ui.loan_interest_doubleSpinBox.value()))
            if(self.ui.loan_interest_doubleSpinBox.value() != 0.00):
                self.message("Oprocentowanie kredytu zmienione pomyślnie", None)
            else:
                self.message(f'Kredyt o długości {self.ui.loan_duration_spinBox.value()} usunięta pomyślnie', None)
            self.refresh()
            self.go_to_options()
        except KeyError:
            self.message("Podana długość kredytu już i tak nie istnieje", None)


class LoginWindow(QMainWindow):
    def __init__(self, bank : Bank, parent=None):
        super().__init__(parent)
        self.bank = bank
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.file_path = "data_base/testing_file.json"

        self.ui.LoginStackedWidget.setCurrentIndex(0)

        self.ui.log_to_reg_pushButton.clicked.connect(self.go_to_reg)
        self.ui.reg_to_log_pushButton.clicked.connect(self.go_to_log)

        self.ui.Login_pushButton.clicked.connect(self.login)
        self.ui.Register_pushButton.clicked.connect(self.register)

    def login(self):
        try:
            if(self.ui.lineEdit_naccount.text() and self.ui.lineEdit_password.text()):
                client_id = int(self.ui.lineEdit_naccount.text())
                self.bank.log(client_id, self.ui.lineEdit_password.text())
                if (type(self.bank.current_user) == Client):
                    self.show_client_window()
                elif (type(self.bank.current_user) == Admin):
                    self.show_admin_window()
            else:
                self.message("Błąd", 'Wpisz numer konta i hasło aby się zalogować')
        except InvalidUserId:
            self.message("Błąd", 'Błędny numer konta lub hasło')
        except ValueError:
            self.message("Błąd", 'Numer konta składa się wyłącznie z cyfr')
        except InvalidLoginPassword:
            self.message("Błąd", 'Błędny numer konta lub hasło')

    def register(self):
        id = self.bank.register_client(self.ui.reg_password_lineEdit.text(), self.ui.reg_name_lineEdit.text() + self.ui.reg_surname_lineEdit.text(), int(self.ui.reg_phone_lineEdit.text()))
        self.message("Konto utworzone pomyślnie", f'Twoje id to: {id}')
        self.bank.write_to_file(self.file_path)

    def show_client_window(self):
        if(self.bank.current_user):
            self.client_window = ClientWindow(self.bank)
            self.client_window.show()
            self.close()

    def show_admin_window(self):
        if(self.bank.current_user):
            self.admin_window = AdminWindow(self.bank)
            self.admin_window.show()
            self.close()

    def message(self, Title, InformativeText):
        msg = QMessageBox()
        msg.setText(Title)
        msg.setInformativeText(InformativeText)
        msg.setWindowTitle(Title)
        msg.exec_()

    def go_to_log(self):
        self.ui.LoginStackedWidget.setCurrentIndex(0)
        self.setWindowTitle("Logowanie")

    def go_to_reg(self):
        self.ui.LoginStackedWidget.setCurrentIndex(1)
        self.setWindowTitle("Rejestracja")


