import discord
import random
import os
from discord.ext import app_commands, tasks
import datetime
from datetime import timedelta, timezone

@app_commands.command(name="flip", description="flip a coin!")
async def flip(interaction: discord.Interaction):
    # 1 in 1000 chance for "on it's side"
    if random.randint(1, 1000) == 1:
        result = "somehow, God KNOWS how, the coin landed on its side!"
    else:
        result = random.choice(["it's heads!", "it's tails!", "looks like it's heads!", "looks like it's tails!", "and... it's heads!", "it landed on tails!", "heads! hopefully nobody put money on that.", "tails never fails!"])
    await interaction.response.send_message(f"{result} 🪙")

@app_commands.command(name="bodycount", description="i'm not telling you. there's like a 1% chance that i'd tell you.")
async def bodycount(interaction: discord.Interaction):
    if random.randint(1,100) == 67:
        bodycountnumber = random.randint(2,1000)
        bodycountanswer = f"like, {bodycountnumber}, give or take"
    else:
        bodycountanswer = "not telling you."
    await interaction.response.send_message(f"{bodycountanswer}")

@app_commands.command(name="say", description="send a message as the bot")
async def say(
    interaction: discord.Interaction,
    channel: discord.TextChannel,
    message: str
):
    await channel.send(message)
    await interaction.response.send_message("Message sent!", ephemeral=True)

@app_commands.command(name="purge", description="delete's messages from a specified usstier within the specified timeframe in the current channel")
async def purge(
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