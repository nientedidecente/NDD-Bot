import discord
import json
from discord.ext import commands
import logging

logger = logging.getLogger(__name__)

with open('config.json') as config:
    json_data = json.load(config)

'''
------------------------------------------------
                CONFIG VARIABLES
------------------------------------------------
'''
bot = json_data["bot"]
event = json_data["eventsVars"]

# HiemSword: Yes, i know this loop is not the best method, but it works
for i in json_data["bot"]:
    bot_branch = i["branch"]
    bot_version = i["version"]
# ------------------------------------------------


class Cog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # !play command
    @commands.command()
    async def play(self, ctx, *args):
        logger.debug("Play command called")

        if args[0] == "reset":
            await ctx.send('Ok! Setting my playing status to: `default`')
            await self.bot.change_presence(activity=discord.Game(name=f'Hello! I am the NDD Bot! version {bot_branch}|{bot_version}'))
        else:
            await ctx.send(f'Ok! Im setting my playing status to: {" ".join(args)}')  # Send what the user just said
            await self.bot.change_presence(activity=discord.Game(name=" ".join(args)))
