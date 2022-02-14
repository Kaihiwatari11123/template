import discord 
from discord.ext import commands
from discord.ui import Button, View
from discord.commands import slash_command, Option

class Battle(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @slash_command(guild_ids=[798132349476405268])
  async def battle(self, ctx,
  user: Option(discord.Member, "The Member You want to Battle" )
  ):
    embed = discord.Embed(
      title="Battle Request!",
      description=f"<@{user.id}> You have been challenged for a battle by <@{ctx.author.id}>.",
      color= discord.Color.green()
    )
    await ctx.respond(f"<@{user.id}>",embed=embed)


def setup(bot):
  bot.add_cog(Battle(bot))