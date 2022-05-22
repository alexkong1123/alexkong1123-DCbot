import discord
import keep_alive
from discord import Embed
import command

client = discord.Client()

@client.event
async def on_ready():
    print('logged! {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('test'):
        await message.channel.send('testing....')

       
if __name__ == "__main__":
 keep_alive.keep_alive()
 client.run('OTc3Mzg2MzQwMjAxMTYwNzI0.GuzMBH.dsIMJFJpb-uC7O01qzvnTknokxEbnaK8JD4pZw')
