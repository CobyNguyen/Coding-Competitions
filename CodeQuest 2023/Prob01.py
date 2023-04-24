import sys

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    words = input().split()
    print(words.index("Nimo") + 1)
    # for word in words:
    #     if word == "Nimo":
    #         print(word.index())