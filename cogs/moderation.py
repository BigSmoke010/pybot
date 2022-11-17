# soon
import discord
from discord.ext import commands

class moderate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='ban')
    @commands.has_permissions(ban_members=True, kick_members=True)
    async def ban(self, ctx, user:discord.Member = None, reason: str = None):
        if user == None:
            await ctx.send('you need to mention a user')
        else:
            await user.ban(reason=reason)
            await ctx.send(user.name + ' has been banned')
    @commands.command(name='kick')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user:discord.Member = None, reason: str = None):
        if user == None:
            await ctx.send('you need to mention a user')
        else:
            await user.kick(reason=reason)
            await ctx.send(user.name + ' has been kicked')
    @commands.command(name='mute')
    @commands.has_permissions(ban_members=True, kick_members=True)
    async def mute(self, ctx, user:discord.Member = None):
        if user == None:
            await ctx.send('you need to mention a user')
        else:
            role = discord.utils.get(user.guild.roles, name='muted')
            await user.add_roles(role)
            await ctx.send(user.name + ' has been muted')






async def setup(bot):
    await bot.add_cog(moderate(bot))