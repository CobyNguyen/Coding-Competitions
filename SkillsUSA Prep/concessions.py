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
    def __init__(self, root, entryInt, outputString):
        self.inputFrame = ttk.Frame(root)
        self.entry = ttk.Entry(self.inputFrame, textvariable = entryInt)
        self.button = ttk.Button(self.inputFrame, text = "Convert", command = lambda: addToPrice(entryInt, outputString))
        self.entry.pack(side = "left", padx = 10)
        self.button.pack(side = "left")
        self.inputFrame.pack(pady = 10)

def addToPrice(entryInt, outputString):
    try:
        miles = int(entryInt.get())
        outputString.set(miles * 1.61)
    except:
        outputString.set("Error! Whole numbers only")

entryInt1 = tk.IntVar()
outputString1 = tk.StringVar()
inputFrame1 = InputFrame(root, entryInt1, outputString1)

entryInt2 = tk.IntVar()
outputString2 = tk.StringVar()
inputFrame2 = InputFrame(root, entryInt2, outputString2)

entryInt3 = tk.IntVar()
outputString3 = tk.StringVar()
inputFrame3 = InputFrame(root, entryInt3, outputString3)

outputLabel1 = ttk.Label(root, text = "Output 1: ", font = "Arial 24", textvariable = outputString1).pack()
outputLabel2 = ttk.Label(root, text = "Output 2: ", font = "Arial 24", textvariable = outputString2).pack()
outputLabel3 = ttk.Label(root, text = "Output 3: ", font = "Arial 24", textvariable = outputString3).pack()

# Starts the main loop
root.mainloop()