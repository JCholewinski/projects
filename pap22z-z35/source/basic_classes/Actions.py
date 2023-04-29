from datetime import datetime, timedelta
from dateutil.relativedelta import *
from basic_classes.Errors import IdIsANumberError, InvalidMoneyNumber
from basic_classes.Currency_and_Money import Money, Currency
import math

class BankTransfer:
    """
    Klasa reprezentująca przelew
    """
    def __init__(self, sender_id: int, reciver_id: int, amount: Money, title):
        if type(sender_id) != int or type(reciver_id) != int:
            raise IdIsANumberError
        if type(amount) != Money:
            raise TypeError
        self.sender_id = sender_id
        self.reciver_id = reciver_id
        self.amount = amount
        self.title = str(title)
        self.send_date = None
        self.recive_date = None

    def get_sender_id(self):
        return self.sender_id

    def get_reciver_id(self):
        return self.reciver_id

    def get_amount(self):
        return self.amount

    def sended(self):
        self.send_date = datetime.today()

    def recived(self):
        self.recive_date = datetime.today()

    def set_send_date(self, date):
        self.send_date = date

    def set_recive_date(self, date):
        self.recive_date = date

    def is_sended(self):
        if (self.send_date != None):
            return True
        else:
            return False

    def is_recived(self):
        if (self.recive_date != None):
            return True
        else:
            return False

    def repr_outcoming(self):
        return f"PRZELEW WYCHODZĄCY\nDO: {self.reciver_id}   TYTUŁ: {self.title}\nKWOTA: {self.amount}"

    def repr_incoming(self):
        return f"PRZELEW PRZYCHODZĄCY\nOD: {self.sender_id}   TYTUŁ: {self.title}\nKWOTA: {self.amount}"

    def __str__(self):
        s = f'Transfer: {self.title}\n{repr(self.amount)}'
        return s

    def __repr__(self):
        rep = f'Transfer: {self.title}\n{repr(self.amount)}\n From:{self.get_sender_id()}  To:{self.get_reciver_id()}'
        return rep


class Credit_installments_transfer:
    def __init__(self, amount: Money, date: datetime = None):
        self.amount = amount
        if date == None:
            self.date = datetime.today()
        else:
            self.date = date

    def __repr__(self):
        rep = f'Spłata rat kredytu\nKwota: {repr(self.amount)}'
        return rep


class CurrencyAccount:
    """
    Reprezentacja konta walutowego:
    test repr
    """
    global_id = 0
    def __init__(self, money: Money, main_bank_currency: Currency, form_date: datetime = None, scrap_date: datetime = None):
        if type(money) != Money:
            raise TypeError
        self._money = money
        self.form_date = form_date
        self.scrap_date = scrap_date
        self._main_bank_currency = main_bank_currency
        self._id = 0

    def get_currency(self):
        return self._money.currency

    def get_money(self):
        return self._money

    def get_amount_in_main_currency_to_buy(self):
        return self._money.get_amount_in_main_currency_to_buy()

    def form(self):
        self.form_date = datetime.today()

    def scrap(self):
        self.scrap_date = datetime.today()

    def repr_creation(self):
        return f"KONTO WALUTOWE\nKWOTA: +{self._money}\nGŁÓWNE KONTO: -{Money(self._main_bank_currency, self._money.get_amount_in_main_currency_for_sale())}"

    def repr_transfer_to_main(self):
        return f"KONTO WALUTOWE\nKWOTA: -{self._money}\nGŁÓWNE KONTO: +{Money(self._main_bank_currency, self._money.get_amount_in_main_currency_to_buy())}"

    def __repr__(self): #porawić reprezentacje i dodac numerki
        return f"WALUTA: {self._money.currency.name}\nŚRODKI: {self._money}\nKWOTA ZAKUPU WALUTY: {Money(self._main_bank_currency, self._money.get_amount_in_main_currency_for_sale())}"


class Deposit:
    """
    Reprezentacja lokaty oszczędnościowej
    Oprocentowanie w skali roku
    zakładamy ze w przypadku zerwania umowy przez klienta
    traci on odsetki
    Nie jest to zrobione z banktransfer lub jakos inaczej z zapisem do pliku
    """
    def __init__(self, duration: int, creation_money: Money, interest_rate: float, creation_date: datetime = None, scrap_date: datetime = None):
        if type(duration) != int:
            raise TypeError
        if type(creation_money) != Money:
            raise TypeError
        self._duration = duration  #miesiace
        if creation_money.amount < 0:
            raise InvalidMoneyNumber
        self._creation_money = creation_money
        self._interest_rate_percent = interest_rate
        self.money = Money(creation_money.currency, 0)
        # inrterest rate jest w procentach
        if interest_rate < 0:
            raise ValueError
        self._interest_rate = float(interest_rate/100)
        if creation_date == None:
            self._creation_date = datetime.today()
        else:
            self._creation_date = creation_date
        self.scrap_date = scrap_date
        self._withdrawal_date = self._creation_date + relativedelta(months =+ duration)
        # jak nie dziala to tu ^^^^^^^^

    def get_creation_money(self):
        return self._creation_money

    def get_interest_rate_percent(self):
        return self._interest_rate_percent

    def get_creation_date(self):
        return self._creation_date

    def get_duration(self):
        return self._duration

    def done_scrap_date(self):
        self.scrap_date = datetime.today()

    def days_since_creation(self):
        today = datetime.today()
        days = int((today-self._creation_date).days)
        return days

    def get_money(self):
        days = self.days_since_creation()
        yfunds = self._creation_money.amount*self._interest_rate
        self.money.amount = round(self._creation_money.amount+yfunds*days/365)
        return self.money

    def days_to_withdrawal(self):
        today = datetime.today()
        days = self._withdrawal_date - today
        return days.days

    def withdrawal(self):
        days = self.days_to_withdrawal()
        if int(days) > 0:
            return self._creation_money
        else:
            return self.get_money()

    def __repr__(self):
        rep = f'Lokata: {self.get_duration()}-miesięczna\n\tOdsetki: {self.get_interest_rate_percent()}%\n\tObecna wartość lokaty: {repr(self.get_money())}\n\tWkład początkowy: {repr(self.get_creation_money())}'
        return rep

    def repr_creation(self):
        return f'LOKATA\nKWOTA: +{repr(self.get_creation_money())}\n GŁÓWNE KONTO: -{repr(self.get_creation_money())}'

    def repr_withdrawal(self):
        return f'LOKATA\nKWOTA: -{repr(self.get_money())}\n GŁÓWNE KONTO: +{repr(self.get_money())}'


class Credit:
    def __init__(self, duration: int, money: Money, interest_rate: int, creation_date: datetime = None, last_installment_date: datetime = None, scrap_date: datetime = None):
        if type(duration) != int:
            raise TypeError
        if type(money) != Money:
            raise TypeError
        self._duration = duration  #miesiące
        if money.amount < 0:
            raise InvalidMoneyNumber
        self._money = money
        if interest_rate < 0:
            raise ValueError
        self.interest_rate_percent = interest_rate
        self.interest_rate = interest_rate/100
        if creation_date == None:
            self._creation_date = datetime.today()
        else:
            self._creation_date = creation_date
        if scrap_date == None:
            self._end_of_paying_off = datetime.today() + relativedelta(months=+duration)
        else:
            self._end_of_paying_off = scrap_date
        if last_installment_date == None:
            self.last_installment_date = datetime.today()
        else:
            self.last_installment_date = last_installment_date
        self.paid_off_money = Money(money.currency, 0)
        self.money_to_pay_off = Money(money.currency, self._money.amount - self.paid_off_money.amount)
        self.installment = Money(money.currency, round((self._money.amount/self._duration)*(1+self.interest_rate*(self._duration/12))))
        self._installment_without_rate = money.amount/duration

    def get_installment(self):  # rata
        return self.installment

    def repr_installment(self):
        return repr(self.installment)

    def change_interest_rate(self, new_rate):
        self.interest_rate = float(new_rate/100)
        self.interest_rate_percent = new_rate

    def get_interest_rate_percent(self):
        return self.interest_rate_percent

    def get_creation_date(self):
        return self._creation_date

    def get_borrowed_money(self):
        return self._money

    def get_paid_off_money(self):
        return self.paid_off_money

    def get_money_to_pay_off(self):
        return self.money_to_pay_off

    def days_since_last_installment(self):
        last = min(datetime.today(), self._end_of_paying_off)
        d = last - self.last_installment_date
        return d.days

    def pay_the_installment(self):
        d = self.days_since_last_installment()
        if d > 30:
            self.last_installment_date = self.last_installment_date + relativedelta(months=+int(math.floor(d/30.4)))
            installments = math.floor(d/30.4)*self.get_installment().amount
            self.paid_off_money.amount += math.floor(self.get_borrowed_money().amount/self._duration)
            return installments
        else:
            return 0

    def __str__(self):
        rep = f'Credit {self._duration}-month    Funds:{repr(self._money)}    Interest rate: {self.get_interest_rate_percent()}%'
        return rep

    def __repr__(self):
        rep = f'Kredyt\n\t{self._duration}-miesięczny\n\tWartość:{repr(self._money)}\n\tOprocentowanie: {self.get_interest_rate_percent()}%\n\tPieniądze do spłacenia: {repr(self.get_money_to_pay_off())}'
        return rep

    def repr_creation(self):
        rep = f'KREDYT\nKWOTA: {repr(self.get_borrowed_money())}\nGŁÓWNE KONTO: +{repr(self.get_borrowed_money())}'
        return rep

    # def repr_installment(self):
    #     rep = f'RATA KREDYTU\nKWOTA: {self.get_installment()}\nGŁÓWNE KONTO: -{self.get_installment()}'
    #     return rep



