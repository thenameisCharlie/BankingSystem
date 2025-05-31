import tkinter as tk
from savings_account import SavingsAccount
from checking_account import CheckingAccount


def display_gui():

    def clearScreen():
        #Destroys all the widgets on the screen before continuing to the next interface
        for widget in guiScreen.winfo_children():
            widget.destroy()


    def handle_option(selected, bankAccount1):
       clearScreen()

       if selected == 1:
            tk.Label(guiScreen, text="How much would you like to deposit? ").grid(row=0, column=0, pady=20) 

            deposit_amount = tk.Entry(guiScreen, width=30)
            deposit_amount.grid(row=1, column=0, pady=(0, 10))

            def confirm_deposit():
                try:
                    amount_conversion = float(deposit_amount.get())
                    bankAccount1.deposit(amount_conversion)
                    tk.Label(guiScreen, text=f"${amount_conversion} deposited successfully!").grid(row=3, column=0)
                except ValueError:
                    tk.Label(guiScreen, text="Invalid amount. Please enter a number.").grid(row=3, column=0)

            tk.Button(guiScreen, text="Confirm", command=confirm_deposit).grid(row=2, column=0, pady=(0, 10))


    
    def show_menu(customerName):
        clearScreen()
        
        optionSelected = tk.IntVar()

        tk.Label(guiScreen, text=f"Welcome to Richfolk Bank, {customerName}! ").grid(row=0, column=0, pady=20) 

        options = [("Deposit", 1), ("Withdraw", 2), ("Transfer", 3), ("Open new account", 4), ("Check balance", 5), ("Exit", 6)]

        for idx, (text, val) in enumerate(options):
            tk.Radiobutton(guiScreen, text=text, variable=optionSelected, value=val).grid(row=idx + 1, column=0, pady=2)

        tk.Button(guiScreen, text="Continue", command=lambda: handle_option(optionSelected.get(), bankAccount1)).grid( 
        row=len(options) + 1, column=0, pady=(10, 0)) #lambda creates an anonymous one time function that doesnt run until button is pressed

    #handles the GUI screen
    guiScreen = tk.Tk()
    guiScreen.title("Richfolk Bank")
    guiScreen.geometry("600x400")

    # Configure center-alignment
    guiScreen.grid_rowconfigure(0, weight=1)
    guiScreen.grid_rowconfigure(1, weight=1)
    guiScreen.grid_rowconfigure(2, weight=1)
    guiScreen.grid_columnconfigure(0, weight=1)

    # Create a frame to hold widgets
    centerFrame = tk.Frame(guiScreen)
    centerFrame.grid(row=1, column=0)

    # Center contents inside the frame
    centerFrame.grid_rowconfigure(0, weight=1)
    centerFrame.grid_columnconfigure(0, weight=1)

    tk.Label(centerFrame, text="Please enter your full name:").grid(row=0, column=0, pady=(0, 10))
    nameEntry = tk.Entry(centerFrame, width=30)
    nameEntry.grid(row=1, column=0, pady=(0, 10))
    tk.Button(centerFrame, text="Enter", command=lambda:show_menu(nameEntry.get())).grid(row=2, column=0)

    #Bank account generated after entering name
    bankAccount1 = CheckingAccount(nameEntry.get())
    bankAccount2 = SavingsAccount(nameEntry.get())
    
   

    guiScreen.mainloop()