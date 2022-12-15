import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
   numbers = sys.stdin.readline().rstrip()
   num1, num2 = numbers.split(" ")
   solution1 = int(num1) + int(num2)
   solution2 = int(num1) * int(num2)
   print(solution1, solution2)

# Solved!
