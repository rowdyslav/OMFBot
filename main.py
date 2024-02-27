import asyncio
import logging
import sys

from aiogram import Dispatcher, F
from aiogram.filters import CommandStart

from core import BOT
from handlers.message import some_message, start
from handlers.payment import pre_checkout_query, success_payment

dp = Dispatcher()


async def main() -> None:
    dp.message.register(start, CommandStart())
    dp.message.register(success_payment, F.successful_payment)
    dp.message.register(some_message)

    dp.pre_checkout_query.register(pre_checkout_query)
    await dp.start_polling(BOT)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
