from aiogram import Bot
from aiogram.types import Message, PreCheckoutQuery
from mcrcon import MCRcon

import config


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def sucess_payment(message: Message):
    with MCRcon(config.RCON_IP, config.RCON_PASSWORD) as rcon:
        pay = message.successful_payment
        assert pay
        info = pay.order_info
        assert info
        rcon.command(f"/whitelist add {info.name}")
