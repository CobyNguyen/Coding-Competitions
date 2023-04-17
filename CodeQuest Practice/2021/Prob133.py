# Bigger is Better 2021
import sys

greatest = 0

cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    numbers = [x for x in sys.stdin.readline().rstrip().split(" ")]
    for num in numbers:
        if int(num) > int(greatest):
            greatest = num
    print(greatest)