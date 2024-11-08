from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import types


def get_main_menu_keyboard() -> types.ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="Распознать музыку"))
    builder.add(types.KeyboardButton(text="Искусственный интеллект"))
    builder.add(types.KeyboardButton(text="Размытие лиц на фото"))

    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)