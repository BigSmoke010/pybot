import discord
from discord.ext import commands
from time import sleep

class moderate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='ban')
    @commands.has_permissions(ban_members=True, kick_members=True)
    async def ban(self, ctx, user:discord.Member = None, reason: str = None):
        if user == None:
            await ctx.send('you need to __mention__ an user')
        else:
            await user.ban(reason=reason)
            await ctx.send('**'+user.name + '** has been banned')
    @commands.command(name='kick')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user:discord.Member = None, reason: str = None):
        if user == None:
            await ctx.send('you need to __mention__ an user')
        else:
            await user.kick(reason=reason)
            await ctx.send('**'+user.name + '** has been kicked')
    @commands.command(name='mute')
    @commands.has_permissions(ban_members=True, kick_members=True)
    async def mute(self, ctx, user:discord.Member = None):
        if user == None:
            await ctx.send('you need to __mention__ an user')
        else:
            role = discord.utils.get(user.guild.roles, name='muted')
            await user.add_roles(role)
            await ctx.send('**'+user.name + '** has been muted')
    @commands.command(name='purge')
    @commands.has_permissions(ban_members=True, kick_members=True)
    async def purge(self, ctx, amount: int):
        await ctx.channel.purge(limit=int(amount))
        await ctx.send('deleted **' + str(amount) + '** messages!')






async def setup(bot):
    await bot.add_cog(moderate(bot))