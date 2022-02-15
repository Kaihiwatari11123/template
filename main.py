import discord
import os
from discord.ext import commands
from keep_alive import keep_alive

intents = discord.Intents.all()

class Bot(commands.Bot):
  def __init__(self):
    super().__init__(
      command_prefix = commands.when_mentioned_or(
        "!"
      ), 
      intents = intents, 
      strip_after_prefix = True, 
      owner_ids = {
        724447396066754643
      }, 
      case_insensitive = True, 
      self_bot = False, 
    )
  async def on_ready(self):
    print(f"Logged in as {self.user.name} with id {self.user.id}")

bot = Bot()
TOKEN = os.environ['TOKEN']

for file in os.listdir("./cogs"):
    if file.endswith('.py'):
        bot.load_extension(f'cogs.{file[:-3]}')
bot.load_extension("jishaku")



@bot.command()
@commands.is_owner()
async def load(ctx, cog):
    bot.load_extension(f'cogs.{cog.title()}')
    await ctx.send(f'Loaded {cog.title()}')


@bot.command()
@commands.is_owner()
async def unload(ctx, cog):
    bot.unload_extension(f'cogs.{cog.title()}')
    await ctx.send(f'Unloaded {cog.title()}')


@bot.command()
@commands.is_owner()
async def reload(ctx, cog):
    bot.reload_extension(f"cogs.{cog.title()}")
    await ctx.send(f"{cog.title()} was reloaded")


keep_alive()


bot.run(TOKEN)

