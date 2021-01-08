import discord
from discord.ext import commands
client = commands.Bot(command_prefix="(#>O<#)")


@client.event
async def is_ready():
    print("Prepare yourselves")


@client.command()
async def greetings(ctx):
    await ctx.send("Annyeonghaseyo! (Onions on for Sale!)")


client.run("Nzk2OTE5NTY5NTQwMzE3MTg0.X_e7Lw.qBspeNIT1kL0H47dlAVy3GXKtfI")