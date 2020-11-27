# bestbot.py
#import os
#
#import discord
#from dotenv import load_dotenv

#load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')

#client = discord.Client()

#@client.event
#async def on_ready():
#    print(f'{client.user} has connected to Discord!')

#client.run(TOKEN)

import discord
from discord.ext import commands 
import random
import time
from datetime import datetime

client = commands.Bot(command_prefix = '.') #prefix is .

@client.event 
async def on_ready(): #when the bot first boots up online it will say hi
    general_channel = client.get_channel(761659292716892160)
    await general_channel.send('I hopped online')
    print('Bot is Ready.')

@client.event
async def on_message(message):

    if message.content == '.random':
         general_channel = client.get_channel(761659292716892160)
         RandintEmbed = discord.Embed(title="Random Number", description="Chooses a random number between 1 and 10", color=0xff0000)
         RandintEmbed.add_field(name="It is...", value=random.randint(1,10), inline=False)

         await general_channel.send(embed=RandintEmbed)

    await client.process_commands(message)
         


@client.command(name="randint") #gives you a random number between 1 and 10
async def randint(ctx):
         
    RandintEmbed = discord.Embed(title="Random Number", description="Chooses a random number between 1 and 10", color=0xff0000)
    RandintEmbed.add_field(name="It is...", value=random.randint(1,10), inline=False)

    await ctx.send(embed=RandintEmbed)

@client.command()
async def ping(ctx): #determines your ping

    PingEmbed = discord.Embed(title="Ping", description="What is your ping???", color=0xd35400)
    PingEmbed.add_field(name="Your ping is...", value=f'Pong! {round(client.latency*1000)}ms', inline=True)

    await ctx.send(embed=PingEmbed)

@client.command()
async def localtime(ctx):
    seconds=time.time()
    local_time = time.ctime(seconds)
    result = time.localtime(seconds)
    
    TimeEmbed = discord.Embed(title="Time", description="Local", color=0x58d68d)
    TimeEmbed.add_field(name="Year", value=result.tm_year, inline=True)
    TimeEmbed.add_field(name="Month", value=result.tm_mon, inline=True)
    TimeEmbed.add_field(name="Day of the Month", value=result.tm_mday, inline=True)
    TimeEmbed.add_field(name="Day of the Week", value=result.tm_wday, inline=True)
    TimeEmbed.add_field(name="Hour", value=result.tm_hour, inline=True)
    TimeEmbed.add_field(name="Minute", value=result.tm_min, inline=True)
    TimeEmbed.add_field(name="Second", value=result.tm_sec, inline=True)
    TimeEmbed.set_footer(text=local_time)
    
    await ctx.send(embed=TimeEmbed)

@client.command() #this command will give UTC time 
async def utc(ctx):
    seconds=time.time()
    local_time = time.gmtime(seconds)
    result = time.gmtime(seconds)
    
    TimeEmbed = discord.Embed(title="Time", description="Local", color=0x58d68d) #making a discord embed
    TimeEmbed.add_field(name="Year", value=result.tm_year, inline=True) #what year
    TimeEmbed.add_field(name="Month", value=result.tm_mon, inline=True) #what month
    TimeEmbed.add_field(name="Day of the Month", value=result.tm_mday, inline=True) #what day of the month
    TimeEmbed.add_field(name="Day of the Week", value=result.tm_wday, inline=True) # what day of the week
    TimeEmbed.add_field(name="Hour", value=result.tm_hour, inline=True) # what hour
    TimeEmbed.add_field(name="Minute", value=result.tm_min, inline=True) #what minute
    TimeEmbed.add_field(name="Second", value=result.tm_sec, inline=True) #what second
    
    await ctx.send(embed=TimeEmbed) #send embed when command is typed

@client.command()
async def rhea(ctx):

    await ctx.send(file=discord.File(""))
    




client.run('NzgxNjMzNTUyODkwNDYyMjA4.X8Ae-Q.c1lIrSLYqWk_blOeQ-nsJt5vgu0')



