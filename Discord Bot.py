import discord
from discord.ext import commands

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


#roaster
@client.event
async def on_command_error(ctx, error):

    if isinstance(error, commands.CommandNotFound):

        roasts = ['Imagine being a dummy', 'Imagine not reading the !help page', 'lol what a bot. I bet my code has more brain than u.', 'Nice try stupid. Next time try harder.', 'Yooo we got a dumb one here guys.', 'Haha i bet noodle is smarter than u.']

        await ctx.send('Shout out to ' + ctx.message.author.mention + ' for getting the command wrong.')
        await ctx.send(random.choice(roasts))

        print(str(ctx.message.author) + ' Used this: ' + str(ctx.message.content) + ' Instead of the correct command.')

#censor
@client.command()
async def censor(ctx,*,amount):
        await ctx.channel.purge(limit=int(amount))
        if amount == '1':
            await ctx.send(ctx.message.author + ' censored ' + amount + ' message because it was sus.')
        else:
            await ctx.send(ctx.message.author + ' censored ' + amount + ' messages because they were sus.') 
        print(str(ctx.message.author) + ' cleared ' + str(amount) + ' messages from ' + str(ctx.message.channel) + ' text chat.')
        print('=======')



#translate
@client.command()
async def translate(ctx,*,message):
    text=str(message)
    translator = Translator()

    result = translator.translate(text, dest='es')

    await ctx.send(result.text)
    print(str(ctx.message.author) + ' translated ' + message + ' to ' + result.text)
    print('=======')

#choir
@client.command()
async def choir(ctx):
    await ctx.send(str(ctx.message.author) + ' has summoned the choir.')
    await ctx.send(':-0')
    await ctx.send(':-o')
    await ctx.send(':-0')
    await ctx.send(':-o')

    print(ctx.message.author.name + ' has summoned the choir')


#finds bot latency
@client.command()
async def ping(ctx):
    await ctx.send(f'Ping is {round(client.latency * 1000)} ms')
    print(str(ctx.message.author) + ' tested the bots latency. It is: ' + str(round(client.latency * 1000)) + ' ms')
    print('=======')

#dinner command
@client.command()
async def dinner(ctx):
    dinnerTimes = ['8:30', '9:00', '10:45', '11:00', '12:00']
    await ctx.send('Ricky will eat dinner at ' + random.choice(dinnerTimes) + ' tonight')
    print(str(ctx.message.author) + ' found what time Ricky will eat dinner tonight.')
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
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Color.orange()
    )

    embed.set_author(name='Help')
    embed.add_field(name='!kd', value='!kd + UPlay Username prints out the users K/D', inline=False)
    embed.add_field(name='!kills', value='!kills + UPlay Username prints out the users total kills', inline=False)
    embed.add_field(name='!rank', value='!rank + UPlay Username prints out the users current Rank and MMR', inline=False)
    embed.add_field(name='!ball', value='!ball + a question returns a magic 8 ball response', inline=False)
    embed.add_field(name='!dinner', value='It just returns when @Junoqi will eat dinner', inline=False)
    embed.add_field(name='!translate', value='It translates your message to spanish very hastily', inline=False)
    embed.add_field(name='!censor', value='Use this command to delete any previous strange message', inline=False)
    embed.add_field(name='!ping', value='Returns the bot latency', inline=False)
    embed.add_field(name='!clear', value='!clear + amount Clears the selected amount of messages (ONLY AVAILABLE TO ADMINS)', inline=False)

    await ctx.send(author, embed=embed)
    print(str(ctx.message.author) + ' opened the !help page.')
    print('=======')

#developer tools
@client.command()
async def sleep(ctx):
    await ctx.send('Noodle Bot will be logging off for the night. See you in the morning! :)')
    exit()

@client.command()
async def spam(ctx,*,message):

    await ctx.send('Spam has been initiated on ' + message.upper())

    if message.lower() == 'ryan':
        id = '<@430451874773073960>'
        for x in range(10):

            await ctx.send(id + ' it appears you are late')

    elif message.lower() == 'viper':
        id = '<@509473152997261330>'

        for x in range(10):

            await ctx.send(id + ' it appears you are late')

    if message.lower() == 'henry':
        id = '<@477961589178499094>'

        for x in range(10):

            await ctx.send(id + ' it appears you are late')

    
    elif message.lower() == 'variable':
        id = '<@414179453158293506>'

        for x in range(10):

            await ctx.send(id + ' it appears you are late')

    elif message.lower() == 'smeagol':
        id = '<@321370792682192896>'

        for x in range(10):

            await ctx.send(id + ' it appears you are late')
    
    elif message.lower() == 'everyone':
        id = '<@321370792682192896>'
        id1 = '<@477961589178499094>'
        id2 = '<@430451874773073960>'
        id3 = '<@509473152997261330>'
        id4 = '<@414179453158293506>'

        for x in range(10):

            await ctx.send(id + ' it appears you are late')
            await ctx.send(id1 + ' it appears you are late')
            await ctx.send(id2+ ' it appears you are late')
            await ctx.send(id3 + ' it appears you are late')
            await ctx.send(id4 + ' it appears you are late')

    
#8 ball
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

#run 
client.run(token)
