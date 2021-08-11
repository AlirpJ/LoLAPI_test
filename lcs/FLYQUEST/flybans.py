import leaguepedia_parser as lp
import pprint

# Setup:
pp = pprint.PrettyPrinter(indent=4)
tournaments = lp.get_tournaments("North America", year=2020)
tourney = []
flyBans = []
flyBans_versus = []
gameData = []
for x in tournaments: 
    tourney.append(x["overviewPage"])
tourneyIDX = tourney.index("LCS/2020 Season/Summer Playoffs")
games = lp.get_games(tourney[tourneyIDX]) 


#
# THEORY / UNDERSTANDING THE OUTPUT
#n = 0 # different numbers correspond to different games
# for any game x, list(x.values()) will present an array with information for the game
# As of now, index 8 contains a dictionary with blue and red side draft

#y = list(games[n].values())[8] 
#n2 = 0 # Set to 1 for blue side, and set to 2 for red side
#z = list(y.values())[n2]

# if you do [ z.get('name') == "FlyQuest": ] # obtain picks and bans for this side
# From here, we can do "z.get("bansNames")" to obtain bans for one side of a game.
# :)
#

# Bans for all games of one team (teamChoice) in a given tournament
teamChoice = "FlyQuest"
for game in games:
    x = list(game.values())[8]
    for side in range(0,2):
        y = list(x.values())[side]
        if y.get('name') == teamChoice:
            z = y.get("bansNames")
            flyBans.append(z)

for cc in range (0,len(flyBans)):
    indec = cc + 1
    indec = str(indec)
    ban = str(flyBans[cc])
    string = ("Game "+indec+": "+ ban)
    ##pp.pprint(string) # Prints bans for the game examined
# Get count
f = {}
count = 0
for lst in flyBans:
    for champ in lst:
        if champ in f.keys():
            tempCount = f.get(champ)
            tempCount += 1
            f[champ] = tempCount
            tempCount = 0
        else:
            f[champ] = 1
#f = sorted(f.items()) # lol idk how to sort the dict... ordered dictionaries?
# OUTPUT HERE FOR BANS:
print("Bans By Frequency: ")
pp.pprint(f)

# Alternate version, bans against your teamChoice
for game in games:
    x = list(game.values())[8]
    for side in range(0,2):
        y = list(x.values())[side]
        if y.get('name') == teamChoice:
            z = y.get("bansNames")
            if side == 0:
                z = list(x.values())[1].get("bansNames")
            elif side == 1:
                list(x.values())[0].get("bansNames")
            flyBans_versus.append(z)
print("Bans against "+teamChoice+":")
pp.pprint(flyBans_versus)
f2 = {}
count = 0
for lst in flyBans:
    for champ in lst:
        if champ in f2.keys():
            tempCount = f.get(champ)
            tempCount += 1
            f2[champ] = tempCount
            tempCount = 0
        else:
            f2[champ] = 1
print("By Frequency: ")
pp.pprint(f2)
