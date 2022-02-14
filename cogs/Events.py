import discord
from discord.ext import commands

class Event(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  # @cog.listener()
  # async def on_ready(self):
    


def setup(bot):
  bot.add_cog(Event(bot))