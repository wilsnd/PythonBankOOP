import datetime
from banking_system.account import Account, SavingsAccount, CheckingAccount, SecureAccount
from banking_system.bank import Bank
from banking_system.money import Money


def main():
    """Main function to demonstrate the banking system"""
    print("----- Creating a Bank -----")
    bank = Bank("BankRut")

    print("\n----- Creating Different Account Types -----")
    regular = bank.open_account("regular", "Harry Potter", balance=1000)
    savings = bank.open_account("savings", "Hermione Money", interest_rate=0.03, balance=2000)
    checking = bank.open_account("checking", "Charlie Chaplin Puth", fee=2, balance=500)
    secure = bank.open_account("secure", "Davey504", passcode="1234", balance=3000)

    print("\n----- Account Listing -----")
    bank.list_accounts()

    print("\n----- Account Information -----")
    regular.info()
    savings.info()
    checking.info()

    print("\n----- Basic Transactions -----")
    print(regular.deposit(500))
    print(savings.withdraw(100))
    print(checking.withdraw(200))

    print("\n----- Special Account Features -----")
    print(savings.add_interest())
    print(secure.withdraw(500, "1234"))  # Correct passcode
    print(secure.withdraw(500, "wrong"))  # Wrong passcode

    print("\n----- Money Class Demo -----")
    m1 = Money(100)
    m2 = Money(50)
    print(f"m1: {m1}")
    print(f"m2: {m2}")
    print(f"m1 + m2: {m1 + m2}")
    print(f"m1 - m2: {m1 - m2}")
    print(f"m1 + 25: {m1 + 25}")
    print(f"m1 == m2: {m1 == m2}")

    print("\n----- Class and Static Methods -----")
    print(Bank.set_global_interest_rate(0.04))
    print(f"Bob's new interest rate: {savings.interest_rate}")

    today = datetime.datetime.now()
    if Bank.is_business_day(today):
        print(f"Today ({today.strftime('%Y-%m-%d')}) is a business day")
    else:
        print(f"Today ({today.strftime('%Y-%m-%d')}) is not a business day")

    print("\n----- Final Account Status -----")
    bank.list_accounts()


if __name__ == "__main__":
    main()