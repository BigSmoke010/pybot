from discord.ext import commands
import requests
import discord
import json
from random import choice
from PIL import Image
import pygame
import asyncpraw
from os import getenv

class cmds(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.reddit = asyncpraw.Reddit(client_id=getenv('CLIENTID'),
                                client_secret=getenv('TOKENSECRET'),
                                password=getenv('REDDITPASS'),
                                user_agent="SmokBot",
                                username="BigSmug101")

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

    @commands.command(name='gay')
    async def gay(self, ctx, user : discord.Member):
        img = requests.get(user.avatar.url)
        with open('images/tmp.png', 'wb') as imaging:
            imaging.write(img.content)

        # Front Image
        filename = 'images/tmp.png'

        # Back Image
        filename1 = 'images/gay_flag.png'

        # Open Front Image
        frontImage = Image.open(filename1)

        # Open Background Image
        background = Image.open(filename)

        frontImage = frontImage.resize([background.height, background.width])

        background.paste(frontImage, (0, 0), frontImage)
        background.save("images/result.png", format="png")
        with open('images/result.png', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)

    @commands.command(name='wide')
    async def wide(self, ctx, user : discord.Member):
        img = requests.get(user.avatar.url)

        with open('images/tmp.png', 'wb') as imaging:
            imaging.write(img.content)

        img = Image.open('images/tmp.png')
        resizedimg = img.resize([img.width + 1000,img.height])
        resizedimg.save('images/result.png', format='png')
        with open('images/result.png', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)

    @commands.command(name='obamium')
    async def obamium(self, ctx, *, text):
        pygame.font.init()
        surface = pygame.image.load('images/obamium.png')
        font = pygame.font.Font('fonts/Akkurat.ttf', 18)
        label = font.render(text, False, '#FFFFFF')
        surface.blit(label, (70,30))
        pygame.image.save(surface, 'images/resultobamium.png')
        dcfile = discord.File('images/resultobamium.png')
        await ctx.send(file=dcfile)

    @commands.command(name='uwuify')
    async def uwu(self, ctx, *, text):
        txt = text
        litsed = []
        for i in txt:
            if i in ['l','r']:
                i = 'w'
                litsed.append(i)
            else:
                i = i
                litsed.append(i)

        await ctx.send(''.join(litsed))
    @commands.command(name='meme')
    async def meme(self, ctx):

        chosensubs = []
        sub = await self.reddit.subreddit('memes')
        submissions = sub.hot()

        async for i in submissions:
            if i.url[-4:] == '.jpg' or i.url[-4:] == '.png':
                chosensubs.append(i)
        chosensubmission = choice(chosensubs)
        embed = discord.Embed(title=chosensubmission.title, url=chosensubmission.url).set_image(url=chosensubmission.url).set_author(name=chosensubmission.author)
        await ctx.send(embed=embed)

    @commands.command(name='roast')
    async def roast(self, ctx, *, someone:discord.Member =None):
        with open('JSONS/roasts.json', encoding='utf-8') as inf:
            cmds= json.load(inf)
        chosenroast = choice(cmds)
        await ctx.send(chosenroast['roast'])




async def setup(bot):
    await bot.add_cog(cmds(bot))
