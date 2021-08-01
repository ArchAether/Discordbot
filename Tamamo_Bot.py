import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# class CustomClient(discord.Client):
#     async def on_ready(self):
#         print(f'{self.user} has connected to Discord!')
#         
# client = CustomClient()

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Greetings, {member.name}, welcome to our Discord server!'
    )
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "!mikon":
        await message.channel.send("Mikon~!")
    elif message.content == 'raise-exception':
        raise discord.DiscordException
    
@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if even == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

          
client.run(TOKEN)