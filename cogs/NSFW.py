from discord.ext import commands
from os import getenv
from dotenv import load_dotenv
import asyncpraw
import discord
from random import choice


class nsfw(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='nsfw')
    async def notsafeforwork(self, ctx):
        if ctx.channel.nsfw:
            reddit = asyncpraw.Reddit(client_id=getenv('CLIENTID'),
                                      client_secret=getenv('TOKENSECRET'),
                                      password=getenv('REDDITPASS'),
                                      user_agent="SmokBot",
                                      username="BigSmug101")
            chosensubs = []
            sub = await reddit.subreddit('nsfw')
            submissions = sub.hot()

            async for i in submissions:
                if i.url[-4:] == '.jpg' or i.url[-4:] == '.png':
                    chosensubs.append(i)
            chosensubmission = choice(chosensubs)
            embed = discord.Embed(title=chosensubmission.title, url=chosensubmission.url).set_image(url=chosensubmission.url).set_author(name=chosensubmission.author)
            await ctx.send(embed=embed)
        else:
            await ctx.send('you are not in an nsfw channel')

    @commands.command(name='boobs')
    async def boob(self, ctx):
        if ctx.channel.nsfw:
            reddit = asyncpraw.Reddit(client_id=getenv('CLIENTID'),
                                      client_secret=getenv('TOKENSECRET'),
                                      password=getenv('REDDITPASS'),
                                      user_agent="SmokBot",
                                      username="BigSmug101")
            chosensubs = []
            sub = await reddit.subreddit('boobs')
            submissions = sub.hot()

            async for i in submissions:
                if i.url[-4:] == '.jpg' or i.url[-4:] == '.png':
                    chosensubs.append(i)
            chosensubmission = choice(chosensubs)
            embed = discord.Embed(title=chosensubmission.title, url=chosensubmission.url).set_image(url=chosensubmission.url).set_author(name=chosensubmission.author)
            await ctx.send(embed=embed)
        else:
            await ctx.send('you are not in an nsfw channel')

    @commands.command(name='gonewild')
    async def goinwild(self, ctx):
        if ctx.channel.nsfw:
            reddit = asyncpraw.Reddit(client_id=getenv('CLIENTID'),
                                      client_secret=getenv('TOKENSECRET'),
                                      password=getenv('REDDITPASS'),
                                      user_agent="SmokBot",
                                      username="BigSmug101")
            chosensubs = []
            sub = await reddit.subreddit('gonewild')
            submissions = sub.hot()

            async for i in submissions:
                if i.url[-4:] == '.jpg' or i.url[-4:] == '.png':
                    chosensubs.append(i)
            chosensubmission = choice(chosensubs)
            embed = discord.Embed(title=chosensubmission.title, url=chosensubmission.url).set_image(url=chosensubmission.url).set_author(name=chosensubmission.author)
            await ctx.send(embed=embed)
        else:
            await ctx.send('you are not in an nsfw channel')


async def setup(bot):
    await bot.add_cog(nsfw(bot))
