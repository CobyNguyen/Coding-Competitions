# import sys
# import math
# import string

# results = []
# cases = int(sys.stdin.readline().rstrip())

# for caseNum in range(cases):
#     pass

# for x in results:
#     print(x)

import tkinter as tk
import ttkbootstrap as ttk

class InputFrame:
    def __init__(self, root, entryInt, outputString):
        self.inputFrame = ttk.Frame(root)
        self.entry = ttk.Entry(self.inputFrame, textvariable = entryInt)
        self.button = ttk.Button(self.inputFrame, text = "Convert", command = lambda: convert(entryInt, outputString))
        self.entry.pack(side = "left", padx = 10)
        self.button.pack(side = "left")
        self.inputFrame.pack(pady = 10)

def convert(entryInt, outputString):
    try:
        miles = int(entryInt.get())
        outputString.set(miles * 1.61)
    except:
        outputString.set("Error!")

root = ttk.Window(themename = "superhero")
root.title("Miles to Kilometers")
root.geometry("400x200")

titleLabel = ttk.Label(root, text = "Miles to Kilometers", font = "Arial 24 bold")
titleLabel.pack()

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
root.mainloop()
