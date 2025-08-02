# i have absolutely no idea what i am doing, please have mercy on me
# all i know is that the imports go at the top and that's about it
import os
import discord
from discord.ext import commands
import random # for random numbers
import aiohttp # for fetching the picture of the day
from discord.ext import tasks
import itertools # rotating statuses
import time
from datetime import datetime, timedelta, timezone

# Define the bot class with slash command support
class jim(commands.Bot):
    def __init__(self):
        # Enable reading messages
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        # Sync slash commands globally
        await self.tree.sync()
        await self.load_extension("cogs.statuses")
        await self.load_extension("cogs.respond")
        await self.load_extension("cogs.slash")

# Create the bot instance
bot = jim()

# Logging
async def setup_hook(self):
    print("Setup: Starting cog loading")
    await self.load_extension("cogs.statuses")
    print("Loaded statuses")
    await self.load_extension("cogs.respond")
    print("Loaded respond")
    await self.load_extension("cogs.slash")
    print("Loaded slash")
    print("Setup: Syncing tree...")
    await self.tree.sync()
    print("Setup complete")

# KEEP THESE AT THE BOTTOM NO MATTER WHAT

# Run the bot using your secret TOKEN
bot.run(os.getenv("TOKEN"))
