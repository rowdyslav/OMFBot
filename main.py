import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart

import config
from handlers.message import some_message, start
from handlers.payment import pre_checkout_query, sucess_payment


async def main() -> None:
    bot = Bot(config.BOT_TOKEN)
    dp = Dispatcher()

    dp.message.register(start, CommandStart())
    dp.message.register(some_message)

    dp.pre_checkout_query.register(pre_checkout_query)
    dp.message.register(sucess_payment, F.successful_payment)

    await dp.start_polling(bot, skip_updates=False)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
