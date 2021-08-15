import discord
import json
import os
import sys
import aiohttp
import asyncio

from discord.ext import commands

# Only if you want to use variables that are in the config.json file.
if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)


# Here we name the cog and create a new class for the cog.
class Template(commands.Cog, name="template"):
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


# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
def setup(bot):
    bot.add_cog(Template(bot))
