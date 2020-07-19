


class Account :

    def __init__(self,owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amt):
       self.balance = self.balance + amt
       print(self.balance)
       print("Deposit Accepted")

    def withdraw(self, ded):
        if self.balance < ded:
            print("Fund Unavailable")
        else:
         self.balance = self.balance - ded
         print(self.balance)
         print("Withdrawal Accepted")

acct1 = Account('jose',100)


acct1.deposit(100)
acct1.withdraw(50)

print(acct1.balance)