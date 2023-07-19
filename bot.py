# This example requires the 'message_content' intent.
import os
import discord
from discord import Intents
from discord.ext import commands
import logging
from dotenv import load_dotenv
import config.bot


#logging
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

#load env variables from .env file
load_dotenv()

intents:  Intents = Intents.default()
intents.message_content = True
cogs: list = ["cogs.tournament","cogs.jansou", "cogs.ReactionRoles"]
#cogs: list = ["cogs.tournament","cogs.jansou"]

class RiichiBot(commands.Bot):

    def __init__(self, command_prefix, intents, cogslist):
        super().__init__(command_prefix=command_prefix,intents=intents)
        self.cogslist = cogslist


bot = RiichiBot(command_prefix=config.bot.PREFIX,intents=intents, cogslist=cogs)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(config.bot.BOT_STATUS))
    for cog in cogs:
        try:
            print(f"Loading cog {cog}")
            await bot.load_extension(cog)
            print(f"Loaded cog {cog}")
        except Exception as e:
            exc = "{}: {}".format(type(e).__name__, e)
            print("Failed to load cog {}\n{}".format(cog, exc))


bot.run(config.bot.DISCORD_TOKEN,log_handler=handler,log_level=logging.DEBUG, reconnect=True)

