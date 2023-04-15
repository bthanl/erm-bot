from discord.ext import commands

currentChannel = 0

class meirl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if(message.channel.id != 1088099933372026982):
            return

        global currentChannel

        if message.content.startswith("!"):
            currentChannel = int(message.content[1:])
            print("new channel", currentChannel)
            return

        ch = self.bot.get_channel(currentChannel)

        await ch.send(message.content)

async def setup(bot):
    await bot.add_cog(meirl(bot))
