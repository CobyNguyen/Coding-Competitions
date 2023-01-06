import os

def average(scores):
    averageTestScore = int(sum(scores) / len(scores))
    if averageTestScore >= 90:
        letterAverage = "A"
    elif averageTestScore >= 80:
        letterAverage = "B"
    elif averageTestScore >= 70:
        letterAverage = "C"
    elif averageTestScore >= 60:
        letterAverage = "D"
    elif averageTestScore < 60:
        letterAverage = "F"
    return averageTestScore, letterAverage

def bestSoFar(scores):
    highest = 0
    for i, score in enumerate(scores):
        if score > highest:
            highest = score
            highestTest = i + 1
    return highest, highestTest

def lowSoFar(scores):
    lowest = 100
    for i, score in enumerate(scores):
        if i < lowest:
            lowest = score
            lowestTest = i + 1
    return lowest, lowestTest

name = input("Enter your name: ")
className = input("Enter your class: ")
scores = input("Enter your test scores: ").split()
scores = [int(i) for i in scores]

os.system('cls')
averageTestScore, letterAverage = average(scores)
highest, highestTest = bestSoFar(scores)
lowest, lowestTest = lowSoFar(scores)
print(f"{name} in {className} has an average test score of {averageTestScore}, with an {letterAverage}\nThe highest score was a {highest} which was test #{highestTest}, while the lowest score was a {lowest} which was test #{lowestTest}")