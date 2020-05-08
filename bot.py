import os
import discord

TOKEN = os.getenv('ANIMAL_TOKEN')
BOT_ID = os.getenv('ANIMAL_CLIENT_ID')
phrase = ''

client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")

@client.event
async def on_message(message):
    if BOT_ID in message.content:
        await message.channel.send(phrase) 

client.run(TOKEN)

