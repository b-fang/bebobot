# imports

from cgi import print_form
from riotwatcher import LolWatcher , TftWatcher
import config

import os
import discord
from dotenv import load_dotenv

from discord.ext import commands


# initialize

riotApiKey = config.api_key
watcherLol = LolWatcher(riotApiKey)

discordToken = config.discordToken

load_dotenv()
TOKEN = os.getenv(discordToken)

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

#platform routing value
prv = 'NA1'
summonerName = 'b3b0'


summoner = watcherLol.summoner.by_name(prv, summonerName)

my_ranked_stats = watcherLol.league.by_summoner(prv, summoner['id'])
print(my_ranked_stats)

@bot.command(name='beboLOL', help="gives bebo's current rank in solo/duo")
async def sendMessage(ctx):
    response = summoner['summonerLevel']
    await ctx.send(response)

#@bot.command(name='beboTFT', help="gives bebo's current rank in TFT")

bot.run(discordToken)