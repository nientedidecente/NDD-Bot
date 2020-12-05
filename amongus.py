import json
import discord
import logging.config
from discord.ext import commands

import helpers.config as config

logger = logging.getLogger(__name__)


class AmongUs(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    '''
------------------------------------------------
                BOT COMMANDS
------------------------------------------------
    '''


    @commands.command()
    async def start(self, ctx, dude1, dude2):
        guild = ctx.message.guild
        role = discord.utils.get(ctx.guild.roles, name="AmongUs")

        name = 'Among Us'
        category = discord.utils.get(ctx.guild.categories, name=name)
        
        await ctx.send(f'{dude1} aaa {dude2}')
        channel = await guild.create_text_channel('this-is-a-test', category=category)
        logger.info('Created text channel')





def setup(bot):

    bot.add_cog(AmongUs(bot))

    logger.info('Loaded Among Us for Discord')
