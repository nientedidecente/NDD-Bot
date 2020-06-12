import os
import discord
import asyncio
import json
from discord.ext import commands

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
    
    # !ver command
    @commands.command()
    async def ver(self, ctx):
        await ctx.send(f'NDD Bot version: branch {bot_branch} ver.{bot_version}')