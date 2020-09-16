from discord.ext import commands
import discord
import logging # Required for logging in discord.log and console
import json

logger = logging.getLogger(__name__) # Required for logging in discord.log and console

with open('config.json') as config:
    json_data = json.load(config) #load json file

#   This extensions contains the default commands


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
    bot_prefix = i["prefix"]
    bot_prefix_dev = i["prefix_dev"]


# ------------|  Join/Left event config variables  |-----

for i in json_data["eventsVars"]:
    for ii in i["join&leave"]:

        welcome_dm = ii["dm_msg"]

        welcome_ch_id = ii["ch_id"]
        welcome_ch_name = ii["ch_name"]

        join_msg = ii["hello_msg"]
        left_msg = ii["bye_msg"]




'''
------------------------------------------------
                    COMMANDS
------------------------------------------------
'''

def __init__(self, bot):
        self.bot = bot


# !ping command
@commands.command()
async def ping(ctx, self):
    logger.debug("Ping command called")
    await ctx.send(f':ping_pong: Pong! {round(int(self.bot.latency * 1000))}ms')  # Send the latency of the bot


# !play command
@commands.command()
async def play(ctx, *args):
    logger.debug("Play command called")

    if args[0] == "reset":
        await ctx.send('Ok! Setting my playing status to: `default`')
        await self.bot.change_presence(activity=discord.Game(name=f'Hello! I am the NDD Bot! version {bot_branch}|{bot_version}'))
    else:
        await ctx.send(f'Ok! Im setting my playing status to: {" ".join(args)}')  # Send what the user just said
        await self.bot.change_presence(activity=discord.Game(name=" ".join(args)))


# !say command
@commands.command()
async def say(self, ctx, *, arg):
    logger.debug("Say command called") 
    await ctx.send(arg)  # Send what the user just said

# !ver command
@commands.command()
async def ver(self, ctx):
    logger.debug("Ver command called")
    embed = discord.Embed(title="_Version Info_", colour=discord.Colour(0x6eff00))

    embed.set_author(name="NDD Bot", icon_url="https://cdn.discordapp.com/avatars/711283853972602901/9bed0ea2ddbc0a42c149ba06a42913a4.png?size=128")

    embed.add_field(name="‎", value="‎", inline=False)
    embed.add_field(name=":scroll: Bot Version", value=f"{bot_version}", inline=True)
    embed.add_field(name="‎", value="‎", inline=True)
    embed.add_field(name=":nut_and_bolt: Branch", value=f"{bot_branch}", inline=True)
    embed.add_field(name=":tools: Dev Version", value=f"{bot_version_dev}", inline=True)

    await ctx.channel.send(embed=embed)


'''
------------------------------------------------
                EVENTS
------------------------------------------------
'''


# ---- Member Join event
@commands.command()
async def on_member_join(member): # when a user joins a guild do:

    logger.info(f'User {member} joined guild {member.guild}')
    logger.debug('on_member_join event triggered')

    for channel in member.guild.channels: #search the channel
        logger.debug(f'- - - Searching the "{welcome_ch_name}" channel...- - - ')
        logger.debug(f'ID is <{welcome_ch_id}>')
        logger.debug(f'Is "{str(channel)}" id the same as "{welcome_ch_name} id" ? {str(channel.id) == welcome_ch_id}')

        if str(channel.id) == welcome_ch_id: #compare channels id
            logger.debug(f'{welcome_ch_name} channel found.')
            logger.debug(f'- - - Done. Sending to the channel "{welcome_ch_name}" the welcome messagge- - - ')

            await channel.send(f'{member.mention}{join_msg}') # Send the "chwelcome_msg" object value to the channel
            await member.send(f'Benvenut* {member.mention}{welcome_dm}') # Send the "chwelcome_dm" object value to the user
            return


# ---- Member Leave event
@commands.command()
async def on_member_remove(member): # when a user leaves a guild do:

    logger.debug('on_member_remove event triggered')

    for channel in member.guild.channels: #search the channel
        logger.debug(f'- - - Searching the "{welcome_ch_name}" channel...- - - ')
        logger.debug(f'ID is <{welcome_ch_id}>')
        logger.debug(f'Is "{str(channel)}" id the same as "{welcome_ch_name} id" ? {str(channel.id) == welcome_ch_id}')

        if str(channel.id) == welcome_ch_id: #compare channels id
            logger.debug(f'{welcome_ch_name} channel found.')
            logger.debug(f'- - - Done. Sending to the channel "{welcome_ch_name}" the welcome messagge- - - ')

            await channel.send(f'{member.mention}{left_msg}')
            return







def setup(bot): # Required for every extension. Executed at extension load

    bot.add_command(ping)
    bot.add_command(play)
    bot.add_command(say)
    bot.add_command(ver)
    bot.add_command(on_member_join)
    bot.add_command(on_member_remove)

    logger.info('Default commands extension loaded')