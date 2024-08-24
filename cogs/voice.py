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
        lastMsg = ""
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
    async def ye(self, ctx, *, args):
        await voice.play(self, ctx, url="kanye "+args)

    @commands.command()
    async def play(self, ctx, *, url):
        await ctx.send("youtube doesnt work my bad gangy wangy")
        #return

        if not await player.ensureVoice(ctx):
            return
        ctx.voice_client.stop()
        '''
        if(ctx.voice_client.is_paused()):
            ctx.voice_client.resume()
            await ctx.send("resuming....")
        '''

        if fuzz.ratio(url, "demondice") >= 90 or fuzz.ratio(url, "mori calliope") >= 90:
            await ctx.send("ill kill you")
            return

        async with ctx.typing():
            source = await YTDL.YTDLSource.from_url(url, loop = self.bot.loop, stream = False)

            #try cus not all sources have title and descriptions
            try:
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
            except:
                pass
            
            ctx.voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)
            
            await ctx.send(f'im playig ummm ermmmm... {source.title}')
            print("playing:", source.title)

        #potentially high elo
        #unless they pause lol all good tho
        await asyncio.sleep(source.data.get("duration") + 10)
        os.remove("temp/" + str(source.data.get("id")) + "." + str(source.data.get("ext")))


    @commands.command(aliases = ["skip"])
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

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        #if(self.)
        
        if len(before.channel.members) != 1:
            return

        #only the bot in channel
        if before.channel.members[0] == self.bot.user:
            #await ctx.voice_client.disconnect()
            #print(dir(self.bot))
            await self.bot.voice_clients[0].disconnect()
            #ctx.send
        
async def setup(bot):
    await bot.add_cog(voice(bot))
