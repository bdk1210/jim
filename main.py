# i have absolutely no idea what i am doing, please have mercy on me
# all i know is that the imports go at the top and that's about it
import os
import discord
from discord.ext import commands
import random # for random numbers
import aiohttp # for fetching the picture of the day  
from keep_alive import keep_alive # self-explanatory
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

    # hi jim feature
    hi_triggers = [
        "hi jim",
        "hello jim",
        "hey jim",
        "jim hi",
        "jim hello",
        "jim hey",
        "hi jim",
    ]
    # If someone says "hi jim" (case-insensitive)
    if any(phrase in message.content.lower() for phrase in hi_triggers):
        # Send a random confidence percentage
        random_number = random.randint(60, 100)
        # Send the message
        await message.channel.send(f"hi\n-# {random_number}% confidence")

    # how to join feature
    # List of trigger phrases (lowercase)
    htj_triggers = [
        "how to join",
        "how do i join",
        "how can i join",
        "join instructions",
        "how do you join",
        "htj",
    ]

    ily_triggers = [
        "i love you jim",
        "jim i love you",
        "i love jim"]
    
    ily_responses = [
        "i can't say it back but i appreciate the sentiment! :3",
        "thanks but i'm not saying it back",
        "i know what you're trying to do, and i won't say it back",
        "thank you but you aren't fooling me."
        ]
    
    if any(phrase in message.content.lower() for phrase in ily_triggers):
        ilymessage = random.choice(ily_responses)
        await message.channel.send(ilymessage)
            

    
    if any(phrase in message.content.lower() for phrase in htj_triggers):
        await message.channel.send(
            "here's how to join:\n"
            "go to #server-info and take note of the server's ip address and port. *please note, we are a bedrock server.*\n"
            "then, open minecraft. from the main screen, click play, and then servers at the top-right.\n"
            "scroll down through the servers until you see Add Server. click it, and enter the details from #server-info. the server name can be whatever you like.\n\n"
            "have fun!")

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
        bodycountnumber = random.randint(2,1000)
        bodycountanswer = f"like, {bodycountnumber}, give or take"
    else:
        bodycountanswer = "not telling you."
    await interaction.response.send_message(f"{bodycountanswer}")

@bot.tree.command(name="say", description="send a message as the bot")
async def say(
    interaction: discord.Interaction,
    channel: discord.TextChannel,
    message: str
):
    await channel.send(message)
    await interaction.response.send_message("Message sent!", ephemeral=True)

@bot.tree.command(name="purge", description="delete's messages from a specified user within the specified timeframe in the current channel")
async def purge(
    interaction: discord.Interaction,
    user: discord.Member,
    minutes: int = 10
):
    await interaction.response.defer(ephemeral=True)  # Acknowledge the command immediately
    channel = interaction.channel
    after_time = datetime.now(datetime.timezone.utc)
    deleted = 0

    after_time = datetime.now(datetime.timezone.utc) - timedelta(minutes=minutes)
    async for msg in channel.history(after=after_time):
        if msg.author == user:
            await msg.delete()
            deleted += 1

    await interaction.followup.send(f"Deleted {deleted} messages from {user.mention} in the last {minutes} minutes.", ephemeral=True)
    
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
async def rotate_status():
    status, activity = next(status_cycle)  # Get the next status and activity from the cycle
    await bot.change_presence(status=status, activity=activity)

# KEEP THESE AT THE BOTTOM NO MATTER WHAT
# Start the keep-alive server so the bot stays online (managed on UptimeRobot)
keep_alive()

# Run the bot using your secret TOKEN
bot.run(os.getenv("TOKEN"))
