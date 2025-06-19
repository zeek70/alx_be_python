class BankAccount:
    def __init__(self, balance_file='balance.txt'):
        self.balance_file = balance_file
        try:
            with open(self.balance_file, 'r') as f:
                self.__account_balance = float(f.read())
        except FileNotFoundError:
            self.__account_balance = 100  # Default starting balance
            self._save_balance()

    def _save_balance(self):
        with open(self.balance_file, 'w') as f:
            f.write(str(self.__account_balance))

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            self._save_balance()

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            self._save_balance()
            return True
        return False

    def get_balance(self):
        return self.__account_balance
