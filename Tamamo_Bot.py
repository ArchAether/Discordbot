import os
import random
import discord

from discord.ext import commands

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'I, {bot.user.name} have connected to Discord!')
    
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

bot.run(TOKEN)