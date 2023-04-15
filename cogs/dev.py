from discord.ext import commands
import os

class dev(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.files = dev.getCogs()

    def getCogs():
        files = list()
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                files.append(filename)
        return files

    @commands.command()
    async def reload(self, ctx):
        if(ctx.author.id != 164515512544395264):
            return

        filesOld = self.files
        filesNew = dev.getCogs()

        for filename in filesOld:
            if filename.endswith(".py"):
                await self.bot.unload_extension(f"cogs.{filename[:-3]}")
                print("unloaded", filename)

        for filename in filesNew:
            if filename.endswith(".py"):
                # cut off the .py from the file name
                await self.bot.load_extension(f"cogs.{filename[:-3]}")
                print("loaded", filename)

        print("finished reloading")
        diff = len(filesNew) - len(filesOld)
        if(diff >= 0):
            print("added", diff, "new cog(s)")
        else:
            print("removed", diff * -1, "cog(s)")

        await ctx.send("oge")
            
    @commands.command()
    async def exec(self, ctx):
        if(ctx.channel.id != 1088726019600564255):
            return
        
        exec(str(ctx.message.content[9:]))

async def setup(bot):
    await bot.add_cog(dev(bot))