from .account import Account, SavingsAccount, CheckingAccount, SecureAccount


class Bank:
    """Bank class to manage accounts"""

    def __init__(self, name):
        self.name = name
        self.accounts = {}
        print(f"{name} bank initialized")

    def open_account(self, account_type, name, **kwargs):
        """Open a new account"""
        if account_type.lower() == "savings":
            account = SavingsAccount(name, **kwargs)
        elif account_type.lower() == "checking":
            account = CheckingAccount(name, **kwargs)
        elif account_type.lower() == "secure":
            account = SecureAccount(name, **kwargs)
        else:
            account = Account(name, **kwargs)

        self.accounts[account.account_number] = account
        print(f"Account {account.account_number} created for {name}")
        return account

    def get_account(self, account_number):
        """Get an account by number"""
        return self.accounts.get(account_number)

    def list_accounts(self):
        """List all accounts"""
        print(f"{self.name} Bank Accounts:")
        for acc_num, account in self.accounts.items():
            print(f"{acc_num} - {account.name}: ${account.balance}")

    @classmethod
    def set_global_interest_rate(cls, rate):
        """Set global interest rate for all savings accounts"""
        SavingsAccount.interest_rate = rate
        return f"Global interest rate set to {rate}"

    @staticmethod
    def is_business_day(date):
        """Check if given date is a business day"""
        if date.weekday() >= 5:  # 5=Saturday, 6=Sunday
            return False
        return True