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

    @commands.command(name='nsfw')
    @commands.is_nsfw()
    async def notsafeforwork(self, ctx):
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

    @commands.command(name='boobs')
    @commands.is_nsfw()
    async def boob(self, ctx):
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

    @commands.command(name='gonewild')
    @commands.is_nsfw()
    async def goinwild(self, ctx):
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

    @commands.command(name='danbooru')
    @commands.is_nsfw()
    async def dan(self, ctx, topic:str=None):
        if topic == None:
            rqst = requests.get("https://danbooru.donmai.us/posts.json?limit=100").text
        else:

            rqst = requests.get("https://danbooru.donmai.us/posts.json?limit=100&post[tag_string]=" + topic).text
        jsn = json.loads(rqst)
        chosenurl = jsn[choice(range(0,100))]
        embd = discord.Embed().set_image(url=chosenurl["file_url"])
        await ctx.send(embed=embd)


async def setup(bot):
    await bot.add_cog(nsfw(bot))
