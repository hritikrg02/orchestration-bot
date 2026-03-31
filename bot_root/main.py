# file:         main.py
# description:  contains the main implementation for the bot.
# author:       Hritik "Ricky" Saynganthone | hritikrg02@gmail.com

import discord
from discord.ext import commands
from loguru import logger
from glob import glob
from io import BytesIO
from PIL import Image

from utils import get_token

# constants

TOKEN_FILE = "bot_root/token.txt"
TOKEN = get_token(TOKEN_FILE)

# discord stuff

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    logger.success(f"Log on successful as {bot.user}.")

bot.run(TOKEN)
