import discord
from discord import app_commands
from discord.ext import commands

from commands.data import *
from commands.pictures import *


class HELLO(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('ready')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild_id = str(member.guild.id)
        if check_set('data/daichi_settings.json', guild_id):
            settings = get_settings('data/daichi_settings.json', guild_id)

            get_picture(member.avatar.url)
            match guild_id:
                case "1097196815822110720":  # 1097196815822110720 <- nomc
                    nomc(member.name)

                case _:
                    make_banner(settings['banner'],
                                settings['color'],
                                member.name,
                                settings['join_information'],
                                settings['greet']
                                )

            channel = self.bot.get_channel(settings['channel_mention'])
            try:
                with open("work/final.png", "rb") as file:
                    await channel.send(file=discord.File(file))
            except Exception as e:
                print(f"An error occurred while sending the file: {e}")
            clear("work/")

    @app_commands.command(name="test", description="")
    async def test(self, interaction: discord.Interaction):
        get_picture(interaction.user.avatar.url)
        nomc(interaction.user.name)

        channel = self.bot.get_channel(interaction.response)
        try:
            with open("work/final.png", "rb") as file:
                await channel.send(file=discord.File(file))
        except Exception as e:
            print(f"An error occurred while sending the file: {e}")
        clear("work/")

    @app_commands.command(name="greet", description="Select welcome channel")
    async def hello_set(
            self,
            interaction: discord.Interaction,
            channel_mention: str,
            join_information: str = "just joined",
            greet: str = "Welcome to the server!",
            banner: str = "horizontal",
            color: str = "default",

    ) -> None:
        if interaction.user.guild_permissions.administrator:
            guild_id = str(interaction.guild.id)

            if not check_set('data/daichi_settings.json', guild_id):
                add = {str(guild_id): {
                    "channel_mention": int(channel_mention[2:-1]),
                    "join_information": str(join_information),
                    "greet": str(greet),
                    "banner": str(banner),
                    "color": str(color)
                }}
                add_settings('data/daichi_settings.json', add)
                await interaction.response.send_message("Welcome channel set.", ephemeral=True)
            else:
                await interaction.response.send_message("The welcome channel is already set up on this server. "
                                                        "To select a new one, delete the old one "
                                                        "using the ```/stop_greet``` command. ", ephemeral=True)
        else:
            await interaction.response.send_message("Only admin can use this command", ephemeral=True)

    @app_commands.command(name="stop_greet", description="Clear welcome channel")
    async def fire_command(self, interaction: discord.Interaction) -> None:
        if interaction.user.guild_permissions.administrator:
            guild_id = str(interaction.guild.id)
            if check_set('data/daichi_settings.json', guild_id):

                remove_settings('data/daichi_settings.json', [guild_id])

                await interaction.response.send_message("Welcome channel removed.", ephemeral=True)
            else:
                await interaction.response.send_message("Welcome channel not found.", ephemeral=True)
        else:
            await interaction.response.send_message("Only admin can use this command", ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(HELLO(bot))
