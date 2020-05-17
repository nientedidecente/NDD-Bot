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


@client.event
async def on_ready():  # When the bot is connected to Discord do:
    print('Bot is ready')


@client.command()
async def ping(ctx): # !ping command
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')  # Send the latency of the bot

@client.command()
async def say(ctx, *, arg): # !say command
    await ctx.send(arg) # Send what the user just said



client.run(TOKEN) #Start the bot
