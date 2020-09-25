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
    async def start(self, ctx):
        guild = ctx.message.guild

        category = await guild.create_category('This is a Test')
        logger.info('Created category channel')

        channel = await guild.create_text_channel('this-is-a-test', category=category)
        logger.info('Created text channel')





def setup(bot):

    bot.add_cog(AmongUs(bot))

    logger.info('Loaded Among Us for Discord')
