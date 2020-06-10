import os
import discord
import asyncio
import json
from discord.ext import commands
#simport bot

#client = commands.Bot(command_prefix='!') #Command prefix

with open('config.json') as config:
    json_data = json.load(config)


'''
------------------------------------------------
                CONFIG VARIABLES
------------------------------------------------
'''
# ------------------------------------------------



class Basic(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    # !ping command
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f':ping_pong: Pong! {round(int(self.bot.latency * 1000))}ms')  # Send the latency of the bot