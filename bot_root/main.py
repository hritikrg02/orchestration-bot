# file:         main.py
# description:  contains the main implementation for the bot.
# author:       Hritik "Ricky" Saynganthone | hritikrg02@gmail.com

import discord
from discord.ext import commands
from loguru import logger
from glob import glob
from io import BytesIO
from PIL import Image

from utils import get_token, create_bird_image

# constants

TOKEN_FILE = "bot_root/token.txt"
TOKEN = get_token(TOKEN_FILE)

CHANNEL_IDS = [1223003631293431851]

# discord stuff

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="$", intents=intents)


@bot.event
async def on_ready():
    logger.success(f"Log on successful as {bot.user}.")


@bot.event
async def on_message(message):
    if message.channel.id in CHANNEL_IDS:
        if "tion" in message.content:
            logger.info(f"Triggered bird creation on: {message.content}")
            bird = create_bird_image("test")

            buffer = BytesIO()
            bird.save(buffer, format="JPEG")
            buffer.seek(0)

            f = discord.File(buffer, filename="composite.jpg")
            await message.channel.send(file=f)
            logger.success(f"Bird sent.")


bot.run(TOKEN)
