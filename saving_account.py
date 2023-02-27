from account import Account


class SavingAccount(Account):

    def __init__(self, opening_amount, interest_rate):
        super().__init__(opening_amount)
        self._interest_rate = interest_rate

    @property
    def interest_rate(self):
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, new_interest_rate):
        self._interest_rate = new_interest_rate

    def __str__(self):
        return f"{self._firstname} {self._lastname}'s saving account balance is: {self._balance}"
