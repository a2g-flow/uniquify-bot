import os
import logging


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Config(object):
    # Get a bot token from @botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6987366378:AAHZ5_12fbiJLUDQ7tXV1QUnoUsupy7eQ2Q")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "22941360"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "cd8fb83bbf47a7e373b650bd338ad3d6")

    # Authorized users to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    # session name
    TG_USER_SESSION_NAME = os.environ.get("TG_USER_SESSION_NAME", "angrah")

    # tg user session string
    TG_USER_SESSION_STRING = os.environ.get("TG_USER_SESSION_STRING", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
