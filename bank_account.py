import random

class BankAccount: 
    #constructor (How you create an instanace of an object)
    def __init__(self, customerName, balance = 0):
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
        # return self.customerName, self.accountNum, self.balance
        displayDict = {"Name": self.customerName, "Account Number": self.accountNum, "Current Balance": self.balance}
        lines = []
        
        for k, v in displayDict.items():
            lines.append(f"{k}: {v}")
        
        return  "\n".join(lines) #converts the lines list into a string and it's joined by a space










