#Checking system class
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

#Testing cases with inputs
#When you re-run an object it destroys the old object in the memory and creates a new one
customerName = input("Please enter your name: ")

bankAccount1 = BankAccount(customerName)

customerOptions = input(" 1. Deposit \n 2. Withdraw \n 3. Transfer \n 4. Open new account \n 5. Check Balance")


if customerOptions == 1:
    depositAmount = input("How much would you like to deposit? ")
    bankAccount1.deposit(depositAmount)


# accountType = input("What type of account would you like to open (Checking or Savings)? ").lower()
# customerName = input("Please provide your full name: ")
# balanceAmount = input("Enter a balance amount for your new account: ")

# if accountType == "checking" or accountType == "savings": 
#     print("This is correct!")

# else:
#     print("Invalid entry. Please try again")

