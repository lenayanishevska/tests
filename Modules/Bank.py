from Modules.CurrentAccount import CurrentAccount
from Modules.SavingsAccount import SavingsAccount


class Bank:
    def __init__(self):
        self.accounts = []

    def open_account(self, account):
        self.accounts.append(account)

    def close_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                print(f"Account {account_number} closed.")

    def pay_dividend(self, dividend_amount):
        for account in self.accounts:
            account.deposit(dividend_amount)

    def update_accounts(self):
        for account in self.accounts:
            if isinstance(account, SavingsAccount):
                account.add_interest()
            elif isinstance(account, CurrentAccount):
                account.send_overdraft_letter()

    def show_accounts(self):
        for account in self.accounts:
            print(account)
