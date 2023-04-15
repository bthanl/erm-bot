import apiKeys

import logging
import sys
import os
import asyncio
import discord
from cogs import dev
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix=["erm ", "Erm "],
    description='lol',
    intents=intents,
    help_command=None,
    case_insensitive = True,

)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    await bot.change_presence(activity=discord.Game(name='erm help'))

async def main():
    async with bot:
        for filename in dev.dev.getCogs():
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print("loaded", filename)
        
        await bot.start(apiKeys.apiKeys.discord_key)

logging.basicConfig(stream=sys.stdout, level=logging.WARNING)

asyncio.run(main())
