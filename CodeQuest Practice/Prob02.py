cases = int(input())

for caseNum in range(cases):
    word, index = input().split()
    letter = [x for x in word]
    letter.pop(int(index))
    print("".join(letter))    
# Solved