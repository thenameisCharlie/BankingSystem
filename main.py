from savings_account import SavingsAccount
from checking_account import CheckingAccount
from bankgui import display_gui

def main():

    display_gui()
    
    #Testing cases with inputs
    #When you re-run an object it destroys the old object in the memory and creates a new one
    customerName = input("Please enter your name: ")

    bankAccount1 = CheckingAccount(customerName)
    bankAccount2 = SavingsAccount(customerName)
    customerOptions = 0
    

    #function that converts the inputs to ints and returns an error message if the input is not an integer
    def prompt_message(msg):
        try:
            return int(input(msg))

        except ValueError:
            print("\nInvalid entry! Please try again")
            return prompt_message(msg)

    while customerOptions != 6:
        customerOptions = prompt_message(f"What would you like to do {customerName}?\n 1. Deposit \n 2. Withdraw \n 3. Transfer \n 4. Open new account \n 5. Check Balance\n 6. Exit\n\n")

        if customerOptions == 1:
            depositAccountOption = prompt_message("Which account would you like to make the deposit \n 1. Checking\n 2.Savings\n")
            depositAmount = prompt_message("How much would you like to deposit? ")

            if depositAccountOption == 1:
                bankAccount1.deposit(depositAmount)
                print(f"${depositAmount} has been deposited into your Checking account")
            
            if depositAccountOption ==2:
                bankAccount2.deposit(depositAmount)
                print(f"${depositAmount} has been deposited into your Savings account")


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
                accountType = prompt_message("What type of account would you like to open \n 1. Checking\n 2. Savings?\n ")

                
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
                    

if __name__ == "__main__":
    main()
    
