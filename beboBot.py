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

counter = 0

LP = my_ranked_stats[0].get('leaguePoints')
Rank = my_ranked_stats[0].get('tier')

print(my_ranked_stats)

@bot.command(name='beboLOL')
async def sendMessage(ctx):
    response = summoner['summonerLevel']
    await ctx.send(response)

#@bot.command(name='beboTFT', help="gives bebo's current rank in TFT")
@bot.command(name='test')
async def sendMessage(ctx):
    embed = discord.Embed(
        title="B3B0 Rank Tracker"
    )
    embed.add_field(
        name='Current Rank',
        value= str(Rank) + ' : ' + str(LP), 
    )
    await ctx.send(embed=embed)

bot.run(discordToken)