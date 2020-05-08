import os
import discord

TOKEN = os.getenv('DUCK_TOKEN')
BOT_ID = os.getenv('DUCK_CLIENT_ID')
phrase = ':duck: Quack :duck:'

client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")

@client.event
async def on_message(message):
    if BOT_ID in message.content:
        await message.channel.send(phrase) 

client.run(TOKEN)

