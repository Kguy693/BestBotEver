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
import urllib.parse, urllib.request, re
import lavalink
from glob import glob
from pathlib import Path











        



'''class MusicCog(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.client.music = lavalink.Client(self.client.user.id)
        self.client.music.add_node('localhost', 2333, 'youshallnotpass', 'na', 'mynodemusic')
        self.client.add_listener(self.bot.music.voice_update_handler, 'on_socket_response')
        self.client.music.add_event_hook(self.track_hook)

    @commands.command(name="hola")
    async def hi(self, ctx):
        await ctx.send("hi")'''


class Hi939(commands.Cog):
    @commands.command()
    async def nopls(self, ctx):
        await ctx.send('no pls no')

players = {}

client = commands.Bot(command_prefix = '.') #prefix is .

@client.event 
async def on_ready(): #when the bot first boots up online it will say hi
    general_channel = client.get_channel(761659292716892160)
    #await general_channel.send('I hopped online')
    print(f'{client.user} is Ready.')
    client.load_extension('cogs.lavalinkmusic')

reaction_title  = ""
reactions = {}






@client.event 
async def on_ready(): #when the bot first boots up online it will say hi
    general_channel = client.get_channel(761659292716892160)
    #await general_channel.send('I hopped online')
    print(f'{client.user} is Ready.')
    time.sleep(3)
    client.load_extension('cogs.lavalinkmusic')
   
    

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

    arg1 = int(arg1)
    arg2 = int(arg2)     
    RandintEmbed = discord.Embed(title="Random Number", description=f"Chooses a random number between {arg1} and {arg2}", color=0xff0000)
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

url = hyperlink.parse(u"https://github.com/Kguy693/BestBotEver/blob/main/BestBot.py")
@client.command()
async def code(ctx):
    CodeEmbed = discord.Embed(title="Github Repository", description=url.to_text(), color=0x00ff00)

    await ctx.send(embed=CodeEmbed)

'''@client.command(pass_context=True, aliases=['j', 'joi'])
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

    await ctx.send(f"Joined {channel}")'''

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
async def yturl(ctx, url: str):

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
async def ytsearch(ctx, *, query):
    query_string = urllib.parse.urlencode({
        'search_query': query
    })
    htm_content = urllib.request.urlopen(
        'http://www.youtube.com/results?' + query_string
    )
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', htm_content.read().decode())
    print('http://www.youtube.com/watch?v=' + search_results[0])


@client.command()
async def reactionpost(ctx):

    ReactionEmbed = discord.Embed(title="Create your reaction post", color=0xcb6ea5)
    ReactionEmbed.set_author(name="BestBot")
    ReactionEmbed.add_field(name="Set Title", value=".reactionnewtitle \"new title\"", inline=False)
    ReactionEmbed.add_field(name="Add Role", value=".ReactionAddRole @Role Emoji here", inline=False)
    ReactionEmbed.add_field(name="Add Post", value=".ReactionSendPost", inline=False)

    await ctx.send(embed=ReactionEmbed)
    await ctx.message.delete()

@client.command()
async def ReactionNewTitle(ctx, *, thetitle):

    global reaction_title
    reaction_title = thetitle
    
    await ctx.send(f"The title is now `{reaction_title}`")
    await ctx.message.delete()


@client.command(name = "ReactionAddRole")
async def ReactionAddRole(ctx, role: discord.Role, reaction1):

    if role != None:
        reactions[role.name] = reaction1
        await ctx.send(f"Role `{role.name}` has been added with {reaction1}.")
    
    else:
        await ctx.send("Try Again")

@client.command(name = "ReactionRemoveRole")
async def ReactionRemoveRole(ctx, role: discord.Role):
    if role.name in reactions:
        del reactions[role.name]
        await ctx.send(f"Role {role.name} has been successfully deleted.")
    else:
        await ctx.send("That role is not there")

@client.command()
async def ReactionSendPost(ctx):
    description = "React To Add Roles\n"

    for role in reactions:
        description += f'`{role}` - {reactions[role]}\n'

    embed = discord.Embed(title=reaction_title, description=description, color=0xabcdef)
    embed.set_author(name="BestBot")

    await ctx.send(embed=embed)




@client.command()
async def purge(ctx, int2):
    username1 = ctx.message.author.name
    int2 = int(int2)
    await ctx.channel.purge(limit=int2, check=purge)
    message69 = f'{username1} deleted {int2} messages'
    await ctx.send(message69)
    del int2


@client.command()
async def spam(ctx, *, string1):

    await ctx.send((string1+' ')*40)











    



TOKEN = os.getenv('pp123')


client.run('NzgxNjMzNTUyODkwNDYyMjA4.X8Ae-Q.HJx8wFu6KqoCliBwLBcCq56Bzpo')



