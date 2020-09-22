from riotwatcher import LolWatcher
import pandas as pd
import json
import pprint
# Fetches ranked stats from riotAPI using riotwatcher/LoLWatcher
# Riot-Watcher: https://github.com/pseudonym117/Riot-Watcher 

# Setup and output generation
# API Key found in: https://developer.riotgames.com/
def outputGen(my_region="na1",username="Kiidlat",apiKey=1):
    watcher = LolWatcher(apiKey)

    me = watcher.summoner.by_name(my_region, username) # JSON object containing a LOT of data
    # the 'id' key is what holds your summoner ID
    my_ranked_stats = watcher.league.by_summoner(my_region, me['id']) # Returns JSON object output
    return my_ranked_stats

# Main asks for user input, then calls on outputGen, then prints output
def main():
    
    x = 0
    x = int((input("Type '0' to find your ranked stats, or type 1 for champion data! ")))
    
    if(x==1): # Print champion data
        my_region = (str)(input("Type in your region (NA is 'na1'): "))
        apiKey = (str) (input("API Key: "))

        output = champions(my_region,apiKey)

        # Use PrettyPrinter to format output
        pp = pprint.PrettyPrinter(indent=4)
        # Champion output not clean
        pp.pprint(x)

    elif(x==0): # Print ranked stats
        my_region = (str)(input("Type in your region (NA is 'na1'): "))
        username = (str)(input("Type in your username (no spaces): "))
        apiKey = (str) (input("API Key: "))

        my_ranked_stats = outputGen(my_region,username,apiKey)
        # Use PrettyPrinter to format output
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(my_ranked_stats)

        #print("Last game info: ")
        #watcher = LolWatcher(apiKey)
        #me = watcher.summoner.by_name(my_region, username)
        #my_matches = watcher.match.matchlist_by_account(my_region, me['accountId'])
        #lastMatch = my_matches['matches'][0]
        #match_detail = watcher.match.by_id(my_region, lastMatch['gameId'])
        # Very long output!!
        #pp.pprint(match_detail)

        
    else:
        print("Error. entered invalid number. Please try again! :)")

# Returns output containing information for all champions
# (Warning: long output!)
def champions(my_region,apiKey):
    watcher = LolWatcher(apiKey)
    # Prints data for champions
    versions = watcher.data_dragon.versions_for_region(my_region)
    champions_version = versions['n']['champion']

    current_champ_list = watcher.data_dragon.champions(champions_version)
    print(current_champ_list)

if __name__ == "__main__":
    main()
