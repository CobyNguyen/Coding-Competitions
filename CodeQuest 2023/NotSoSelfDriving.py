import sys

results = []
cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    speed_distance = sys.stdin.readline().rstrip()
    cursor_speed, cursor_distance = speed_distance.split(":")
    #find m/s to match speed, needs an equation, DISTANCE/RATE
    if float(cursor_speed) == 0 or 0.00:
        results.append("SAFE")
    else:
        collision_time = float(cursor_distance) / float(cursor_speed)
        if collision_time <= 1.00:
            results.append("SWERVE")
        elif collision_time <= 5.00:
            results.append("BRAKE")
        else: results.append("SAFE")

for x in range(len(results)):
    print(results[x])
