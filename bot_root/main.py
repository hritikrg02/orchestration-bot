# file:         main.py
# description:  contains the main implementation for the bot.
# author:       Hritik "Ricky" Saynganthone | hritikrg02@gmail.com

import discord
from discord.ext import commands
from loguru import logger
from glob import glob
from io import BytesIO
from PIL import Image

from utils import get_token, generate_image

# constants

TOKEN_FILE = "bot_root/token.txt"
TOKEN = get_token(TOKEN_FILE)

BASE_IMAGES_DIR = "images/base/"
ACCESSORY_IMAGES_DIR = "images/accessory/"
EXTENSION = "*.png"

COMPOSITE_FILENAME = "composite.png"

BASE_IMAGES = [Image.open(img) for img in glob(f"{BASE_IMAGES_DIR}{EXTENSION}")]
ACCESSORY_IMAGES = [
    Image.open(img) for img in glob(f"{ACCESSORY_IMAGES_DIR}{EXTENSION}")
]

CALLABLE_ROLE = "Board of Directors"

# discord stuff

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    logger.success(f"Log on successful as {bot.user}.")


@bot.command()
async def reset(ctx: discord.ext.commands.Context):
    logger.info("Reset initiated.")

    if ctx.author.top_role.name != CALLABLE_ROLE:
        logger.warning(f"User {ctx.author} does not have role {CALLABLE_ROLE}.")
        return

    # this physically pains me as a programmer to do
    global BASE_IMAGES
    global ACCESSORY_IMAGES

    BASE_IMAGES = [Image.open(img) for img in glob(f"{BASE_IMAGES_DIR}{EXTENSION}")]
    ACCESSORY_IMAGES = [
        Image.open(img) for img in glob(f"{ACCESSORY_IMAGES_DIR}{EXTENSION}")
    ]

    logger.success(f"Image pool has been updated and reset.")


@bot.command()
async def roll(ctx: discord.ext.commands.Context):
    logger.info("Roll initiated.")

    if ctx.author.top_role.name != CALLABLE_ROLE:
        logger.warning(f"User {ctx.author} does not have role {CALLABLE_ROLE}.")
        return

    composite = generate_image(BASE_IMAGES, ACCESSORY_IMAGES)

    buffer = BytesIO()
    composite.save(buffer, format="PNG")
    buffer.seek(0)

    f = discord.File(buffer, filename=COMPOSITE_FILENAME)
    await ctx.channel.send(file=f)
    logger.success(f"File {COMPOSITE_FILENAME} sent.")


bot.run(TOKEN)
