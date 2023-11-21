import asyncio
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv


def run():
    bot = commands.Bot(command_prefix='-', intents=discord.Intents.all(),
                       activity=discord.Game(name="Starting"))

    # @bot.event
    # async def on_ready():
    #     fmt = await bot.tree.sync()
    #     print(f'Synced {len(fmt)} commands.')
    #     guild_count = len(bot.guilds)
    #     await bot.change_presence(
    #         activity=discord.Activity(type=discord.ActivityType.watching, name=f'{guild_count} servers.'))

    @bot.event
    async def on_guild_join(guild):
        fmt = await bot.tree.sync()
        print(f'Synced {len(fmt)} commands.')
        # guild_count = len(bot.guilds)
        # await bot.change_presence(
        #     activity=discord.Activity(type=discord.ActivityType.watching, name=f'{guild_count} servers.'))

    # @bot.event
    # async def on_guild_remove(guild):
    #     guild_count = len(bot.guilds)
    #     await bot.change_presence(
    #         activity=discord.Activity(type=discord.ActivityType.watching, name=f'{guild_count} servers.'))

    @bot.command()
    @commands.is_owner()
    async def sync(ctx) -> None:
        fmt = await ctx.bot.tree.sync()
        print(f'Synced {len(fmt)} commands.')
        await ctx.message.delete()

    @bot.command()
    @commands.is_owner()
    async def unload(ctx, name):
        await bot.unload_extension(f'cogs.{name}')
        await ctx.message.delete()

    @bot.command()
    @commands.is_owner()
    async def load(ctx, name):
        await bot.load_extension(f'cogs.{name}')
        await ctx.message.delete()

    async def load():
        for file in os.listdir('./cogs'):
            if file.endswith('.py'):
                try:
                    await bot.load_extension(f'cogs.{file[:-3]}')
                    print(f"{file[:-3]} ✔")
                except Exception as e:
                    print(f"{file[:-3]} X - Error {e} ")

    async def main():
        await load()
        load_dotenv()
        await bot.start(os.getenv('DISCORD_TOKEN'))

    asyncio.run(main())


if __name__ == "__main__":
    run()

