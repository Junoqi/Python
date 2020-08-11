import discord
from discord.ext import commands
import r6sapi as api
import asyncio

#discord
token = ''
client = commands.Bot(command_prefix = '.') 
client.remove_command('help')


#when logged on
@client.event  
async def on_ready():  
    print(f'We have logged in as {client.user}')
    await client.change_presence(activity=discord.Game(name="Just Vibin"))
    print('Latency: ' + str(round(client.latency * 1000, 2)))
    print('==============')

#print messages
@client.event
async def on_message(message):  
    print(f"{message.channel}: {message.author.name}: {message.content}")
    await client.process_commands(message)

#finds kd
@client.command()
async def kd(ctx,*,username):
    await ctx.send('Finding K/D for ' + username + '...')
  
    try:
        auth = api.Auth("spyhenry99@gmail.com", "katobear")
        player = await auth.get_player(username, api.Platforms.UPLAY)
        operator = await player.check_general()
        await ctx.send(str(username) + 's K/D is: ' + str((round(player.kills / player.deaths, 2))))

        await auth.close()
        print(str(ctx.message.author) + ' found the K/D ratio for ' + str(username) + '. It is: ' + str((round(player.kills / player.deaths, 2))) + '.')
        print('=======')

        if round(player.kills / player.deaths, 2) < 0.70:
            KDRoast = ['Maybe you should hit your shots :) ']
            await ctx.send(random.choice(KDRoast))
        
        if round(player.kills / player.deaths, 2) > 0.90:
            KDHacks = ['Bro we know you are aimbotting', 'Blocked and Reported']
            await ctx.send(random.choice(KDHacks))

    except:
        await ctx.send('An error occured. Unable to find that username :(')

#find total kills
@client.command()
async def kills(ctx,*,username):
    await ctx.send('Finding total kills for ' + username + '...')

    try:
        auth = api.Auth("spyhenry99@gmail.com", "katobear")
        player = await auth.get_player(username, api.Platforms.UPLAY)
        operator = await player.check_general()
        await ctx.send(str(username) + ' has ' + str(player.kills) + ' total kills')

        await auth.close() 

        print(str(ctx.message.author) + ' found the total kills for ' + str(username) + '. It is: ' + str(player.kills) + '.')
        print('=======')

    except:
        await ctx.send('An error occured. Unable to find that username :(')

#finds rank + mmr
@client.command()
async def rank(ctx,*,username):
    await ctx.send('Finding ' + str(username) + 's Rank and MMR')

    try:
        auth = api.Auth("spyhenry99@gmail.com", "katobear")

        player_batch = await auth.get_player_batch([username], api.Platforms.UPLAY)
        ranks = await player_batch.get_rank(api.RankedRegions.NA)

        for player in player_batch:
            rank = ranks[player.id]


        await ctx.send(str(username) + 's MMR is ' + str(rank.mmr))
        await ctx.send(str(username) + 's Rank is ' + str(rank.rank))

        await auth.close()
    except:
        await ctx.send('An error occured. Unable to find that username :(')

#help embed
@client.command()
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Color.orange()
    )

    embed.set_author(name='Help')
    embed.add_field(name='.kd', value='.kd + UPlay Username prints out the users K/D', inline=False)
    embed.add_field(name='.kills', value='.kills + UPlay Username prints out the users total kills', inline=False)
    embed.add_field(name='.rank', value='.rank + UPlay Username prints out the users current Rank and MMR', inline=False)
    embed.add_field(name='.role', value='.role + A game you play', inline=False)

    await ctx.send(author, embed=embed)
    print(str(ctx.message.author) + ' opened the !help page.')
    print('=======')

#on member join
@client.event
async def on_member_join(ctx):
    await ctx.send("Hey! Welcome to the server :) Please use  the .Role command + a game that you play so that we can identify what games you play!")

#autorole
@client.command()
async def role(ctx,*,message):
    if(message.lower() == 'valorant'):

        member = ctx.message.author

        role = discord.utils.get(member.guild.roles, name='Valorant')
        await member.add_roles(role)
        await ctx.send("Role Added :)")

    elif(message.lower() == 'siege'):

        member = ctx.message.author

        role = discord.utils.get(member.guild.roles, name='Siege')
        await member.add_roles(role)
        await ctx.send("Role added :)")
    
    elif(message.lower() == 'admins'):
        await ctx.send("Please contact and Admin if you would like to become an administrator or moderator")
    
    else:
        await ctx.send('''Sorry :( That isn't a game this server supports right now. Contact an administrator  if you want to add that to the list of roles.''')
    
#run 
client.run(token)
