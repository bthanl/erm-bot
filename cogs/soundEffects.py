from discord.ext import commands
from cogs.libs import player

class soundEffects(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    '''
    @commands.Cog.listener()
    async def on_message(self, message):
        if(message.content[:4] != "erm "):
            return

        match message.content[4:]:
            case "feet":
                file = "mmfeet.mp3"
                msg = "mmm..... feet"
            case _:
                return

        await player.playSound(message, "audio/boowomp.mp3", "boowomp")
        lol = await (message.author.voice.channel).connect()
        lol.play(discord.FFmpegPCMAudio("audio/mmfeet.mp3"))
    '''

    #implement per-server sound effects + comamnd to add sounds?

    @commands.command()
    async def feet(self, ctx):
        await player.playSound(ctx, "audio/mmfeet.mp3", "mmm..... feet")

    @commands.command()
    async def boowomp(self, ctx):
        await player.playSound(ctx, "audio/boowomp.mp3", "boowomp")

    @commands.command()
    async def steel(self, ctx, *, sting):
        if sting == "sting":
            await player.playSound(ctx, "audio/steelsting.mp3", "booooooooooooooooo doooooo-doooooooooooooooooooooooooooo")

    @commands.command()
    async def lamb(self, ctx, *, sauce):
        if sauce == "sauce":
            await player.playSound(ctx, "audio/lambsauce.mp3", "eeEeeeeEEEEeEeEeeEeeEEEeeeeEeeEEeeee")

    @commands.command()
    async def huh(self, ctx):
        await player.playSound(ctx, "audio/huh.mp3", ":scream:")

    @commands.command()
    async def sus(self, ctx):
        await player.playSound(ctx, "audio/sus.mp3", ":eyes:")

    @commands.command()
    async def nerd(self, ctx):
        await player.playSound(ctx, "audio/nerd.mp3", ":nerd:")

    @commands.command()
    async def you(self, ctx, *, args):
        if(args == "are black"):
            await player.playSound(ctx, "audio/black.mp3", ":monkey: :woman_gesturing_no:")

async def setup(bot):
    await bot.add_cog(soundEffects(bot))
