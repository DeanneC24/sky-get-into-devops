# create a blueprint class for a bank account
from withdrawal_exceptions import NegativeWithdrawalException, InsufficientFundsException


class Account:

    def __init__(self, opening_amount):
        self._balance = opening_amount  # semi private
        self._firstname = None  # semi private
        self._lastname = None  # semi private

    # overloading of str method
    def __add__(self, other):
        return self.get_balance() + other.get_balance()

    # overloading of str method
    def __str__(self):
        return f"{self._firstname} {self._lastname}'s account balance is: {self._balance}"

    def get_firstname(self):
        return self._firstname

    def set_firstname(self, firstname):
        self._firstname = firstname

    # properties
    @property  # function that takes a function as an argument
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        self._lastname = lastname

    def get_balance(self):
        return self._balance  # getter

    def deposit(self, amount):
        if isinstance(amount, int) and amount > 0:
            self._balance += amount

    def withdrawal(self, amount):
        if amount < 0:
            raise NegativeWithdrawalException()
        elif amount > self.get_balance():
            raise InsufficientFundsException()

        self._balance -= amount


if __name__ == "__main__":
    test_account = Account(200)
    test_account.withdrawal(20)
    print(test_account.get_balance())
