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

    def get_uptime(self):
        now = datetime.now(timezone.utc)
        delta = now - self.start_time
        days = delta.days
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{days} days, {hours} hours, {minutes} minutes, and {seconds} seconds"

    async def on_ready(self):
        print(f"✅ logged in as {self.user} (ID: {self.user.id}) :3", flush=True)

        guild = discord.Object(id=1398587580320059392)
        await self.tree.sync(guild=guild)
        print(f"Synced commands to guild {guild.id}")

    # Logging
    async def setup_hook(self):
        try:
            print("setup: starting cog loading", flush=True)
            await self.load_extension("cogs.statuses")
            print("loaded statuses", flush=True)
            await self.load_extension("cogs.respond")
            print("loaded respond", flush=True)
            await self.load_extension("cogs.slash")
            print("loaded slash", flush=True)
            print("setup: syncing tree...", flush=True)
            await self.tree.sync()
            print("tree synced", flush=True)
            self.start_time = datetime.datetime.utcnow()
            print("start time recorded", flush=True)
            print("setup complete", flush=True)
        except Exception as e:
            print(f"well, shit. setup failed: {e}", flush=True)

# Create the bot instance
bot = jim()

# KEEP THESE AT THE BOTTOM NO MATTER WHAT

# Run the bot using your secret TOKEN
bot.run(os.getenv("TOKEN"))
