import random

players = ["Player1", "Player2", "Player3", "Player4"]
overall_players = len(players)

team_1 = []
team_2 = []

while len(players) > 0:
    select = random.choice(players)
    if len(team_1) < overall_players // 2:
        team_1.append(select)
    else:
        team_2.append(select)
    players.remove(select)

print(f"TEAM 1: {team_1}")
print(f"TEAM 2: {team_2}")
