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
        #self.waiting = asyncio.task_create(lambda duration: waitForEnd(duration))

    #dict of server ids to keep seperate queues for every server
    #init new class for every server instance to enable use of self.queue or similar?
    serverQueues = dict()


    #add queue
    #support for spotify
    #api shittery probaly
    #steal playlist
    #search on yt 
    #low elo

    async def waitForEnd(duration):
        try:
            await asyncio.sleep(duration)
        except asyncio.CancelledError:
            pass
        finally:
            pass

    @commands.command()
    async def join(self, ctx):
        await player.ensureVoice(ctx, True)

    @commands.command()
    async def skip(self, ctx):


        waiting.cancel()

        await ctx.send("low elo bot cant skip cope")
        return
        '''
        if len(self.queue) != 0:
            ctx.voice_client.stop()
            waiting.cancel()
            await ctx.send("skipped " + self.queue[0])
        else:
            await ctx.send("erm... thres nothing to skip to...")
        '''


    @commands.command()
    async def np(self, ctx):
        if(not ctx.voice_client.is_playing()):
            await ctx.send("ermm.. nothign is playuibg..")
        await ctx.send("ermm.. im playing " + self.np)

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
        
        self.queue.append(url)

        if(ctx.voice_client.is_playing()):
            await ctx.send("queued <" + self.queue[-1] + ">")
            return

        if self.loopPlayerIsStarted == False:
            return

        voice.loopPlayer

    async def playerQueue(self, ctx):
        self.loopPlayerIsStarted = True
        while len(self.queue != 0):
            source = await YTDL.YTDLSource.from_url(self.queue[0], loop = self.bot.loop, stream = False)
            self.queue.pop(0)

            title = (source.title).lower()
            desc = (source.data.get("description")).lower()

            self.np = source.title

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

            
            self.waiting = asyncio.create_task(voice.waitForEnd(source.data.get("duration") + 1))


            waiting.cancel()

            #start waiting
            #await asyncio.sleep(0.1)

            await asyncio.sleep(source.data.get("duration") + 1)
            
            
            #subprocess.run(["cmd", "/c", "del", "/Q", "/S", "temp\*"])


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

    @commands.command(aliases=["queue", "q"])
    async def _queue(self, ctx, *, url = None):
        if url is not None:
            voice.play()
            return
        if len(self.queue) == 0:
            await ctx.send("erm.. queue is empty....")
            return

        output = "```\n"
        for x in range(len(self.queue)):
            output += str(x + 1) + ": " + self.queue[x] + "\n"
        output += "```"

        await ctx.send(output)

    @commands.command()
    async def clear(self, ctx):
        self.queue.clear()
        await ctx.send("cleared the queue")

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
