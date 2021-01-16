import discord
from discord.ext import commands
import asyncio
import random
from random import randint

token = ''
client = commands.Bot(command_prefix = '/', case_insensitive=True)
client.remove_command('help')

print('poop')
#when logged on
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await client.change_presence(activity=discord.Game(name="VALORANT Battle Royale"))
    print('Latency: ' + str(round(client.latency * 1000, 2)))
    print('==============')

@client.command()
async def twitch(ctx):
    await ctx.send(f'{ctx.message.author.mention}, Check out itzwinnable at: https://www.twitch.tv/itzwinnable')

#Excuses
@client.command()
async def excuses(ctx):
    await ctx.send('ItzWinnable has made ' + str(randint(100, 999)) + ',' + str(randint(100, 999)) + ',' + str(randint(100, 999)) + ' excuses')

#help embed
@client.command()
async def help(ctx):
    author = ctx.message.author.mention

    embed = discord.Embed(
        colour = discord.Color.orange()
    )

    embed.set_author(name='Help')
    embed.add_field(name='/twitch', value='Sends twitch link of ItzWinnable' inline=False)
    embed.add_field(name='/excuses', value='Use this command to see how many excuses ItzWinnable has made!', inline=False)
    await ctx.send(embed=embed)

client.run(token)
