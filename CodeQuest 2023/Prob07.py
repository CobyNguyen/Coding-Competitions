
import decimal
cases = int(input())

for caseNum in range(cases):
    lines = int(input())
    weights = 0
    numbers = []
    for lineNum in range(lines):
        priority, score = input().split()
        if priority == "LOW":
            numbers.append(int(score))
            weights += 1
        elif priority=="MEDIUM":
            numbers.append(int(score))
            numbers.append(int(score))
            weights += 2
        elif priority=="HIGH":
            numbers.append(int(score))
            numbers.append(int(score))
            numbers.append(int(score))
            weights += 3

    print(round(sum(numbers)/weights * 10))

