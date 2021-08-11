import leaguepedia_parser as lp
import pprint
pp = pprint.PrettyPrinter(indent=4)


# Joshua Prila
# LCS Lock In Tournament, 2020

# Pick role and team name here
# 0 = Top. 1 = Jungle. 2 = Mid. 3 = Bot. 4 = Support
role = 1
teamName = 'Cloud9'


regions = lp.get_regions()
# print(regions)
# ['', 'Africa', 'Asia', 'Brazil', 'China', 'CIS', 'Europe', 'International', 'Japan', 'Korea', 'LAN', 'LAS', 'Latin America', 'LMS', 'MENA', 'North America', 'Oceania', 'PCS', 'SEA', 'Turkey', 'Unknown', 'Vietnam', 'Wildcard']

tournaments = lp.get_tournaments("North America", year=2021)

tourney = []
for x in tournaments: 
    tourney.append(x["overviewPage"])

pick = "LCS/2021 Season/Lock In"
tourneyIDX = tourney.index(pick) # TourneyIDX is idx of desired tournament

games = lp.get_games(tourney[tourneyIDX])
game = lp.get_game_details(games[0]) 


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

print(teamName)
print(pick)
