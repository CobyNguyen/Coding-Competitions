import csv #imports csv library to enable reading of the csv file.
import copy #so lists can be duplicated as a complete and individual copy
#Python is required to run 🗿

with open ("SkillsUSA 2023/State/red_rover_bracket_6587/teams.csv", newline = "") as csvfile: #reads the csv file with DictReader and creates a dictionary of the field names (headers)
    reader = csv.DictReader(csvfile)
    ranks = {row["Team Name"]: int(row["Seeding"]) for row in reader} #creates the keys for each team name and assigns the seed to it in a dictionary
    sorted_seeds = (sorted(ranks.values())) #sorts seed values in a list so they can be used like sorted_seeds[1] and sorted_seeds[-1]
    remaining_seeds = copy.copy(sorted_seeds)
    if len(ranks) % 2 != 0: #if number of teams
        byes = int((((len(ranks) - 1) ** 2)/ 2) - len(ranks)) #the total number of rounds is always amount of teams ^2, in order for there to be an even amount byes are calculated using this equation

with open ("SkillsUSA 2023/State/red_rover_bracket_6587/bracket.txt", "w", encoding = "utf-8") as f: #erases previously existing bracket.txt and adds names and seeds of team
    f.write(f"Team Name - Seeding\n{str(ranks).strip('{}')}\n\nTHE CRUSHING 🥵😱👩🏿‍🤝‍👩🏿🤰\n\n")



#Bracket sorting begins
game = [] #creates empty list to nest more lists for each set
for round_number in range(1, int((len(ranks) + int(byes)) / 2), 1):
    rounds = [] #creates list of every set in this round, so it can be appended to game list
    for i in sorted_seeds: #for each number in sorted_seeds
        if byes > 0:
            try:
                rounds.append((remaining_seeds[0], "bye"))
                remaining_seeds.remove(remaining_seeds[0]) #removes from sorted seeds once used
            except:
                pass #teehee for trying to remove from list, but if list is empty it will be skipped
            byes -= 1
        else:
            try: 
                rounds.append((remaining_seeds[0], remaining_seeds[-1]))
                remaining_seeds.remove(remaining_seeds[0])
                remaining_seeds.remove(remaining_seeds[-1])
            except:
                pass
    for set in rounds:
        remaining_seeds.append(set[0]) #appends new remaining seeds to list so that they may compete again. The first seed is always the highest, so it only takes the first seed in each list in the round list
    game.append(f"Round Number {round_number}")
    game.append(rounds)
    

    with open ("SkillsUSA 2023/State/red_rover_bracket_6587/bracket.txt", "a", encoding = "utf-8") as f: #prints results to text file
        f.write(f"Round Number {str(round_number)}\n")
        f.write(str(rounds).strip("[]") + "\n")
with open ("SkillsUSA 2023/State/red_rover_bracket_6587/bracket.txt", "a", encoding = "utf-8") as f: #prints final projected winner
    f.write(f"TONIGHT'S BIGGEST WINNER IS ALWAYS SEED 1 🤣😁😊🤩🤩🙂☺🙂🙂🙂😶😪😫🤐🤐☺🙂")
