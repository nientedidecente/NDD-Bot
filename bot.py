# bot.py
import os
import discord
import random
import json
import threading
import asyncio
from dotenv import load_dotenv
from discord.ext import commands

'''
------------------------------------------------
                CONFIG VARIABLES
------------------------------------------------
'''

welcome_dm = ", su NDD Games, la community italiana di sviluppatori di giochi open source.\n1. Scrivi due righe su di te sul channel <#709745996938084433>.\n2. Leggi il <#710950825182101635>\n\nBuona permanenza!\n\nQuando puoi:\nChiedi accesso alla org github ad uno dei mod (https://github.com/nientedidecente)\nCompila il modulo in <#711220093631332443>"

welcome_chid = "709733538181808172"






load_dotenv() # Load the .env file
TOKEN = os.getenv('DISCORD_TOKEN') # get token 
GUILD = os.getenv('DISCORD_GUILD') # UNUSED - get guild name
client = commands.Bot(command_prefix='!')

'''with open('config.json') as json_config:
    #json_config = data.read().decode("utf-8")
    
    data = json.loads("json_config")
-----
    data = json.load(config)

    random_status = data["random_status"]'''


@client.event
async def on_ready():  # When the bot is connected to Discord do:
    print('Bot is ready')


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
    await ctx.send(f'NDD Bot version: ')

# !say command
@client.command()
async def say(ctx, *, arg): 
    await ctx.send(arg) # Send what the user just said



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
        print(f'- - - Searching the "{data["chwelcome_name"]}" channel...- - - ')
        print(f'ID is <{data["chwelcome_id"]}>')
        print(f'Is "{str(channel)}" id the same as "{data["chwelcome_name"]} id" ? {str(channel.id) == data["chwelcome_id"]}')

        if str(channel.id) == data["chwelcome_id"]: #compare channels id
            print(f'{data["chwelcome_name"]} channel found.')
            print(f'- - - Done. Sending to the channel "{data["chwelcome_name"]}" the welcome messagge- - - ')

            await channel.send(f'{member.mention}{data["chwelcome_msg"]}') # Send the "chwelcome_msg" object value to the channel
            await member.send(f'Benvenut* {member.mention}{data["chwelcome_dm"]}') # Send the "chwelcome_dm" object value to the user
            return

# ---- Member Leave event
@client.event
async def on_member_remove(member): # when a user joins a guild do:

    print('on_member_remove event triggered')

    for channel in member.guild.channels: #search the channel
        print(f'- - - Searching the "{data["chwelcome_name"]}" channel...- - - ')
        print(f'Is "{str(channel)}" the same as "{data["chwelcome_name"]}" ? {str(channel) == data["chwelcome_name"]}')

        if str(channel) == data["chwelcome_name"]: #compare channels id
            print(f'{data["chwelcome_name"]} channel found. Checking channel id...')
            print(f'DISCORD {str(channel.id)}  < - - >  {data["chwelcome_id"]} CONFIG')
            print(f'IDs are the same? {str(channel.id) == data["chwelcome_id"]}')

            if str(channel.id) == data["chwelcome_id"]:
                print(f'- - - Done. Sending to the channel "{data["chwelcome_name"]}" the welcome messagge- - - ')
                await channel.send(f'{member.mention}{data["chwelcome_left"]}')
                #await member.send(f'Benvenut* {member.mention}{data["chwelcome_dm"]}')
                return





client.run(TOKEN) #Start the bot
