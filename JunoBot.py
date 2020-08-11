import discord
from discord.ext import commands

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

#help embed
@client.command()
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Color.orange()
    )

    embed.set_author(name='Help')

    await ctx.send(author, embed=embed)
    print(str(ctx.message.author) + ' opened the !help page.')
    print('=======')

@client.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    if reaction.emoji == '😎':
        role = discord.utils.get(user.guild.roles, name='boy')
        await user.add_roles(role)
        await channel.send("Role added: Boy")
    
    elif reaction.emoji == '😋':
        role = discord.utils.get(user.guild.roles, name='girl')
        await user.add_roles(role)
        await channel.send("Role added: Girl")
    
    elif reaction.emoji == '💯':
        role = discord.utils.get(user.guild.roles, name='rb6')
        await user.add_roles(role)
        await channel.send("Role added: RB6")

@client.event
async def on_member_join(ctx):
    await ctx.send("Hey! Welcome to the server: Kingdom Of Antz :) Send a message and then react to it in the Your Roles channel to set gender and game roles. 💯 is for Rainbow Six, 😋 is for girl, and 😎 is for boy. This helps the other members of the server identify you properly")




#run 
client.run(token)
