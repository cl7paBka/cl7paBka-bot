import asyncio
import logging

from aiogram import Bot, Dispatcher
from app.loader import bot, dp


async def main():
    logging.basicConfig(level=logging.DEBUG, filename="py_log.log", filemode="w")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
