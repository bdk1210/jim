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

    async def on_ready(self):
        print(f"✅ Logged in as {self.user} (ID: {self.user.id})", flush=True)

    # Logging
    async def setup_hook(self):
        try:
            print("Setup: Starting cog loading", flush=True)
            await self.load_extension("cogs.statuses")
            print("Loaded statuses", flush=True)
            await self.load_extension("cogs.respond")
            print("Loaded respond", flush=True)
            await self.load_extension("cogs.slash")
            print("Loaded slash", flush=True)
            print("Setup: Syncing tree...", flush=True)
            guild = discord.Object(id=1398587580320059392)
            await self.tree.sync(guild=guild)
            print("Tree synced", flush=True)
            print("Setup complete", flush=True)
        except Exception as e:
            print(f"Setup failed: {e}", flush=True)

# Create the bot instance
bot = jim()

# KEEP THESE AT THE BOTTOM NO MATTER WHAT

# Run the bot using your secret TOKEN
bot.run(os.getenv("TOKEN"))
