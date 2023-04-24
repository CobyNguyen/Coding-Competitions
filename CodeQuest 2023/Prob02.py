cases = int(input())

for caseNum in range(cases):
    cassowary, lead = input().split()
    if int(cassowary)  > int(lead):
        print(f"Cassowary Craft sold {int(cassowary) - int(lead)} more aircraft")
    elif int(cassowary)  < int(lead):
        print(f"Lead Balloons Ltd sold {int(lead) - int(cassowary)} more aircraft")
    else:
        print("Cassowary Craft and Lead Balloons Ltd sold the same number of aircraft")