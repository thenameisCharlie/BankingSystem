import tkinter as tk


def display_gui():

    def show_menu(customerName):
        #Destroys all the widgets on the screen before continuing to the next interface
        for widget in guiScreen.winfo_children():
            widget.destroy()

        tk.Label(guiScreen, text="Welcome to Richfolk Bank!").grid(row=0, column=0, pady=20) 
        
        optionSelected = tk.IntVar()

        tk.Label(guiScreen, text=f"What would you like to do {customerName}").grid(row=0, column=0, pady=20) 

        #Create radio buttons
        tk.Radiobutton(guiScreen, text="Deposit", variable=optionSelected, value=1).grid(row=1, column=0, columnspan=2, pady=5)
        tk.Radiobutton(guiScreen, text="Withdraw", variable=optionSelected, value=2).grid(row=2, column=0, columnspan=2, pady=5)
        tk.Radiobutton(guiScreen, text="Transfer", variable=optionSelected, value=3).grid(row=3, column=0, columnspan=2, pady=5)
        tk.Radiobutton(guiScreen, text="Open new account", variable=optionSelected, value=4).grid(row=4, column=0, columnspan=2, pady=5)
        tk.Radiobutton(guiScreen, text="Check balance", variable=optionSelected, value=5).grid(row=5, column=0, columnspan=2, pady=5)
        tk.Radiobutton(guiScreen, text="Exit", variable=optionSelected, value=6).grid(row=6, column=0, columnspan=2, pady=5)

        tk.Button(guiScreen, text="Continue", command=guiScreen.destroy).grid(row=4, column=0, columnspan=2, pady=10)

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
   

    guiScreen.mainloop()