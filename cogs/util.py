import os
from dotenv import load_dotenv, dotenv_values 

load_dotenv()

#curl for tenor json
import subprocess

#asyncio.sleep
import asyncio

#parse tenor json
import json

import glob

from discord.ext import commands
import discord

class util(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["h"])
    async def help(self, ctx):
        with open("help.txt") as h:
            msg = h.read()
        await ctx.send(msg)

    @commands.command()
    async def omg(self, ctx, *, url):

        #check if url

        if util.isTenor(url):
            tenorKey = os.getenv("TENOR_KEY")

            #check for tenor key
            if(tenorKey == ""):
                return

            postID = url[-8:] #rng lol
            tenorJson = json.loads(subprocess.check_output("curl -s https://tenor.googleapis.com/v2/posts?key=" + tenorKey + "&media_filter=gif&ids=" + postID))

            #update url to new one
            url = (tenorJson['results'][0]['media_formats']['gif']['url'])

        fileName = await util.cleanUrl(url)

        #if its not jhust get the normal url
        async with ctx.typing():
            subprocess.run("curl -s " + url + " --output temp/" + fileName)
            subprocess.run(["cmd", "/c", "batch\omg.bat " + "temp/" + fileName])
        
            #[:-4] is only valid for ext with 3 chars 
            #eg .png .jpg, but not .webp etc
            await util.uploadAndClearTemp(ctx, fileName[:-4] + "_new.gif")


        print("processed", url)

    @commands.command()
    async def gif(self, ctx, *, url):

        #check if its a real url

        fileName = await util.cleanUrl(url)

        if (util.isTenor(url) or fileName[-4:] == ".gif"):
            await ctx.send("erm... thats already a gif")
            return

        async with ctx.typing():
            subprocess.run("curl -sL " + url + " --output temp/" + fileName)
            subprocess.run(["cmd", "/c", "batch\pngtogif.bat " + "temp/" + fileName])

            #[:-4] is only valid for ext with 3 chars 
            #eg .png .jpg, but not .webp etc
            await util.uploadAndClearTemp(ctx, fileName[:-4] + ".gif")

        print("turned", url, "into gif")

    #delete everythnig in tmep folder after done
    async def uploadAndClearTemp(ctx, fileName):
        await ctx.send(file=discord.File("temp/" + fileName))
        #for low elo internet
        #await asyncio.sleep(10)
        subprocess.run(["cmd", "/c", "del", "/Q", "/S", "temp\*"])

    #return just name and ext of file
    async def cleanUrl(fileName):
        qMarkIndex = None
        lastSlashIndex = -1
        slash = False

        for i in range(0, len(fileName) * -1, -1):
            if fileName[i] == "/" and not slash:
                lastSlashIndex = i
                slash = True
                
                #no need to check befroe last slash for qmarks
                break

            if fileName[i] == "?":
                qMarkIndex = i

        return fileName[lastSlashIndex + 1:qMarkIndex]

    #check if url is a tenor link lol;xd
    def isTenor(url):
        return "tenor.com/".lower() in url

async def setup(bot):
    await bot.add_cog(util(bot))
