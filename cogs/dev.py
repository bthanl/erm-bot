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
        #only set set user execute reload command
        if(ctx.author.id != 164515512544395264):
            return

        #clear screen with ansi code
        print("\033[H\033[J", end="")
        
        filesOld = self.files
        filesNew = dev.getCogs()
        failed = list()

        for filename in filesOld:
            if filename.endswith(".py"):
                try:
                    await self.bot.unload_extension("cogs." + filename[:-3])
                    print("unloaded", filename)
                except:
                    pass

        print()

        #always load this file first in case of other file failure
        await self.bot.load_extension("cogs.dev")
        print("loaded", "dev.py")
        print()

        for filename in filesNew:
            if filename.endswith(".py"):
                # cut off the .py from the file name
                try:
                    if(filename == "dev.py"):
                        continue
                    await self.bot.load_extension("cogs." + filename[:-3])
                    print("loaded", filename)

                except:
                    print("\033[91mcouldnt load " + filename + "\033[0m")
                    failed.append(filename)


        print("\nfinished reloading")
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