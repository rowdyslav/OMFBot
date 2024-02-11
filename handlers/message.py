from aiogram import Bot
from aiogram.types import LabeledPrice, Message

from config import PRICES
from keyboards.products import PRODUCTS_KEYBOARD

products_titles = [x[0] for x in PRODUCTS_KEYBOARD]


async def start(message: Message):
    await message.answer(
        "Выберите товар и я отправлю вам ссылку для оплаты.",
        reply_markup=PRODUCTS_KEYBOARD,
    )


async def some_message(message: Message, bot: Bot):
    if not message.text in products_titles:
        await message.reply("Извините, но я не знаю как ответить на такое сообщение.")
        return

    title = message.text
    user = message.from_user
    assert user != None
    await bot.send_invoice(
        chat_id=user.id,
        title=title,
        description="Описание",
        payload=title,
        provider_token="381764678:TEST:77850",
        currency="RUB",
        prices=[LabeledPrice(label="Лейбл", amount=PRICES[title] * 100)],
        need_name=True,
    )
