import discord
from discord.ext import commands, tasks
import random


class ACTIVITY(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.rand = None
        self.bot = bot
        self.status.start()
        self.partners = ["Blemur", "KubaVelDudek", "NezukoChill"]
        self.sleep_on = ["a pillow", "the couch", "an armchair",
                         "the bed", "the wardrobe", "a jar", "the sink"]
        self.where = ["on", "in", "behind"]

    def cog_unload(self) -> None:
        self.status.stop()

    @tasks.loop(minutes=5)
    async def status(self):
        self.rand = int(random.randint(1, 5))

        match self.rand:
            case 1:
                guild_count = len(self.bot.guilds)
                await self.bot.change_presence(status=discord.Status.online,
                                               activity=discord.CustomActivity(f"I'm on {guild_count} servers"))
            case 2:
                dis = random.choice(self.partners)
                await self.bot.change_presence(status=discord.Status.dnd,
                                               activity=discord.Activity(type=discord.ActivityType.watching,
                                                                         name=f"{dis}"))
            case 3:
                await self.bot.change_presence(status=discord.Status.online,
                                               activity=discord.CustomActivity(f"Join our server!"))
            case 4:
                await self.bot.change_presence(status=discord.Status.online,
                                               activity=discord.CustomActivity(f"🐈 Meow! 🐈"))
            case 5:
                dis = random.choice(self.where)
                dis2 = random.choice(self.sleep_on)
                await self.bot.change_presence(status=discord.Status.idle,
                                               activity=discord.CustomActivity(f"Sleeps {dis} {dis2}"))


    @status.before_loop
    async def before_status(self):
        await self.bot.wait_until_ready()


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ACTIVITY(bot))
