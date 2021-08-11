import leaguepedia_parser as lp
import pprint
pp = pprint.PrettyPrinter(indent=4)
# Joshua Prila
# November 19, 2020
# Snatch up picks and bans for Flyquest games in the 2020 LCS Summer Playoffs
# flyquest_summer2020Playoffs.py

role = 1 # 0 = Top. 1 = Jungle. 2 = Mid. 3 = Bot. 4 = Support

# Setup:
tournaments = lp.get_tournaments("North America", year=2020)
tourney = []
flyBans = []
gameData = []
for x in tournaments: 
    tourney.append(x["overviewPage"])
tourneyIDX = tourney.index("LCS/2020 Season/Summer Playoffs")
games = lp.get_games(tourney[tourneyIDX]) 


# Picks
# Champion picks for one specific role
rolepicks = []
for game in games:
    x = list(game.values())[8]
    for side in range(0,2):
        y = list(x.values())[side]
        if y.get('name') == "FlyQuest":
            z = y.get('players')
            appendMe = z[role]
            rolepicks.append(z[role].get('championName'))
# OUTPUT for specific role picks 
pp.pprint(rolepicks)

# Frequency
f = {}
count = 1
for champ in rolepicks:
        if champ in f.keys():
            tempCount = f.get(champ)
            tempCount += 1
            f[champ] = tempCount
            tempCount = 0
        else:
            f[champ] = 1
print("Frequency:")
pp.pprint(f)