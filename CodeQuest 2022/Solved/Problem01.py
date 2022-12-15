import sys
import math
import sys
import random
import re

results = [] ###
cases = int(sys.stdin.readline().rstrip())
text = str()
for caseNum in range(cases):
    add=False
    input = sys.stdin.readline().rstrip()
    for character in input:
        if add == True:
            text = text + character
            add=False
        elif character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
            add=True
    results.append(text)
    text=str()

for x in results:
    print(x)

