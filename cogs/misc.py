from discord.ext import commands
import discord
class miscelanous(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='pfp')
    async def pfp(self, ctx, idd : discord.Member=None):
        if idd == None:
            idd = ctx.author
        embd = discord.Embed(title=str(idd.name) + '\'s pfp', color=16777112).set_image(url=idd.avatar.url)
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

    @commands.command(name='help')
    async def help(self, ctx, cmd=None):
        cmds = [('pfp', 'return someones profile picture', 'p#pfp [user]'), ('say', 'make the bot say something', 'p#say [text]'), ('8ball', 'let the bot decide your fate', '8ball [text]'), ('inspire', 'gets a random quote that may inspire you', 'p#inspire'), ('guessing', 'number guessing game', 'p#guessing'), ('balance', 'return the balance of an user', 'p#balance [user]'), ('bet', 'lose or win an amount of money', 'p#bet [amount]'), ('work', 'gain an amount of monney', 'p#work')]
        if not ctx.channel.nsfw:
            embed = discord.Embed(title='pybot\'s commands', description='**misc**\n`say`,`pfp`\n**fun**\n`8ball`,`inspire`,`guessing`\n**economy**\n`balance`,`bet`,`register`,`work`').set_footer(text='do p#help [command] for more information on that command')
        else:
            embed = discord.Embed(title='pybot\'s commands', description='**misc**\n`say`,`pfp`\n**fun**\n`8ball`,`inspire`,`guessing`\n**economy**\n`balance`,`bet`,`register`,`work`\n**NSFW**\n`nsfw`,`boobs`,`gonewild`').set_footer(text='do p#help [command] for more information on that command')
        for x,y,z in cmds:
            if cmd == x:
                embed = discord.Embed(title=x, description=y, color=16777112).set_footer(text='usage: ' + z)

        await ctx.send(embed=embed)



async def setup(bot):
    await bot.add_cog(miscelanous(bot))
