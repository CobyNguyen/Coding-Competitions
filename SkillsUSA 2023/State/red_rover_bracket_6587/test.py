import csv 
import copy 

with open ("SkillsUSA 2023/State/red_rover_bracket_6587/teams.csv", newline = "") as csvfile:
    reader = csv.DictReader(csvfile)
    ranks = {row["Team Name"]: int(row["Seeding"]) for row in reader}
    sorted_seeds = (sorted(ranks.values())) 
    remaining_seeds = copy.copy(sorted_seeds)
    if len(ranks) % 2 != 0: 
        byes = int((((len(ranks) - 1) ** 2)/ 2) - len(ranks))

with open ("SkillsUSA 2023/State/red_rover_bracket_6587/bracket.txt", "w", encoding = "utf-8") as f:
    f.write(f"Team Name - Seeding\n{str(ranks).strip('{}')}\n\nTHE CRUSHING 🥵😱👩🏿‍🤝‍👩🏿🤰\n\n")

game = [] 
for round_number in range(1, int((len(ranks) + int(byes)) / 2), 1):
    rounds = [] 
    for i in sorted_seeds: 
        if byes > 0:
            try:
                rounds.append((remaining_seeds[0], "bye"))
                remaining_seeds.remove(remaining_seeds[0]) 
            except:
                pass 
            byes -= 1
        else:
            try: 
                rounds.append((remaining_seeds[0], remaining_seeds[-1]))
                remaining_seeds.remove(remaining_seeds[0])
                remaining_seeds.remove(remaining_seeds[-1])
            except:
                pass
    for set in rounds:
        remaining_seeds.append(set[0]) 
    game.append(f"Round Number {round_number}")
    game.append(rounds)

with open ("SkillsUSA 2023/State/red_rover_bracket_6587/bracket.txt", "a", encoding = "utf-8") as f:
    for round_number, round_results in enumerate(game[1:], 1):
        f.write(f"\nRound Number {round_number}\n")
        for game_number, game_result in enumerate(round_results):
            if game_result[1] == 'bye':
                f.write(f"{game_result[0]} had a bye\n")
            else:
                winner_prompt = f"Enter the winner of game {game_number+1} ({game_result[0]} - Seed {ranks[game_result[0]]}) in round {round_number}: "
                winner = input(winner_prompt)
                loser = game_result[0] if game_result[0] != winner else game_result[1]
                f.write(f"{winner} defeated {loser}\n")


        
    winner_name = None
    for name, seed in ranks.items():
        if seed == 1:
            winner_name = name
            break

    if winner_name:
        f.write(f"\n{winner_name} ARE TONIGHT'S BIGGEST WINNER 🤣😁😊🤩🤩🙂☺🙂🙂🙂😶😪😫🤐🤐☺🙂\n")
    else:
        f.write("ERROR: COULD NOT FIND WINNER\n")
