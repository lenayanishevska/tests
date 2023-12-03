from Modules.Account import Account


class CurrentAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def send_overdraft_letter(self):
        if self.balance < 0:
            print(f"Overdraft letter sent for Account {self.account_number}")
