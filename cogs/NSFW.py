from discord.ext import commands
from os import getenv
import asyncpraw
import discord
from random import choice
import requests
import json

class nsfw(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.reddit = asyncpraw.Reddit(client_id=getenv('CLIENTID'),
                                client_secret=getenv('TOKENSECRET'),
                                password=getenv('REDDITPASS'),
                                user_agent="SmokBot",
                                username="BigSmug101")

    @commands.command(name='nsfw')
    @commands.is_nsfw()
    async def notsafeforwork(self, ctx):
        chosensubs = []
        sub = await self.reddit.subreddit('nsfw')
        submissions = sub.hot()

        async for i in submissions:
            if i.url[-4:] == '.jpg' or i.url[-4:] == '.png':
                chosensubs.append(i)
        chosensubmission = choice(chosensubs)
        embed = discord.Embed(title=chosensubmission.title, url=chosensubmission.url).set_image(url=chosensubmission.url).set_author(name=chosensubmission.author)
        await ctx.send(embed=embed)

    @commands.command(name='boobs')
    @commands.is_nsfw()
    async def boob(self, ctx):
        chosensubs = []
        sub = await self.reddit.subreddit('boobs')
        submissions = sub.hot()

        async for i in submissions:
            if i.url[-4:] == '.jpg' or i.url[-4:] == '.png':
                chosensubs.append(i)
        chosensubmission = choice(chosensubs)
        embed = discord.Embed(title=chosensubmission.title, url=chosensubmission.url).set_image(url=chosensubmission.url).set_author(name=chosensubmission.author)
        await ctx.send(embed=embed)

    @commands.command(name='gonewild')
    @commands.is_nsfw()
    async def goinwild(self, ctx):
        chosensubs = []
        sub = await self.reddit.subreddit('gonewild')
        submissions = sub.hot()

        async for i in submissions:
            if i.url[-4:] == '.jpg' or i.url[-4:] == '.png':
                chosensubs.append(i)
        chosensubmission = choice(chosensubs)
        embed = discord.Embed(title=chosensubmission.title, url=chosensubmission.url).set_image(url=chosensubmission.url).set_author(name=chosensubmission.author)
        await ctx.send(embed=embed)

    @commands.command(name='danbooru')
    @commands.is_nsfw()
    async def dan(self, ctx):
        rqst = requests.get("https://danbooru.donmai.us/posts.json?limit=200&page=" + str(choice(range(0, 1000)))).text
        jsn = json.loads(rqst)
        chosenurl = jsn[choice(range(0,len(jsn)))]
        if chosenurl['rating'] != 'e':
            while chosenurl['rating'] != 'e':
                rqst = requests.get("https://danbooru.donmai.us/posts.json?limit=200&page=" + str(choice(range(0, 1000)))).text
                jsn = json.loads(rqst)
                chosenurl = jsn[choice(range(0,len(jsn)))]
                if chosenurl['rating'] == 'e':
                    break
        embd = discord.Embed().set_image(url=chosenurl["file_url"])
        await ctx.send(embed=embd)


async def setup(bot):
    await bot.add_cog(nsfw(bot))
