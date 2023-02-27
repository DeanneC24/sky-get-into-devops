from account import Account
from saving_account import SavingAccount
from withdrawal_exceptions import NegativeWithdrawalException, InsufficientFundsException

lisa_account = Account(200)
bart_account = Account(20)

lisa_balance = lisa_account.get_balance()
bart_balance = bart_account.get_balance()

print(f"Lisa has £{lisa_balance}")
print(f"Bart has £{bart_balance}")
print(bart_account)
print(lisa_account)
print(f"Lisa and Bart have a total of £{lisa_account + bart_account}")

# using Java style getters and setters
lisa_account.set_firstname('Lisa')
print(lisa_account.get_firstname())
account_firstname = lisa_account.get_firstname()

# using .Net type properties for data
lisa_account.lastname = "Simpson"
print(lisa_account)
print(bart_account)

lisa_saving_account = SavingAccount(100, 0.30)
lisa_saving_account.set_firstname('Lisa')
lisa_saving_account.lastname = 'Simpson'
print(lisa_saving_account.interest_rate)
print(lisa_saving_account)


def withdraw_from_lisa_saving_account(amount):
    try:
        lisa_saving_account.withdrawal(amount)
    except InsufficientFundsException as err:
        print(f"Withdrawal failed with error: {err}")
    except NegativeWithdrawalException as err:
        print(f"Withdrawal failed with error: {err}")
    except Exception as err:
        print(f"Withdrawal failed with error: {err}")
    finally:
        print("End of withdrawal transaction on Lisa's Saving Account.")


# withdraw 20 successfully
withdraw_from_lisa_saving_account(20)

# Attempt to withdraw more than balance
withdraw_from_lisa_saving_account(120)

# Attempt to withdraw negative amount
withdraw_from_lisa_saving_account(-120)

# Attempt to withdraw using incorrect data type (to test that neither the Insufficent funds or Negative amount
# exceptions are thrown
withdraw_from_lisa_saving_account("Incorrect arg type")
