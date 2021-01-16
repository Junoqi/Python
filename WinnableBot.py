import discord
from discord.ext import commands
import asyncio
import random
from random import randint

token = 'ODAwMTE2Njg2OTI5NTI2Nzk1.YANcuw.ZF539HG3BxTO-_HME4MdNEK9_fc'
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
    await ctx.send('ItzWinnable has made ' + str(randint(1, 999)) + ',' + str(randint(1, 999)) + ',' + str(randint(1, 999)) + ' excuses')

client.run(token)
