# bot.py
import os
import time
import discord
import random
import json
import threading
import asyncio
import logging
from dotenv import load_dotenv
from discord.ext import commands

import BotCommands.ping
import BotCommands.ver
import BotCommands.play
import BotCommands.say
import BotCommands.changelog
import BotCommands.reload
import BotCommands.__init__
# In the future this huge list of "import BotCommands" wil be deleted


# LOAD CONFIG FILE
with open('config.json') as config:
    json_data = json.load(config)




localtime = time.asctime(time.localtime(time.time()))


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

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



load_dotenv() # Load the .env file
TOKEN = os.getenv('DISCORD_TOKEN') # get token 
GUILD = os.getenv('DISCORD_GUILD') # UNUSED - get guild name
client = commands.Bot(command_prefix=bot_prefix) #Command prefix






@client.event
async def on_ready():  # When the bot is connected to Discord do:
    log('Setting discord presence...')
    await client.change_presence(activity=discord.Game(name=f'Hello! I am the NDD Bot! version {bot_branch}|{bot_version}')) # Set presence
    log('Loading Cogs...')
    loadCogsCommands(BotCommands) # Load cogs from ./BotCommands
    log('------')
    log('| Logged in as')
    log(f'| {client.user.name}')
    log(f'| ID: {client.user.id}')
    log('------')
    log('Bot is ready')
    



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

    log('on_member_join event triggered')

    for channel in member.guild.channels: #search the channel
        log(f'- - - Searching the "{welcome_ch_name}" channel...- - - ')
        log(f'ID is <{welcome_ch_id}>')
        log(f'Is "{str(channel)}" id the same as "{welcome_ch_name} id" ? {str(channel.id) == welcome_ch_id}')

        if str(channel.id) == welcome_ch_id: #compare channels id
            log(f'{welcome_ch_name} channel found.')
            log(f'- - - Done. Sending to the channel "{welcome_ch_name}" the welcome messagge- - - ')

            await channel.send(f'{member.mention}{join_msg}') # Send the "chwelcome_msg" object value to the channel
            await member.send(f'Benvenut* {member.mention}{welcome_dm}') # Send the "chwelcome_dm" object value to the user
            return

# ---- Member Leave event
@client.event
async def on_member_remove(member): # when a user joins a guild do:

    log('on_member_remove event triggered')

    for channel in member.guild.channels: #search the channel
        log(f'- - - Searching the "{welcome_ch_name}" channel...- - - ')
        log(f'ID is <{welcome_ch_id}>')
        log(f'Is "{str(channel)}" id the same as "{welcome_ch_name} id" ? {str(channel.id) == welcome_ch_id}')

        if str(channel.id) == welcome_ch_id: #compare channels id
            log(f'{welcome_ch_name} channel found.')
            log(f'- - - Done. Sending to the channel "{welcome_ch_name}" the welcome messagge- - - ')

            await channel.send(f'{member.mention}{left_msg}') 
            #await member.send(f'Benvenut* {member.mention}{welcome_dm}') # There is no DM left message
            return



def loadCogsCommands(_dir):
    client.add_cog(_dir.ping.Basic(client))
    client.add_cog(_dir.ver.Basic(client))
    client.add_cog(_dir.say.Basic(client))
    client.add_cog(_dir.play.Basic(client))
    client.add_cog(_dir.changelog.Basic(client))
    client.add_cog(_dir.reload.Basic(client))


def log(txt):    
    
    print(f'[{localtime}]: {txt}\n')
    with open("./bot.log", "a") as debugFile:
        debugFile.write(f'[{localtime}]: {txt}\n')
        print(debugFile.closed)

    print(debugFile.closed)






client.run(TOKEN) #Start the bot
