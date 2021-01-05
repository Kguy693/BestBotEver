from discord.ext import tasks, commands
import lavalink
from discord import utils
from discord import Embed
import random
import discord
import asyncio

values = []
class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rhea(self, ctx):
        
        images = ["magik.png", "magik1.jpg", "pfp1.jpg"]

        randomimage = random.choice(images)

        await ctx.send(file=discord.File(randomimage))

    @commands.command()
    async def avatar(self, ctx, *,  avamember : discord.Member=None):
        userAvatarUrl = avamember.avatar_url
        await ctx.send(userAvatarUrl)
        await ctx.send('ExPoSeD')

    @commands.command()
    async def dm(self, ctx, *, dms):
        await ctx.author.send(dms)
    @commands.command()
    async def poll(self, ctx, hello, *args):
                '''Add your question and then the options'''
                global values
                values.clear()
                argslist = list(args)
                for i in argslist:
                    s=args.index(i)
                    y=s+1
                    values.append(f"{y} : {i}")

                

                if len(argslist) > 5:
                    await ctx.send('Too many choices to poll')
                    return

                
                mbed = discord.Embed(title=hello)
                mbed.description = '\n'.join(values)
                if len(argslist) < 1:
                    mbed.description = '1️⃣ for Yes   2️⃣ for No'
                message = await ctx.send(embed=mbed)

                if len(argslist) < 1:
                    await message.add_reaction('1️⃣')
                    await message.add_reaction('2️⃣')
                if len(argslist) == 1:
                    await ctx.send("You win now SpAm")
                    await message.add_reaction('1️⃣')
                if len(argslist) == 2:
                    await message.add_reaction('1️⃣')
                    await message.add_reaction('2️⃣')
                
                if len(argslist) == 3:
                    await message.add_reaction('1️⃣')
                    await message.add_reaction('2️⃣')
                    await message.add_reaction('3️⃣')
                if len(argslist) == 4:
                    await message.add_reaction('1️⃣')
                    await message.add_reaction('2️⃣')
                    await message.add_reaction('3️⃣')
                    await message.add_reaction('4️⃣')

                if len(argslist) == 5:
                    await message.add_reaction('1️⃣')
                    await message.add_reaction('2️⃣')
                    await message.add_reaction('3️⃣')
                    await message.add_reaction('4️⃣')
                    await message.add_reaction('5️⃣')
 
    

    


def setup(client):
    client.add_cog(Misc(client))