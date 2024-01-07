import discord
from discord.ext import commands
from discord.gateway import DiscordWebSocket

from core import lavalink
from core import status
from core import prefix
from config import config

from rich.console import Console
import glob
import re

console = Console()
bot = commands.Bot(
    command_prefix=prefix.get_prefix,
    intents=discord.Intents().all(),
    activity=status.activity("Adapt >> xyzbot"),
    help_command=None
)

@bot.event
async def on_guild_join(guild):
    default_prefix = '-'
    server_id = str(guild.id)
    prefix.save_prefix(server_id, default_prefix)

@bot.event
async def on_guild_remove(guild):
    server_id = str(guild.id)
    prefix.remove_prefix(server_id)

@bot.event
async def on_ready():
    await lavalink.start_nodes(bot)
    await bot.load_extension("jishaku")
    for file in glob.iglob("cogs/*.py"):
        try:
            await bot.load_extension("cogs.{}".format(re.split(r"/|\\", file)[-1][:-3]))
        except Exception as e:
            print(f"Failed to load {file} \n{type(e).__name__}: {e}")

    console.log("Connected to discord gateway with mobile payload")
    console.log(f"Currently logged in as {bot.name}")

DiscordWebSocket.identify = status.identify
bot.run(
    config.TOKEN,
    log_handler=None
)