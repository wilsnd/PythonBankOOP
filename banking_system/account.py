from abc import ABC, abstractmethod


class BankAccount(ABC):
    """Abstract base class for all bank accounts"""
    account_count = 0

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @property
    @abstractmethod
    def balance(self):
        pass


class Account(BankAccount):
    """Base account implementation"""

    def __init__(self, name, balance=0):
        self.name = name
        self._balance = balance  # Protected attribute

        # Auto-increment account number
        BankAccount.account_count += 1
        self.account_number = f"ACC{BankAccount.account_count:04d}"

    @property
    def balance(self):
        """Get the current balance"""
        return self._balance

    def deposit(self, amount):
        """Deposit money into the account"""
        if amount > 0:
            self._balance += amount
            return f"Deposited ${amount}. New balance: ${self._balance}"
        return "Invalid amount"

    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return f"Withdrawn ${amount}. New balance: ${self._balance}"
        return "Invalid amount or insufficient funds"

    def info(self):
        """Display account information"""
        print(f"{self.name}'s balance: ${self._balance}")

    def __str__(self):
        return f"Account: {self.name}, Balance: ${self._balance}"

    def transfer(self, destination, amount):
        """Transfer money to another account"""
        if self.withdraw(amount) != "Invalid amount or insufficient funds":
            destination.deposit(amount)
            return f"Transferred ${amount} to {destination.name}"
        return "Transfer failed"


class SavingsAccount(Account):
    """Savings account with interest"""

    def __init__(self, name, interest_rate=0.01, balance=0):
        super().__init__(name, balance)
        self.interest_rate = interest_rate
        self.account_number = f"SAV{BankAccount.account_count:04d}"

    def add_interest(self):
        """Add interest to the account"""
        interest = self._balance * self.interest_rate
        self._balance += interest
        return f"Added ${interest:.2f} interest. New balance: ${self._balance:.2f}"

    def withdraw(self, amount):
        """Withdraw with minimum balance check"""
        if self._balance - amount < 100:  # minimum $100 balance
            return "Cannot withdraw. Minimum balance of $100 required."
        return super().withdraw(amount)


class CheckingAccount(Account):
    """Checking account with transaction fee"""

    def __init__(self, name, fee=1, balance=0):
        super().__init__(name, balance)
        self.fee = fee
        self.account_number = f"CHK{BankAccount.account_count:04d}"

    def withdraw(self, amount):
        """Withdraw with fee"""
        return super().withdraw(amount + self.fee)  # Add fee to withdrawal


class SecureAccount(Account):
    """Account with passcode protection"""

    def __init__(self, name, passcode, balance=0):
        super().__init__(name, balance)
        self.__passcode = str(passcode)  # Private attribute

    def _check_passcode(self, passcode):
        """Check if passcode is correct"""
        return self.__passcode == str(passcode)

    def change_pass(self, old_passcode, new_passcode):
        """Change the account passcode"""
        if self._check_passcode(old_passcode):
            self.__passcode = str(new_passcode)
            return f"{self.name}'s passcode has been changed"
        return "Wrong passcode"

    @property
    def passcode(self):
        """Prevent direct access to passcode"""
        raise AttributeError("Passcode cannot be accessed directly")

    @passcode.setter
    def passcode(self, new_passcode):
        """Prevent direct setting of passcode"""
        raise AttributeError("Direct setting of passcode is not allowed. Use change_pass method.")

    def withdraw(self, amount, passcode):
        """Secure withdrawal requiring passcode"""
        if not self._check_passcode(passcode):
            return "Wrong passcode"
        return super().withdraw(amount)