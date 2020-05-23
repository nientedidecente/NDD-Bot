# bot.py
import os
import discord
import random
import json
import asyncio
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv() # Load the .env file
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot(command_prefix='!')

with open('config.json') as config:
    data = json.load(config)





@client.event
async def on_ready():  # When the bot is connected to Discord do:
    print('Bot is ready')
    await client.change_presence(activity=discord.Game(name='Hello'))

'''
------------------------------------------------
                BOT COMMANDS
------------------------------------------------
'''

# DEBUG
@client.command()
async def debug(ctx):
    await ctx.send(data["chwelcome_id"])
    await ctx.send(data["chwelcome_name"])
    await ctx.send(data["chwelcome_msg"])

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


@client.event
async def on_member_join(member): # when a user joins a guild do:

    print('on_member_join event triggered')

    for channel in member.guild.channels: #search the channel
        print(f'- - - Searching the "{data["chwelcome_name"]}" channel...- - - ')
        print(f'Is "{str(channel)}" the same as "{data["chwelcome_name"]}" ? {str(channel) == data["chwelcome_name"]}')

        if str(channel) == data["chwelcome_name"]: #compare channels id
            print(f'{data["chwelcome_name"]} channel found. Checking channel id...')
            print(f'DISCORD {str(channel.id)}  < - - >  {data["chwelcome_id"]} CONFIG')
            print(f'IDs are the same? {str(channel.id) == data["chwelcome_id"]}')

            if str(channel.id) == data["chwelcome_id"]:
                print(f'- - - Done. Sending to the channel "{data["chwelcome_name"]}" the welcome messagge- - - ')
                await channel.send(f'Benvenut* {member.mention}{data["chwelcome_msg"]}')
                return





client.run(TOKEN) #Start the bot
