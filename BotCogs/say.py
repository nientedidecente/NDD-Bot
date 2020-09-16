import json
from discord.ext import commands

with open('config.json') as config:
    json_data = json.load(config)

'''
------------------------------------------------
                CONFIG VARIABLES
------------------------------------------------
'''
# ------------------------------------------------


class Cog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # !say command
    @commands.command()
    async def say(self, ctx, *, arg): 
        await ctx.send(arg)  # Send what the user just said
