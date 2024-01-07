import discord
from discord.ext import commands
import re

from config import config
from core import prefix

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['sn'])
    @commands.guild_only()
    @commands.has_permissions(manage_nicknames=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def setnick(self, ctx, member: discord.Member, *, nick):
        try:
            await member.edit(nick=nick)
            await ctx.send(f'Nickname for {member.name} was changed to {member.mention}')
        
        except discord.HTTPException:
            await ctx.send("Something went wrong.")

    @commands.command(aliases=['p', 'prefix'])
    @commands.has_permissions(administrator=True)
    async def setprefix(self, ctx, new_prefix):
        if new_prefix == "reset":
            new_prefix = "-"

        server_id = str(ctx.guild.id)
        prefix.save_prefix(server_id, new_prefix)

        embed = discord.Embed(
            title="",
            description=f"{new_prefix}",
            color=config.COLOR
        )
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Moderation(bot))