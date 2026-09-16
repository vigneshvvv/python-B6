class InsufficientFundException(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundException("Insufficient Fund")

        self.balance -= amount
        print("Withdraw successful")


account = BankAccount(10000)
try:
    account.withdraw(12000)
except InsufficientFundException as e:
    print("Transaction Failed: ", e )

