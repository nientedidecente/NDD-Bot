import json
import discord
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
    bot_version_dev = i["dev"]
    bot_version_info = i["info"]
# ------------------------------------------------


class Cog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # !ver command
    @commands.command()
    async def ver(self, ctx):
        embed = discord.Embed(title="_Version Info_", colour=discord.Colour(0x6eff00))

        embed.set_author(name="NDD Bot", icon_url="https://cdn.discordapp.com/avatars/711283853972602901/9bed0ea2ddbc0a42c149ba06a42913a4.png?size=128")

        embed.add_field(name="‎", value="‎", inline=False)
        embed.add_field(name=":scroll: Bot Version", value=f"{bot_version}", inline=True)
        embed.add_field(name="‎", value="‎", inline=True)
        embed.add_field(name=":nut_and_bolt: Branch", value=f"{bot_branch}", inline=True)
        embed.add_field(name=":tools: Dev Version", value=f"{bot_version_dev}", inline=True)

        await ctx.channel.send(embed=embed)