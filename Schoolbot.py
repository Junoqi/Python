import discord
from discord.ext import commands
import asyncio
import json 
import random
import time

#discord
token = 'Nzg0MDg4OTQ1MzY0NTY2MDU2.X8kNvA.-dDsHGPAjfLytImNlQqb2dlHQhA'
client = commands.Bot(command_prefix = '/', case_insensitive=True) 
client.remove_command('help')


#when logged on
@client.event  
async def on_ready():  
    print(f'We have logged in as {client.user}')
    await client.change_presence(activity=discord.Game(name="Kinda Awk"))
    print('Latency: ' + str(round(client.latency * 1000, 2)))
    print('==============')


@client.command()
async def awk(ctx):
    await ctx.send("Kinda awk")

@client.command()
async def heyl(ctx):
    await ctx.send("hey lol")

@client.command()
async def ant(ctx):
    await ctx.send("Kinda awk")

@client.command()
async def lhey(ctx):
    await ctx.send("lol hey")

@client.command()
async def solly(ctx):
    await ctx.send("Who want me?")

@client.command()
async def rule(ctx,*,number):
    if(number == "1"):
        await ctx.send("Rule 1: This is a server used for school, but not moderated by the school. This means that members have more freedom, but we want to keep this a welcoming and friendly environment for everyone. Keep everything PG-13. ")
    elif(number == "2"):
        await ctx.send("Rule 2: Being PG-13 means that there should not be any NSFW(not safe for work) images, jokes, references etc. If you post and delete something that is NSFW, Admins are still able to see it, so please follow these rules.")
    elif(number == "3"):
        await ctx.send("Rule 3: There will be no discrimination of race, skin color, ethnic, national or social origin, gender, language, religion, political opinion or any other opinion, financial status, birth or any other status, sexual orientation or any other reason. ")
    elif(number == "4"):
        await ctx.send("Rule 4: Please respect these rules, or admins will take appropriate action. ")
    elif(number == "5"):
        await ctx.send("Rule 5: All of this being said, the main use of this server is to connect upper and lowerclassmen, as we are unable to do so during this year, and to have a good time. Admins are here to help, and please feel free to reach out. ")
    elif(number == "6"):
        await ctx.send("Rule 6: Please refrain from streaming classes in calls. Similarly, please do not talk about teachers on this server. ")
    else: 
        await ctx.send(f"There is no rule number: {number}")


#help embed
@client.command()
async def help(ctx):
    author = ctx.message.author.mention

    embed = discord.Embed(
        colour = discord.Color.orange()
    )

    embed.set_author(name='Help')
    embed.add_field(name='!ant', value='Says: Kinda awk', inline=False)
    embed.add_field(name='!lhey', value='Says: lol hey', inline=False)
    embed.add_field(name='!heyl', value='Says: hey lol', inline=False)
    embed.add_field(name='solly', value='Says: who want me', inline=False)
    embed.add_field(name='!rule + number', value='Says: rule number *X*', inline=False)


    await ctx.send(embed=embed)
    print(str(ctx.message.author) + ' opened the !help page.')
    print('=======')


@client.event
async def on_message(message):  
    print(f"{message.channel}: {message.author.name}: {message.content}")
    await client.process_commands(message) 


client.run(token)
