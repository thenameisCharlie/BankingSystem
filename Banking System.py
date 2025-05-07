#Checking system class
import random

class BankAccount: 
    #constructor (How you create an instanace of an object)
    def __init__(self, customerName, balance):
        self.accountNum = BankAccount._account_num_randomizer()
        self.customerName = customerName
        self.balance = balance

    #Function creates a random account number for the user
    @staticmethod
    def _account_num_randomizer():
        return random.randint(1000, 5000)
    
    #Function that deposits money to account
    def deposit(self, amount):
        self.balance += amount
    
    #Function that withdraws money from account
    def withdraw(self, amount):
        self.balance -= amount
    
    #Function to check balance
    def check_balance(self):
        return self.balance, self.customerName, self.accountNum

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


class SavingsAccount(BankAccount):
    def transfer_to_checking(self, amount, checkingAccount):
        if self.balance >= amount:
            self.balance -= amount
            checkingAccount.balance += amount

#Testing cases
bankAccount1 = CheckingAccount("Carlos Villatoro", 3000)
print(bankAccount1.check_balance())
