# bot.py
import os
import discord
import random
from dotenv import load_dotenv

load_dotenv() # Carichiamo le variabili del file .env
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready(): # se il bot stabilisce un collegamento a discord ed è pronto a operare fai:
    guild = discord.utils.get(client.guilds, name=GUILD) # richiedi id di tutte le guild a cui il bot è collegato
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message): # se il bot rileva un nuovo messaggio fai:

    # Questo if impedisce al bot di rispondersi da solo nel caso il messaggio
    # che stiamo cercando sia uguale alla risposta del bot
    if message.author == client.user: 
        return
    
    if message.content == 'Test':
        response = 'Hello World'
        await message.channel.send(response)
    
    if message.content == 'raise-exception':
        raise discord.DiscordException

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


client.run(TOKEN) # avvia bot
