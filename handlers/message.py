from aiogram.types import LabeledPrice, Message
from icecream import ic

import config
from bot import BOT
from keyboards.products import PRODUCTS_KEYBOARD

products_titles = [
    button.text for button in [keyboard for _, keyboard in PRODUCTS_KEYBOARD][0][0]
]


async def start(message: Message):
    await BOT.send_message(
        chat_id=message.chat.id,
        text="Выберите товар и я отправлю вам ссылку для оплаты.",
        reply_markup=PRODUCTS_KEYBOARD,
    )


async def some_message(message: Message):
    user = message.from_user
    if not user:
        return
    if not message.text in products_titles:
        await message.reply("Извините, но я не знаю как ответить на такое сообщение.")
        return

    title = message.text
    assert title
    await BOT.send_invoice(
        chat_id=user.id,
        title=title,
        description="Описание",
        payload=title,
        provider_token=config.YOOKASSA_KEY,
        currency="RUB",
        prices=[LabeledPrice(label="Лейбл", amount=config.PRICES[title] * 100)],
        need_name=True,
    )
