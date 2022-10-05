# imports

from riotwatcher import LolWatcher , TftWatcher
import config

import os
import discord
from dotenv import load_dotenv

from discord.ext import commands


rankImg = {
    0: 'https://raw.githubusercontent.com/b-fang/bebobot/master/rankedImages/Iron.png',
    1: 'https://raw.githubusercontent.com/b-fang/bebobot/master/rankedImages/Bronze.png',
    2: 'https://raw.githubusercontent.com/b-fang/bebobot/master/rankedImages/Silver.png',
    3: 'https://raw.githubusercontent.com/b-fang/bebobot/master/rankedImages/Gold.png',
    4: 'https://raw.githubusercontent.com/b-fang/bebobot/master/rankedImages/Platinum.png',
    5: 'https://raw.githubusercontent.com/b-fang/bebobot/master/rankedImages/Diamond.png',
    6: 'https://raw.githubusercontent.com/b-fang/bebobot/master/rankedImages/Master.png',
    7: 'https://raw.githubusercontent.com/b-fang/bebobot/master/rankedImages/Grandmaster.png',
    8: 'https://raw.githubusercontent.com/b-fang/bebobot/master/rankedImages/Challenger.png',
}

# initialize

riotApiKey = config.api_key
watcherLol = LolWatcher(riotApiKey)
watcherTFT = TftWatcher(riotApiKey)

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
summonerTFT = watcherTFT.summoner.by_name(prv, summonerName)

my_ranked_stats = watcherLol.league.by_summoner(prv, summoner['id'])
tft_stats = watcherTFT.league.by_summoner(prv, summonerTFT['id'])

#swapped tier and ranked since the api's naming scheme seems backwards to me
LP = my_ranked_stats[0].get('leaguePoints')
Rank = my_ranked_stats[0].get('tier')
tier = my_ranked_stats[0].get('rank')

LP_TFT = tft_stats[0].get('leaguePoints')
RankTFT = tft_stats[0].get('tier')
tierTFT =tft_stats[0].get('rank')

def checkRank(Rank):
    imgSelect = 0
    if(Rank == 'BRONZE'):
        imgSelect = 1
    elif(Rank == 'SILVER'):
        imgSelect = 2
    elif(Rank == 'GOLD'):
        imgSelect = 3
    elif(Rank == 'PLATINUM'):
        imgSelect = 4
    elif(Rank == 'DIAMOND'):
        imgSelect = 5
    elif(Rank == 'MASTER'):
        imgSelect = 6
    elif(Rank == 'GRANDMASTER'):
        imgSelect = 7
    elif(Rank == 'CHALLENGER'):
        imgSelect = 8
    return imgSelect

#@bot.command(name='TFT', help="gives bebo's current rank in TFT")
@bot.command(name='TFT')
async def sendMessage(ctx):
    embed = discord.Embed(
        title="B3B0 Rank Tracker",
    )
    embed.set_thumbnail(url=rankImg[checkRank(RankTFT)])
    embed.add_field(
        name='Current Rank',
        value= str(RankTFT) + ' ' + tierTFT + ' : ' + str(LP_TFT) + ' LP',
    )
    await ctx.send(embed=embed)

#@bot.command(name='LOL', help="gives bebo's current rank in solo/duo")
@bot.command(name='LOL')
async def sendMessage(ctx):
    embed = discord.Embed(
        title="B3B0 Rank Tracker",
    )
    embed.set_thumbnail(url=rankImg[checkRank(Rank)])
    embed.add_field(
        name='Current Rank',
        value= str(Rank) + ' ' + tier + ' : ' + str(LP) + ' LP',
    )
    await ctx.send(embed=embed)


#help command

bot.remove_command('help')
@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="Bot Commands",
        description = "These are the currently available commands:"
    )
    embed.add_field(
        name='Commands',
        value='!LOL : displays current rank in solo/duo for summoner b3b0\n !TFT : displays current rank in TFT for summoner b3b0'
    )
    await ctx.send(embed=embed)

bot.run(discordToken)