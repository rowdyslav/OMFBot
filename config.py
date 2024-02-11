from json import load
from os import environ

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = environ["BOT_TOKEN"]

YOOKASSA_KEY = environ["YOOKASSA_TOKEN"]

RCON_IP = environ["RCON_IP"]
RCON_PORT = int(environ["RCON_PORT"])
RCON_PASSWORD = environ["RCON_PASSWORD"]

with open("prices.json", "r", encoding="UTF-8") as f:
    PRICES = load(f)
