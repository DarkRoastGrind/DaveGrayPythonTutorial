class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initial_amount, acct_first, acct_last):
        self.balance = initial_amount
        self.first = acct_first
        self.last = acct_last
        print(
            f"\nAccount created for client {acct_first} {acct_last}.\nBalance = ${self.balance:,.2f}"
        )

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nInsufficient funds in {self.first} {self.last}'s account.\nAttempted withdraw: ${amount:,.2f}\nAvailable funds: ${self.balance:,.2f}"
            )

    def get_balance(self):
        print(
            f"Account balance for client {self.first} {self.last} is ${self.balance:,.2f}"
        )

    def deposit(self, amount):
        self.balance += amount
        print(
            f"\nDeposit successful."
        )
        self.get_balance()

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print(
                f"\nWithdraw successful, ${amount:,.2f} withdrawn from the account."
            )
            self.get_balance()

        except BalanceException as error:
            print(f"\nWithdraw denied. Reason: {error}")

    def transfer(self, amount, account):
        try:
            print('\n**********\n\nBeginning Transfer of Funds...')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f"\nTransfer complete.\n\n**********")

        except BalanceException as error:
            print(f"\nTransfer denied. Reason: {error}\n\n**********")


# Has a 5% interest on deposits.
class InterestRewardsAccount(BankAccount):
    def deposit(self, amount):
        # Add additional 5% for rewards.
        self.balance += (amount * 1.05)
        print(f"\nDeposit Successful. Interest of 5% applied.")
        self.get_balance()


# $5 fee on any withdraw, but inherets the 5% interest on deposit.
class SavingsAccount(InterestRewardsAccount):
    def __init__(self, initial_amount, acct_first, acct_last):
        super().__init__(initial_amount, acct_first, acct_last)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance -= (amount + self.fee)
            print("\nWithdraw successful. $5 fee applied.")
            self.get_balance()

        except BalanceException as error:
            print(f'\nWithdraw denied. Reason: {error}')
