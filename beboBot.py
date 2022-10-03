# imports

from cgi import print_form
from riotwatcher import LolWatcher , TftWatcher
import config

import os
import discord
from dotenv import load_dotenv




# initialize

riotApiKey = config.api_key
watcherLol = LolWatcher(riotApiKey)

discordToken = config.discordToken
discordGuild = config.discordGuild
load_dotenv()
TOKEN = os.getenv(discordToken)
GUILD = os.getenv(discordGuild)

client = discord.Client(intents=discord.Intents.default())

#platform routing value
prv = 'NA1'
summonerName = 'b3b0'

summoner = watcherLol.summoner.by_name(prv, summonerName)

print(summoner)


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(summoner['summonerLevel'])

client.run(discordToken)