import os
import discord
import asyncio
import json
from discord.ext import commands
import logging

logger = logging.getLogger(__name__)

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
    async def play(self, ctx, arg):
        logger.debug("Play command called")

        if arg == "reset":
            await ctx.send('Ok! Setting my playing status to: `default`')
            await commands.change_presence(activity=discord.Game(name=f'Hello! I am the NDD Bot! version {bot_branch}|{bot_version}'))
        else:
            await ctx.send(f'Ok! Im setting my playing status to: {arg}') # Send what the user just said
            await commands.change_presence(activity=discord.Game(name=arg))