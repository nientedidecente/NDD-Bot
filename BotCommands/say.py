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
    
    # !say command
    @commands.command()
    async def say(self, ctx, *, arg): 
        await ctx.send(arg) # Send what the user just said