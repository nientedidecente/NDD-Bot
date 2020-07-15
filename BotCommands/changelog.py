import json
from discord.ext import commands

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
    bot_version_info = i["info"]
# ------------------------------------------------

class Cog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # !changelog command
    @commands.command()
    async def changelog(self, ctx): 
        await ctx.send(bot_version_info.format(bot_version, bot_branch))
