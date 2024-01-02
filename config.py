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
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "6555075797").split())

    # session name
    TG_USER_SESSION_NAME = os.environ.get("TG_USER_SESSION_NAME", "angrah")

    # tg user session string
    TG_USER_SESSION_STRING = os.environ.get("TG_USER_SESSION_STRING", "BQFeDrAAiMV8uj--Q3mOBcvgzo8MlmZsm4HaJnexUvbxnBvfO8gvCSgOYZCuHxen-jlId6kFX71E9fxJT6dvYGuhXAwYks4DN-qp_MH5rebgIy1Jag5a87ZR8OGrnl2bDh7sCRB8Hmi1Q20T5f6co_3xyAPOIo7MjfuPOFzMEn6QwRwr6OnrT4pX0weXqoBpCF-5M4gug1YcjJ1V4Wf0XqrETHZM9OPgMVqF7GOre23gXlL_ONvwS0TfwaQuksLtRjupj_5OYjUgd09VvcdD26PaaEuHBNEF6x443LXX4QeMH0lBKZXddOJM9hrsBdqzMkO-1nMSCorVm7A9wfoCKBkLK1NTCQAAAAGGtoTVAA")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
