import leaguepedia_parser as lp
import pprint


# Gets regions names
regions = lp.get_regions()
# print(regions)
# ['', 'Africa', 'Asia', 'Brazil', 'China', 'CIS', 'Europe', 'International', 'Japan', 'Korea', 'LAN', 'LAS', 'Latin America', 'LMS', 'MENA', 'North America', 'Oceania', 'PCS', 'SEA', 'Turkey', 'Unknown', 'Vietnam', 'Wildcard']

# get_tournaments takes in string and integer, returns json dict (?) for containing info for all tournaments
# NA example: Spring split, Spring playoffs, Summer split, Summer playoffs
# Use overviewPage to obtain game information
tournaments = lp.get_tournaments("North America", year=2020)

# Here we can fill an array with overviewPage information for all tournaments in North America, for the 2020 season
tourney = []
for x in tournaments: 
    tourney.append(x["overviewPage"])

tourney.index("LCS/2020 Season/Summer Playoffs")
games = lp.get_games(tourney[0])
game = lp.get_game_details(games[0])
# Let's print out the stats of a game
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(game)