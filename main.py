import discord
import keep_alive

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('test'):
        await message.channel.send('testing...')

    if message.content.startswith('test'):
        embed = discord.Embed(
            title = "Title",
            description = "test",
            colour = discord.Colour.blue()
        )
      
if __name__ == "__main__":
 keep_alive.keep_alive()
 client.run('OTc3Mzg2MzQwMjAxMTYwNzI0.GuzMBH.dsIMJFJpb-uC7O01qzvnTknokxEbnaK8JD4pZw')
