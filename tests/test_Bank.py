from io import StringIO
import unittest
from unittest.mock import patch
from Modules.Bank import Bank, SavingsAccount, CurrentAccount


class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        self.savings_account = SavingsAccount(account_number=123, balance=1000, interest_rate=2)
        self.current_account = CurrentAccount(account_number=321, balance=500, overdraft_limit=100)

        self.bank.open_account(self.savings_account)
        self.bank.open_account(self.current_account)

    def test_open_account(self):
        bank1 = Bank()
        initial_balance = 1000
        account_number = "12345"
        savings_account = SavingsAccount(account_number, initial_balance, interest_rate=5)

        bank1.open_account(savings_account)

        self.assertIn(savings_account, bank1.accounts)

        self.assertEqual(savings_account.balance, initial_balance)

    def test_update_accounts_with_savings_account(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.bank.update_accounts()

            self.assertGreater(self.savings_account.balance, 1000)

            self.assertEqual(mock_stdout.getvalue(), '')

    def test_update_accounts_with_current_account(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.bank.accounts[1].balance -= 600
            self.bank.update_accounts()

            self.assertLess(self.bank.accounts[1].balance, 0)

            expected_message = f'Overdraft letter sent for Account {self.bank.accounts[1].account_number}\n'
            self.assertIn(expected_message, mock_stdout.getvalue())



if __name__ == "__main__":
    unittest.main()
            