from aiogram.filters import CommandStart
from aiogram.types import Message
from app.keyboards.reply.main_menu import get_main_menu_keyboard
from app.loader import dp


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привет!", reply_markup=get_main_menu_keyboard())
