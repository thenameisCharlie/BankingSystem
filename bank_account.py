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

bankAccount1 = CheckingAccount(customerName)
bankAccount2 = SavingsAccount(customerName)
customerOptions = 0

def prompt_message(msg):
    try:
        return int(input(msg))

    except ValueError:
        print("\nInvalid entry! Please try again")
        return prompt_message(msg)


while customerOptions != 6:
    customerOptions = prompt_message(f"What would you like to do {customerName}?\n 1. Deposit \n 2. Withdraw \n 3. Transfer \n 4. Open new account \n 5. Check Balance\n 6. Exit\n\n")

    if customerOptions == 1:
        depositAmount = prompt_message("How much would you like to deposit? ")
        bankAccount1.deposit(depositAmount)

    elif customerOptions == 2: 
        withdrawAmount = prompt_message("How much would you like to withdraw? ")
        bankAccount1.withdraw(withdrawAmount)

    elif customerOptions == 3:
        #This while loop along with the if statement simulates a do while loop
        while True:
            accountOption = prompt_message("Which account would you like to transfer to?\n 1. Checking\n 2. Savings\n ")

            if accountOption == 1:
                transferAmount = prompt_message("What is the amount you would like to transfer? ")
                bankAccount2.transfer_to_checking(transferAmount, bankAccount1)
                break
            
            elif accountOption == 2:
                transferAmount = prompt_message("What is the amount you would like to transfer? ")
                bankAccount1.transfer_to_savings(transferAmount, bankAccount2)
                break
            
            else:
                print("Invalid entry. Please try again")

    elif customerOptions == 4:
        
        while True:
            accountType = prompt_message("What type of account would you like to open (\n 1. Checking\n 2. Savings\n)? ")

            
            if accountType == 1:
                bankAccount3 = CheckingAccount(customerName)
                print("\nNew checking account created!")
                break

            elif accountType == 2: 
                bankAccount4 = SavingsAccount(customerName)
                print("\nNew savings account created!")
                break
            
            else:
                print("Invalid entry. Please try again")

    elif customerOptions == 5:
        
        while True: 
            accountBalanceCheck = prompt_message("Which account would you like to check \n 1. Checking\n 2. Savings \n 3. All \n")

            if accountBalanceCheck == 1: 
                print(f"\n {bankAccount1.check_balance()}")
                break

            elif accountBalanceCheck == 2:
                print(f"\n {bankAccount2.check_balance()}")
                break
            
            elif accountBalanceCheck == 3:
                print(f"\n {bankAccount1.check_balance()}\n")
                print(f"{bankAccount2.check_balance()}\n")
                break
        
            else:
                print("Invalid entry, please try again")