import discord

async def playSound(ctx, fileName, arg):
    if (not await ensureVoice(ctx)):
        return

    async with ctx.typing():
        '''
        if(ctx.voice_client.is_playing()):
            ctx.voice_client.pause()
        '''
        ctx.voice_client.play(discord.FFmpegPCMAudio(fileName))
    await ctx.send(arg)

async def ensureVoice(ctx, join = False):
    if ctx.voice_client is None:
        if ctx.author.voice:
            await ctx.author.voice.channel.connect()
            await ctx.send("hiiii :heart_eyes:")
        else:
            await ctx.send("ermmmmm... join a voice channel first....")
            return False
    elif ctx.voice_client is not None:
        if(join):
            await ctx.send("ermmm im already here.....")
        #else:
            #ctx.voice_client.stop()
    return True