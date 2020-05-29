# bot.py
import os
import discord
import random
import threading
import asyncio
from dotenv import load_dotenv
from discord.ext import commands

'''
------------------------------------------------
                CONFIG VARIABLES
------------------------------------------------
'''
bot_branch = "ndd-specific"
bot_version = "1.0"
bot_defaultStatus = "Hello! Im the NDD Bot! ver.{bot_branch}|{bot_version}"

# ------------|  Join/Left event config variables  |-----

welcome_dm = ", su NDD Games, la community italiana di sviluppatori di giochi open source.\n1. Scrivi due righe su di te sul channel <#709745996938084433>.\n2. Leggi il <#710950825182101635>\n\nBuona permanenza!\n\nQuando puoi:\nChiedi accesso alla org github ad uno dei mod (https://github.com/nientedidecente)\nCompila il modulo in <#711220093631332443>"

welcome_ch_id = "709733538181808172"
welcome_ch_name = "general"

join_msg = " \u00E8 entrato nel server! Dategli un caloroso benvenuto!"
left_msg = " \u00E8 uscito dal server. **F**"




load_dotenv() # Load the .env file
TOKEN = os.getenv('DISCORD_TOKEN') # get token 
GUILD = os.getenv('DISCORD_GUILD') # UNUSED - get guild name
client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():  # When the bot is connected to Discord do:
    print('Bot is ready')
    await client.change_presence(activity=discord.Game(name=f'{bot_defaultStatus}'))

'''
------------------------------------------------
                BOT COMMANDS
------------------------------------------------
'''


# !ping command
@client.command()
async def ping(ctx):
    await ctx.send(f':ping_pong: Pong! {round(client.latency * 1000)}ms')  # Send the latency of the bot

# !ver command
@client.command()
async def ver(ctx):
    await ctx.send(f'NDD Bot version: branch {bot_branch} ver.{bot_version}')

# !say command
@client.command()
async def say(ctx, *, arg): 
    await ctx.send(arg) # Send what the user just said

# !play command
@client.command()
async def play(ctx, *, arg): 
    if arg == "reset":
        await ctx.send('Ok! Setting my playing status to: `default`')
        await client.change_presence(activity=discord.Game(name=f'{bot_defaultStatus}'))
    else:
        await ctx.send(f'Ok! Im setting my playing status to: {arg}') # Send what the user just said
        await client.change_presence(activity=discord.Game(name=arg))



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





client.run(TOKEN) #Start the bot
