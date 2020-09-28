from riotwatcher import LolWatcher
import pandas as pd
import json
import pprint
# Fetches ranked stats (and more) from riotAPI using riotwatcher/LoLWatcher
# Riot-Watcher: https://github.com/pseudonym117/Riot-Watcher 

# Setup and output generation
# API Key found in: https://developer.riotgames.com/
def outputGen(my_region="na1",username="Kiidlat",apiKey=1):
    watcher = LolWatcher(apiKey)

    me = watcher.summoner.by_name(my_region, username) # JSON object containing a LOT of data
    # the 'id' key is what holds your summoner ID
    my_ranked_stats = watcher.league.by_summoner(my_region, me['id']) # Returns JSON object output
    return my_ranked_stats

def flexGen(my_region="na1",username="Kiidlat",apiKey=1):
    # Obtains mastery level for top n champions, then divides by total champion mastery score
    n=50
    watcher = LolWatcher(apiKey)
    me = watcher.summoner.by_name(my_region,username)
    counter = 0
    champMastery = watcher.champion_mastery.by_summoner(my_region, me['id'])
    
    for i in range(0,n):
        #print(champMastery[i]['championId'])

        if champMastery[i]['championLevel'] == 5 or champMastery[i]['championLevel'] == 6 or champMastery[i]['championLevel'] == 7:
            counter+=1
    
    flexScore = watcher.champion_mastery.scores_by_summoner(my_region,me['id'])
    output = flexScore/counter
    return output

def matchHistory(my_region="na1",username="Kiidlat",apiKey=1):

    watcher = LolWatcher(apiKey)
    me = watcher.summoner.by_name(my_region, username)
    my_matches = watcher.match.matchlist_by_account(my_region, me['accountId'])
    lastMatch = my_matches['matches'][0]
    match_detail = watcher.match.by_id(my_region, lastMatch['gameId'])
    return match_detail

# Main asks for user input, then calls on outputGen (or searches for champions list in your region), then prints output
def main():
    
    x = 0
    x = int((input("Type '0' to find your ranked stats, or '1' for champion data, or '2' for champion mastery," 
    +"or '3' for last match details!")))

    if(x==0): # Print ranked stats
        my_region = (str)(input("Type in your region (NA is 'na1'): "))
        username = (str)(input("Type in your username (no spaces): "))
        apiKey = (str) (input("API Key: "))

        my_ranked_stats = outputGen(my_region,username,apiKey)
        # Use PrettyPrinter to format output
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(my_ranked_stats)

    elif(x==1): # Print champion data
        my_region = (str)(input("Type in your region (NA is 'na1'): "))
        apiKey = (str) (input("API Key: "))

        output = champions(my_region,apiKey)

        # Use PrettyPrinter to format output
        pp = pprint.PrettyPrinter(indent=4)
        # Champion output not clean
        pp.pprint(output)

    elif(x==2):
        my_region = (str)(input("Type in your region (NA is 'na1'): "))
        username = (str)(input("Type in your username (no spaces): "))
        apiKey = (str) (input("API Key: "))    
        output = flexGen(my_region, username, apiKey)
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(output)


    elif(x==3):
        my_region = (str)(input("Type in your region (NA is 'na1'): "))
        username = (str)(input("Type in your username (no space): "))
        apiKey = (str) (input("API Key: "))
        print("Last game info: ")
        match_detail = matchHistory(my_region,username,apiKey)

        # Very long output!!
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(match_detail)

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
    return (current_champ_list)

if __name__ == "__main__":
    main()
