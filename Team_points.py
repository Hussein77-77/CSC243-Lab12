def points_by_team(scores, teams):
    result = {}
    for team, players in teams.items():
        total = 0
        for player in players:
            total += scores[player]
        result[team] = total
    return result
scores = {}
teams = {}
try:
    with open("players.txt", "r") as file:
        for line in file:
            fields = line.split()
            name = fields[0]
            points = int(fields[1])
            team = fields[2]

            scores[name] = points
            if team not in teams:
                teams[team] = []
            teams[team].append(name)
except FileNotFoundError:
    print("File not found.")
else:
    print("Scores:", scores)
    print("Teams:", teams)
    print("Points by team:", points_by_team(scores, teams))