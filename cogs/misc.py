from discord.ext import commands
import discord
class miscelanous(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='pfp')
    async def pfp(self, ctx, idd : discord.Member=None):
        embd = discord.Embed(title=str(idd.name) + '\'s pfp').set_image(url=idd.avatar.url)
        await ctx.send(embed=embd)

    @commands.command(name='say')
    async def goodmorning(self, ctx):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            await original.reply(ctx.message.content[6:])
        elif ctx.message.content[6:] == '':
            await ctx.send('nothing to say')
        else:
            await ctx.send(ctx.message.content[6:])




async def setup(bot):
    await bot.add_cog(miscelanous(bot))
