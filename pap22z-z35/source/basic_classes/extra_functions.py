from basic_classes.Currency_and_Money import Currency, Money
from basic_classes.Actions import BankTransfer, CurrencyAccount, Deposit, Credit, Credit_installments_transfer
from basic_classes.Users import Client, Admin
from basic_classes.Account import Account
from basic_classes.History_and_Goals import History, Expenses
from datetime import datetime


def reading_currencies(tab_of_currencies_dict):
    currencies = []
    for currency_dict in tab_of_currencies_dict:
        name = currency_dict['name']
        sign = currency_dict['sign']
        rate = float(currency_dict['rate'])
        buying_rate = float(currency_dict['buying_rate'])
        selling_rate = float(currency_dict['selling_rate'])
        currencies.append(Currency(name, sign, rate, buying_rate, selling_rate))
    return currencies


def reading_bank_transfers(tab_of_bank_transfers_dict, main_currency: Currency):
    bank_transfers_tab = []
    for bank_transfer in tab_of_bank_transfers_dict:
        s_id = int(bank_transfer['sender_id'])
        r_id = int(bank_transfer['reciver_id'])
        amount = Money(main_currency, int(bank_transfer['amount']))
        title = bank_transfer['title']
        s_d = bank_transfer['send_date']
        r_d = bank_transfer['recive_date']
        send_date = datetime(s_d[0], s_d[1], s_d[2], s_d[3], s_d[4], s_d[5])
        recive_date = datetime(r_d[0], r_d[1], r_d[2], r_d[3], r_d[4], r_d[5])
        transfer = BankTransfer(s_id, r_id, amount, title)
        transfer.set_send_date(send_date)
        transfer.set_recive_date(recive_date)
        bank_transfers_tab.append(transfer)
    return bank_transfers_tab


def reading_currency_accounts(currency_accounts_dict, currencies):
    currency_accounts = []
    for cur_account in currency_accounts_dict:
        for currency in currencies:
            if currency.sign == cur_account['currency_sign']:
                cash = Money(currency, int(cur_account['amount']))
                f_d = cur_account['form_date']
                s_d = cur_account['scrap_date']
                form_date = datetime(f_d[0], f_d[1], f_d[2], f_d[3], f_d[4], f_d[5])
                if cur_account['scrap_date'] == [0]:
                    scrap_date = None
                else:
                    scrap_date = datetime(s_d[0], s_d[1], s_d[2], s_d[3], s_d[4], s_d[5])
                currency_accounts.append(CurrencyAccount(cash, currencies[0], form_date, scrap_date))
    return currency_accounts


def reading_deposits(deposits_dict, currencies):
    deposits = []
    for deposit in deposits_dict:
        duration = int(deposit['duration'])
        creation_money = Money(currencies[0], int(deposit['amount']))
        interest_rate = float(deposit['interest_rate'])
        c_d = deposit["creation_date"]
        s_d = deposit["scrap_date"]
        creation_date = datetime(c_d[0], c_d[1], c_d[2], c_d[3], c_d[4], c_d[5])
        if deposit['scrap_date'] == [0]:
            scrap_date = None
        else:
            scrap_date = datetime(s_d[0], s_d[1], s_d[2], s_d[3], s_d[4], s_d[5])
        deposits.append(Deposit(duration, creation_money, interest_rate, creation_date, scrap_date))
    return deposits


def reading_credits(credits_dict, currencies):
    credits = []
    for credit in credits_dict:
        duration = int(credit['duration'])
        money = Money(currencies[0], int(credit['amount']))
        interest_rate = float(credit['interest_rate'])
        c_d = credit['creation_date']
        l_d = credit['last_installment_date']
        s_d = credit['scrap_date']
        creation_date = datetime(c_d[0], c_d[1], c_d[2], c_d[3], c_d[4], c_d[5])
        last_installment_date = datetime(l_d[0], l_d[1], l_d[2], l_d[3], l_d[4], l_d[5])
        scrap_date = datetime(s_d[0], s_d[1], s_d[2], s_d[3], s_d[4], s_d[5])
        credits.append(Credit(duration, money, interest_rate, creation_date, last_installment_date, scrap_date))
    return credits


def reading_expenses(expenses_dict, currencies):
    expenses = []
    for expense in expenses_dict:
        month = int(expense['month'])
        year = int(expense['year'])
        money = Money(currencies[0], int(expense['amount']))
        expenses.append(Expenses(month, year, money))
    return expenses


def reading_credit_installments(credit_installments_dict, currencies):
    credit_installments = []
    for credit_installment in credit_installments_dict:
        money = Money(currencies[0], int(credit_installment['amount']))
        c_d = credit_installment['date']
        date = datetime(c_d[0], c_d[1], c_d[2], c_d[3], c_d[4], c_d[5])
        credit_installments.append(Credit_installments_transfer(money, date))
    return credit_installments


def reading_clients(clients_dict, currencies):
    tab_clients = []
    for client in clients_dict:
        id = int(client['id'])
        password = client['pass']
        name = client['name']
        phone_number = int(client['phone'])
        main_account = Account(int(client['main_acc']['id']), Money(currencies[0], int(client['main_acc']['money'])), History())
        main_account.transfers = reading_bank_transfers(client["main_acc"]["bank_transfers"], currencies[0])
        main_account.currency_accounts = reading_currency_accounts(client["main_acc"]['currency_accounts'], currencies)
        main_account.deposits = reading_deposits(client['main_acc']['deposits'], currencies)
        main_account.credits = reading_credits(client['main_acc']['credits'], currencies)
        main_account.expenses_list = reading_expenses(client['main_acc']['expenses'], currencies)
        main_account.credit_transfers = reading_credit_installments(client['main_acc']['credit_transfer'], currencies)
        main_account.overdue_credit_installments = int(client['main_acc']['overdue_credit_installments'])
        tab_clients.append(Client(id, password, name, phone_number, main_account))
    return tab_clients


def reading_admins(admins_dict):
    tab_admins = []
    for admin in admins_dict:
        id = int(admin['id'])
        name = admin['name']
        password = admin['password']
        tab_admins.append(Admin(password, name, id))
    return tab_admins


def reading_deposits_rates(deposits_rates_dict):
    number_dict_deposits_rates = {}
    items = deposits_rates_dict.items()
    for deposit_rate in items:
        number_dict_deposits_rates[int(deposit_rate[0])]=deposit_rate[1]
    return number_dict_deposits_rates


def reading_credit_rates(credit_rates_dict):
    number_dict_credits_rates = {}
    items = credit_rates_dict.items()
    for credit_rates in items:
        number_dict_credits_rates[int(credit_rates[0])]=credit_rates[1]
    return number_dict_credits_rates


def add_clients_history(clients): #dodać tu jeszcze historie
    for client in clients:
        for bank_transfer in client.get_account().transfers:
            if bank_transfer.sender_id == client._id:
                client.get_account().history.add_acction(bank_transfer.repr_outcoming(), bank_transfer.send_date)
            else:
                client.get_account().history.add_acction(bank_transfer.repr_incoming(), bank_transfer.recive_date)
        for currency_account in client.get_account().currency_accounts:
            client.get_account().history.add_acction(currency_account.repr_creation(), currency_account.form_date)
            if currency_account.scrap_date != None:
                client.get_account().history.add_acction(currency_account.repr_transfer_to_main(), currency_account.scrap_date)
        for deposit in client.get_account().deposits:
            client.get_account().history.add_acction(deposit.repr_creation(), deposit._creation_date)
            if currency_account.scrap_date != None:
                client.get_account().history.add_acction(deposit.repr_withdrawal(), deposit.scrap_date)
        for credit in client.get_account().credits:
            client.get_account().history.add_acction(credit.repr_creation(), credit._creation_date)
        for credit_installment in client.get_account().credit_transfers:
            client.get_account().history.add_acction(credit_installment.__repr__(), credit_installment.date)
    client.get_account().history.sort_history_by_date()


def write_currencies(currencies: Currency = []):
    tab_dict_of_currencies = []
    for currency in currencies:
        tab_dict_of_currencies.append({
                "name": f"{currency.name}",
                "sign": f"{currency.sign}",
                "rate": f"{currency.exchange_rate}",
                "buying_rate": f"{currency.buying_rate}",
                "selling_rate": f"{currency.selling_rate}"
                })
    return tab_dict_of_currencies


def write_bank_transfers(client: Client):
    tab_of_dict_of_bank_transfers = []
    for bank_transfer in client._main_account.transfers:
        s_d = bank_transfer.send_date
        r_d = bank_transfer.recive_date
        dict_transfer = {
            "sender_id": f"{bank_transfer.sender_id}",
            "reciver_id": f"{bank_transfer.reciver_id}",
            "amount": f"{bank_transfer.amount.amount}",
            "title": f"{bank_transfer.title}",
            "send_date": [s_d.year, s_d.month, s_d.day, s_d.hour, s_d.minute, s_d.second],
            "recive_date": [r_d.year, r_d.month, r_d.day, r_d.hour, r_d.minute, r_d.second]
        }
        tab_of_dict_of_bank_transfers.append(dict_transfer)
    return tab_of_dict_of_bank_transfers


def write_currency_account(client: Client):
    tab_dict_of_currency_accounts = []
    for currency_account in client._main_account.currency_accounts:
        f_d = currency_account.form_date
        if currency_account.scrap_date == None:
            scrap_date_format = [0]
        else:    
            s_d = currency_account.scrap_date
            scrap_date_format = [s_d.year, s_d.month, s_d.day, s_d.hour, s_d.minute, s_d.second]
        dict_curr_acc = {
            "currency_sign": f"{currency_account._money.currency.sign}",
            "amount": f"{currency_account._money.amount}",
            "form_date": [f_d.year, f_d.month, f_d.day, f_d.hour, f_d.minute, f_d.second],
            "scrap_date": scrap_date_format       
        }
        tab_dict_of_currency_accounts.append(dict_curr_acc)
    return tab_dict_of_currency_accounts


def write_deposits(client: Client):
    tab_dict_of_depostis = []
    for deposit in client._main_account.deposits:
        c_d = deposit._creation_date
        if deposit.scrap_date == None:
            scrap_date_format = [0]
        else:    
            s_d = deposit.scrap_date
            scrap_date_format = [s_d.year, s_d.month, s_d.day, s_d.hour, s_d.minute, s_d.second]
        dict_deposit = {
            "duration": f"{deposit._duration}",
            "amount": f"{deposit._creation_money.amount}",
            "interest_rate": f"{deposit._interest_rate_percent}",
            "creation_date": [c_d.year, c_d.month, c_d.day, c_d.hour, c_d.minute, c_d.second],
            "scrap_date": scrap_date_format
        }
        tab_dict_of_depostis.append(dict_deposit)
    return tab_dict_of_depostis


def write_credits(client: Client):
    tab_dict_of_credits = []
    for credit in client._main_account.credits:
        c_d = credit._creation_date
        l_d = credit.last_installment_date
        s_d = credit._end_of_paying_off
        dict_credit = {
            "duration": f"{credit._duration}",
            "amount": f"{credit._money.amount}",
            "interest_rate": f"{credit.interest_rate_percent}",
            "creation_date": [c_d.year, c_d.month, c_d.day, c_d.hour, c_d.minute, c_d.second],
            "last_installment_date": [l_d.year, l_d.month, l_d.day, l_d.hour, l_d.minute, l_d.second],
            "scrap_date": [s_d.year, s_d.month, s_d.day, s_d.hour, s_d.minute, s_d.second]
        }
        tab_dict_of_credits.append(dict_credit)
    return tab_dict_of_credits


def write_expenses(client: Client):
    tab_dict_of_expenses = []
    for expense in client._main_account.expenses_list:
        tab_dict_of_expenses.append({
            "month": f"{expense._month}",
            "year": f"{expense._year}",
            "amount": f"{expense.money.amount}"
        })
    return tab_dict_of_expenses


def write_credit_transfer(client: Client):
    tab_dict_of_credit_transfer = []
    for credit_transfer in client._main_account.credit_transfers:
        c_d = credit_transfer.date
        tab_dict_of_credit_transfer.append({
            "amount": f"{credit_transfer.amount.amount}",
            "date": [c_d.year, c_d.month, c_d.day, c_d.hour, c_d.minute, c_d.second]
        })
    return tab_dict_of_credit_transfer


def write_clients(clients: Client = []):
    tab_dict_of_clients = []
    for client in clients:
        tab_dict_of_clients.append({
                "id": f"{client._id}",
                "pass": f"{client.password}",
                "name": f"{client.name}",
                "phone": f"{client.phone}",
                "main_acc": {
                    "id": f"{client._main_account.user_id}",
                    "money": f"{client._main_account.main_banking_account.amount}",
                    "bank_transfers": write_bank_transfers(client),
                    "currency_accounts": write_currency_account(client),
                    "deposits": write_deposits(client),
                    "credits": write_credits(client),
                    "expenses": write_expenses(client),
                    "credit_transfer": write_credit_transfer(client),
                    "overdue_credit_installments": f"{client._main_account.overdue_credit_installments}"
                }
            })
    return tab_dict_of_clients


def write_admins(admins: Admin = []):
    tab_dict_of_admins = []
    for admin in admins:
        tab_dict_of_admins.append({
            "id": f"{admin._admin_n}",
            "name": f"{admin._name}",
            "password": f"{admin.password}"
        })
    return tab_dict_of_admins


def write_deposits_rates(deposits):
    dict_deposits_rates = {}
    items = deposits.items()
    for deposit_rate in items:
        dict_deposits_rates[str(deposit_rate[0])]=deposit_rate[1]
    return dict_deposits_rates


def write_credits_rates(credits):
    dict_credits_rates = {}
    items = credits.items()
    for credit_rate in items:
        dict_credits_rates[str(credit_rate[0])]=credit_rate[1]
    return dict_credits_rates