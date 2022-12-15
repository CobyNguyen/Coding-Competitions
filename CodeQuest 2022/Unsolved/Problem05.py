
import sys
import math
import string

results = []
cases = int(sys.stdin.readline().rstrip())
hour = 0
mini =  0
promth="hours"
promtm="minutes"
for caseNum in range(cases):
    full = sys.stdin.readline().rstrip()
    name = full.split(",")[0]
    times = full.split(",")[1::]
    for time in times:
        add = time.split(":")
        hour += int(add[0])
        mini += int(add[1])
    while mini >= 60:
        mini -= 60
        hour += 1
    if hour == 1:
        promth="hour"
    if mini == 1:
        promtm="minute"
    appen = name + "=" + str(hour) + promth + " " + str(mini) + " " + promtm
    results.append(appen)

for x in results:
    print(x)