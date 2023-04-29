import pytest
import sys
sys.path.append("source")
from basic_classes.Account import Account
from basic_classes.Currency_and_Money import Currency, Money
from basic_classes.History_and_Goals import History
from basic_classes.Users import Client, Admin


def test_Client_init():
    zloty = Currency("złoty", "zł", 1)
    cash = Money(zloty, 10000)
    his = History()
    acc = Account(1, cash, his)
    c = Client(1, "jablko321", "Patryk", 637496847, acc, 1)
    assert c.get_id() == 1
    assert c.get_money().currency == zloty
    assert c.get_money() == Money(zloty, 10000)


def test_Admin_init():
    c = Admin("kluska", "Patryk", 637496847)
    assert c.get_name() == "Patryk"
    assert c.get_admin_number() == 637496847


def test_Admin_mcd_name():
    zloty = Currency("złoty", "zł", 1)
    cash = Money(zloty, 10000)
    his = History()
    acc = Account(1, cash, his)
    c = Client(1, "jablko321", "Patryk", 637496847, acc, 1)
    a = Admin("kluska", "Patryk", 637496847)
    a.change_client_name(c, "Kasia")
    assert c.name == "Kasia"


def test_Admin_mcd_password():
    zloty = Currency("złoty", "zł", 1)
    cash = Money(zloty, 10000)
    his = History()
    acc = Account(1, cash, his)
    c = Client(1, "jablko321", "Patryk", 637496847, acc, 1)
    a = Admin("kluska", "Patryk", 637496847)
    a.change_client_password(c, "gruszka2")
    assert c.password == "gruszka2"


def test_Admin_mcd_phone():
    zloty = Currency("złoty", "zł", 1)
    cash = Money(zloty, 10000)
    his = History()
    acc = Account(1, cash, his)
    c = Client(1, "jablko321", "Patryk", 637496847, acc, 1)
    a = Admin("kluska", "Patryk", 637496847)
    a.change_client_phone(c, 632678543)
    assert c.phone == 632678543


def test_Admin_exchange_rate():
    dolar = Currency("dolar", "$", 3.5)
    a = Admin("kluska", "Patryk", 637496847)
    a.exchange_rate(dolar, 4.48)
    assert dolar.get_exchange_rate() == 4.48


def test_Client_logout():
    zloty = Currency("złoty", "zł", 1)
    cash = Money(zloty, 10000)
    his = History()
    acc = Account(1, cash, his)
    c = Client(1, "jablko321", "Patryk", 637496847, acc, 1)
    c.logout()
    assert c.logged == 0


def test_Client_logout2():
    zloty = Currency("złoty", "zł", 1)
    cash = Money(zloty, 10000)
    his = History()
    acc = Account(1, cash, his)
    c = Client(1, "jablko321", "Patryk", 637496847, acc, 0)
    c.logout()
    assert c.logged == 0


def test_Client_login():
    zloty = Currency("złoty", "zł", 1)
    cash = Money(zloty, 10000)
    his = History()
    acc = Account(1, cash, his)
    c = Client(1, "jablko321", "Patryk", 637496847, acc, 0)
    c.login()
    assert c.logged == 1


def test_Client_login():
    zloty = Currency("złoty", "zł", 1)
    cash = Money(zloty, 10000)
    his = History()
    acc = Account(1, cash, his)
    c = Client(1, "jablko321", "Patryk", 637496847, acc, 1)
    c.login()
    assert c.logged == 1
