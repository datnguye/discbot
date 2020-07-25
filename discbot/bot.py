
import os
from dotenv import load_dotenv
import random
from datetime import datetime
import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
ERRORPATH = os.getenv('ERROR_PATH')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
    print(f'{bot.user} is ready on:')
    for guild in bot.guilds:
        print(f'    {guild.name} ({guild.id})')
    bot.remove_command('help')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('--help or --h'))

@bot.event
async def on_member_join(member):
    guild = discord.utils.find(lambda g: g.name == GUILD, bot.guilds)
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to {guild.name}!')

@bot.event
async def on_error(event, *args, **kwargs):
    timestamp = datetime.today().strftime('%Y%m%d')
    with open(ERRORPATH.replace("<time>", timestamp), 'a') as f:
        f.write(f'Unhandled message: {args[0]}\n')

@bot.command(name='roll', aliases=['r','R'], description='Simulates rolling dice.')
async def roll(ctx, number_of_dice=3, number_of_sides=100):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(','.join(dice))

@bot.command(name="-help", aliases=['-h'], description="Returns all commands available")
async def help(ctx):
    helptext = "```"
    for command in bot.commands:
        command_name = command.__original_kwargs__['name']
        if command_name == '-help':
            continue
        
        if command_name in ['quit'] and ctx.message.author.guild_permissions.administrator:
            helptext += f"-{command_name}: {command.__original_kwargs__['description']}\n"
        else:
            helptext += f"-{command_name}: {command.__original_kwargs__['description']}\n"

    helptext += "```"
    await ctx.send(helptext)

# @bot.command(name='check', description='ADMIN: Check rights')
# @commands.has_permissions(administrator=True)
# async def check(ctx):
#     await ctx.send('You are cool indeed')

@bot.command(name='quit', aliases=['q','Q'], description='OWNER - Quit and log out the bot. Affected by owner request only')
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send('Roger that! Logged out.')
    await ctx.bot.logout()

@bot.command(name='raise', aliases=['rs','Rs', 'RS'], description='OWNER - Raise exceptions')
@commands.is_owner()
async def raise_exception(ctx):
    raise

def start():
    bot.run(TOKEN)