import discord
import time
from discord.ext import commands, tasks
import itertools

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ROTATING STATUSES
    # List of statuses to rotate through
    statuses = [
        (discord.Status.online, discord.Activity(type=discord.ActivityType.playing, name="with your mom")),
        (discord.Status.dnd, discord.Activity(type=discord.ActivityType.listening, name="the screams of the damned :3")),
        (discord.Status.idle, discord.Activity(type=discord.ActivityType.watching, name="you sleep")),
        (discord.Status.online, discord.Activity(type=discord.ActivityType.competing, name="the hunger games")),
        (discord.Status.online, discord.Streaming(name="the one and only", url="https://twitch.tv/lofigirl")),
    ]

    status_cycle = itertools.cycle(statuses) # idk what this does but chatgpt said it "create the cycle iterator once"

    @tasks.loop(seconds=5)  # Change every 5 seconds
    async def rotate_status(self):
        status, activity = next(self.status_cycle)  # Get the next status and activity from the cycle
        await self.bot.change_presence(status=status, activity=activity)
    
    @commands.Cog.listener()
    async def on_ready(self):
        if not self.rotate_status.is_running():
            self.rotate_status.start()