# bot.py
import os
import discord
import random
import json
import threading
import asyncio
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

load_dotenv() # Load the .env file
TOKEN = os.getenv('DISCORD_TOKEN') # get token 
GUILD = os.getenv('DISCORD_GUILD') # UNUSED - get guild name
client = commands.Bot(command_prefix='!') #Command prefix

#print (len([name for name in os.listdir('.') if os.path.isfile(name)]))

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
bot_version_info = "none"#json_data["bot_version_info"]

# ------------|  Join/Left event config variables  |-----

welcome_dm = json_data["welcome_dm"]

welcome_ch_id = json_data["welcome_ch_id"]
welcome_ch_name = json_data["welcome_ch_name"]

join_msg = json_data["welcome_ch_msg"]
left_msg = json_data["goodbye_ch_msg"]

# ------------------------------------------------




@client.event
async def on_ready():  # When the bot is connected to Discord do:
    print('Bot is ready')
    await client.change_presence(activity=discord.Game(name=f'Hello! I am the NDD Bot! version {bot_branch}|{bot_version}'))
    loadCogsCommands(BotCommands) # Loads all the commands in a folder


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

    print('on_member_join event triggered')

    for channel in member.guild.channels: #search the channel
        print(f'- - - Searching the "{welcome_ch_name}" channel...- - - ')
        print(f'ID is <{welcome_ch_id}>')
        print(f'Is "{str(channel)}" id the same as "{welcome_ch_name} id" ? {str(channel.id) == welcome_ch_id}')

        if str(channel.id) == welcome_ch_id: #compare channels id
            print(f'{welcome_ch_name} channel found.')
            print(f'- - - Done. Sending to the channel "{welcome_ch_name}" the welcome messagge- - - ')

            await channel.send(f'{member.mention}{join_msg}') # Send the "chwelcome_msg" object value to the channel
            await member.send(f'Benvenut* {member.mention}{welcome_dm}') # Send the "chwelcome_dm" object value to the user
            return

# ---- Member Leave event
@client.event
async def on_member_remove(member): # when a user joins a guild do:

    print('on_member_remove event triggered')

    for channel in member.guild.channels: #search the channel
        print(f'- - - Searching the "{welcome_ch_name}" channel...- - - ')
        print(f'ID is <{welcome_ch_id}>')
        print(f'Is "{str(channel)}" id the same as "{welcome_ch_name} id" ? {str(channel.id) == welcome_ch_id}')

        if str(channel.id) == welcome_ch_id: #compare channels id
            print(f'{welcome_ch_name} channel found.')
            print(f'- - - Done. Sending to the channel "{welcome_ch_name}" the welcome messagge- - - ')

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



client.run(TOKEN) #Start the bot
