# importing libs
import disnake
from disnake.ext import commands
from config import settings
import os

# setting up discord bot client
bot = commands.InteractionBot(intents=disnake.Intents().all())

# logging about starting bot
@bot.event
async def on_ready():
    print("bot ready")

#loading cogs from folder
list_cogs = []
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension("cogs." + filename[:-3])
        list_cogs.append(filename[:-3])

# run bot
bot.run(settings['token'])
