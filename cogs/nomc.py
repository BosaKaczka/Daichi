import json
import discord
from discord import app_commands
from discord.ext import commands
from commands.data import check_set, add_settings


class NOMC(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="nomc", description="your custom banner")
    async def hello_set(
            self,
            interaction: discord.Interaction,
            channel_mention: str,
    ) -> None:
        if interaction.user.guild_permissions.administrator:
            guild_id = str(interaction.guild.id)
            if not check_set('data/daichi_settings.json', guild_id):
                new_settings = {str(guild_id): {
                    "channel_mention": int(channel_mention[2:-1]),
                }}
                await interaction.response.send_message("Welcome channel set.", ephemeral=True)
                add_settings('data/daichi_settings.json', new_settings)
            else:
                await interaction.response.send_message("The welcome channel is already set up on this server. "
                                                        "To select a new one, delete the old one "
                                                        "using the ```/stop_greet``` command. ", ephemeral=True)
        else:
            await interaction.response.send_message("Only admin can use this command", ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(NOMC(bot))
