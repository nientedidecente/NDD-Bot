# bot.py

import os
import discord
import json
import logging.config

from dotenv import load_dotenv
from discord.ext import commands
from pathlib import Path

from BotCommands import *

import import_all_modules 

# Initial Setup
logging.config.fileConfig("{}/logging.ini".format(Path(__file__).parent.absolute()))
logger = logging.getLogger(__name__)

logger.info('.------------------------------.')
logger.info('|      Starting Bot...         |')
logger.info('.------------------------------.')

# LOAD CONFIG FILE
with open('config.json') as config:
    json_data = json.load(config)

'''
------------------------------------------------
                CONFIG VARIABLES
------------------------------------------------
'''
bot = json_data["bot"]
event = json_data["eventsVars"]

# HiemSword: Yes, i know this loop is not the best method, but it works
for i in json_data["bot"]:
    bot_branch = i["branch"]
    bot_version = i["version"]
    bot_version_dev = i["dev"]
    bot_version_info = i["info"]
    bot_prefix = i["prefix"]
    bot_prefix_dev = i["prefix_dev"]

    extensionsEnabled = i["extensionsEnabled"]

# ------------|  Join/Left event config variables  |-----

for i in json_data["eventsVars"]:
    for ii in i["join&leave"]:

        welcome_dm = ii["dm_msg"]

        welcome_ch_id = ii["ch_id"]
        welcome_ch_name = ii["ch_name"]

        join_msg = ii["hello_msg"]
        left_msg = ii["bye_msg"]
# ------------|  Extensions variables |-----


extensions_list = [""] * 30 # please someone find a better way to do this

# ------------------------------------------------

load_dotenv()  # Load the .env file
TOKEN = os.getenv('DISCORD_TOKEN')  # get token


prefix = bot_prefix

if bot_version_dev == True:
    logger.debug('Using bot in Developer Mode')
    prefix = bot_prefix_dev

if bot_prefix == bot_prefix_dev:
    logger.warning('The Normal Mode command prefix is equal to the prefix for Developer Mode, please change it to another value')

logger.debug(f'Setting command prefix to "{prefix}"')
client = commands.Bot(command_prefix=prefix)  # Command prefix



@client.event
async def on_ready():  # When the bot is connected to Discord do:
    logger.debug('Setting discord presence...')
    await client.change_presence(activity=discord.Game(name=f'Hello! I am the NDD Bot! version {bot_branch}|{bot_version}')) # Set presence
    logger.debug('Loading Cogs...')
    load_cogs()
    logger.debug('Loading Extensions...')
    extensions_num = load_ext()
    logger.debug('------')
    logger.debug('| Logged in as')
    logger.debug(f'| {client.user.name}')
    logger.debug(f'| ID: {client.user.id}')
    logger.debug(f'| Total extensions installed: {extensions_num}')
    logger.debug('------')
    logger.info("Bot is ready")

'''
------------------------------------------------
                BOT COMMANDS
------------------------------------------------
'''


@client.command()
async def debug(ctx, arg):

    if bot_version_dev == True:
        
            await ctx.send(f'Please check your DMs {ctx.author.display_name}!')

            # We send the debug message to the author DMs to prevent notification spam        
            await ctx.author.send('-----Debug start-----')

            for i in json_data: 
                await ctx.author.send('|')
                await ctx.author.send(f'{i}:        `{json_data[i]}`')
            
            await ctx.author.send('|')
            await ctx.author.send('-----Debug end-----')
            
    else:
        await ctx.send('Bot is in stable version, no need for debuging')


@debug.error
async def debug_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title=":tools: Debug Menu :tools:", colour=discord.Colour(0xf8e71c), description="Please select an option")

        embed.set_author(name="Please select an option")

        embed.add_field(name="‎", value="‎", inline=False)
        embed.add_field(name="!debug event [name_of_event]", value="Invoke an event", inline=True)
        embed.add_field(name="!debug var", value="Print all the variables", inline=True)

        await ctx.channel.send(embed=embed)





'''
------------------------------------------------
                EVENTS
------------------------------------------------
'''


# ---- Member Join event
@client.event
async def on_member_join(member): # when a user joins a guild do:

    logger.info(f'User {member} joined guild {member.guild}')
    logger.debug('on_member_join event triggered')

    for channel in member.guild.channels: #search the channel
        logger.debug(f'- - - Searching the "{welcome_ch_name}" channel...- - - ')
        logger.debug(f'ID is <{welcome_ch_id}>')
        logger.debug(f'Is "{str(channel)}" id the same as "{welcome_ch_name} id" ? {str(channel.id) == welcome_ch_id}')

        if str(channel.id) == welcome_ch_id: #compare channels id
            logger.debug(f'{welcome_ch_name} channel found.')
            logger.debug(f'- - - Done. Sending to the channel "{welcome_ch_name}" the welcome messagge- - - ')

            await channel.send(f'{member.mention}{join_msg}') # Send the "chwelcome_msg" object value to the channel
            await member.send(f'Benvenut* {member.mention}{welcome_dm}') # Send the "chwelcome_dm" object value to the user
            return


# ---- Member Leave event
@client.event
async def on_member_remove(member): # when a user joins a guild do:

    logger.debug('on_member_remove event triggered')

    for channel in member.guild.channels: #search the channel
        logger.debug(f'- - - Searching the "{welcome_ch_name}" channel...- - - ')
        logger.debug(f'ID is <{welcome_ch_id}>')
        logger.debug(f'Is "{str(channel)}" id the same as "{welcome_ch_name} id" ? {str(channel.id) == welcome_ch_id}')

        if str(channel.id) == welcome_ch_id: #compare channels id
            logger.debug(f'{welcome_ch_name} channel found.')
            logger.debug(f'- - - Done. Sending to the channel "{welcome_ch_name}" the welcome messagge- - - ')

            await channel.send(f'{member.mention}{left_msg}') 
            #await member.send(f'Benvenut* {member.mention}{welcome_dm}') # There is no DM left message
            return


def load_cogs():
    client.add_cog(changelog.Cog(client))
    client.add_cog(ping.Cog(client))
    client.add_cog(play.Cog(client))
    client.add_cog(reload.Cog(client))
    client.add_cog(say.Cog(client))
    client.add_cog(ver.Cog(client))

def load_ext():

    index = 0

    if extensionsEnabled == True:

        for module in import_all_modules._import_all_modules():
            logger.debug(f'Importing extension {module}')
            client.load_extension('BotExtensions.{}'.format(module))
            extensions_list[index] = module
            index += 1
        return index
        

    else:
        logger.debug('Extensions are disabled. Ignoring')

client.run(TOKEN)  # Start the bot
