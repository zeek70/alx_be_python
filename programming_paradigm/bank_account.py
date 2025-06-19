class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance (default: 0)."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """
        Deduct the amount from the account balance if sufficient funds are available.
        Returns True if the withdrawal was successful, else False.
        """
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def get_balance(self):
        """Return the current account balance."""
        return self.__account_balance
