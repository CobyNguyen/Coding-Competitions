import os
<<<<<<< HEAD

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
=======
import math

name = input("Enter your name: ")
className = input("Enter your class: ")
testScores = input("Enter your test scores: ")

scores = [x for x in testScores if True]
>>>>>>> f686d4a88e6b033c82e1912e7cf22fac915a66dc
