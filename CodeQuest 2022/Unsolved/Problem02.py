import sys
import math
import string

results = []
cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    full = sys.stdin.readline().rstrip()
    volume, fillRate, leakRate = full.split(" ")splir

    if int(leakRate) == int(fillRate):
        wasteVolume = volume * leakRate
    elif int(leakRate) == 0:
        wasteVolume = 0
    elif int(fillRate) == 0:
        wasteVolume = int(volume)/int(leakRate)
    else: 
        wasteVolume = int(volume)/(int(fillRate) - int(leakRate))
        wasteVolume *= int(leakRate)
    results.append(str(math.ceil(wasteVolume)))
       
                                                                                          
for x in results:
    print(x)