
import os
import discord
from dotenv import load_dotenv
import random
from datetime import datetime

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
ERRORPATH = os.getenv('ERROR_PATH')

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    print(f'{client.user} is connected to the following guild: {guild.name}(id: {guild.id})')
    
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

    
@client.event
async def on_member_join(member):
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to {guild.name}!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(f"New message detected as: {message.content}")

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

    if message.content == 'raise-ex':
        raise

@client.event
async def on_error(event, *args, **kwargs):
    timestamp = datetime.today().strftime('%Y%m%d')
    with open(ERRORPATH.replace("<time>", timestamp), 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

def start():
    client.run(TOKEN)