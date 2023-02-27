class InsufficientFundsException(Exception):

    def __init__(self, msg="Insufficient funds in account. Unable to proceed with withdrawal."):
        self.msg = msg
        super().__init__(self.msg)


class NegativeWithdrawalException(Exception):
    def __init__(self, msg="Cannot withdraw a negative amount from account. Unable to proceed."):
        self.msg = msg
        super().__init__(self.msg)


