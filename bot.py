# bot.py
import os
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv() # Load the .env file
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot(command_prefix='!')
chwelcome_id = "709733538181808172"
chwelcome_name = "general"



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
    chwelcome_msg = f"""Benvenut* {member.mention}, su NDD Games, la community italiana di sviluppatori di giochi open source.\n1. Scrivi due righe su di te sul channel <#709745996938084433>.\n2. Leggi il <#710950825182101635>\n\nBuona permanenza!\n\nQuando puoi:\nChiedi accesso alla org github ad uno dei mod (https://github.com/nientedidecente)\nCompila il modulo in <#711220093631332443>"""
    for channel in member.guild.channels:
        if str(channel) == chwelcome_name:
            if str(channel.id) == chwelcome_id:
                await channel.send(chwelcome_msg)



client.run(TOKEN) #Start the bot
