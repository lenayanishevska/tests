from Modules.Bank import Bank
from Modules.Account import Account
from Modules.CurrentAccount import CurrentAccount
from Modules.SavingsAccount import SavingsAccount


account1 = SavingsAccount(1, 1000, 3.0)
account2 = CurrentAccount(2, 500, -200)
account3 = Account(3, 1500)

bank = Bank()
bank.open_account(account1)
bank.open_account(account2)
bank.open_account(account3)

bank.show_accounts()

bank.pay_dividend(100)
bank.update_accounts()

bank.show_accounts()
