import os

def average(scores):
    global letterAverage, averageTestScore
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
def bestSoFar(scores):
    global highest
    for i in scores:
        if i > highest:
            highest = i

name = input("Enter your name: ")
className = input("Enter your class: ")
scores = input("Enter your test scores: ").split()
scores = [int(i) for i in scores]

os.system('cls')
average(scores)
print(f"{name} in {className} has an average test score of {averageTestScore}, meaning they have an {letterAverage}\n The highest score was a {highest}")