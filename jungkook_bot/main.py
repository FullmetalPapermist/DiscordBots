import discord
from discord.ext import commands
client = commands.Bot(command_prefix="(#>O<#)")


@client.event
async def is_ready():
    print("Prepare yourselves")


@client.command()
async def greetings(ctx):
    await ctx.send("")