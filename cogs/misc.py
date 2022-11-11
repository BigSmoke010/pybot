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
        cmds = [('pfp', 'return someones profile picture', 'p#pfp [user]'), ('say', 'make the bot say something', 'p#say [text]'), ('8ball', 'let the bot decide your fate', '8ball [text]'), ('inspire', 'gets a random quote that may inspire you', 'p#inspire'), ('guessing', 'number guessing game', 'p#guessing'), ('balance', 'return the balance of an user', 'p#balance [user]'), ('bet', 'lose or win an amount of money', 'p#bet [amount]'), ('work', 'gain an amount of monney', 'p#work'), ('serverinfo', 'returns some info about the server')]
        if not ctx.channel.nsfw:
            embed = discord.Embed(title='pybot\'s commands', description='**moderation**\n`ban`,`mute`,`kick`,`unban`\n**misc**\n`say`,`pfp`\n**fun**\n`8ball`,`inspire`,`guessing`\n**economy**\n`balance`,`bet`,`register`,`work`').set_footer(text='do p#help [command] for more information on that command')
        else:
            embed = discord.Embed(title='pybot\'s commands', description='**moderation**\n`ban`,`mute`,`kick`,`unban`\n**misc**\n`say`,`pfp`\n**fun**\n`8ball`,`inspire`,`guessing`\n**economy**\n`balance`,`bet`,`register`,`work`\n**NSFW**\n`nsfw`,`boobs`,`gonewild`').set_footer(text='do p#help [command] for more information on that command')
        for x,y,z in cmds:
            if cmd == x:
                embed = discord.Embed(title=x, description=y, color=16777112).set_footer(text='usage: ' + z)

        await ctx.send(embed=embed)
    @commands.command(name='serverinfo')
    async def info(self, ctx):
        embed = discord.Embed(title=str(ctx.guild.name) + '\'s Server Info', description='**Creation date**: ' + str(ctx.guild.created_at.strftime("%Y-%m-%d %H:%M:%S")) + '\n**Member Count**: ' + str(ctx.guild.member_count) + '\n **Owner**: ' + str(ctx.guild.owner) + '\n**Emojis**: ' + str([':' + i.name + ':' for i in ctx.guild.emojis])).set_thumbnail(url=ctx.guild.icon)
        await ctx.send(embed=embed)
    @commands.command(name='userinfo')
    async def usrinfo(self, ctx, usr: discord.Member=None):
        if usr == None:
            embed = discord.Embed(title=ctx.author.name + '\'s user info\n', description='**Account Creation Date**: '+ str(ctx.author.created_at.strftime("%Y-%m-%d %H:%M:%S")) + '\n**Join Date**: ' + str(ctx.author.joined_at.strftime("%Y-%m-%d %H:%M:%S")) + '\n**Roles**: ' + str([i.name for i in ctx.author.roles]), color=ctx.author.colour).set_thumbnail(url=ctx.author.avatar)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=usr.name + '\'s user info\n', description='**Account Creation Date**: '+ str(usr.created_at.strftime("%Y-%m-%d %H:%M:%S")) + '\n**Join Date**: ' + str(usr.joined_at.strftime("%Y-%m-%d %H:%M:%S")) + '\n**Roles**: ' + str([i.name for i in usr.roles]), color=usr.colour).set_thumbnail(url=usr.avatar)
            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(miscelanous(bot))
