# Bigger is Better 2021
import sys



cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    numbers = [x for x in sys.stdin.readline().rstrip().split(" ")]
    greatest = 0
    for num in numbers:
        greatest = max(int(greatest), int(num))
    print(greatest)