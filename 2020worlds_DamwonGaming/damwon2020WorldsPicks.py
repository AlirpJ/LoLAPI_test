import leaguepedia_parser as lp
import pprint

pp = pprint.PrettyPrinter(indent=4)

# Joshua Prila
# December 31, 2020
# Snatch up picks for Damwon's games in the 2020 World Championship

# Pick role and team name here
# 0 = Top. 1 = Jungle. 2 = Mid. 3 = Bot. 4 = Support
role = 1 
teamName = 'DAMWON Gaming'
#

# Setup:
tournaments = lp.get_tournaments("International", year=2020)
tourney = []
gameData = []
for x in tournaments: 
    tourney.append(x["overviewPage"])
tourneyIDX = tourney.index("2020 Season World Championship/Main Event")
games = lp.get_games(tourney[tourneyIDX]) 


# Picks
# Champion picks for one specific role

rolepicks = []
for game in games:
    x = list(game.values())[8]
    for side in range(0,2):
        y = list(x.values())[side]
        if y.get('name') == teamName:
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