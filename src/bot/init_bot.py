from aiogram import Bot

from src.config import BOT_TOKEN

__all__ = [
    "bot"
]


bot = Bot(BOT_TOKEN)
