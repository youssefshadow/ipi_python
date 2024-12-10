import json


# Open and read the JSON file
with open('./db/players.json', 'r') as file:
    players:list = json.load(file)

players_sorted = sorted(players, key=lambda player:player['elo_points'])

players_s1 = players_sorted[:len(players)//2]
players_s2 = players_sorted[(len(players)//2):]

versus = []
for i in range(0, len(players)//2):
    versus.append([players_s1[i], players_s2[i]])

with open('./db/versus.json', 'w') as outfile:
    json.dump(versus, outfile, indent=4)

