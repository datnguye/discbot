
import os
from dotenv import load_dotenv
import random
from datetime import datetime
import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
ERRORPATH = os.getenv('ERROR_PATH')

bot = commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, bot.guilds)
    print(f'{bot.user} is connected to the following guild: {guild.name} (id: {guild.id})')
    
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

    
@bot.event
async def on_member_join(member):
    guild = discord.utils.find(lambda g: g.name == GUILD, bot.guilds)
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to {guild.name}!')

@bot.event
async def on_error(event, *args, **kwargs):
    timestamp = datetime.today().strftime('%Y%m%d')
    with open(ERRORPATH.replace("<time>", timestamp), 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

@bot.command(name='99', help='Giving Brooklyn 99 quotes')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]
    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='roll', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice=3, number_of_sides=100):
    #print(ctx.author.id)
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(','.join(dice))

@bot.command(name='check', help='MOD: Check rights')
@commands.has_any_role('admin')
async def check(ctx):
    await ctx.send('You are cool indeed')

@bot.command(name='quit', help='Quit and log out the bot. Affected by owner request only')
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send('OK! Logged out.')
    await ctx.bot.logout()

def start():
    bot.run(TOKEN)