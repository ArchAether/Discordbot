import os, random, discord, asyncio

from datetime import date, datetime

from dotenv import load_dotenv
from discord.ext import commands, tasks

load_dotenv()

TOKEN = os.environ.get('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'I, {bot.user.name} have connected to Discord!')
    channel = bot.get_channel(808479275538710578)
    text = 'React to this message to get a role~!\n'\
           '⚔️: Hunter'
    watched_message = await channel.send(text)
    
    
@bot.event
async def on_reaction_add(reaction, user):
    channel = bot.get_channel(808479275538710578)
    if reaction.emoji == '⚔️':
        role = discord.utils.get(user.guild.roles, name="Hunter")
        print(f'Setting {user.name} as a Hunter!')
        await user.add_roles(role)
        
    
@bot.command(name='mikon', help='Responds with a Tamamo quote.')
async def mikon(ctx):
    tamamo_quotes = [
        'Mikon!', 'Tamamo KIIIIICK!',    
    ]
    
    response = random.choice(tamamo_quotes)
    await ctx.send(response)
    
@bot.command(name='roll', help='Simulates rolling dice.')
async def diceRoll(ctx, number_of_dice: int, number_of_sides: int):
    dice=[
     str(random.choice(range(1, number_of_sides + 1)))
     for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))
    
@bot.command(name='create-channel')
@commands.has_role('Admin')
async def create_channel(ctx, channel_name='default-channel'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)
    else:
        print(f'Failed to create channel!')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

@tasks.loop(hours=24)
async def called_once_a_day():
    message_channel = bot.get_channel(808492405518893097)
    await message_channel.sent("This is a timed Message~!")

@called_once_a_day.before_loop
async def before():
    now = datetime.now()
    if(now.weekday() == 3):
        meeting_time = datetime.now().replace(hour=20, minute=29)
        now = datetime.now()
        time_till_meeting = meeting_time - now
        print(f'Time \'till meeting: {time_till_meeting}')
        asyncio.sleep(time_till_meeting)

        await bot.wait_until_ready()
    else:
        print(f'No meeting today!')


bot.run(TOKEN)