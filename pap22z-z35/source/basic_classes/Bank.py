from basic_classes.Users import Client, Admin
from basic_classes.Currency_and_Money import Currency, Money
from basic_classes.extra_functions import reading_clients, reading_currencies, reading_admins, reading_deposits_rates, reading_credit_rates, add_clients_history
from basic_classes.extra_functions import write_currencies, write_clients, write_admins, write_deposits_rates, write_credits_rates
from basic_classes.History_and_Goals import History
from basic_classes.Actions import BankTransfer, CurrencyAccount, Deposit, Credit
from basic_classes.Account import Account
from basic_classes.Errors import LetterinPhoneNumber, NumbersInName
from basic_classes.Errors import InvalidLoginPassword, InvalidUserId, NoCurrencyInBank
import json
from random import randint

"""

"""


class Bank:
    def __init__(self, clients=[], admins=[], currencies=[]):
        self.currencies = currencies #git wczytywanie
        self.clients = clients #przetestowac
        self.admins = admins #zrobione
        self.current_user: Client = None
        self.main_currency = None
        self.deposits = None
        self.credits = None

    def read_from_file(self, path):
        with open(path, 'r') as file_handle:
            reader = json.load(file_handle)
        self.currencies = reading_currencies(reader[0]['currencies'])
        self.main_currency = self.currencies[0]  #jezeli cos sie wywala ze zmianami walut to najpierw szukaj tutaj
        self.clients = reading_clients(reader[0]['clients'], self.currencies)
        self.admins = reading_admins(reader[0]['admins'])
        self.deposits = reading_deposits_rates(reader[0]['deposits_rates'])
        self.credits = reading_credit_rates(reader[0]['credit_rates'])
        add_clients_history(self.clients)

    def write_to_file(self, path):
        data = [
            {
                "currencies": write_currencies(self.currencies),
                "clients": write_clients(self.clients),
                "admins": write_admins(self.admins),
                "deposits_rates": write_deposits_rates(self.deposits),
                "credit_rates": write_credits_rates(self.credits)
            }
        ]
        with open(path, 'w') as file_handle:
            json.dump(data, file_handle)

    def get_currencies(self):
        return self.currencies

    def find_user_from_id(self, user_id: int):
        if type(user_id) != int:
            raise TypeError("Id is a number")
        for admin in self.admins:
            if admin.get_anumber() == user_id:
                return admin
        for client in self.clients:
            if client.get_id() == user_id:
                return client
        raise InvalidUserId('Incorrect Id')

    # def transfer_money(self, transfer: BankTransfer):
    #     reciver = self.find_user_from_id(transfer.get_reciver_id())
    #     account = reciver.get_account()
    #     account.recive_transfer(transfer)

    def log(self, user_id: int, password: str):
        try:
            user = self.find_user_from_id(user_id)
            if user.is_password_correct(password):
                self.current_user = user
            else:
                raise InvalidLoginPassword
        except TypeError:
            raise InvalidUserId
        except ValueError:
            raise InvalidUserId

    def logout(self):
        if type(self.current_user) == Client:
            self.current_user.logout()
        self.current_user = None

    def get_current_user(self, user: Client):
        if type(user) != Client:
            raise TypeError
        self.current_user = user

    def get_user_money(self):
        return self.current_user.get_money()

    def get_user_money_currency(self):
        return self.current_user.get_money().currency

    def user_transfer(self, cash_to_transfer: Money, reciver_id: int, title: str):
        if type(cash_to_transfer) != Money:
            raise TypeError
        if type(reciver_id) != int:
            raise ValueError("Incorrect receiver Id")
        transfer = self.current_user.get_account().transfer(cash_to_transfer, reciver_id, title)
        reciver = self.find_user_from_id(transfer.get_reciver_id())
        account = reciver.get_account()
        account.recive_transfer(transfer)

    # def user_receive_transfer(self, transfer: BankTransfer):
    #     if type(transfer) != BankTransfer:
    #         raise TypeError
    #     self.current_user.get_account().recive_transfer(transfer)

    #zwracanie kursu waluty po nazwie

    def get_expenses(self): # zwraca liste miesiecy - wydatkow
        return self.current_user.get_account().expenses_list

    def create_deposit(self, duration: int, amount: int):
        money_to_create = Money(self.main_currency, amount)
        interest_rate = self.deposits[duration]
        if interest_rate == None:
            raise ValueError
        self.current_user.get_account().add_Deposit(duration, money_to_create, interest_rate)

    def withdrawal_deposit(self, opis: str):
        for deposit in self.current_user.get_account().deposits:
            if opis == repr(deposit):
                d = deposit
                self.current_user.get_account().withdrawal_Deposit(d)
                return
        raise ValueError

    def create_credit(self, duration: int, amount: int):
        money = Money(self.main_currency, amount)
        interest_rate = self.credits[duration]
        if interest_rate == None:
            raise ValueError
        self.current_user.get_account().add_Credit(duration, money, interest_rate)

    def get_installment_without_credit(self, money_amount: int, duration: int):
        interest_rate = float(self.credits[duration]/100)
        installment = Money(self.main_currency, round((money_amount)/(duration)*(1+interest_rate*(duration/12))))
        return repr(installment)

    def credit_installment(self, opis: str):  #  < ???????????? to musi byc automatycznie odpalane w sekcji kredyt jak ktos wejdzie
        for credit in self.current_user.get_account().credits:
            if repr(credit) == opis:
                c = credit
                break
        self.current_user.get_account().credit_installment(c)

    def pay_off_overdue_credit_installments(self, amount):
        money = Money(self.main_currency, amount)
        self.current_user.get_account().credit_pay_off_overdue_installments(money)

    def credit_repr(credit: Credit):
        repr(credit)

    def create_currency_account(self, amount: int, name_of_currency: str): #poprawic kreaowanie konta po nazwie
        currency = None
        for curr in self.currencies:
            if curr.name == name_of_currency:
                currency = curr
        if currency == None:
            raise TypeError
        currency_for_sale = Money(currency, amount)
        self.current_user.get_account().add_CurrencyAccount(currency_for_sale, self.main_currency)

    def list_of_names_of_currenccies_for_sale(self):
        names_of_currencies = []
        for curr in self.currencies[:1]:
            names_of_currencies.append(curr.name)
        return names_of_currencies

    def transfer_currency_to_main_account(self, repr: str):
        self.current_user._main_account.transfer_CurrencyAccount_to_main_account(repr)
        # self.current_user.get_account().transfer_CurrencyAccount_to_main_account(currency_account)

    def register_client(self, password: str, name: str, phone_number: int):
        condition = True
        while condition:
            id = randint(10000, 99999)
            try:
                self.find_user_from_id(id)
            except InvalidUserId:
                condition = False
        password = str(password)
        if type(phone_number) != int:
            raise LetterinPhoneNumber
        name_without_space = ''
        for l in name:
            if l.isspace():
                pass
            name_without_space += l
        if not name_without_space.isalpha():
            raise NumbersInName
        self.clients.append(Client(id, password, name, phone_number, Account(id, Money(self.main_currency, 0), History())))
        return id

    def set_modified_client_by_repr(self, repr: str):
        for client in self.clients:
            if client.__repr__() == repr:
                self.current_user.set_client_modify(client)
                break

    def change_currency_rate(self, repr_of_currency: str, buying_rate: float, selling_rate: float):
        if (type(selling_rate) != float) or (type(buying_rate) != float):
            raise TypeError
        for currency in self.currencies:
            if currency.__repr__() == repr_of_currency:
                currency.buying_rate = buying_rate
                currency.selling_rate = selling_rate
                return
        raise NoCurrencyInBank

    def change_deposit_rate(self, duration: int, rate: float):
        if (type(duration) != int) or (type(rate) != float):
            raise TypeError
        if rate > 0:
            self.deposits[duration] = rate
        else:
            self.deposits.pop(duration)

    def change_credit_rate(self, duration: int, rate: float):
        if (type(duration) != int) or (type(rate) != float):
            raise TypeError
        if rate > 0:
            self.credits[duration] = rate
        else:
            self.credits.pop(duration)
