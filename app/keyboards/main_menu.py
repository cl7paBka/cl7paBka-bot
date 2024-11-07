from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_menu_keyboard():
    """Main menu with bot feature options."""
    keyboard = ReplyKeyboardMarkup()
    keyboard.add(KeyboardButton("AI Assistant"))
    keyboard.add(KeyboardButton("Music Recognition"))
    keyboard.add(KeyboardButton("Photo Blurring"))
    keyboard.add(KeyboardButton("About the Creator"))
    return keyboard
