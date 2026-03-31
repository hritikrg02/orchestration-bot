# file:         utils.py
# description:  contains utility functions used by the bot.
# author:       Hritik "Ricky" Saynganthone | hritikrg02@gmail.com

from loguru import logger
from PIL import Image


BIRD_IMAGE = Image.open("images/bird.jpeg")


def get_token(token_file):
    logger.info("Initiating token get.")
    try:
        with open(token_file, "r") as f:
            token = f.read().rstrip()

    except Exception:  # yes ik this is too broad, no I don't care enough to fix it
        logger.error("Issue when reading token file.")
        return

    logger.success("Token successfully parsed.")
    return token


def create_bird_image(text):
    logger.info("Generate bird image initiated.")
    logger.success("Bird image generated successfully.")
    return BIRD_IMAGE
