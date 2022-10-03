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
discordGuild = config.discordGuild
load_dotenv()
TOKEN = os.getenv(discordToken)

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

#platform routing value
prv = 'NA1'
summonerName = 'b3b0'

summoner = watcherLol.summoner.by_name(prv, summonerName)

print(summoner)

@bot.command(name='bebo', help="gives bebo's current rank")
async def sendMessage(ctx):
    response = summoner['summonerLevel']
    await ctx.send(response)

bot.run(discordToken)