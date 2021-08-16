import json
import os
import sys
import aiohttp
import asyncio
import discord
from discord.ext import commands

# Only if you want to use variables that are in the config.json file.
if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)


# Here we name the cog and create a new class for the cog.
class apis(commands.Cog, name="apis"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="slap")
    async def slap(self, context, User:discord.User):
        """
        slaps another user
        """

        url = "https://api.waifu.pics/sfw/slap"
        # Async HTTP request
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            embed = discord.Embed(
                title=f"{context.message.author.display_name} slaps {User.display_name}",
                description="",
                color=0x42F56C
            )
            embed.set_image(url=response['url'])
            await context.message.delete()
            await context.send(embed=embed)

    @commands.command(name="yeet")
    async def yeet(self, context, User:discord.User):
        """
        slaps another user
        """

        url = "https://api.waifu.pics/sfw/yeet"
        # Async HTTP request
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            embed = discord.Embed(
                title=f"{context.message.author.display_name} yeets {User.display_name}",
                description="",
                color=0x42F56C
            )
            embed.set_image(url=response['url'])
            await context.message.delete()
            await context.send(embed=embed)

    @commands.command(name="kill")
    async def kill(self, context, User:discord.User):
        """
        kills another user
        """

        url = "https://api.waifu.pics/sfw/kill"
        # Async HTTP request
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            embed = discord.Embed(
                title=f"{context.message.author.display_name} wants to kill {User.display_name}",
                description="",
                color=0x42F56C
            )
            embed.set_image(url=response['url'])
            await context.message.delete()
            await context.send(embed=embed)

    @commands.command(name="hug")
    async def hug(self, context, User:discord.User):
        """
        hugs another user
        """

        url = "https://api.waifu.pics/sfw/hug"
        # Async HTTP request
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            embed = discord.Embed(
                title=f"{context.message.author.display_name} hugs {User.display_name}",
                description="",
                color=0x42F56C
            )
            embed.set_image(url=response['url'])
            await context.message.delete()
            await context.send(embed=embed)

    @commands.command(name="kick")
    async def kick(self, context, User:discord.User):
        """
        kicks another user
        """

        url = "https://api.waifu.pics/sfw/kick"
        # Async HTTP request
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            embed = discord.Embed(
                title=f"{context.message.author.display_name} kicks {User.display_name}",
                description="",
                color=0x42F56C
            )
            embed.set_image(url=response['url'])
            await context.message.delete()
            await context.send(embed=embed)

    @commands.command(name="pat")
    async def pat(self, context, User:discord.User):
        """
        pats another user
        """

        url = "https://api.waifu.pics/sfw/pat"
        # Async HTTP request
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            embed = discord.Embed(
                title=f"{context.message.author.display_name} pats {User.display_name}",
                description="",
                color=0x42F56C
            )
            embed.set_image(url=response['url'])
            await context.message.delete()
            await context.send(embed=embed)


# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
def setup(bot):
    bot.add_cog(apis(bot))
