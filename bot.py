# bot.py
import os
import discord
import random
import json
import threading
import asyncio
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv() # Load the .env file
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
counter = 0
client = commands.Bot(command_prefix='!')

with open('config.json') as json_config:
    #json_config = data.read().decode("utf-8")
    
    data = json.loads("json_config")
'''
    data = json.load(config)

    random_status = data["random_status"]'''


@client.event
async def on_ready():  # When the bot is connected to Discord do:
    print('Bot is ready')
    #print(data["random_status"])
    #print(random_status["dude"])

# -----Change bot activity after 10 seconds (Doesn't work for now)-----
'''
def __init__(self, *args, **kwargs):
        super().__init__*args, **kwargs)
        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.my_background_task())
        print('dude im an def thing')'''

 
'''@client.event
async def on_ready():  # When the bot is connected to Discord do:
    print('Bot is ready')
    counter = 0
    await client.change_presence(activity=discord.Game(name='Hello'))
    print('dude')
    if True:
        t = threading.Timer(5.0, my_background_task())
        print('thhhhhherrrrffddfd')
        t.start()

def my_background_task():
    print('fuck you dude')
---------------------------------
    await client.wait_until_ready()
    print('dude im background')
    channel = client.get_channel(709854752195870762) # channel ID goes here
    print('dude im in the ultime state')
    counter += 1
    await channel.send(counter)'''

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
    await ctx.send(data["chwelcome_dm"])
    await ctx.send(data["chwelcome_left"])
    await ctx.send("Sending json data")
    await ctx.send(data)
    await ctx.send("Done.")
    await ctx.send("Sending random_status data")
    await ctx.send(data["random_status"])
    await ctx.send("Done.")
    await ctx.send("Sending random_status child data 'dude'")
    for channel in data:

        await ctx.send(channel['dude'])

    await ctx.send("Done.")


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
