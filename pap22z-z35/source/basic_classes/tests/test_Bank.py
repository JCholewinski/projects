import pytest
import sys
sys.path.append("source")
from basic_classes.Errors import TooLittleMoneyToTakeaLoan
from basic_classes.Users import Client, Admin
from basic_classes.Currency_and_Money import Currency, Money
from basic_classes.History_and_Goals import History
from basic_classes.Actions import BankTransfer, CurrencyAccount, Deposit, Credit
from basic_classes.Actions import Credit_installments_transfer
from basic_classes.Account import Account
from basic_classes.Errors import InvalidLoginPassword, InvalidUserId
from basic_classes.Bank import Bank
import datetime


#Testy Currency


def test_currency_init():
    dolar = Currency("dolar", "$", 4)
    assert dolar.get_name() == "dolar"
    assert dolar.get_sign() == "$"
    assert dolar.get_exchange_rate() == 4


def test_currency_repr():
    dolar = Currency("dolar", "$", 4, 3.8, 4.2)
    assert dolar.get_name() == "dolar"
    assert dolar.get_sign() == "$"
    assert repr(dolar) == 'dolar ($)     Kurs kupna: 3.8  Kurs sprzedaży: 4.2'


# Testy Money

def test_Money_init():
    dolar = Currency("dolar", "$", 4)
    a1 = Money(dolar, 5000)
    assert a1.get_pounds() == 50
    assert a1.get_pens() == 0
    assert a1.get_currency_name() == "dolar"


def test_Money_repr():
    dolar = Currency("dolar", "$", 4)
    a1 = Money(dolar, 5000)
    assert a1.get_pounds() == 50
    assert a1.get_pens() == 0
    assert a1.get_currency_name() == "dolar"
    assert repr(a1) == '50.00 $'


def test_Money_with_pens():
    dolar = Currency("dolar", "$", 4)
    a1 = Money(dolar, 5005)
    assert a1.get_pounds() == 50
    assert a1.get_pens() == 5


def test_Money_round():
    dolar = Currency("dolar", "$", 4)
    a1 = Money(dolar, 5027)
    assert a1.get_pounds() == 50
    assert a1.get_pens() == 27


def test_Money_eq():
    dolar = Currency("dolar", "$", 4)
    a1 = Money(dolar, 20110)
    a2 = Money(dolar, 20110)
    assert a1 == a2


def test_Money_sub():
    dolar = Currency("dolar", "$", 4)
    a1 = Money(dolar, 20110)
    a2 = Money(dolar, 110)
    assert a1 - a2 == Money(dolar, 20000)


# Testy BankTransfer


def test_BankTransfer_init():
    dolar = Currency("dolar", "$", 4)
    a1 = Money(dolar, 20000)
    t1 = BankTransfer(1, 2, a1, "title")
    assert t1.get_reciver_id() == 2
    assert t1.get_sender_id() == 1
    assert t1.get_amount() == a1


def test_BankTransfer_repr():
    dolar = Currency("dolar", "$", 4)
    a1 = Money(dolar, 5000)
    t1 = BankTransfer(1, 2, a1, "title")
    assert t1.get_reciver_id() == 2
    assert t1.get_sender_id() == 1
    assert t1.get_amount() == a1
    assert str(t1) == 'Transfer: title\n50.00 $'


def test_BankTransfer_sended():
    dolar = Currency("dolar", "$", 4)
    a1 = Money(dolar, 20000)
    t1 = BankTransfer(1, 2, a1, "title")
    t1.sended()
    t1.recived()
    assert t1.is_sended() == True
    assert t1.is_recived() == True


# Testy Account


def test_Account_init():
    zloty = Currency("złoty", "zł", 1)
    cash = Money(zloty, 10000)
    history = History()
    acc = Account(13, cash, history)
    assert acc.get_id() == 13
    assert acc.get_money_on_main_account() == cash
    assert acc.get_history() == history


def test_Account_transfer():
    zloty = Currency("złoty", "zł", 1)
    cash = Money(zloty, 10000)
    cash_on_accouont = Money(zloty, 100000)
    history = History()
    acc1 = Account(14, cash_on_accouont, history)
    acc2 = Account(13, cash, history)
    transfer = acc1.transfer(cash, acc2.get_id(), "tytuł")
    acc2.recive_transfer(transfer)
    assert acc1.get_money_on_main_account() == cash_on_accouont - cash
    assert acc2.get_money_on_main_account() == cash + cash


def test_expenses():
    zloty = Currency("złoty", "zł", 1)
    cash = Money(zloty, 10000)
    cash_on_accouont = Money(zloty, 100000)
    history = History()
    acc1 = Account(15, cash_on_accouont, history)
    acc2 = Account(13, cash, history)
    transfer = acc1.transfer(cash, acc2.get_id(), "tytuł")
    acc2.recive_transfer(transfer)
    assert acc1.expenses_list[0].get_month() == 1
    assert acc1.expenses_list[0].get_year() == 2023
    assert acc1.expenses_list[0].get_money_amount() == 10000


def test_add_deposit():
    zloty = Currency("złoty", "zł", 1)
    cash_on_accouont = Money(zloty, 100000)
    history = History()
    acc1 = Account(15, cash_on_accouont, history)
    m = Money(zloty, 20000)
    acc1.add_Deposit(3, m, 3)
    assert acc1.get_money_on_main_account().amount == 80000
    assert acc1.deposits[0].get_creation_money().amount == 20000


def test_withdrawal_deposit():
    zloty = Currency("złoty", "zł", 1)
    cash_on_accouont = Money(zloty, 100000)
    history = History()
    acc1 = Account(15, cash_on_accouont, history)
    m = Money(zloty, 20000)
    acc1.add_Deposit(3, m, 3)
    assert acc1.get_money_on_main_account().amount == 80000
    assert len(acc1.deposits) == 1
    assert len(acc1.all_active_deposits()) == 1
    acc1.withdrawal_Deposit(acc1.deposits[0])
    assert acc1.get_money_on_main_account().amount == 100000
    assert len(acc1.all_active_deposits()) == 0


def test_add_Credit():
    zloty = Currency("złoty", "zł", 1)
    cash_on_accouont = Money(zloty, 100000)
    history = History()
    acc1 = Account(15, cash_on_accouont, history)
    m = Money(zloty, 20000)
    acc1.add_Credit(6, m, 4)
    assert len(acc1.credits) == 1
    assert acc1.credits[0].get_paid_off_money().amount == 0


def test_add_Credit_too_little_money():
    zloty = Currency("złoty", "zł", 1)
    cash_on_accouont = Money(zloty, 1000)
    history = History()
    acc1 = Account(15, cash_on_accouont, history)
    m = Money(zloty, 20000)
    with pytest.raises(TooLittleMoneyToTakeaLoan):
        acc1.add_Credit(6, m, 4)
    assert len(acc1.credits) == 0


def test_credit_pay_overdue_installments():
    zloty = Currency("złoty", "zł", 1)
    cash_on_accouont = Money(zloty, 10000)
    history = History()
    acc1 = Account(15, cash_on_accouont, history)
    m = Money(zloty, 2000)
    acc1.overdue_credit_installments = 3000
    acc1.credit_pay_off_overdue_installments(m)
    assert len(acc1.credit_transfers) == 1
    assert acc1.overdue_credit_installments == 1000
    assert acc1.get_money_on_main_account().amount == 8000
    assert acc1.expenses_list[0].get_money_amount() == 2000


# def test_Bank_init():
#     zloty = Currency("złoty", "zł", 1)
#     cash = Money(zloty, 10000)
#     cash_on_accouont = Money(zloty, 10000)
#     c1 = Client()
#     c2 = Client()


# Testy Currency Account


def test_CurrencyAccount_init():
    zloty = Currency("złoty", "zł", 1)
    currency = Currency("dolar", "$", 4)
    funds = Money(currency, 40000)
    currencyaccount = CurrencyAccount(funds, zloty)
    assert currencyaccount.get_currency() == currency
    assert currencyaccount.get_currency().get_name() == "dolar"
    assert currencyaccount.get_currency().get_sign() == "$"
    assert currencyaccount.get_currency().get_exchange_rate() == 4
    assert currencyaccount.get_money() == funds
    assert currencyaccount.get_money().amount == 40000
    assert currencyaccount.get_money().get_currency_name() == "dolar"
    assert currencyaccount.get_money().get_pounds() == 400


def test_CurrencyAccount_in_Bank():
    zloty = Currency("złoty", "zł", 1)
    dolar = Currency("dolar", "$", 4, 3.8, 4.2)
    cash = Money(zloty, 100000)
    his = History()
    acc = Account(1, cash, his)
    c = Client(1, "jablko321", "Patryk", 637496847, acc, 0)
    clients = [c]
    a = Admin("kluska", "Patryk", 637496847)
    admins = [a]
    currencies = [zloty, dolar]
    bank = Bank(clients, admins, currencies)
    bank.main_currency = zloty
    bank.current_user = c
    bank.create_currency_account(10000, dolar.name)
    assert len(c.get_account().currency_accounts) == 1
    assert c.get_account().main_banking_account.amount == 100000 - 42000
    assert c.get_account().currency_accounts[0]._money.amount == 10000
    assert acc.return_all_active_currency_accounts()[0].scrap_date == None


def test_CurrencyAccount_in_Bank_transfer_to_main_account():
    zloty = Currency("złoty", "zł", 1)
    dolar = Currency("dolar", "$", 4, 3.8, 4.2)
    cash = Money(zloty, 100000)
    his = History()
    acc = Account(1, cash, his)
    c = Client(1, "jablko321", "Patryk", 637496847, acc, 0)
    clients = [c]
    a = Admin("kluska", "Patryk", 637496847)
    admins = [a]
    currencies = [zloty, dolar]
    bank = Bank(clients, admins, currencies) #zabezpieczyć, przed tym, że musi być zawsze główna waluta w banku
    bank.main_currency = zloty
    bank.current_user = c
    bank.create_currency_account(10000, dolar.name)
    bank.transfer_currency_to_main_account(c.get_account().currency_accounts[0].__repr__())
    assert len(c.get_account().return_all_active_currency_accounts()) == 0
    assert c.get_account().main_banking_account.amount == 100000 - 42000 + 38000


# Testy Deposit


def test_Deposit_init():
    currency = Currency("dolar", "$", 4)
    creation_money = Money(currency, 40000)
    deposit = Deposit(9, creation_money, 3)
    assert deposit.get_creation_money() == creation_money
    assert deposit.get_interest_rate_percent() == 3
    assert deposit.get_duration() == 9


def test_deposit_get_money(monkeypatch):
    currency = Currency("dolar", "$", 4)
    creation_money = Money(currency, 60000)
    deposit = Deposit(6, creation_money, 3)
    def days_monkeypatch():
        return 82
    monkeypatch.setattr(deposit, 'days_since_creation', days_monkeypatch)
    assert deposit.days_since_creation() == 82
    assert deposit.get_money().amount == 60404


def test_deposit_get_money2(monkeypatch):
    currency = Currency("dolar", "$", 4)
    creation_money = Money(currency, 10000000)
    deposit = Deposit(24, creation_money, 8)
    def days_monkeypatch():
        return 395
    monkeypatch.setattr(deposit, 'days_since_creation', days_monkeypatch)
    assert deposit.days_since_creation() == 395
    assert deposit.get_money().amount == 10865753


def test_deposit_withdrawal_b4_withdrawal_date(monkeypatch):
    currency = Currency("dolar", "$", 4)
    creation_money = Money(currency, 10000000)
    deposit = Deposit(24, creation_money, 8)
    def days_to_w_monkeypatch():
        return 24
    monkeypatch.setattr(deposit, 'days_to_withdrawal', days_to_w_monkeypatch)
    assert deposit.days_to_withdrawal() == 24
    assert deposit.withdrawal().amount == 10000000


def test_deposit_withdrawal_after_withdrawal_date(monkeypatch):
    currency = Currency("dolar", "$", 4)
    creation_money = Money(currency, 10000)
    deposit = Deposit(3, creation_money, 2)
    def days_since_c_monkeypatch():
        return 100
    def days_to_w_monkeypatch():
        return -8
    monkeypatch.setattr(deposit, 'days_since_creation', days_since_c_monkeypatch)
    assert deposit.days_since_creation() == 100
    assert deposit.get_money().amount == 10055
    monkeypatch.setattr(deposit, 'days_to_withdrawal', days_to_w_monkeypatch)
    assert deposit.days_to_withdrawal() == -8
    assert deposit.withdrawal().amount == 10055


def test_deposit_in_Bank():
    zloty = Currency("złoty", "zł", 1)
    dolar = Currency("dolar", "$", 4, 3.8, 4.2)
    cash = Money(zloty, 100000)
    his = History()
    acc = Account(1, cash, his)
    c = Client(1, "jablko321", "Patryk", 637496847, acc, 0)
    clients = [c]
    a = Admin("kluska", "Patryk", 637496847)
    admins = [a]
    currencies = [zloty, dolar]
    bank = Bank(clients, admins, currencies)
    bank.main_currency = zloty
    bank.current_user = c
    bank.deposits = {
        3: 6
    }
    bank.create_deposit(3, 20000)
    assert len(c.get_account().deposits) == 1
    assert c.get_account().deposits[0].get_money().amount == 20000
    assert c.get_account().get_money_on_main_account().amount == 80000
    bank.withdrawal_deposit(repr(c.get_account().deposits[0]))
    assert len(c.get_account().deposits) == 1
    assert len(c.get_account().all_active_deposits()) == 0
    assert c.get_account().get_money_on_main_account().amount == 100000


# Testy Credit


def test_Credit_init():
    currency = Currency("dolar", "$", 4)
    money = Money(currency, 36000)
    credit = Credit(6, money, 3)
    assert credit.interest_rate == 0.03
    assert credit.get_installment().amount == 6090
    assert credit.get_borrowed_money().amount == 36000
    assert credit.get_paid_off_money().amount == 0
    assert credit.get_money_to_pay_off().amount == 36000
    credit.change_interest_rate(4)
    assert credit.get_interest_rate_percent() == 4
    assert credit._installment_without_rate == 6000


def test_Credit_installment():
    currency = Currency("dolar", "$", 4)
    money = Money(currency, 40000)
    credit = Credit(5, money, 5)
    assert credit.get_installment().amount == 8167


def test_Credit_installment2():
    currency = Currency("dolar", "$", 4)
    money = Money(currency, 23421)
    credit = Credit(5, money, 5)
    assert credit.get_installment().amount == 4782


def test_Credit_installment3():
    currency = Currency("dolar", "$", 4)
    money = Money(currency, 217)
    credit = Credit(1, money, 1)
    assert credit.get_installment().amount == 217


def test_Credit_pay_the_installment(monkeypatch):
    currency = Currency("dolar", "$", 4)
    money = Money(currency, 30000)
    credit = Credit(6, money, 3)
    assert credit.get_installment().amount == 5075
    # monkeypatch.setattr(credit, '_creation_date', datetime.date(2022, 10, 5))
    # monkeypatch.setattr(credit, 'last_installment_date', datetime.date(2022, 10, 5))
    # monkeypatch.setattr(credit, '_end_of_paying_off', datetime.date(2023, 4, 5))
    def dni_monkeypatch():
        return 92
    monkeypatch.setattr(credit, 'days_since_last_installment', dni_monkeypatch)
    assert credit.days_since_last_installment() == 92
    overdue_installments = credit.pay_the_installment()
    assert overdue_installments == 15225


def test_credit_pay_the_installment2(monkeypatch):
    currency = Currency("dolar", "$", 4)
    money = Money(currency, 500000)
    credit = Credit(24, money, 3)
    assert credit.get_installment().amount == 22083
    def dni_monkeypatch():
        return 730
    monkeypatch.setattr(credit, 'days_since_last_installment', dni_monkeypatch)
    overdue_installments = credit.pay_the_installment()
    assert overdue_installments == 529992


def test_Credit_in_Bank():
    zloty = Currency("złoty", "zł", 1)
    dolar = Currency("dolar", "$", 4, 3.8, 4.2)
    cash = Money(zloty, 100000)
    his = History()
    acc = Account(1, cash, his)
    c = Client(1, "jablko321", "Patryk", 637496847, acc, 0)
    clients = [c]
    a = Admin("kluska", "Patryk", 637496847)
    admins = [a]
    currencies = [zloty, dolar]
    bank = Bank(clients, admins, currencies)
    bank.main_currency = zloty
    bank.current_user = c
    bank.credits = {
        6: 6
    }
    bank.create_credit(6, 10000)
    assert len(c.get_account().credits) == 1
    assert c.get_account().credits[0].get_borrowed_money().amount == 10000


# Testy Credit Installments Transfer


def test_Credit_installments_transfer_init():
    currency = Currency("dolar", "$", 4)
    money = Money(currency, 10000)
    t = Credit_installments_transfer(money)
    assert t.amount.amount == 10000


# Testy Bank


def test_Bank_gettery():
    zloty = Currency("złoty", "zł", 1)
    cash = Money(zloty, 10000)
    his = History()
    acc = Account(1, cash, his)
    c = Client(1, "jablko321", "Patryk", 637496847, acc, 0)
    clients = [c]
    a = Admin("kluska", "Patryk", 637496847)
    admins = [a]
    currencies = [zloty]
    b = Bank(clients, admins, currencies)
    b.current_user = c
    assert b.current_user.get_money() == cash
    assert b.current_user.get_money().amount == 10000
    assert b.get_user_money() == Money(zloty, 10000)
    assert b.get_user_money_currency() == zloty


def test_bank_transfery():
    zloty = Currency("złoty", "zł", 1)
    cash = Money(zloty, 10000)
    cash2 = Money(zloty, 3000)
    casht = Money(zloty, 1500)
    his = History()
    his2 = History()
    acc2 = Account(23, cash2, his2)
    acc = Account(1, cash, his)
    c1 = Client(23, "kot343", "Waldek", 434567232, acc2)
    c = Client(1, "jablko321", "Patryk", 637496847, acc, 0)
    clients = [c, c1]
    a = Admin("kluska", "Patryk", 637496847)
    admins = [a]
    currencies = [zloty]
    b = Bank(clients, admins, currencies)
    b.current_user = c
    b.user_transfer(casht, 23, "test przelewu")
    assert b.get_user_money() == Money(zloty, 8500)


def test_bank_read_file():
    bank = Bank()
    bank.read_from_file("source/data_base/bank_data.json")
    bank.write_to_file("source/data_base/testing_file.json")
    client = bank.find_user_from_id(1)
    assert bank.main_currency.get_name() == "złoty"
    assert bank.main_currency.get_sign() == "zł"
    assert bank.main_currency.get_exchange_rate() == 1
    assert bank.main_currency.buying_rate == 1
    assert bank.currencies[1].sign == "$"
    assert len(bank.get_currencies()) == 4
    assert client.name == "Patryk"
    assert client.logged == 0
    assert client.get_money().currency == bank.main_currency
    assert client.get_money() == Money(bank.main_currency, 10000)
    assert client._main_account.transfers[0].sender_id == 1
    assert client._main_account.currency_accounts[0]._money.currency == bank.currencies[1]
    assert client._main_account.deposits[0]._duration == 3
    assert client._main_account.credits[0].interest_rate_percent == 5
    assert client._main_account.expenses_list[0]._month == 12
    assert client._main_account.overdue_credit_installments == 1
    assert bank.admins[0].password == "admin"
    assert bank.deposits[3] == 2
    assert bank.credits[6] == 5
    assert len(client._main_account.deposits) == 1


# def test_extended_reading_from_file():
#     bank = Bank()
#     bank.read_from_file("source/data_base/testing_file.json")
#     client = bank.find_user_from_id(1)
#     assert client._main_account.history.transactions[0][0].sender_id == 1
#     assert client._main_account.history.transactions[0][0].reciver_id == 3
#     assert client._main_account.history.transactions[0][0].amount.amount == 1000
#     assert client._main_account.history.transactions[0][0].title == "przelew"
#     assert client._main_account.history.transactions[0][0].send_date == datetime(2022, 12, 17, 10, 10, 10)
#     assert client._main_account.history.transactions[0][0].recive_date == datetime(2022, 12, 17, 10, 11, 10)