import os

JOGGING = 398
RUNNING = 557

bigMacs = int(input("How many Big Macs have you eaten today? "))
mediumFries = int(input("How many medium fries have you eaten today? "))
smallShakes = int(input("How many small shakes have you consumed today? "))
calories = (bigMacs * 563) + (mediumFries * 378) + (smallShakes * 530)
os.system('cls')

print(f"Big Macs: {bigMacs}\nMedium fries: {mediumFries}\nSmall shakes: {smallShakes}")
print(f"Calories consumed: {calories}")
print(f"It will take {round(calories/JOGGING, 2)} hours to burn these calories jogging.\nIt will take {round(calories/RUNNING, 2)} to burn these calories by running.")

input()
os.system('cls')