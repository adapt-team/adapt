import discord
from discord.ext import commands

from core import prefix
from config import config

class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
            aliases=[
                'h',
                'cmds',
                'commands'
            ]
    )
    async def help(self, ctx):
        embed = discord.Embed(
            type="rich",
            description="<:i_:1193246587967774730>  **` Core Commands  `**\n\n"
                        " ​ ​ ` help      ` ​ ​ ​ ​ ​Show full command list\n"
                        " ​ ​ ` ping      ` ​ ​ ​ ​ ​Bot connection details\n"
                        " \n"
                        f"Use   ` {prefix.get_prefix(self.bot, ctx)}help <command> ` to view more information about a command.",
            color=config.COLOR
        )
        embed.set_footer(
            text=f"{self.bot.user.name} • Page 1/7",
            icon_url=f"{self.bot.user.avatar}",
        )

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Main(bot))