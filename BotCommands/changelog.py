import json
from discord.ext import commands

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


class Cog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # !changelog command
    @commands.command()
    async def changelog(self, ctx): 
        await ctx.send(bot_version_info.format(bot_version, bot_branch))
