import json
import discord
import logging.config
from discord.ext import commands

import func.vars as v

logger = logging.getLogger(__name__)


class Default(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    '''
------------------------------------------------
                BOT COMMANDS
------------------------------------------------
    '''


    # !changelog command
    @commands.command()
    async def changelog(self, ctx): 
        await ctx.send(v.bot_version_info.format(v.bot_version, v.bot_branch))

    # !ping command
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f':ping_pong: Pong! {round(int(self.bot.latency * 1000))}ms')  # Send the latency of the bot


    # !play command
    @commands.command()
    async def play(self, ctx, *args):
        logger.debug("Play command called")

        if args[0] == "reset":
            await ctx.send('Ok! Setting my playing status to: `default`')
            await self.bot.change_presence(activity=discord.Game(name=f'Hello! I am the NDD Bot! version {v.bot_branch}|{v.bot_version}'))
        else:
            await ctx.send(f'Ok! Im setting my playing status to: {" ".join(args)}')  # Send what the user just said
            await self.bot.change_presence(activity=discord.Game(name=" ".join(args)))


    # !say command
    @commands.command()
    async def say(self, ctx, *, arg): 
        await ctx.send(arg)  # Send what the user just said



    # !ver command
    @commands.command()
    async def ver(self, ctx):
        embed = discord.Embed(title="_Version Info_", colour=discord.Colour(0x6eff00))

        embed.set_author(name="NDD Bot", icon_url="https://cdn.discordapp.com/avatars/711283853972602901/9bed0ea2ddbc0a42c149ba06a42913a4.png?size=128")

        embed.add_field(name="‎", value="‎", inline=False)
        embed.add_field(name=":scroll: Bot Version", value=f"{v.bot_version}", inline=True)
        embed.add_field(name="‎", value="‎", inline=True)
        embed.add_field(name=":nut_and_bolt: Branch", value=f"{v.bot_branch}", inline=True)
        embed.add_field(name=":tools: Dev Version", value=f"{v.bot_version_dev}", inline=True)

        await ctx.channel.send(embed=embed)


    '''
------------------------------------------------
                EVENTS
------------------------------------------------
    '''

# ---- Member Join event
@commands.Cog.listener()
async def on_member_join(self, member): # when a user joins a guild do:

    logger.info(f'User {member} joined guild {member.guild}')
    logger.debug('on_member_join event triggered')

    for channel in member.guild.channels: #search the channel
        logger.debug(f'- - - Searching the "{v.welcome_ch_name}" channel...- - - ')
        logger.debug(f'ID is <{v.welcome_ch_id}>')
        logger.debug(f'Is "{str(channel)}" id the same as "{v.welcome_ch_name} id" ? {str(channel.id) == v.welcome_ch_id}')

        if str(channel.id) == v.welcome_ch_id: #compare channels id
            logger.debug(f'{v.welcome_ch_name} channel found.')
            logger.debug(f'- - - Done. Sending to the channel "{v.welcome_ch_name}" the welcome messagge- - - ')

            await channel.send(f'{member.mention}{v.join_msg}') # Send the "chwelcome_msg" object value to the channel
            await member.send(v.welcome_dm.format(member.mention)) # Send the "chwelcome_dm" object value to the user
            return


# ---- Member Leave event
@commands.Cog.listener()
async def on_member_remove(self, member): # when a user leaves a guild do:

    logger.debug('on_member_remove event triggered')

    for channel in member.guild.channels: #search the channel
        logger.debug(f'- - - Searching the "{v.welcome_ch_name}" channel...- - - ')
        logger.debug(f'ID is <{v.welcome_ch_id}>')
        logger.debug(f'Is "{str(channel)}" id the same as "{v.welcome_ch_name} id" ? {str(channel.id) == v.welcome_ch_id}')

        if str(channel.id) == v.welcome_ch_id: #compare channels id
            logger.debug(f'{v.welcome_ch_name} channel found.')
            logger.debug(f'- - - Done. Sending to the channel "{v.welcome_ch_name}" the welcome messagge- - - ')

            await channel.send(f'{member.mention}{v.left_msg}') 
            #await member.send(f'Benvenut* {member.mention}{welcome_dm}') # There is no DM left message
            return






def setup(bot):

    bot.add_cog(Default(bot))

    logger.info('-----------------------------------')
    logger.info('Loaded DEFAULT Bot Commands&Events')
    logger.info('-----------------------------------')
