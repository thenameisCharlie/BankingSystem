from bank_account import BankAccount

class CheckingAccount(BankAccount):
    #Overdraft fee for accounts that are in the negative
    def overdraft_fee(self):
        if self.balance < 0:
            self.balance -= 35

    #Override function that withdraws money from the account and adds an overdraft fee if account is under 0
    def withdraw(self, amount):
        super().withdraw(amount) #calls the parents withdraw method
        self.overdraft_fee()
    
    #Function that transfers funds from checking to savings
    def transfer_to_savings(self, amount, savingsAccount):
        if self.balance >= amount: 
            self.balance -= amount
            savingsAccount.balance += amount