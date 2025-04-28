#Checking system class
import random

class BankAccount: 
    def __init__(self, customerName, balance):
        self.accountNum = BankAccount._account_num_randomizer()
        self.customerName = customerName
        self.balance = balance

    #Function creates a random account number for the user
    @staticmethod
    def _account_num_randomizer():
        random.randint(1000, 5000)
    
    #Function that deposits money to account
    def deposit(self, amount):
        self.balance += amount
    
    #Function that withdraws money from account
    def withdraw(self, amount):
        self.balance -= amount
    
    #Function to check balance
    def check_balance(self):
        return self.balance

#class CheckingAccount(BankAccount):
    