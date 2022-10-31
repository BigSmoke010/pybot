from discord.ext import commands
import requests
import discord
import json
from random import choice


class cmds(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='8ball')
    async def ball(self, ctx):
        req = requests.get('https://8ball.delegator.com/magic/JSON/' +
                           ctx.message.content[8:]).text
        jsonresp = json.loads(req)
        embed = discord.Embed(title=ctx.message.content[8:],
                              description=jsonresp["magic"]["answer"])
        await ctx.send(embed=embed)

    @commands.command(name='inspire')
    async def inspiration(self, ctx):
        req = requests.get('https://zenquotes.io/api/random').text
        jsonresp = json.loads(req)
        quote = jsonresp[0]['q']
        author = jsonresp[0]['a']
        await ctx.send(f'{quote}\n-{author}')

    @commands.command(name='guessing')
    async def guess(self, ctx, x: int, y: int):
        await ctx.send('guess the number')
        num = choice(range(x, y))
        num_of_tries = 0
        print(num)
        msg = await self.bot.wait_for('message')

        while int(msg.content) != num:
            if int(msg.content) > num:
                await ctx.send('number guessed is higher')
                msg = await self.bot.wait_for('message')
                num_of_tries += 1
            if int(msg.content) < num:
                await ctx.send('number guessed is lower')
                msg = await self.bot.wait_for('message')
                num_of_tries += 1

        await ctx.send('correct, you guessed the number after ' +
                       str(num_of_tries) + ' tries')


async def setup(bot):
    await bot.add_cog(cmds(bot))
