import tkinter as tk
import ttkbootstrap as ttk

# Creating the window
root = ttk.Window(themename = "superhero")
root.title("Concessions")

# Creating intial options window
# titleStr = tk.StringVar()
# titleLabel = ttk.Label(root, text = titleStr, font = "Arial 24 bold").pack()

# Creating the menu labels
# titleStr.set("Concessions Stand")
titleLabel = ttk.Label(root, text = "Concessions Menu", font = "Arial 24 bold").pack()
menuLabels = ttk.Label(root, text = "", font = "Arial 24 bold").pack()

class InputFrame:
    def __init__(self, root, optionString, entryInt, outputString):
        self.inputFrame = ttk.Frame(root)
        self.optionLabel =  ttk.Label(self.inputFrame, text = optionString)
        self.entry = ttk.Entry(self.inputFrame, textvariable = entryInt)
        self.entry.grid(row=0,column=1,padx=10)
        self.button = ttk.Button(self.inputFrame, text = "Add", command = lambda: addToPrice(entryInt, outputString))
        self.button.grid(row=0,column=2,padx=10)
        self.optionLabel.grid(row=0,column=0,padx=10)
        self.inputFrame.pack(pady = 5) #Center/align each widget

def addToPrice(entryInt, outputString): #Change the function so that pressing the button adds to the current total price
    try:
        miles = int(entryInt.get())
        outputString.set(miles * 1.61)
    except:
        outputString.set("Error! Whole numbers only")

# Creating objects for each menu option
smallPopcorn = tk.IntVar()
smallPopcornPrice = tk.StringVar()
smallPopcornFrame = InputFrame(root, "Small Popcorn", smallPopcorn, smallPopcornPrice)

mediumPopcorn = tk.IntVar()
mediumPopcornPrice = tk.StringVar()
mediumPopcornFrame = InputFrame(root, "Medium Popcorn", mediumPopcorn, mediumPopcornPrice,)

largePopcorn = tk.IntVar()
largePopcornPrice = tk.StringVar()
largePopcornFrame = InputFrame(root, "Large Popcorn", largePopcorn, largePopcornPrice)

soda = tk.IntVar()
sodaPrice = tk.StringVar()
sodaFrame = InputFrame(root, "Soda", soda, sodaPrice)

candy = tk.IntVar()
candyPrice = tk.StringVar()
candyFrame = InputFrame(root, "Candy", candy, candyPrice)

smallPopcornLabel = ttk.Label(root, text = "Output 1: ", font = "Arial 24", textvariable = smallPopcornPrice).pack()
mediumPopcornLabel = ttk.Label(root, text = "Output 2: ", font = "Arial 24", textvariable = mediumPopcornPrice).pack()
largePopcornLabel = ttk.Label(root, text = "Output 3: ", font = "Arial 24", textvariable = largePopcornPrice).pack()
sodaLabel = ttk.Label(root, text = "Output 4: ", font = "Arial 24", textvariable = sodaPrice).pack()
candyLabel = ttk.Label(root, text = "Output 5: ", font = "Arial 24", textvariable = candyPrice).pack()

# Starts the main loop
root.mainloop()