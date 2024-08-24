from discord.ext import commands
from apiKeys import apiKeys
import random

class chat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.content == 'erm...':
            await message.channel.send("<:erm:1098821385914167427>")

        if self.bot.user.mentioned_in(message):
            await message.channel.send('hiii...')
            await message.channel.send('<a:mumeishy:990103420243443773>')

    @commands.command(aliases=['is'])
    async def _is(self, ctx, *, balls):
        if balls != "it a beast or a burger angle" and balls != "is it a burger or a beast angle":
            return

        match random.randint(0, 1):
            case 0:
                await ctx.send("its a beast angle for today i think")
            case 1:
                await ctx.send("its a burger angle 100 eprc on my momma")

    @commands.command()
    async def what(self, ctx, *, args):
        await ctx.send(args.replace('the', '').strip() + '??!?!?')

async def setup(bot):
    await bot.add_cog(chat(bot))
