import discord 
from discord.ext import commands



class Error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error,commands.CommandNotFound):
            return
        if isinstance(error,commands.CheckFailure):
            await ctx.send(error)
        else:
            print(error)



def setup(bot):
  bot.add_cog(Error(bot))        