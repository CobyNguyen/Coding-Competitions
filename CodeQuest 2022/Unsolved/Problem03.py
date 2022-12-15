import sys
import math
import string

database = []
registered = []
results = []
cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    sysNum, sysRep = (sys.stdin.readline().rstrip()).split()
    for sysList in range(int(sysNum)):
        database.append(sys.stdin.readline().rstrip())
    for sysRep in range(int(sysRep)):
        registered.append(sys.stdin.readline().rstrip())
    for n in database:
        if n not in registered:
            results.append(n)



    """
    pesudoecode:
    for each index in database()
        compare index in registered
        if registered(index) is not database(index)
            unregistered.append(registered(index))

    """

for x in results:
    print(x)

