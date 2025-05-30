import tkinter as tk

def display_gui():
    #handles the GUI screen
    guiScreen = tk.Tk()
    guiScreen.title("Richfolk Bank")
    guiScreen.geometry("600x400")

    # Configure center-alignment
    guiScreen.grid_rowconfigure(0, weight=1)
    guiScreen.grid_columnconfigure(0, weight=1)

    # Create a frame to hold widgets
    centerFrame = tk.Frame(guiScreen)
    centerFrame.grid(row=0, column=0)

    # Center contents inside the frame
    centerFrame.grid_rowconfigure(0, weight=1)
    centerFrame.grid_columnconfigure(0, weight=1)

    label = tk.Label(centerFrame, text="Please enter your full name:")
    label.pack(pady=(0, 10))
    customerName = tk.Entry(centerFrame, width=30)
    customerName.pack() #Center items in the frame automatically
    tk.Button(guiScreen, text="Enter", width=15).pack(pady=10)
    

    guiScreen.mainloop()

    def show_menu():
        #Destroys all the widgets on the screen before continuing to the next interface
        for widget in guiScreen.winfo_children():
            widget.destroy()
        
        optionSelected = tk.IntVar()

        tk.label(guiScreen, text=f"What would you like to do {customerName}").pack(pady = 10)

        #Create radio buttons
        tk.Radiobutton(guiScreen, text="Deposit", variable=optionSelected, value=1).pack()
        tk.Radiobutton(guiScreen, text="Withdraw", variable=optionSelected, value=2).pack()
        tk.Radiobutton(guiScreen, text="Transfer", variable=optionSelected, value=3).pack()
        tk.Radiobutton(guiScreen, text="Open new account", variable=optionSelected, value=4).pack()
        tk.Radiobutton(guiScreen, text="Check balance", variable=optionSelected, value=5).pack()
        tk.Radiobutton(guiScreen, text="Exit", variable=optionSelected, value=6).pack()

