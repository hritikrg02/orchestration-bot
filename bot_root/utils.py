# file:         utils.py
# description:  contains utility functions used by the bot.
# author:       Hritik "Ricky" Saynganthone | hritikrg02@gmail.com

from loguru import logger
from PIL import Image, ImageDraw, ImageFont


BIRD_IMAGE = Image.open("resources/bird.jpeg")
FONT = ImageFont.truetype("resources/Impact.ttf", 100)


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

    bird_image = BIRD_IMAGE.copy()
    bird_draw = ImageDraw.Draw(bird_image)
    bird_draw.text((0, 0), "DAMN!!!!", font=FONT, fill=(255, 255, 255))

    logger.success("Bird image generated successfully.")
    return bird_image
