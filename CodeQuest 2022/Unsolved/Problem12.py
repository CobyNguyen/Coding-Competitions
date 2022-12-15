import sys
import math
import string

morse = {
    "a":". - ",
    "b":"- . . . ",
    "c":"- . - . ",
    "d":"- . . ",
    "e":"." ,
    "f":". . - . ",
    "g":"- - . ",
    "h":"- - . ",
    "i":". .",
    "j":". - - - ",
    "k":"- . - ",
    "l":". - . . ",
    "m":"- - ",
    "n":"- . ",
    "o":"- - - ",
    "p":". - - . ",
    "q":"- - . - ",
    "r":". - . ",
    "s":". . . ",
    "t":"- ",
    "u":". . - ",
    "v":". . . - ",
    "w":". - - ",
    "x":"- . . - ",
    "y":"- . - - ",
    "z":"- - . . "
    }
results = []
cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    encryp = sys.stdin.readline().rstrip()

for x in results:
    print(x)