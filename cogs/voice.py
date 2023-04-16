from cogs.libs import YTDL
from cogs.libs import player
from discord.ext import commands
import discord
import os
import asyncio
from fuzzywuzzy import fuzz

class voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #add queue
    #support for spotify
    #api probaly
    #steal playlist
    #search on yt 
    #low elo

    @commands.command()
    async def join(self, ctx):
        await player.ensureVoice(ctx, True)

    @commands.command()
    async def play(self, ctx, *, url):
        if not await player.ensureVoice(ctx):
            return

        '''
        if(ctx.voice_client.is_paused()):
            ctx.voice_client.resume()
            await ctx.send("resuming....")
        '''

        if fuzz.ratio(url, "demondice") >= 90 or fuzz.ratio(url, "mori calliope") >= 90:
            await ctx.send("ill kill you")
            return

        source = await YTDL.YTDLSource.from_url(url, loop = self.bot.loop, stream = False)

        title = (source.title).lower()
        desc = (source.data.get("description")).lower()
        #top 5 lines of code of all time
        if("demondice" in title or
                "demondice" in desc or
                "mori calliope" in title or
                "mori calliope" in desc or
                "moricalliope" in title or
                "moricalliope" in desc):
            await ctx.send("ill kill you")
            return

        ctx.voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)
        
        await ctx.send(f'im playig ummm ermmmm... {source.title}')
        print("playing:", source.title)

        #potentially high elo
        #unless they pause lol all good tho
        await asyncio.sleep(source.data.get("duration") + 10)
        os.remove("temp/" + str(source.data.get("id")) + "." + str(source.data.get("ext")))


    @commands.command()
    async def stop(self, ctx):
        if ctx.voice_client.is_playing():
            await ctx.send("ogey")
            ctx.voice_client.stop()
        else:
            await ctx.send("erm im not playing anything...")

    @commands.command(aliases = ["unpause"])
    async def pause(self, ctx):
        if(ctx.voice_client.is_paused()):
            ctx.voice_client.resume()
            await ctx.send("resuming....")
        else:
            ctx.voice_client.pause()
            await ctx.send("ermm i paused...")

    @commands.command()
    async def loop(self, ctx):
        await ctx.send("low elo bot sorry cant loop :joy::joy::joy:")

    @commands.command()
    async def leave(self, ctx):
        if ctx.voice_client is not None:
            ctx.voice_client.stop()
            await ctx.voice_client.disconnect()
            await ctx.send("ogey bye")
        else:
            await ctx.send("i think youre schizophrenic....")

    '''
    @commands.Cog.listener()
    async def on_voice_state_update(member, prev, after):
        #if someone joined
        after.channel is not None:
            return

        #if bot was moved to own channel
        if member == self.bot.user:

        #if ther are 0 or 2 or more users
        if len(member.voice.channel.members) >= 2 or len(member.voice.channel.members) == 0:
            return

        #only the bot in channel
        if len(member) == self.bot.user:
            print("ayo")
            #asyncio.sleep(300)

    async def timer(member):
        try:
            asyncio.sleep(300)
        except:
            raise
        finally:
    '''

async def setup(bot):
    await bot.add_cog(voice(bot))
