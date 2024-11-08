from aiogram import types
from aiogram.filters import Command

from app.loader import form_router


@form_router.message(Command("shazam"))
async def recognize_music(message: types.Message):
    await message.answer("Распознать музыку")