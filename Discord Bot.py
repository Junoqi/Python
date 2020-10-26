import discord
from discord.ext import commands
import asyncio
import json 
import random
import time

#discord
token = ''
client = commands.Bot(command_prefix = '!') 
client.remove_command('help')


#when logged on
@client.event  
async def on_ready():  
    print(f'We have logged in as {client.user}')
    await client.change_presence(activity=discord.Game(name="Goldfish Eating Sim"))
    print('Latency: ' + str(round(client.latency * 1000, 2)))
    print('==============')


@client.event
async def on_message(message):  
    print(f"{message.channel}: {message.author.name}: {message.content}")
    await client.process_commands(message) 

    await open_account(message.author)

    if message.content == '!beg':
        return False
    elif message.content == '!balance':
        return False
    elif '!send' in message.content:
        return False
    elif '!leaderboard' in message.content:
        return False
    elif '!withdrawl' in message.content:
        return False
    elif message.author.name == 'Noodle bot':
        return False
    else:
        await AddMoney(message.author, 1)
    
@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "roles":
            await channel.send(f"Hey {member.mention}! Welcome to the Noodle Gang server :) Please use  the !Role command + (minecraft overwatch valorant minecraft destiny2 siege) in the roles channel so that we can identify what games you play!")
    
    role = discord.utils.get(member.guild.roles, name='noodle')
    await member.add_roles(role)

@client.command()
async def balance(ctx, user: discord.Member):
    with open("users.json", "r") as f:
        users = json.load(f)

    try:
        await open_account(user)
    except:
        ctx.send("Please enter a member name! Try Again!")
    wallet_amt = users[str(user.id)]["wallet"]

    await ctx.send(f"{user.mention} has {wallet_amt} noodles!")

@client.command()
@commands.cooldown(1, 3600, commands.BucketType.user)
async def beg(ctx):

    with open("users.json", "r") as f:
        users = json.load(f)

    user = ctx.author

    await open_account(ctx.author)

        
    earnings = random.randrange(10)

    users[str(user.id)]["wallet"] += earnings

    await ctx.send(f"Noodle god gave you {earnings} noodles!")
 
    with open('users.json', 'w') as outfile:
        json.dump(users, outfile)

# async def BankCreated(channel):
#     await channel.send(f"Account has been created :)")

@client.command()
async def withdraw(ctx,amount = None):

    with open("users.json", "r") as f:
        users = json.load(f)

    await open_account(ctx.author)

    if amount == None:
        await ctx.send("Please enter the amount")
        return

    wallet_amt = users[str(ctx.author.id)]["wallet"]


    amount = int(amount)
    if amount>wallet_amt:
        await ctx.send("You dont have sufficient funds!")
        return
    elif amount<0:
        await ctx.send("Amount must be positive")
        return
    
    await update_bank(ctx.author,-1*amount)

    await ctx.send(f"You withdrew {amount} noodles")

@client.command()
async def gamble(ctx,amount = None):

    with open("users.json", "r") as f:
        users = json.load(f)

    await open_account(ctx.author)

    if amount == None:
        await ctx.send("Please enter the amount")
        return

    wallet_amt = users[str(ctx.author.id)]["wallet"]

    amount = int(amount)
    if amount>wallet_amt:
        await ctx.send("You dont have sufficient funds!")
        return
    if amount<=wallet_amt and amount == 69:
        await update_bank(ctx.author, amount)
        await ctx.send("Hehehe...")
        return
    elif amount<0:
        await ctx.send("Amount must be positive")
        return
    
    final_list = []
    for i in range(3):
        choices = random.choice(["💩","👩","👨"])

        final_list.append(choices)

    await ctx.send(str("{" + final_list[0] + final_list[1] + final_list[2]) + "}")

    if final_list[0] == final_list[1] and final_list[0] == final_list[1] and final_list[0] == final_list[2]:
        await update_bank(ctx.author,amount)
        await ctx.send("You won!")
    else:
        await update_bank(ctx.author,-1*amount)
        await ctx.send("You lost!")

@client.command()
async def leaderboard(ctx, x = 5):
    with open("users.json", "r") as f:
        users = json.load(f)
    
    if x > len(users):
        await ctx.send("There aren't that many member accounts! Try again!")
        return


    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"]
        leader_board[total_amount] = name 
        total.append(total_amount)

    total = sorted(total,reverse=True)

    em = discord.Embed(title = f"Top {x} Richest Server Members")
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = client.get_user(id_)
        name = member.name
        em.add_field(name = f"{index}. {name}", value = f"{amt}", inline = False)
        if index == x:
            break
        else:
            index += 1

    await ctx.send(embed = em)     

@client.command()
async def send(ctx,member:discord.Member,amount = None):

    with open("users.json", "r") as f:
        users = json.load(f)

    await open_account(ctx.author)
    await open_account(member)
    
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    wallet_amt = users[str(ctx.author.id)]["wallet"]


    amount = int(amount)
    if amount>wallet_amt:
        await ctx.send("You dont have sufficient funds!")
        return
    elif amount<0:
        await ctx.send("Amount must be positive")
        return
    
    await update_bank(ctx.author,-1*amount)
    await update_bank(member,amount)

    await ctx.send(f"{ctx.author.mention} gave {member.mention} {amount} noodles")

async def update_bank(user, change = 0):
    with open("users.json", "r") as f:
        users = json.load(f)

    users[str(user.id)]["wallet"] += change

    with open('users.json', 'w') as outfile:
        json.dump(users, outfile)


async def AddMoney(user, amount):
    with open("users.json", "r") as f:
        users = json.load(f)

    await open_account(user)

    users[str(user.id)]["wallet"] += amount

    with open('users.json', 'w') as outfile:
        json.dump(users, outfile)

async def SubMoney(user, amount):
    with open("users.json", "r") as f:
        users = json.load(f)

    await open_account(user)

    users[str(user.id)]["wallet"] - amount

    with open('users.json', 'w') as outfile:
        json.dump(users, outfile)



async def open_account(user):

    with open("users.json", "r") as f:
        users = json.load(f)

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        # await BankCreated(user)

    with open("users.json", "w") as f:
        users = json.dump(users,f)

async def get_bank_data():
    with open("users.json", "r") as f:
        users = json.load(f)

#autorole
@client.command()
async def role(ctx,*,message):
    if(message.lower() == 'valorant'):

        member = ctx.message.author

        role = discord.utils.get(member.guild.roles, name='valorant')
        await member.add_roles(role)
        await ctx.send("Valorant Role Added :)")

    elif(message.lower() == 'siege'):

        member = ctx.message.author

        role = discord.utils.get(member.guild.roles, name='siege')
        await member.add_roles(role)
        await ctx.send("Siege Role added :)")
    
    elif(message.lower() == 'destiny2'):

        member = ctx.message.author

        role = discord.utils.get(member.guild.roles, name='destiny2')
        await member.add_roles(role)
        await ctx.send("Destiny 2 Role added :)")

    elif(message.lower() == 'minecraft'):

        member = ctx.message.author

        role = discord.utils.get(member.guild.roles, name='minecraft')
        await member.add_roles(role)
        await ctx.send("Minecraft Role added :)")
    
    elif(message.lower() == 'overwatch'):

        member = ctx.message.author

        role = discord.utils.get(member.guild.roles, name='overwatch')
        await member.add_roles(role)
        await ctx.send("Overwatch Role added :)")
    
    elif(message.lower() == 'big boi'):

        member = ctx.message.author

        role = discord.utils.get(member.guild.roles, name='big boi')
        await member.add_roles(role)
        await ctx.send("Big boi role added :) (Warning! This is an NSFW role!)")   
        
    elif(message.lower() == 'halo'):

        member = ctx.message.author

        role = discord.utils.get(member.guild.roles, name='halo')
        await member.add_roles(role)
        await ctx.send("Halo Role added :)") 

    elif(message.lower() == 'noodle mod'):
        await ctx.send("Please contact and Admin if you would like to become an administrator or moderator")
    
    else:
        await ctx.send('''Sorry :( That isn't a game this server supports right now. Contact an administrator  if you want to add that to the list of roles.''')


@client.command()
async def removerole(ctx,*,message):
    if(message.lower() == 'valorant'):

        member = ctx.message.author

        role = discord.utils.get(member.guild.roles, name='valorant')
        await member.remove_roles(role)
        await ctx.send("Valorant Role removed :(")

    elif(message.lower() == 'siege'):

        member = ctx.message.author

        role = discord.utils.get(member.guild.roles, name='siege')
        await member.remove_roles(role)
        await ctx.send("Siege Role removed :(")
    
    elif(message.lower() == 'destiny2'):

        member = ctx.message.author

        role = discord.utils.get(member.guild.roles, name='destiny2')
        await member.remove_roles(role)
        await ctx.send("Destiny 2 Role removed :(")

    elif(message.lower() == 'minecraft'):

        member = ctx.message.author

        role = discord.utils.get(member.guild.roles, name='minecraft')
        await member.remove_roles(role)
        await ctx.send("Minecraft Role removed :(")
    
    elif(message.lower() == 'overwatch'):

        member = ctx.message.author

        role = discord.utils.get(member.guild.roles, name='overwatch')
        await member.remove_roles(role)
        await ctx.send("Overwatch Role removed :(")
    
    elif(message.lower() == 'big boi'):

        member = ctx.message.author

        role = discord.utils.get(member.guild.roles, name='big boi')
        await member.remove_roles(role)
        await ctx.send("Big boi role removed :(")   
        
    elif(message.lower() == 'halo'):

        member = ctx.message.author

        role = discord.utils.get(member.guild.roles, name='halo')
        await member.remove_roles(role)
        await ctx.send("Halo Role removed :(") 

    elif(message.lower() == 'all'):

        member = ctx.message.author

        role = discord.utils.get(member.guild.roles, name='halo')
        role1 = discord.utils.get(member.guild.roles, name='siege')
        role2 = discord.utils.get(member.guild.roles, name='destiny2')
        role3 = discord.utils.get(member.guild.roles, name='minecraft')
        role4 = discord.utils.get(member.guild.roles, name='overwatch')
        role5 = discord.utils.get(member.guild.roles, name='big boi')

        await member.remove_roles(role)
        await member.remove_roles(role1)
        await member.remove_roles(role2)
        await member.remove_roles(role3)
        await member.remove_roles(role4)
        await member.remove_roles(role5)

        await ctx.send("All roles removed :(") 





#roaster
@client.event
async def on_command_error(ctx, error):

    if isinstance(error, commands.CommandNotFound):

        roasts = ['Imagine being a dummy', 'Imagine not reading the !help page', 'lol what a bot. I bet my code has more brain than u.', 'Nice try stupid. Next time try harder.', 'Yooo we got a dumb one here guys.', 'Haha i bet noodle is smarter than u.']

        await ctx.send('Shout out to ' + ctx.message.author.mention + ' for getting the command wrong.')
        await ctx.send(random.choice(roasts))

         
        
        print(str(ctx.message.author) + ' Used this: ' + str(ctx.message.content) + ' Instead of the correct command.')
    
    if isinstance(error, discord.ext.commands.errors.CommandOnCooldown):
        if error.retry_after > 60:
            minutes = int(error.retry_after) / 60
            await ctx.send("Sorry, that command is on cooldown for {:.0f} more minutes.".format(minutes))
        else:
            await ctx.send("Sorry, that command is on cooldown for {:.0f} more seconds.").format(error.retry_after)

# #censor
@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
@commands.has_permissions(manage_messages=True)
async def censor(ctx,*,amount):
    try:
        if(int(amount) > 10):
            await ctx.send("The clear command can only clear up to 10 messages.")
        else:
            await ctx.channel.purge(limit=int(amount) + 1)
    except:
        await ctx.send("Sorry you dont have permission to use this command")
#choir
@client.command()
async def choir(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send(str(ctx.message.author) + ' has summoned the choir.')
    await ctx.send(':-0')
    await ctx.send(':-o')
    await ctx.send(':-0')
    await ctx.send(':-o')
    await ctx.send(':-0')

    print(ctx.message.author.name + ' has summoned the choir')


#finds bot latency
@client.command()
async def ping(ctx):
    await ctx.send(f'Ping is {round(client.latency * 1000)} ms')
    print(str(ctx.message.author) + ' tested the bots latency. It is: ' + str(round(client.latency * 1000)) + ' ms')
    print('=======')


@client.command()
async def gun(ctx):

    PrimGuns = ['Stinger', 'Spectre', 'Bucky', 'Judge', 'BullDog', 'Guardian', 'Phantom', 'Vandal', 'Marshal', 'Operator', 'Ares', 'Odin']
    SecGuns = ['Classic', 'Shorty', 'Frenzy', 'Ghost', 'Sheriff']

    await ctx.send('Primary: ' + random.choice(PrimGuns))
    await ctx.send('Secondary: ' + random.choice(SecGuns))
    
#clear messages
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx,*,amount):
    await ctx.channel.purge(limit=int(amount))
    print(str(ctx.message.author) + ' cleared ' + str(amount) + ' messages from ' + str(ctx.message.channel) + ' text chat.')
    print('=======')

#help embed
@client.command()
async def help(ctx):
    author = ctx.message.author.mention

    embed = discord.Embed(
        colour = discord.Color.orange()
    )

    embed.set_author(name='Help')
    embed.add_field(name='!ball', value='!ball + a question returns a magic 8 ball response', inline=False)
    embed.add_field(name='!censor', value='Use this command to delete any previous strange message', inline=False)
    embed.add_field(name='!ping', value='Returns the bot latency', inline=False)
    embed.add_field(name='!clear', value='!clear + amount Clears the selected amount of messages (ONLY AVAILABLE TO ADMINS)', inline=False)
    embed.add_field(name='!balance', value='!balance + @User returns that users noodle count', inline=False)
    embed.add_field(name='!leaderboard', value='!leaderboard + AMOUNT returns the top AMOUNT richest member of the server ', inline=False)
    embed.add_field(name='!beg', value='The gods gift the user a random amount of noodles between 1-10. Can only be used once per hour.', inline=False)
    embed.add_field(name='!send', value='!send + @User + AMOUNT sends @User AMOUNT noodles.', inline=False)


    await ctx.send(embed=embed)
    print(str(ctx.message.author) + ' opened the !help page.')
    print('=======')

#developer tools
@client.command()
async def sleep(ctx, *, message):
    if(ctx.message.author.name == 'Junoqi'):
        await ctx.send('Noodle Bot will be logging off for the night. See you in the morning! :)')
        exit()
    
    else:
        await ctx.send('You do not have permissions to excecute this command')

#spam
# @client.command()
# @commands.cooldown(2, 60, commands.BucketType.user)
# async def spam(ctx,*,message):
#     await ctx.send('Spam has been initiated on ' + message.upper())

#     if message.lower() == 'ryan':
#         id = '<@430451874773073960>'
#         for x in range(5):

#             await ctx.send(id + ' it appears you are late')

#     elif message.lower() == 'viper':
#         id = '<@509473152997261330>'

#         for x in range(5):

#             await ctx.send(id + ' it appears you are late')

#     if message.lower() == 'henry':
#         id = '<@477961589178499094>'

#         for x in range(5):

#             await ctx.send(id + ' it appears you are late')

    
#     elif message.lower() == 'variable':
#         id = '<@414179453158293506>'

#         for x in range(5):

#             await ctx.send(id + ' it appears you are late')

#     elif message.lower() == 'smeagol':
#         id = '<@321370792682192896>'

#         for x in range(5):

#             await ctx.send(id + ' it appears you are late')
    
#     elif message.lower() == 'everyone':
#         id = '<@321370792682192896>'
#         id1 = '<@477961589178499094>'
#         id2 = '<@430451874773073960>'
#         id3 = '<@509473152997261330>'
#         id4 = '<@414179453158293506>'

#         for x in range(5):

#             await ctx.send(id + ' it appears you are late')
#             await ctx.send(id1 + ' it appears you are late')
#             await ctx.send(id2+ ' it appears you are late')
#             await ctx.send(id3 + ' it appears you are late')
#             await ctx.send(id4 + ' it appears you are late')


    


#8 ballc
@client.command()
async def ball(ctx,*,message):
    responses = ['As I see it, yes.',
    'Ask again later.',
    'Better not tell you now.',
    'Cannot predict now.',
    'Concentrate and ask again',
    'Don’t count on it.',
    'It is certain.',
    'It is decidedly so.',
    'Most likely.',
    'My reply is no.',
    'My sources say no.',
    'Outlook not so good.',
    'Outlook good.',
    'Reply hazy, try again.',
    'Signs point to yes.',
    'Very doubtful.',
    'Without a doubt.',
    'Yes.',
    'Yes – definitely.',
    'You may rely on it.',
    'IDK, but please dont ban clash'
    ]

    await ctx.send(ctx.message.author.name + ' asked: ' + message + '.')
    await ctx.send('The response is: ' + random.choice(responses))
    print(str(ctx.message.author) + ' asked the Magic 8 ball: ' + str(message))
    print('=======')

client.run(token)
