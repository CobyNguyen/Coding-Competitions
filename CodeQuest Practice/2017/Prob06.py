cases = int(input())

cipher = {
"A":"Alpha",
"B":"Bravo", 
"C":"Charlie",
"D":"Delta",
"E":"Echo",
"F":"Foxtrot",
"G":"Golf",
"H":"Hotel",
"I":"India",
"J":"Juliet",
"K":"Kilo",
"L":"Lima",
"M":"Mike",
"N":"November",
"O":"Oscar",
"P":"Papa",
"Q":"Quebec",
"R":"Romeo",
"S":"Sierra",
"T":"Tango",
"U":"Uniform",
"V":"Victor",
"W":"Whiskey",
"X":"Xray",
"Y":"Yankee",
"Z":"Zulu"
}

for caseNum in range(cases):
    lines = int(input())
    for i in range(lines):
        word = input()
        letters = [x for x in word]
        # letters = [letters.replace()]
        for j in letters:
            letters = [letters.replace(j, cipher.get(j))]
        #     # new = cipher.get(j)
        #     # letters.replace(j, cipher.get(j), 1)
        print("-".join(letters))
