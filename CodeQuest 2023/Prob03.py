cases = int(input())

alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for caseNum in range(cases):
    value, wordAmount = input().split()
    for wordNum in range(1, int(wordAmount) + 1):
        word = input()
        worth = 0.0
        for letter in word:
            if alp.index(letter) + 1 + int(value) > 26:
                worth += (((alp.index(letter)) - 26) + int(value))
            else:
               worth += (alp.index(letter)) + int(value)
        worth /= 100
        if worth == 1.00:
            print(f"WINNER {value}: {word}")