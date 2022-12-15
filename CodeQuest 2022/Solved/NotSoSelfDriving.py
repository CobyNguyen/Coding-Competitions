import sys
import math
import string

results = []
cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    SpeedandDistance = sys.stdin.readline().rstrip()
    curSpeed, curDistance = SpeedandDistance.split(":")
    #find m/s to match speed, needs an equation, DISTANCE/RATE
    if float(curSpeed) == 0 or 0.00:
        results.append("SAFE")
    else:
        collisionTime = float(curDistance) / float(curSpeed)
        if collisionTime <= 1.00:
            results.append("SWERVE")
        elif collisionTime <= 5.00:
            results.append("BRAKE")
        else: results.append("SAFE")

for x in range(len(results)):
    print(results[x])
