from discord.ext import commands
import discord
import json

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
    async def goodmorning(self, ctx, *, text):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            await original.reply(text)
        else:
            await ctx.send(text)

    @commands.command(name='help')
    async def helpcmd(self, ctx, *, cmd=None):
        with open ('JSONS/help.json', encoding='utf-8') as f:
            commands = json.load(f)
        allcmds = [('economy',),('fun',),('nsfw',),('misc',),('moderation',)]
        for i in commands:
            for ind, x in enumerate(allcmds):
                if x[0] == i['category']:
                    y = x + (i['name'],)
                    allcmds.remove(allcmds[ind])
                    allcmds.insert(ind, y)

        embed = discord.Embed(title='pybots help',description='**'+allcmds[0][0]+'**\n'+','.join(allcmds[0][1:]) +'\n**'+allcmds[1][0]+'**\n' +','.join(allcmds[1][1:])+ '\n**'+allcmds[2][0]+'**\n' +','.join(allcmds[2][1:])+'\n**'+allcmds[3][0]+'**\n' +','.join(allcmds[3][1:]) + '\n**'+allcmds[4][0]+'**\n' +','.join(allcmds[4][1:]))
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
