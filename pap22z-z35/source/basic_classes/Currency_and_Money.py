from basic_classes.Errors import InvalidMoneyNumber


class Currency:
    def __init__(self, name: str, sign: str, exchange_rate: float, buying_rate: float = 0, selling_rate: float = 0):
        self.name = name
        self.sign = sign
        if exchange_rate < 0:
            raise ValueError("Exchange rate must be greater than 0.")
        self.exchange_rate = exchange_rate
        self.buying_rate = buying_rate
        self.selling_rate = selling_rate

    def get_name(self):
        return self.name

    def get_sign(self):
        return self.sign

    def get_exchange_rate(self):
        return self.exchange_rate

    def get_buying_rate(self):
        return self.buying_rate

    def get_selling_rate(self):
        return self.selling_rate

    def __repr__(self):
        rep = f'{self.name+" "+"("+self.sign+")":10}    Kurs kupna: {float(self.buying_rate):3.2}  Kurs sprzedaży: {float(self.selling_rate):3.2}' #reprezentacja waluty
        return rep
        #poprawic __repr__ z groszami np 1.07


class Money:
    def __init__(self, currency: Currency, amount: int):
        if type(currency) != Currency or type(amount) != int:
            raise TypeError
        self.currency = currency
        if amount < 0:
            raise InvalidMoneyNumber("Amount must be greater than 0.")
        self.amount = amount

    def get_pounds(self):
        return int((self.amount)//100)

    def get_pens(self):
        return int((self.amount)%100)

    def get_currency_name(self):
        return self.currency.get_name()

    def get_currency_sign(self):
        return self.currency.get_sign()

    def get_amount_in_main_currency(self):
        return int(self.amount * self.currency.exchange_rate)

    def get_amount_in_main_currency_for_sale(self):
        return int(self.amount * self.currency.selling_rate)

    def get_amount_in_main_currency_to_buy(self):
        return int(self.amount * self.currency.buying_rate)

    def add_amount(self, amount: int):
        self.amount += amount

    def __add__(self, other):
        return Money(self.currency, self.amount + other.amount)

    def __sub__(self, other):
        return Money(self.currency, self.amount - other.amount)

    def __eq__(self, other):
        if self.currency == other.currency and self.amount == other.amount:
            return True
        else:
            return False

    def __repr__(self):
        if self.get_pens() < 10:
            pens = "0" + f"{self.get_pens()}"
        else:
            pens = f"{self.get_pens()}"
        rep = f'{self.get_pounds()}.{pens} {self.currency.get_sign()}' #reprezentacja money
        return rep
