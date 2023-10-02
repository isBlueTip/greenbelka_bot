import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    # TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN", default="111:aaa")
    TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN_DEV", default="111:aaa")
