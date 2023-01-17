import tkinter as tk
import ttkbootstrap as ttk

# Creating the window
root = ttk.Window(themename = "superhero")
root.title("Concessions")

# Creating menu dictionary
menu = {
    "smallPopcorn": 3.00,
    "mediumPopcorn": 4.00,
    "largePopcorn": 5.00,
    "soda": 2.00,
    "candy": 1.50
}

# Creating the menu labels
titleLabel = ttk.Label(root, text = "Concessions Menu", font = "Arial 24 bold").pack()
menuLabels = ttk.Label(root, text = "", font = "Arial 24 bold").pack()

class InputFrame:
    def __init__(self, root, optionString, amountInt, itemName):
        self.inputFrame = ttk.Frame(root)
        self.optionLabel =  ttk.Label(self.inputFrame, text = optionString)
        self.entry = ttk.Entry(self.inputFrame, textvariable = amountInt)
        self.entry.grid(row=0,column=1)
        self.optionLabel.grid(row=0,column=0,padx=10)
        self.inputFrame.pack(pady = 5)
        self.entry._name = itemName

def checkout():
    total_cost = 0.0
    # Iterate over all the input variables and add their values to the total cost
    for item in menu.keys():
        total_cost += eval(item).get() * menu[item]
    totalCostString.set( "${:,.2f}".format(total_cost))

# Creating objects for each menu option
smallPopcorn = tk.IntVar()
smallPopcornFrame = InputFrame(root, "Small Popcorn", smallPopcorn, "smallPopcorn")

mediumPopcorn = tk.IntVar()
mediumPopcornFrame = InputFrame(root, "Medium Popcorn", mediumPopcorn, "mediumPopcorn")

largePopcorn = tk.IntVar()
largePopcornFrame = InputFrame(root, "Large Popcorn", largePopcorn, "largePopcorn")

soda = tk.IntVar()
sodaFrame = InputFrame(root, "Soda", soda, "soda")

candy = tk.IntVar()
candyFrame = InputFrame(root, "Candy", candy, "candy")

# Create a variable to store the total cost
totalCostString = tk.StringVar()
totalCostString.set("")

# Create the checkout button and displays the total cost
checkoutButton = ttk.Button(root, text = "Checkout", command = checkout).pack()
totalCostLabel = ttk.Label(root, text = "Total Cost", font = "Arial 24", textvariable = totalCostString).pack()

# Starts the main loop
root.mainloop()
