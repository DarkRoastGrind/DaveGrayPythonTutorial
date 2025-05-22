from bank_accounts import *

Nicholas = BankAccount(1000, "Nicholas", "La Claire")
NicholasInterest = InterestRewardsAccount(1000, "Nicholas", "La Claire")

Sara = BankAccount(2000, "Sara", "Smith")
SaraInterest = InterestRewardsAccount(2000, "Sara", "Smith")


# -------------- Regular Account Management --------------
Nicholas.get_balance()
Sara.get_balance()

print()

Nicholas.deposit(200)

print()

Nicholas.withdraw(500000)
Nicholas.withdraw(10)

Nicholas.transfer(500000, Sara)
Nicholas.transfer(50, Sara)

print()

# -------------- Interest Account Management --------------
NicholasInterest.get_balance()
NicholasInterest.deposit(200)
NicholasInterest.transfer(500, SaraInterest)

print()

NicholasSavings = SavingsAccount(1000, "Nicholas", "La Claire")
NicholasSavings.get_balance
NicholasSavings.deposit(200)
NicholasSavings.withdraw(20000)
NicholasSavings.withdraw(200)
