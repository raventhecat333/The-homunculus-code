import discord
import json
import os
import sys
import aiohttp
import asyncio

from discord.ext import commands


# Here we name the cog and create a new class for the cog.
class apis(commands.Cog, name="apis"):
    def __init__(self, bot):
        self.bot = bot

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.
    @commands.command(name="nextmcu")
    async def nextmcu(self, context):
        """
        idk
        """

        url = "https://whenisthenextmcufilm.com/api"
        # Async HTTP request
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            embed = discord.Embed(
                title=f"Next {response['type']} is:",
                description=f"{response['title']}",
                color=0x42F56C
            )
            embed.add_field(
            name="Overview",
            value=f"{response['overview']}"
            )
            embed.add_field(
            name="Days until:",
            value=f"{response['days_until']}"
            )
            embed.set_image(url=response['poster_url'])
            await context.send(embed=embed)

    @commands.command(name="bitcoin")
    async def bitcoin(self, context):
        """
        Get the current price of bitcoin.
        """
        url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
        # Async HTTP request
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            embed = discord.Embed(
                title=":information_source: Info",
                description=f"Bitcoin price is: ${response['bpi']['USD']['rate']}",
                color=0x42F56C
            )
            await context.send(embed=embed)
    @commands.command(name="doesnotexist")
    async def doesnotexist(self, context, args):
        """
        this object does not exist
        """
        if args == "help":
            await context.send('valid args are "artwork, person, cat"')
        else:
            url = f"https://this{args}doesnotexist.com"
            embed = discord.Embed(
                title="",
                description="",
                color=0x42F56C
            )
            embed.set_image(url=url)
            await context.send(embed=embed)

    @commands.command(name="QRify")
    async def QRify(self, context, url):
        """
        create a qr code based on the string given
        """
        embed = discord.Embed(
        title=f"QR code for {url}",
            description="",
            color=0x42F56C
        )
        embed.set_image(url=f"https://chart.googleapis.com/chart?chs=300x300&cht=qr&chl={url}")
        embed.set_footer(
            text=f"Requested by {context.message.author}"
        )
        await context.send(embed=embed)

    @commands.command(name="waifu")
    async def waifu(self, context, args):
        """
        Get anime images, idk
        """
        if args != "help":
            url = f"https://api.waifu.pics/sfw/{args}"
            # Async HTTP request
            async with aiohttp.ClientSession() as session:
                raw_response = await session.get(url)
                response = await raw_response.text()
                response = json.loads(response)
                embed = discord.Embed(
                    title="",
                    description="",
                    color=0x42F56C
                )
                embed.set_image(url=response['url'])
                await context.send(embed=embed)
        elif args == "shinobu":
            context.send("this cat is disabled")
        else:
            url = "https://api.waifu.pics/endpoints"
            # Async HTTP request
            async with aiohttp.ClientSession() as session:
                raw_response = await session.get(url)
                response = await raw_response.text()
                response = json.loads(response)
                embed = discord.Embed(
                    title="Valid categories are:",
                    description=f"{response['sfw']}",
                    color=0x42F56C
                )
                await context.send(embed=embed)
# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
def setup(bot):
    bot.add_cog(apis(bot))
