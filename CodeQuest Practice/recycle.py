import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())

def calculate():
        aluminum = aluminum * 1.55
        plastic = plastic * 1.50
        glass = glass * .10
        price = aluminum + glass + plastic
        return price
        print(price)
for caseNum in range(cases):
    items = sys.stdin.readline().rstrip()
    aluminum, plastic, glass = items.split()
    calculate()

    #alum  1.55
    # bottle = 1.5
    # glass = 10c