import discord
import os
from discord.ext import commands
client = commands.Bot(command_prefix="*_*")


@client.command()
async def hello(ctx):
    await ctx.send("Annyeonghaseyo! (Onions on Sale!)")

print("Running client")
client.run(os.environ["DISCORD_TOKEN"])
