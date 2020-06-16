# bot.py

import os
import discord
import json
import logging.config

from dotenv import load_dotenv
from discord.ext import commands
from pathlib import Path

from BotCommands import *

# Initial Setup
logging.config.fileConfig("{}/logging.ini".format(Path(__file__).parent.absolute()))
logger = logging.getLogger(__name__)

# LOAD CONFIG FILE
with open('config.json') as config:
    json_data = json.load(config)

'''
------------------------------------------------
                CONFIG VARIABLES
------------------------------------------------
'''
bot_branch = json_data["bot_branch"]
bot_version = json_data["bot_version"]
bot_version_dev = json_data["bot_version_dev"]
bot_version_info = json_data["bot_version_info"]
bot_prefix = json_data["bot_prefix"]
# ------------|  Join/Left event config variables  |-----

welcome_dm = json_data["welcome_dm"]

welcome_ch_id = json_data["welcome_ch_id"]
welcome_ch_name = json_data["welcome_ch_name"]

join_msg = json_data["welcome_ch_msg"]
left_msg = json_data["goodbye_ch_msg"]

# ------------------------------------------------

load_dotenv()  # Load the .env file
TOKEN = os.getenv('DISCORD_TOKEN')  # get token
client = commands.Bot(command_prefix="!")  # Command prefix


@client.event
async def on_ready():  # When the bot is connected to Discord do:
    logger.debug('Setting discord presence...')
    await client.change_presence(activity=discord.Game(name=f'Hello! I am the NDD Bot! version {bot_branch}|{bot_version}')) # Set presence
    logger.debug('Loading Cogs...')
    load_cogs()
    logger.debug('------')
    logger.debug('| Logged in as')
    logger.debug(f'| {client.user.name}')
    logger.debug(f'| ID: {client.user.id}')
    logger.debug('------')
    logger.debug('Bot is ready')


'''
------------------------------------------------
                BOT COMMANDS
------------------------------------------------
'''


@client.command()
async def debug(ctx, *, arg):

    if bot_version_dev == "True":
        if arg == "y":
            await ctx.send('-----Debug start-----')
            await ctx.send('|')
            await ctx.send(f'bot_branch:        `{bot_branch}`')
            await ctx.send(f'bot_version:       `{bot_version}`')
            await ctx.send(f'bot_version_dev:   `{bot_version_dev}`')
            await ctx.send(f'bot_version_info:  `{bot_version_info}`')
            await ctx.send(f'welcome_dm:        `{welcome_dm}`')
            await ctx.send(f'welcome_ch_id:     `{welcome_ch_id}`')
            await ctx.send(f'welcome_ch_name:   `{welcome_ch_name}`')
            await ctx.send(f'welcome_ch_msg:    `{join_msg}`')
            await ctx.send(f'goodbye_ch_msg:    `{left_msg}`')
            await ctx.send(f'cake:              `{json_data["cake"]}`')
            await ctx.send('|')
            await ctx.send('-----Debug end-----')
    else:
        await ctx.send('Bot is in stable version, no need for debuging')


@debug.error
async def debug_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('WARNING! The bot will spam all the variables, it could disturb people with notifications active.\nContinue? (!debug y)')


'''
------------------------------------------------
                EVENTS
------------------------------------------------
'''


# ---- Member Join event
@client.event
async def on_member_join(member): # when a user joins a guild do:

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


client.run(TOKEN)  # Start the bot
