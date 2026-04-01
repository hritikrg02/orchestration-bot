# file:         main.py
# description:  contains the main implementation for the bot.
# author:       Hritik "Ricky" Saynganthone | hritikrg02@gmail.com

import discord
from discord.ext import commands
from loguru import logger
from io import BytesIO

from utils import get_token, create_bird_image

# constants

TOKEN_FILE = "bot_root/token.txt"
TOKEN = get_token(TOKEN_FILE)

CHANNEL_IDS = [673011713750073354]
# CHANNEL_IDS = [673011713750073354, 673010571926568979, 364810641384538116, 521560661642313729, 884198330580742214, 505479223750819840, 431491107394813952, 1012874671806480495, 1284996328635633766]

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
        if "tion" in message.content.lower():
            logger.info(f"Triggered bird creation on: {message.content}")

            text = ""
            words = message.content.split(" ")
            for w in words:
                if "tion" in w.lower():
                    text = f"{w.upper()}!!!"

            bird = create_bird_image(text)

            buffer = BytesIO()
            bird.save(buffer, format="JPEG")
            buffer.seek(0)

            f = discord.File(buffer, filename=f"{text}-bird.jpg")
            await message.channel.send(file=f)
            logger.success(f"Bird sent.")


bot.run(TOKEN)
