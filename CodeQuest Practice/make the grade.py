# Problem 4: Make The Grade 
#SOLVED

import sys
import math
import string

print("Enter the number of test cases: ")
cases = int(sys.stdin.readline().rstrip()) #gets number of cases

def split(word):
    return tuple(word)


for caseNum in range(cases):
    total = []
    print("Input the amount of students and the answer key: ")
    amount = str(sys.stdin.readline().rstrip()) #you input (student number) (key) ex: 3 ABACDD
    amount, key = amount.split() #splits the number into an amount of students and the key into its own key
    amount = int(amount) #makes the amount a variable so it can be iterated in a range
    for stuNum in range(amount): #for each student, types in the name then their answer
     print("Enter the student name and their response")
     names = str(sys.stdin.readline().rstrip())  #you input the student name and their answers ex. BOB ABACDA
     names, response = names.split() #splits the student name and then their response into separate variables
     response = split(response)
     key = split(key) 
     correct = 0 #initializes the correct
     for qNumber in range(len(key)): #repeats for each character (question answer) in the key and compares it to the response
        if response[qNumber] == key[qNumber]:
            correct += 1
     score = correct/len(key) #Divides number correct by amount, and that would be the score
     if score < .60: #find the letter grades
        letter = "F"
     if .60 <= score < .70:
        letter = "D"
     if .70 <= score < .80:
        letter = "C"
     if .80 <= score < .90:
        letter = "B"
     if score >= .90:
        letter = "A"
     total.append(names + " " + str(round(score*100, 1)) + "% " + letter) #rounds the score and prints the name, score, then letter for each person and adds it to the total list
for student in total: #prints each person and their scores on the list
    print(student)
