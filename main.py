import discord
import typing
from discord.ext import commands
import requests
import json

bot = commands.Bot(command_prefix="!", description="Bot de Twitmund")

def mmrr_rankedS(username):
    req = requests.get(f"https://euw.whatismymmr.com/api/v1/summoner?name={username}")

    mmr = req.json()
    mmr_dump = json.dumps(mmr)
    mrrs = json.loads(mmr_dump)
    return (mrrs["ranked"]["avg"])

def mmrr_rank(username):
    req = requests.get(f"https://euw.whatismymmr.com/api/v1/summoner?name={username}")

    mmr = req.json()
    mmr_dump = json.dumps(mmr)
    mrrs = json.loads(mmr_dump)
    return (mrrs["ranked"]["closestRank"])

def mmrr_aram(username):
    req = requests.get(f"https://euw.whatismymmr.com/api/v1/summoner?name={username}")

    mmr = req.json()
    mmr_dump = json.dumps(mmr)
    mrrs = json.loads(mmr_dump)
    return (mrrs["ARAM"]["avg"])

def mmrr_normal(username):
    req = requests.get(f"https://euw.whatismymmr.com/api/v1/summoner?name={username}")

    mmr = req.json()
    mmr_dump = json.dumps(mmr)
    mrrs = json.loads(mmr_dump)
    return (mrrs["normal"]["avg"])


@bot.event
async def on_ready():
    print("Bot lancé")

@bot.command()
async def mmr(ctx, *arg):
    reason = "".join(arg)
    mmr_rankedS = mmrr_rankedS(reason)
    mmr_rank = mmrr_rank(reason)
    mmr_aram = mmrr_aram(reason)
    mmr_normal = mmrr_normal(reason)

    embed = discord.Embed(title="__MMR LOL__", description="Voici le mmr de "  + reason, color=0x4933ff)
    embed.set_author(name="Twitmund.exe")
    embed.add_field(name="Utilisateur :", value=f"{reason}", inline=False)
    embed.add_field(name="MMR normal :", value=f"{mmr_normal}",inline=False)
    embed.add_field(name="Rank :", value=f"{mmr_rank}", inline=False)
    embed.add_field(name="MMR ranked solo :", value=f"{mmr_rankedS}",inline=False)
    embed.add_field(name="MMR Aram :",value=f"{mmr_aram}", inline=False)
    embed.set_footer(text="MMR League of legends")
    await ctx.send(embed=embed)



bot.run()

