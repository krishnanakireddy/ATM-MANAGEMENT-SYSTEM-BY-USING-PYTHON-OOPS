# ATM MANAGEMENT SYSTEM USING OOPS IN PYTHON
# Importing ABC module for abstraction

from abc import ABC, abstractmethod

# PART 1: ABSTRACT CLASS (ABSTRACTION)

class BankAccount(ABC):
    """
    Abstract class that enforces implementation
    of transaction() method in child class
    """
    @abstractmethod
    def transaction(self):
        pass

# PART 2: BASE CLASS (ENCAPSULATION)

class Account:
    """
    This class stores account details securely
    using public, protected, and private variables
    """

    def __init__(self, name, account_number, balance, pin):
        self.name = name                    # Public variable
        self._account_number = account_number  # Protected variable
        self.__balance = balance            # Private variable
        self.__pin = pin                    # Private variable

    # Public getter for balance
    def get_balance(self):
        return self.__balance

    # Public setter for balance
    def set_balance(self, amount):
        self.__balance = amount

    # Getter for PIN
    def get_pin(self):
        return self.__pin


# PART 3: CHILD CLASS (INHERITANCE)

class ATM(Account, BankAccount):
    """
    ATM class inherits Account and BankAccount
    Implements all ATM operations
    """

    bank_name = "ABC BANK"           # Class variable
    MAX_WITHDRAWAL = 10000           # Maximum withdrawal limit

    def __init__(self, name, account_number, balance, pin):
        super().__init__(name, account_number, balance, pin)
        self.transaction_history = []   # Stores transactions
        self.transaction_count = 0      # Counts transactions


    # CLASS METHOD

    @classmethod
    def display_bank_name(cls):
        print("\n--------------------------------")
        print(f"WELCOME TO {cls.bank_name} ATM")
        print("--------------------------------")


    # STATIC METHOD

    @staticmethod
    def validate_amount(amount):
        return amount > 0


    # INSTANCE METHODS

    def check_balance(self):
        print(f"\nCurrent Balance: ₹{self.get_balance()}")

    def deposit_money(self, amount):
        if self.validate_amount(amount):
            self.set_balance(self.get_balance() + amount)
            self.transaction_history.append(f"Deposited ₹{amount}")
            self.transaction_count += 1
            print("\nDeposit Successful!")
            print(f"Updated Balance: ₹{self.get_balance()}")
        else:
            print("Invalid deposit amount!")

    def withdraw_money(self, amount):
        if not self.validate_amount(amount):
            print("Invalid withdrawal amount!")
        elif amount > ATM.MAX_WITHDRAWAL:
            print(f"Maximum withdrawal limit is ₹{ATM.MAX_WITHDRAWAL}")
        elif amount > self.get_balance():
            print("Insufficient balance!")
        else:
            self.set_balance(self.get_balance() - amount)
            self.transaction_history.append(f"Withdrawn ₹{amount}")
            self.transaction_count += 1
            print("\nWithdrawal Successful!")
            print(f"Updated Balance: ₹{self.get_balance()}")

    def show_account_details(self):
        print("\nACCOUNT DETAILS")
        print(f"Account Holder : {self.name}")
        print(f"Account Number : {self._account_number}")
        print(f"Balance        : ₹{self.get_balance()}")
        print(f"Transactions   : {self.transaction_count}")

    def show_transaction_history(self):
        print("\nTRANSACTION HISTORY")
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            for i, record in enumerate(self.transaction_history, 1):
                print(f"{i}. {record}")


    # METHOD OVERRIDING (POLYMORPHISM)

    def transaction(self):
        print("Transaction completed successfully.")



# PART 4: MENU-DRIVEN PROGRAM


ATM.display_bank_name()

# Taking user input
name = input("Enter Account Holder Name: ")
account_number = input("Enter Account Number: ")
while True:
  balance = (input("Enter Initial Balance: "))
  if balance.isdigit():
    balance = int(balance)
    break
  else:
      print("Invalid Balance! Enter numbers only.")
pin = input("Set a 4-digit PIN: ")

# Creating ATM object
user = ATM(name, account_number, balance, pin)

# PIN Verification
entered_pin = input("\nEnter PIN to access ATM: ")
if entered_pin != user.get_pin():
    print("Incorrect PIN! Access Denied.")
else:
    while True:
        print("\n-----------------------------")
        print("ATM MENU")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Account Details")
        print("5. Transaction History")
        print("6. Exit")
        print("-----------------------------")

        choice = input("Enter your choice: ")

        if choice == "1":
            user.check_balance()

        elif choice == "2":
            amount = int(input("Enter amount to deposit: "))
            user.deposit_money(amount)
            user.transaction()

        elif choice == "3":
            amount = int(input("Enter amount to withdraw: "))
            user.withdraw_money(amount)
            user.transaction()

        elif choice == "4":
            user.show_account_details()

        elif choice == "5":
            user.show_transaction_history()

        elif choice == "6":
          confirm = input("Are you sure you want to exit? (yes/no): ").lower()
          if confirm == "yes" or confirm == "y" or confirm == "ye":
            print("\nThank you for using ABC BANK ATM 🙏")
            break

        else:
            print("Invalid choice! Please try again.")
