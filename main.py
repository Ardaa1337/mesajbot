import discord
import os

TOKEN = os.environ["DISCORD_TOKEN"]
CHANNEL_ID = int(os.environ["CHANNEL_ID"])

MESSAGE = "Merhaba! Bu otomatik mesajdır 🚀"

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(MESSAGE)
    await client.close()

client.run(TOKEN)
