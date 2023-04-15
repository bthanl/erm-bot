from discord.ext import commands
from apiKeys import apiKeys
import random
import openai

openai.api_key = apiKeys.openAI_key

class chat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.content == 'erm...':
            await message.channel.send("<:erm:1071525603402063894>")

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

    @commands.command(aliases = ["gptb"])
    async def gpt(self, ctx, *, p):
        async with ctx.typing():
            try:
                completion = openai.Completion.create(model="text-davinci-003",prompt=p,temperature=1,max_tokens=2100)
                await ctx.send(completion.choices[0].text)
            except BaseException as e:
                await ctx.send(e)
                await ctx.send("**if it says something abtou \"Connection aborted\" or \"400 Bad Request\" just try again lol**")
        
    

async def setup(bot):
    await bot.add_cog(chat(bot))
