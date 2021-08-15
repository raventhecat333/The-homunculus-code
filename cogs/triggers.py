import discord
import asyncio
import json
import os
import sys

from discord.ext import commands

# Only if you want to use variables that are in the config.json file.
if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)


# Here we name the cog and create a new class for the cog.
class triggers(commands.Cog, name="triggers"):
    def __init__(self, bot):
        self.bot = bot

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.
    @commands.Cog.listener()
    async def on_message(self, message):
    if message.content == "hello":
        await message.channel.send(f"hello {message.author}")

# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
def setup(bot):
    bot.add_cog(triggers(bot))
