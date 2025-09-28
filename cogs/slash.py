import discord
import random
import os
from discord import app_commands
from discord.ext import commands, tasks
import datetime
from datetime import timedelta, timezone

class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="flip", description="flip a coin!")
    async def flip(self, interaction: discord.Interaction):
        # 1 in 1000 chance for "on it's side"
        if random.randint(1, 1000) == 1:
            result = "somehow, God KNOWS how, the coin landed on its side!"
        else:
            result = random.choice(["it's heads!", "it's tails!", "looks like it's heads!", "looks like it's tails!", "and... it's heads!", "it landed on tails!", "heads! hopefully nobody put money on that.", "tails never fails!"])
        await interaction.response.send_message(f"{result} 🪙")

    @app_commands.command(name="info", description="technical info about the bot")
    async def info(self, interaction: discord.Interaction):
        import subprocess
        uptime = self.bot.get_uptime()

        try:
            # Get the current git tag for this commit
            tag = subprocess.check_output(
                ["git", "describe", "--tags", "--exact-match"],
                stderr=subprocess.DEVNULL
            ).decode().strip()
        except subprocess.CalledProcessError:
            tag = "untagged"

        await interaction.response.send_message(
            f"Copyright (c) 2025 mocha. All rights reserved under the Berne Convention and other applicable international copyright law. \n"
            f"This code is available to read for verification purposes only. Reproduction without authorization is illegal. \n"
            f"jim version {tag}. Stable production release. \n"
            f"Source code can be found on GitHub at: https://github.com/bdk1210/jim. \n"
            f"Hosted on Railway, built using Python in Visual Studio Code. \n"
            f"Utilizes discord.py and various other open source libraries. \n"
            f"This bot has been running for: {uptime} since last restart. \n"
            f"Ping-pong! {round(self.bot.latency * 1000)}ms latency. \n"
            f":3"
        )

    @app_commands.command(name="bodycount", description="i'm not telling you. there's like a 1% chance that i'd tell you.")
    async def bodycount(self, interaction: discord.Interaction):
        if random.randint(1,100) == 67:
            bodycountnumber = random.randint(2,1000)
            bodycountanswer = f"like, {bodycountnumber}, give or take"
        else:
            bodycountanswer = "not telling you."
        await interaction.response.send_message(f"{bodycountanswer}")

    @app_commands.command(name="say", description="send a message as the bot")
    async def say(
        self,
        interaction: discord.Interaction,
        channel: discord.TextChannel,
        message: str
    ):
        await channel.send(message)
        await interaction.response.send_message("Message sent!", ephemeral=True)

    @app_commands.command(name="purge", description="delete's messages from a specified usstier within the specified timeframe in the current channel")
    async def purge(
        self,
        interaction: discord.Interaction,
        user: discord.Member,
        minutes: int = 10
    ):
        await interaction.response.defer(ephemeral=True)  # Acknowledge the command immediately
        channel = interaction.channel
        deleted = 0

        after_time = datetime.now(timezone.utc) - timedelta(minutes=minutes)
        async for msg in channel.history(after=after_time):
            if msg.author == user:
                await msg.delete()
                deleted += 1

        await interaction.followup.send(f"Deleted {deleted} messages from {user.mention} in the last {minutes} minutes.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Slash(bot))