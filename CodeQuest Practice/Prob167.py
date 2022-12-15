# Find the Missing Sensor 2022
import sys

cases = int(sys.stdin.readline().rstrip())
missing = []

for caseNum in range(cases):
    total = sys.stdin.readline().rstrip()
    number = [x for x in sys.stdin.readline().rstrip().split(" ")]
    for i in range(total - 1):
        if i in number:
            missing.append(i)
            
    print(" ".join(missing))