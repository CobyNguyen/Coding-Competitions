import string
import sys

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    lastYear = input().split(",")
    current = input().split(",")
    both = []
    onlyLast = []
    onlyCurrent = []

    for i in lastYear:
        if i in current:
            both.append(i)
        else:
            onlyLast.append(i)
    for j in current:
        if j not in lastYear:
            onlyCurrent.append(j)
    
    print(",".join(sorted(onlyLast)))
    print(",".join(sorted(both)))
    print(",".join(sorted(onlyCurrent)))
# Solved