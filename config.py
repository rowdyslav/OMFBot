from json import load
from os import environ

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = environ["BOT_TOKEN"]

YOOKASSA_KEY = environ["YOOKASSA_KEY"]
YOOKASSA_SHOP_ID = environ["YOOKASSA_SHOP_ID"]

RCON_IP = environ["RCON_IP"]
RCON_PASSWORD = environ["RCON_PASSWORD"]

with open("prices.json", "r") as f:
    PRICES = load(f)
