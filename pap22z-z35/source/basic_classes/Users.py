from basic_classes.Errors import IdIsANumberError
from basic_classes.Currency_and_Money import Currency
from basic_classes.Account import Account

class Client:
    def __init__(self, id: int, password: str, name: str, phone_number: int, main_account: Account, logged: bool = 0):
        if type(id) != int:
            raise IdIsANumberError
        if type(phone_number) != int:
            raise TypeError
        self.password = str(password)
        self._id = id
        self.name = name
        self.phone = phone_number
        self._main_account = main_account
        self.logged = logged

    def get_id(self):
        return self._id

    def get_account(self):
        return self._main_account

    def get_money(self):
        account = self._main_account
        return account.get_money_on_main_account()

    def is_password_correct(self, password):
        password = str(password)
        return self.password == password

    def logout(self):
        self.logged = 0

    def login(self):
        self.logged = 1

    def __repr__(self):
        text = f"ID: {self._id}\nIMIE: {self.name}\nNUMER TELEFONU: {self.phone}"
        return text


class Admin:
    def __init__(self, password: str, name: str, admin_n: int):
        if type(admin_n) != int:
            raise IdIsANumberError
        self._admin_n = admin_n
        self._name = str(name)
        self._number = admin_n
        self.password = str(password)
        self.client_modify = None

    def get_anumber(self):
        return self._admin_n

    def get_name(self):
        return self._name

    def get_admin_number(self):
        return self._number

    def is_password_correct(self, password):
        return self.password == str(password)

    def set_client_modify(self, client: Client):
        self.client_modify = client

    def end_of_modification_client(self):
        self.client_modify = None

    def change_client_name(self, new_name: str):
        new_name = str(new_name)
        self.client_modify.name = new_name

    def change_client_password(self, new_password: str):
        self.client_modify.password = str(new_password)

    def change_client_phone(self, new_phone: int):
        self.client_modify.phone = int(new_phone)

    def change_client_main_account_money(self, amount: int):
        self.client_modify.get_account().main_banking_account.amount = amount

    def exchange_rate(self, currency: Currency, new_rate: float):
        if type(currency) != Currency:
            raise TypeError
        currency.exchange_rate = new_rate

    # def freezing_of_the_funds(self, client: Client, funds):