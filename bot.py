import asyncio
import logging

from aiogram.types import BotCommand
from app.loader import bot, dp

import app.handlers


async def main():
    logging.basicConfig(level=logging.DEBUG)
    await bot.set_my_commands(
        [
            BotCommand(command="/start", description="Старт"),
            BotCommand(command="/ai", description="Искусственный интеллект"),
            BotCommand(command="/shazam", description="Распознать музыку"),
            BotCommand(command="/deface", description="Размыть лица на фотографии")
        ]
    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
