cases = int(input())

for caseNum in range(cases):
    numbers = input().split()
    indexes = []
    for i in numbers:
        if i >= .6 and i <= .85:
            indexes.append(numbers[i])
    if len(indexes) == 1:
        print(f"A multipaction event was detected at time index {indexes[i]}")
