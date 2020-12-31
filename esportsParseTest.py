import leaguepedia_parser as lp
import pprint
pp = pprint.PrettyPrinter(indent=4)

# Joshua Prila
# Use this for learning purposes

# Gets regions names
regions = lp.get_regions()
# print(regions)
# ['', 'Africa', 'Asia', 'Brazil', 'China', 'CIS', 'Europe', 'International', 'Japan', 'Korea', 'LAN', 'LAS', 'Latin America', 'LMS', 'MENA', 'North America', 'Oceania', 'PCS', 'SEA', 'Turkey', 'Unknown', 'Vietnam', 'Wildcard']

# get_tournaments takes in string and integer, returns json object (just like python dictionaries) for containing info for all tournaments
# NA example: Spring split, Spring playoffs, Summer split, Summer playoffs
# Use overviewPage to obtain game information
tournaments = lp.get_tournaments("International", year=2020)

# Here we can fill an array with overviewPage information for all tournaments Internationally, for the 2020 season
tourney = []
for x in tournaments: 
    tourney.append(x["overviewPage"])

tourneyIDX = tourney.index("2020 Season World Championship/Main Event") # TourneyIDX is idx of desired tournament
# In this case, our desired tournament is "2020 Season World Championship/Main Event"
# Another example is "LCS/2020 Season/Summer Playoffs, for region "North America"."

games = lp.get_games(tourney[tourneyIDX])
game = lp.get_game_details(games[-1]) 
# games[-1] respresents the last professional game of 2020, which is the final game of the 2020 World Championship Finals

# Let's print out the stats of this game:

pp.pprint(game)

# Should be able to play with it from there. There are endless possibilities on using this data!
