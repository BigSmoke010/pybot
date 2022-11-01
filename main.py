import discord
from discord.ext import commands
from os import getenv
from dotenv import load_dotenv
import os

load_dotenv('.env')
bot = commands.Bot(command_prefix='p#', intents=discord.Intents.all())
bot.remove_command("help")

@bot.event
async def on_ready():

    game = discord.Game("with filippas juicy fat big penis.")
    await bot.change_presence(activity=game)
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await bot.load_extension(f"cogs.{filename[:-3]}")
    print('loaded modules')
    print("Bot is running!")


@bot.command(name='helpp')
async def helpq(ctx):
    embed = discord.Embed(
        title='Help',
        color=7640463,
        description=
        '**help**\n `` `ok` `kala` \n **tiri** \n `ok` __tiri__ #lka _ok_ ')
    await ctx.send(embed=embed)


@bot.command(name='reloadmodules')
async def relod(ctx):
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await bot.unload_extension(f"cogs.{filename[:-3]}")
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

    await ctx.send('cogs reloaded succesfully')


if __name__ == "__main__":
    bot.run(getenv('TOKEN'))
