from aiogram import Router
from app.handlers import start


def register_all_handlers(router: Router):
    router.include_router(start.router)
