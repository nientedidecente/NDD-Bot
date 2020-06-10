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
bot_branch = json_data["bot_branch"]
bot_version = json_data["bot_version"]
bot_version_info = json_data["bot_version_info"]
# ------------------------------------------------



class Basic(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    # !play command
    @commands.command()
    async def changelog(self, ctx): 
        await ctx.send(bot_version_info)