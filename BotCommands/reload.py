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

    # !reload command
    @commands.command()
    async def reload(self, ctx): 
        await ctx.send(':arrows_counterclockwise: Reloading config file...')

        # Dosen't work. 
        '''with open('config.json') as config:
            config.close()
            json_data = json.load(config)
        
        await ctx.send(':white_check_mark: Config file reloaded')'''
        await ctx.send('Sorry, command in WIP')
