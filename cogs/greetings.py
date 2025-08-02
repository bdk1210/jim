import random
from discord.ext import commands

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        
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
            return

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
            

async def setup(bot):
    await bot.add_cog(Greetings(bot))