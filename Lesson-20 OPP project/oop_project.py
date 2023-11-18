from bank_accounts import *

Dave = BankAccount(1000, "Dave")
sarah = BankAccount(2000, "sarah")

Dave.getBalance()
sarah.getBalance()

sarah.deposit(500)

Dave.withdraw(10000)

Dave.withdraw(100)

Dave.transfer(100, sarah)

jim = InterestRewardsAcct(1000, "jim")
jim.getBalance()
jim.deposit(100)

Blaze = SavingsAcct(1000, "Blaze")

Blaze.getBalance()

Blaze.deposit(100)

Blaze.transfer(100, sarah)
