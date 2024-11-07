from aiogram import types, Router

from aiogram.filters import CommandStart
from aiogram.types import Message

from app.keyboards.main_menu import get_main_menu_keyboard

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "Welcome to cl7paBka-bot! Choose an option from the menu below.",
        reply_markup=get_main_menu_keyboard()
    )
