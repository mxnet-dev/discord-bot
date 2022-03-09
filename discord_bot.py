import os
import discord
from discord.ext import commands
from discord.utils import get
TOKEN = os.environ['DISCORD_TOKEN']
CHANNELID = os.environ['DISCORD_CHANNEL']

bot = discord.Client()

@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

@bot.event
async def on_raw_reaction_add(payload):
    if payload.emoji.name == "✅":
            channel = bot.get_channel(int(CHANNELID))
            message = await channel.fetch_message(payload.message_id)
            reaction = get(message.reactions, emoji=payload.emoji.name)
            if reaction and reaction.count > 0:
                await message.edit(suppress=True)
                await message.clear_reaction("✅")
                await message.reply("Container Updated on <:portainer:949513858106671124>", mention_author=False)
                await message.add_reaction("<:portainer:949513858106671124>")

bot.run(TOKEN)