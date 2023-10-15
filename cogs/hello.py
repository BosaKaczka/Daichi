import asyncio
import discord
from discord.ext import commands
from discord import app_commands

class HELLO(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot



async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(HELLO(bot))
