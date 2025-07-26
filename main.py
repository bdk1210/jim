import os
import discord
from discord.ext import commands
import random # for random numbers
import aiohttp # for fetching the picture of the day i think
from keep_alive import keep_alive # self-explanatory
from discord.ext import tasks
import itertools # rotating statuses

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

# Create the bot instance
bot = jim()

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    if not rotate_status.is_running():
        rotate_status.start()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # If someone says "hi jim" (case-insensitive)
    if message.content.lower() == "hi jim":
        # Send a random confidence percentage
        random_number = random.randint(60, 100)
        # Send the message
        await message.channel.send(f"hi\n-# {random_number}% confidence")

     
    # Keep commands working
    await bot.process_commands(message)

@bot.tree.command(name="flip", description="flip a coin!")
async def flip(interaction: discord.Interaction):
    # 1 in 1000 chance for "on it's side"
    if random.randint(1, 1000) == 1:
        result = "somehow, God KNOWS how, the coin landed on its side!"
    else:
        result = random.choice(["it's heads!", "it's tails!", "looks like it's heads!", "looks like it's tails!", "and... it's heads!", "it landed on tails!", "heads! hopefully nobody put money on that.", "tails never fails!"])
    await interaction.response.send_message(f"{result} 🪙")

@bot.tree.command(name="bodycount", description="i'm not telling you. there's like a 1% chance that i'd tell you.")
async def bodycount(interaction: discord.Interaction):
    if random.randint(1,100) == 67:
        bodycountnumber = random.randit(2,1000)
        bodycountanswer = f"like, {bodycountnumber}, give or take"
    else:
        bodycountanswer = "not telling you."
    await interaction.response.send_message(f"{bodycountanswer}")
    
# ROTATING STATUSES


# List of statuses to rotate through
statuses = [
    (discord.Status.online, discord.Activity(type=discord.ActivityType.playing, name="with your mom")),
    (discord.Status.dnd, discord.Activity(type=discord.ActivityType.listening, name="the screams of the damned :3")),
    (discord.Status.idle, discord.Activity(type=discord.ActivityType.watching, name="you sleep")),
    (discord.Status.online, discord.Activity(type=discord.ActivityType.competing, name="the hunger games"))
]

status_cycle = itertools.cycle(statuses) # idk what this does but chatgpt said it "create the cycle iterator once"

@tasks.loop(seconds=5)  # Change every 5 seconds
async def rotate_status():
    status, activity = next(status_cycle)  # Get the next status and activity from the cycle
    await bot.change_presence(status=status, activity=activity)

# KEEP THESE AT THE BOTTOM NO MATTER WHAT
# Start the keep-alive server so the bot stays online on Replit (managed on UptimeRobot)
keep_alive()

# Run the bot using your secret TOKEN
bot.run(os.getenv("TOKEN"))
