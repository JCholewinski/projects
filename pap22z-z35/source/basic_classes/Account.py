from basic_classes.Errors import IdIsANumberError, TooLittleMoneyToExchange, TooMuchMoney
from basic_classes.Errors import TooLittleMoneyToCreateDeposit, TooLittleMoneyToTakeaLoan
from basic_classes.Currency_and_Money import Money, Currency
from basic_classes.History_and_Goals import History, Expenses
from basic_classes.Actions import BankTransfer, CurrencyAccount, Deposit
from basic_classes.Actions import Credit, Credit_installments_transfer
from datetime import datetime


class Account:
    """
    Reprezentacja głównego konta, z ilością środków. Takie typowe jak
    wyświetli się po otworzeniu aplikacji
    w nim będziemy dodatkowo przechowywać dodatkowe konta walutowe
    lub lokaty oszczędnościowe.
    Zebyy przejść do lokaty lub do walutowego trzeba przejsc przez
    """
    def __init__(self, id: int, main_account: Money, history: History):
        if type(id) != int:
            raise IdIsANumberError
        if type(main_account) != Money:
            raise TypeError
        if type(history) != History:
            raise TypeError
        self.user_id = id
        self.main_banking_account = main_account
        self.transfers: BankTransfer = []
        self.currency_accounts: CurrencyAccount = []
        self.deposits: Deposit = []
        self.credits: Credit = []
        self.expenses_list: Expenses = []
        self.credit_transfers: Credit_installments_transfer = []
        self.history = history
        self.overdue_credit_installments = 0

    def get_id(self):
        return self.user_id

    def get_money_on_main_account(self):
        return self.main_banking_account

    def get_history(self):
        return self.history

    def get_overdue_credit_instalments(self):
        return self.overdue_credit_installments

    def transfer(self, cash_to_transfer: Money, reciver_id: int, title: str):
        transfer = BankTransfer(self.user_id, reciver_id, cash_to_transfer, title)
        self.history.add_acction(transfer.repr_outcoming())
        self.transfers.append(transfer)
        self.main_banking_account = self.main_banking_account - cash_to_transfer
        self.expenses(cash_to_transfer)
        transfer.sended()
        return transfer

    def recive_transfer(self, transfer: BankTransfer):
        self.main_banking_account = self.main_banking_account + transfer.get_amount()
        transfer.recived()
        self.history.add_acction(transfer.repr_incoming())
        self.transfers.append(transfer)

    def expenses(self, money: Money):
        if type(money) != Money:
            raise TypeError
        date = datetime.today()
        m = int(date.month)
        y = int(date.year)
        for expense in self.expenses_list:
            if expense.get_year() == y and expense.get_month() == m:
                expense.add_transfer(money)
                return
        e = Expenses(m, y, money)
        self.expenses_list.append(e)

    def add_Deposit(self, duration: int, money_to_create: Money, interest_rate: float):
        if self.main_banking_account.amount < money_to_create.amount:
            raise TooLittleMoneyToCreateDeposit
        if money_to_create.currency != self.main_banking_account.currency:
            raise TypeError
        self.main_banking_account.amount -= money_to_create.amount
        deposit = Deposit(duration, money_to_create, interest_rate)
        self.deposits.append(deposit)
        self.history.add_acction(deposit.repr_creation())

    def withdrawal_Deposit(self, deposit: Deposit):
        if type(deposit) != Deposit:
            raise TypeError
        for dep in self.deposits:
            if dep == deposit:
                deposit.done_scrap_date()
                self.main_banking_account.add_amount(deposit.withdrawal().amount)
                self.history.add_acction(deposit.repr_withdrawal())

    def all_active_deposits(self):
        active_deposits = []
        for dep in self.deposits:
            if dep.scrap_date == None:
                active_deposits.append(dep)
        return active_deposits

    def add_Credit(self, duration: int, money: Money, interest_rate: int):
        if self.main_banking_account.amount*2 < money.amount:
            raise TooLittleMoneyToTakeaLoan
        self.main_banking_account.amount += money.amount
        credit = Credit(duration, money, interest_rate)
        self.credits.append(credit)
        self.history.add_acction(credit.repr_creation())

    def credit_installment(self, credit: Credit):
        if type(credit) != Credit:
            raise TypeError
        for c in credits:
            if c == credit:
                i = credit.pay_the_installment()
                self.overdue_credit_installments += i

    def return_all_active_credits(self):
        active_credits = []
        for c in self.credits:
            if datetime.today() < c._end_of_paying_off:
                active_credits.append(c)
        return active_credits

    def credit_pay_off_overdue_installments(self, money: Money):
        if money.amount > self.overdue_credit_installments:
            raise TooMuchMoney
        transfer = Credit_installments_transfer(money)
        self.history.add_acction(repr(transfer))
        self.credit_transfers.append(transfer)
        self.main_banking_account.amount -= money.amount
        self.overdue_credit_installments -= money.amount
        self.expenses(money)
        self.history.add_acction(self.repr_paying_off_overdue_installments(money))

    def repr_paying_off_overdue_installments(self, money):
        rep = f'RATA KREDYTU\nKWOTA: {money}\nGŁÓWNE KONTO: -{money}'
        return rep

    def add_CurrencyAccount(self, currency_for_sale: Money, main_bank_currency: Currency):
        if self.main_banking_account.amount < (currency_for_sale.get_amount_in_main_currency_for_sale()):
            raise TooLittleMoneyToExchange
        self.main_banking_account.amount -= currency_for_sale.get_amount_in_main_currency_for_sale()
        cur_account = CurrencyAccount(currency_for_sale, main_bank_currency)
        cur_account.form()
        self.currency_accounts.append(cur_account)
        self.history.add_acction(cur_account.repr_creation())

    def transfer_CurrencyAccount_to_main_account(self, currency_account_repr: str):
        if type(currency_account_repr) != str:
            raise TypeError
        for cur_acc in self.currency_accounts:
            if currency_account_repr == cur_acc.__repr__():
                self.main_banking_account.add_amount(cur_acc.get_amount_in_main_currency_to_buy())
                cur_acc.scrap()
                self.history.add_acction(cur_acc.repr_transfer_to_main())

    def return_all_active_currency_accounts(self):
        active_accounts = []
        for curr_account in self.currency_accounts:
            if curr_account.scrap_date == None:
                active_accounts.append(curr_account)
        return active_accounts