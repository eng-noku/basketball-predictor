def average(scores):
    total = 0
    for score in scores:
        total = total + score
    result = total / len(scores)
    return result
def rating(scored, allowed):
    points = average(scored)
    conceded = average(allowed)
    overall = points - conceded
    return overall
teams = []
file = open("teams.txt")
for line in file:
    line = line.strip()
    parts = line.split(",")
    name = parts[0]
    scored = []
    allowed = []
    for piece in parts[1].split():
        scored.append(float(piece))
    for piece in parts[2].split():
        allowed.append(float(piece))
    team = {"name": name, "scored": scored, "allowed": allowed}
    teams.append(team)
file.close()
home_bonus = 3
def find_team(name):
    name = name.lower().strip()
    for team in teams:
        if team["name"].lower() == name:
            return team
name1 = input("First team ")
name2 = input("Second team ")
team_a = find_team(name1)
team_b = find_team(name2)
if team_a is None or team_b is None:
    print("I do not recognize that team")
elif team_a["name"] == team_b["name"]:
    print("A team cannot play against itself")
else:
    rating_a = rating(team_a["scored"], team_a["allowed"])
    rating_b = rating(team_b["scored"], team_b["allowed"])
    home = input("Which team is at home? ")
    home = home.lower().strip()
    while home != team_a["name"].lower() and home != team_b["name"].lower():
        print("you can only pick between", team_a["name"], "and", team_b["name"])
        home = input("Which team is at home? ")
        home = home.lower().strip()
    if home == team_a["name"].lower():
        rating_a = rating_a + home_bonus
    elif home == team_b["name"].lower():
        rating_b = rating_b + home_bonus
    print(team_a["name"], "rating:", round(rating_a, 1), "vs", team_b["name"], "rating:", round(rating_b, 1))
    if rating_a > rating_b:
        print(team_a["name"], "wins by", round(rating_a - rating_b, 1))
    elif rating_b > rating_a:
        print(team_b["name"], "wins by", round(rating_b - rating_a, 1))
    else:
        print("Its going to be a tie")

