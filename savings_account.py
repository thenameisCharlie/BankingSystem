from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def transfer_to_checking(self, amount, checkingAccount):
        if self.balance >= amount:
            self.balance -= amount
            checkingAccount.balance += amount