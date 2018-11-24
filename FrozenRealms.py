import time
import discord
import asyncio
import discord.ext.commands as commands
import os

client = discord.Client()

@client.event
async def on_ready():
    print("Bot is up and running")
    print("Logged in as:")
    print(client.user.name)
    print(client.user.id)
    print("-----")
    game = discord.Game("-help | frozenrealms.pw")
    await client.change_presence(status=discord.Status.idle, activity=game)

@client.event
async def on_message(message):
    guild = client.get_guild(444656646367608846)
    channel = message.channel
    if message.author == client.user:
        return
    if message.content.startswith("-help"):
        userID = message.author.id
        await channel.send("<@%s>, here is the list of commands:\n-help | Shows list of all commands\n-ip | Gives you the ip of the server\n-trailer | Gives you the link of the server trailer\n-download | Gives you the download link of the server trailer" % (userID))

    if message.content.startswith("-ip"):
        userID = message.author.id
        await channel.send("<@%s>, frozenrealms.pw" % (userID))

    if message.content.startswith("-trailer"):
        userID = message.author.id
        await channel.send("<@%s>, https://youtu.be/1nJDJOzx0zY" % (userID))

    if message.content.startswith("-download"):
        userID = message.author.id
        await channel.send("<@%s>, https://www.dropbox.com/l/scl/AABBhtN0XTRzvNVGU4U8_UfLk0zz4EgueMM" % (userID))

    #if message.content.startswith("-x-code9923452312312178367561236786512messageeveryone"):
     #   for member in guild.members:
      #      try:
       #         await member.send("Hey you!\n**FrozenRealms** is releasing *this* sunday *11:30AM EST*\nTell all your friends to be on for SOTW, we will be running events, KoTHs and we will also do a Key All!")
        #    except:
         #       pass

client.run(os.getenv("token"))
