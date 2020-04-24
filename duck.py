import os

import discord

TOKEN = os.getenv('DUCK_TOKEN')
BOT_ID = os.getenv('DUCK_CLIENT_ID')

client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")

@client.event
async def on_message(message):
    if BOT_ID in message.content:
        await message.channel.send(':duck: Quack :duck:')
    

client.run(TOKEN)
