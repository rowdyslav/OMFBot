from aiogram.types import LabeledPrice, Message

import config
from core import BOT
from keyboards.products import PRODUCTS_KEYBOARD

products_names = list(config.PRICES)


async def start(message: Message):
    await BOT.send_message(
        chat_id=message.chat.id,
        text="Выберите товар и я отправлю вам ссылку для оплаты.",
        reply_markup=PRODUCTS_KEYBOARD,
    )


async def some_message(message: Message):
    user = message.from_user
    if not (user and message.text in products_names):
        return

    product_name = message.text
    assert product_name
    await BOT.send_invoice(
        chat_id=user.id,
        title=product_name,
        description="В дополнительной форме в поле имя указать никнейм на сервере",
        payload=product_name,
        provider_token=config.YOOKASSA_KEY,
        currency="RUB",
        prices=[
            LabeledPrice(label=product_name, amount=config.PRICES[product_name] * 100)
        ],
        need_name=True,
    )
