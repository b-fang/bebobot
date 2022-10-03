# imports

from cgi import print_form
from riotwatcher import LolWatcher , TftWatcher
import config

# initialize

riotApiKey = config.api_key
watcherLol = LolWatcher(riotApiKey)

#platform routing value
prv = 'NA1'
summonerName = 'b3b0'

summoner = watcherLol.summoner.by_name(prv, summonerName)

print(summoner)
