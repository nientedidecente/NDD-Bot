from discord.ext import commands
import logging # Required for logging in discord.log and console

logger = logging.getLogger(__name__) # Required for logging in discord.log and console

'''
This is an extension example.
'''



@commands.command() # Define a command
async def hello(ctx):
    # Do stuff in here like saying hello to someone
    await ctx.send(f'Hello {ctx.author.display_name}.')




def setup(bot): # Required for every extension. Executed at extension load
    bot.add_command(hello) # Add the command we defined
    logger.info('Hello extension loaded')
