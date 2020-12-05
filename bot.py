# bot.py
import os
import sys

import discord
import json
import logging.config

from dotenv import load_dotenv
from discord.ext import commands
from pathlib import Path

import helpers.config as config
from helpers.load_extensions import load_exts
from helpers.import_extensions import import_all_exts

from webserver import keep_alive

# Initial Setup
logging.config.fileConfig("{}/logging.ini".format(Path(__file__).parent.absolute()))
logger = logging.getLogger(__name__)

logger.info('.------------------------------.')
logger.info('|      Starting Bot...         |')
logger.info('.------------------------------.')


load_dotenv()  # Load the .env file
TOKEN = os.getenv('DISCORD_TOKEN')  # get token


prefix = config.bot_prefix

if config.bot_version_dev is True:
    logger.debug('Using bot in Developer Mode')
    prefix = config.bot_prefix_dev

if config.bot_prefix == config.bot_prefix_dev:
    logger.warning('The Normal Mode command prefix is equal to the prefix for Developer Mode, please change it to another value')

logger.debug(f'Setting command prefix to "{prefix}"')
client = commands.Bot(command_prefix=prefix)  # Command prefix



@client.event
async def on_ready():  # When the bot is connected to Discord do:

    logger.debug('Setting discord presence...')
    await client.change_presence(activity=discord.Game(name=config.bot_presence.format(config.bot_version, config.bot_branch)))
    logger.debug('Loading Addons...')
    exts_num = load_exts(client)
    logger.debug('------')
    logger.debug('| Logged in as')
    logger.debug(f'| {client.user.name}')
    logger.debug(f'| ID: {client.user.id}')
    logger.debug(f'| Total addons installed: {exts_num}')
    logger.debug(f'| Discord.py ver: {discord.__version__}')
    logger.debug(f'| Bot version: {config.bot_version}, {config.bot_branch}') # TODO: Replace the hardcoded bot_branch string with something else
    logger.debug('------')
    logger.info("Bot is ready")

'''
------------------------------------------------
                BOT COMMANDS
------------------------------------------------
'''


@client.command()
async def debug(ctx, arg):

    if config.bot_version_dev == True:
        
            await ctx.send(f'Please check your DMs {ctx.author.display_name}!')

            # We send the debug message to the author DMs to prevent notification spam        
            await ctx.author.send('-----Debug start-----')

            for i in config.json_data: 
                await ctx.author.send('|')
                await ctx.author.send(f'{i}:        `{config.json_data[i]}`')
            
            await ctx.author.send('|')
            await ctx.author.send('-----Debug end-----')
            
    else:
        await ctx.send('Bot is in stable version, no need for debuging')


@debug.error
async def debug_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title=":tools: Debug Menu :tools:", colour=discord.Colour(0xf8e71c), description="Please select an option")

        embed.set_author(name="Please select an option")

        embed.add_field(name="‎", value="‎", inline=False)
        embed.add_field(name="WIP !debug event [name_of_event]", value="Invoke an event", inline=True)
        embed.add_field(name="!debug var", value="Print all the variables", inline=True)

        await ctx.channel.send(embed=embed)





try:
    keep_alive() # Run webserver
    client.run(TOKEN)  # Start the bot
except:
    logger.critical(f'Fatal error: {sys.exc_info()[0]}')
    logger.log(f'Error: {sys.exc_info()}')
    logger.error('Bot is exiting...')
    raise

