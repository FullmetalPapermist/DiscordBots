import discord
import os
import random
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="_", intents=intents)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



@client.command()
async def hello(ctx):
    await ctx.send("Annyeonghaseyo! (Onions on Sale!)")
    print()


@client.command()
async def fantasy(ctx):
    names = list()
    for user in ctx.guild.members:
        names.append(user.name)
    names.remove("Jungkook Bot")
    random.shuffle(names)
    create_simple_fantasy(names[0])

@client.command()
async def fanfic(ctx, name):
    # Write custom fanfics here as strings, in a list

    # the structure should be:f'fanfiction{name}fanfiction',
    fanfic = [f'{name} hopelessly fell for Jungkook.', f'Jungkook took {name} on a date to the beach.']
    random.shuffle(fanfic)
    await ctx.send(fanfic[0])


def create_simple_fantasy(name):
    verbs = ['went', 'kissed', 'felt', 'fell', 'loved']
    random.shuffle(verbs)
    return 'Jungkook' + name + verbs[0]


print("Running client")
client.run(os.environ["DISCORD_TOKEN"])
