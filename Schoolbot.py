import discord
from discord.ext import commands
import asyncio
import json 
import random
import time

#discord 
token = ''
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
    await client.delete_message(ctx.message)
    await ctx.send("Kinda awk")

@client.command()
async def heyl(ctx):
    await client.delete_message(ctx.message)
    await ctx.send("hey lol")

@client.command()
async def ant(ctx,*,number):
    if(number == "1"):
        await ctx.send("Kinda awk")
    elif(number == "2"):
        await ctx.send("Sorta awk")
    elif(number == "3"):
        await ctx.send("Kind of awk")

    await client.delete_message(ctx.message)

@client.command()
async def lhey(ctx):
    await client.delete_message(ctx.message)
    await ctx.send("lol hey")

@client.command()
async def solly(ctx):
    await client.delete_message(ctx.message)
    await ctx.send("Who want me?")



@client.command()
async def rule(ctx,*,number):
    await client.delete_message(ctx.message)

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


snipe_message_content = None
snipe_message_author = None
snipe_message_id = None

@client.event
async def on_message_delete(message):

    global snipe_message_content
    global snipe_message_author
    global snipe_message_id


    snipe_message_content = message.content
    snipe_message_author = message.author.id
    snipe_message_id = message.id

    await asyncio.sleep(60)

    if message.id == snipe_message_id:
        snipe_message_author = None
        snipe_message_content = None
        snipe_message_id = None


@client.command()
async def snipe(message):

    snipe_name = client.get_user(snipe_message_author)

    if snipe_message_content==None:
        await message.channel.send("Theres nothing to snipe.")

    else:
        embed = discord.Embed(description=f"{snipe_message_content}")
        embed.set_footer(text=f"Asked by {message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
        embed.set_author(name= f"{snipe_name.name} said:")
        await message.channel.send(embed=embed)
        return

#help embed
@client.command()
async def help(ctx):
    author = ctx.message.author.mention

    embed = discord.Embed(
        colour = discord.Color.orange()
    )

    embed.set_author(name='Help')
    embed.add_field(name='/ant', value='Says: Kinda awk', inline=False)
    embed.add_field(name='/lhey', value='Says: lol hey', inline=False)
    embed.add_field(name='/heyl', value='Says: hey lol', inline=False)
    embed.add_field(name='/solly', value='Says: who want me', inline=False)
    embed.add_field(name='/rule + number', value='Says: rule number *X*', inline=False)


    await ctx.send(embed=embed)
    print(str(ctx.message.author) + ' opened the !help page.')
    print('=======')


@client.event
async def on_message(message):  
    print(f"{message.channel}: {message.author.name}: {message.content}")
    await client.process_commands(message) 


client.run(token)
