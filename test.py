from riotwatcher import LolWatcher
import pandas as pd
import json
import pprint
# Fetches ranked stats (and more) from riotAPI using riotwatcher/LoLWatcher
# Riot-Watcher: https://github.com/pseudonym117/Riot-Watcher 

# API Key found in: https://developer.riotgames.com/


# Main asks for user input, then calls on other functions to prints output
def main():
    running = True
    x = 0

    print("Hello! Please type your API Key below: ")
    apiKey = (str) (input("API Key: "))
    watcher = LolWatcher(apiKey)

    while(running):
        print("Hello! Pick one option: ")
        print("Type '0' to find your ranked stats ")
        print("Type '1' for champion data ")
        print("Type '2' for champion mastery ")
        print("Type '3' for last match details ")
        print("Type '4' to end program.")


        x = int((input("Enter your option here: ")))

        if(x==0): # Print ranked stats
            my_region = (str)(input("Type in your region (NA is 'na1'): "))
            username = (str)(input("Type in your username (no spaces): "))


            my_ranked_stats = outputGen(my_region,username,apiKey)
            # Use PrettyPrinter to format output
            pp = pprint.PrettyPrinter(indent=4)
            pp.pprint(my_ranked_stats)

        elif(x==1): # Print champion data
            my_region = (str)(input("Type in your region (NA is 'na1'): "))


            output = champions(my_region,apiKey)

            # Use PrettyPrinter to format output
            pp = pprint.PrettyPrinter(indent=4)
            # Champion output not clean
            pp.pprint(output)

        elif(x==2): # Print flexScore
            my_region = (str)(input("Type in your region (NA is 'na1'): "))
            username = (str)(input("Type in your username (no spaces): "))
  
            output = flexGen(my_region, username, apiKey)
            pp = pprint.PrettyPrinter(indent=4)
            print("FlexScore: ")
            pp.pprint(output)


        elif(x==3): # Print last match details
            my_region = (str)(input("Type in your region (NA is 'na1'): "))
            username = (str)(input("Type in your username (no space): "))
            print("Last game info: ")
            match_detail = matchHistory(my_region,username,apiKey)

            # (Warning: long output!)
            pp = pprint.PrettyPrinter(indent=4)
            pp.pprint(match_detail)

        elif(x==4): # End program
            print("Thank you! Have a great day :)")
            running = False
            break;

        #elif(x==-1): # TEST
        #    pass

        else:
            print("Error. entered invalid number. Please try again!")


# Setup and output generation

def outputGen(my_region="na1",username="Kiidlat",apiKey=1):
    watcher = LolWatcher(apiKey)

    me = watcher.summoner.by_name(my_region, username) # JSON object containing a LOT of data
    # the 'id' key is what holds your summoner ID
    my_ranked_stats = watcher.league.by_summoner(my_region, me['id']) # Returns JSON object output
    return my_ranked_stats

def champions(my_region,apiKey):
    # Returns output containing information for all champions
    # (Warning: long output!)
    watcher = LolWatcher(apiKey)
    # Prints data for champions
    versions = watcher.data_dragon.versions_for_region(my_region)
    champions_version = versions['n']['champion']

    current_champ_list = watcher.data_dragon.champions(champions_version)
    return (current_champ_list)

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
    
    totalMastery = watcher.champion_mastery.scores_by_summoner(my_region,me['id']) # Total champion mastery
    flexScore = totalMastery/counter 
    return flexScore

def matchHistory(my_region="na1",username="Kiidlat",apiKey=1):

    watcher = LolWatcher(apiKey)
    me = watcher.summoner.by_name(my_region, username)
    my_matches = watcher.match.matchlist_by_account(my_region, me['accountId'])
    lastMatch = my_matches['matches'][0]
    match_detail = watcher.match.by_id(my_region, lastMatch['gameId'])
    return match_detail


if __name__ == "__main__":
    main()
