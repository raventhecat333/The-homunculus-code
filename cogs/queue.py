import json
import os
import sys
import discord

from discord.ext import commands
from helpers import json_manager
# Only if you want to use variables that are in the config.json file.
if not os.path.isfile("queue.json"):
    sys.exit("'queue.json' not found! Please add it and try again.")
else:
    with open("queue.json") as file:
        config = json.load(file)


# Here we name the cog and create a new class for the cog.
class queue(commands.Cog, name="queue"):
    def __init__(self, bot):
        self.bot = bot

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.
    @commands.group(name="queue")
    async def queue(self, context):
        """
        Lets you add or remove a user from not being able to use the bot.
        """
        if context.invoked_subcommand is None:
            with open("queue.json") as file:
                queue = json.load(file)
            embed = discord.Embed(
                title=f"There are currently {len(queue['queue'])} items in the queue",
                description=f"{', '.join(str(queue) for queue in queue['queue'])}",
                color=0x0000FF
            )
            await context.send(embed=embed)

    @queue.command(name="add")
    async def queue_add(self, context, args):
        """
        Lets you add a user from not being able to use the bot.
        """
        item = args
        if "1" == "1":
            try:
                with open("queue.json") as file:
                    queue = json.load(file)
                if (item in queue['queue']):
                    embed = discord.Embed(
                        title="Error!",
                        description=f"**{item}** is already in the queue.",
                        color=0xE02B2B
                    )
                    await context.send(embed=embed)
                    return
                json_manager.add_item_to_queue(queue)
                embed = discord.Embed(
                    title="Item added",
                    description=f"**{item}** has been successfully added to the queue",
                    color=0x42F56C
                )
                with open("queue.json") as file:
                    queue = json.load(file)
                embed.set_footer(
                    text=f"There are now {len(queue['queue'])} items in the queue"
                )
                await context.send(embed=embed)
            except:
                embed = discord.Embed(
                    title="Error!",
                    description=f"An unknown error occurred when trying to add **{item}** to the queue.",
                    color=0xE02B2B
                )
                await context.send(embed=embed)



# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
def setup(bot):
    bot.add_cog(queue(bot))
