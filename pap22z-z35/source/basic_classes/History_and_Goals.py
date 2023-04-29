from datetime import datetime
from basic_classes.Actions import BankTransfer
from basic_classes.Currency_and_Money import Money


class History:
    """
    Klasa reprezentująca historie
    Potrzebne  jesy chyba czy przelew przychodzacy czy wychodzacy
    wystaczy zrobic metode porownujaca id w przelewach
    """
    def __init__(self):
        self.transactions = []

    def add_acction(self, repr_of_action: str, date = None):
        if date == None:
            tuple = repr_of_action, datetime.today()
        else:
            tuple = repr_of_action, date
        self.transactions.insert(0, tuple)

    def sort_history_by_date(self):
        def return_second(transaction):
            return transaction[1]
        self.transactions.sort(key=return_second, reverse=True)

    # krotki opis
    def __str__(self):
        s = ''
        for i in range(0, len(self.transactions)):
            s = s + self.transactions[i][0] + "\nDATA: " + f"{self.transactions[i][1]:%B %d, %Y %H:%M:%S}"  + '\n\n'
        return s

    # dlugi opis
    def __repr__(self):
        rep = ''
        for i in range(0, len(self.transactions)):
            rep = rep + self.transactions[i][0] + "\nDATA: " + f"{self.transactions[i][1]:%B %d, %Y %H:%M:%S}" + '\n\n'
        return rep


class Expenses:
    def __init__(self, month: int, year: int, money: Money):
        if type(money) != Money:
            raise TypeError
        if type(month) != int:
            raise TypeError
        if type(year) != int:
            raise TypeError
        self._month = month
        self._year = year
        self.money = money
        self.months = {
            1: 'Styczeń',
            2: 'Luty',
            3: 'Marzec',
            4: 'Kwiecień',
            5: 'Maj',
            6: 'Czerwiec',
            7: 'Lipiec',
            8: 'Sierpień',
            9: 'Wrzesień',
            10: 'Pażdziernik',
            11: 'Listopad',
            12: 'Grudzień'
        }

    def get_month(self):
        return self._month

    def get_year(self):
        return self._year

    def get_money(self):
        return self.money

    def get_money_amount(self):
        return self.money.amount

    def add_transfer(self, money_to_add: Money):
        if type(money_to_add) != Money:
            raise TypeError
        self.money += money_to_add

    def __repr__(self):
        rep = f"{self.months[self._month]}\n\tWydatki: {repr(self.money)}"
        return rep

# class Goals:
#     def __init__(self, name: str, money: Money):
#         self._name = str(name)
#         if type(money) != Money:
#             raise TypeError
#         self._money = money
#         self.collected_money = Money(money.currency, 0)

#     def get_collected_money_amount(self):
#         return self.collected_money.amount

#     def get_money_amount(self):
#         return self._money.amount

#     def get_name(self):
#         return self._name

#     def get_collected_percent(self):
#         return (self.get_collected_money_amount()*100)/self.get_money_amount()

#     def pay_in(self, amount: int):
#         if type(amount) != int:
#             raise TypeError
#         self.collected_money.add_amount(amount)

#     # def pay_out(self, amount:int): ???

#     def __repr__(self):
#         if self.get_collected_percent() >= 100:
#             rep = f'Goal:{self.get_name()} Collected money: {self.get_collected_percent()}'
#         else:
#             rep = f''
#         return rep
