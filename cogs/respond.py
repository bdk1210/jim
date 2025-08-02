import random
from discord.ext import commands

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        content = message.content.lower()

        hi_triggers = [
            "hi jim",
            "hello jim",
            "hey jim",
            "jim hi",
            "jim hello",
            "jim hey",
        ]
        if any(phrase in content for phrase in hi_triggers):
            random_number = random.randint(60, 100)
            await message.channel.send(f"hi\n-# {random_number}% confidence")
            return  # avoid multiple replies per message

        htj_triggers = [
            "how to join",
            "how do i join",
            "how can i join",
            "join instructions",
            "how do you join",
            "htj",
        ]
        if any(phrase in content for phrase in htj_triggers):
            await message.channel.send(
                "# here's how to join:\n"
                "go to <#1395507047574798537> and take note of the server's ip address and port. ***please note, we are a bedrock server.***\n"
                "then, open minecraft. from the main screen, click *\"play\"*, and then *\"servers\"* at the top-right.\n"
                "scroll down through the servers until you see *\"Add Server\"*. click it, and enter the details from <#1395507047574798537>. the server name can be whatever you like.\n\n"
                "alternatively, you can go to <#1398556073132036187> and click the link under \"connect.\"\n\n"
                "have fun!"
            )
            return

        ily_triggers = [
            "i love you jim",
            "jim i love you",
            "i love jim",
        ]
        ily_responses = [
            "i can't say it back but i appreciate the sentiment! :3",
            "thanks but i'm not saying it back",
            "i know what you're trying to do, and i won't say it back",
            "thank you but you aren't fooling me."
        ]
        if any(phrase in content for phrase in ily_triggers):
            response = random.choice(ily_responses)
            await message.channel.send(response)
            return

        # Keep commands working
        await self.bot.process_commands(message)

async def setup(bot):
    await bot.add_cog(Greetings(bot))