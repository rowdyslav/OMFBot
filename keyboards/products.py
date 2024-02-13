from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from config import PRICES

PRODUCTS_KEYBOARD = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text=x) for x in PRICES]], resize_keyboard=True
)
