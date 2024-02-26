from aiogram import Bot, F
from aiogram.types import Message, PreCheckoutQuery
from icecream import ic
from mcrcon import MCRcon

import config


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    ic("pre_checkout_query")
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def success_payment(message: Message):
    ic("success_payment")
    with MCRcon(config.RCON_IP, config.RCON_PASSWORD, config.RCON_PORT) as rcon:
        pay = message.successful_payment
        assert pay
        info = pay.order_info
        assert info
        rcon.command(f"whitelist add {info.name}")
