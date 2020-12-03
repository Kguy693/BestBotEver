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

import asyncio
import os
import discord
from discord.ext import commands 
import random
import time
from datetime import datetime
import dotenv
import hyperlink
from discord import FFmpegPCMAudio
import youtube_dl
from discord.utils import get


players = {}

client = commands.Bot(command_prefix = '.') #prefix is .

@client.event 
async def on_ready(): #when the bot first boots up online it will say hi
    general_channel = client.get_channel(761659292716892160)
    #await general_channel.send('I hopped online')
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
async def randint(ctx, arg1, arg2):

    int(arg1)
    int(arg2)     
    RandintEmbed = discord.Embed(title="Random Number", description="Chooses a random number between 1 and 10", color=0xff0000)
    RandintEmbed.add_field(name="It is...", value=random.randint(arg1, arg2), inline=False)

    await ctx.send(embed=RandintEmbed)

@client.command()
async def ping(ctx): #determines your ping

    PingEmbed = discord.Embed(title="Ping", description="What is your ping???", color=0xd35400)
    PingEmbed.add_field(name="Your ping is...", value=f'Pong! {round(client.latency*1000)}ms', inline=True)

    await ctx.send(embed=PingEmbed)

@client.command()
async def ltc(ctx):
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

url = hyperlink.parse(u"https://github.com/Kguy693/BestBotEver")
@client.command()
async def code(ctx):
    CodeEmbed = discord.Embed(title="Github Repository", description=url.to_text(), color=0x00ff00)

    await ctx.send(embed=CodeEmbed)

@client.command(pass_context=True, aliases=['j', 'joi'])
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"The bot has connected to {channel}\n")

    await ctx.send(f"Joined {channel}")

@client.command(pass_context=True, aliases=['l', 'lea'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"The bot has left {channel}")
        await ctx.send(f"Left {channel}")
    else:
        print("Bot was told to leave voice channel, but was not in one")
        await ctx.send("Don't think I am in a voice channel")

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}
ffmpeg_options = {
    'options': '-vn'
}
 
 
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
 
 
 
 
@client.command(pass_context=True, aliases=['p', 'pla'])
async def play(ctx, url: str):

    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played")
        await ctx.send("ERROR: Music playing")
        return

    await ctx.send("Getting everything ready now")

    voice = get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio now\n")
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    nname = name.rsplit("-", 2)
    await ctx.send(f"Playing: {nname[0]}")
    print("playing\n")

@client.command()
async def reactionpost(ctx):

    ReactionEmbed = discord.Embed(title="Create your reaction post", color=0xcb6ea5)
    ReactionEmbed.set_author(name="BestBot")
    ReactionEmbed.add_field(name="Set Title", value="--reaction_set_title \"new title\"")

    await ctx.send(embed=ReactionEmbed)
    await ctx.message.delete()

@client.command()
async def purge(ctx):
    username1 = ctx.message.author.name
    await ctx.channel.purge(limit=10, check=purge)
    await ctx.send(username1+" deleted 10 messages")


@client.command()
async def spam(ctx, string1):

    await ctx.send((string1+' ')*40)




    




TOKEN = os.getenv('pp123')


client.run('TOKEN')



