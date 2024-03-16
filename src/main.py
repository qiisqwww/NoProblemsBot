from aiogram import Dispatcher
from loguru import logger

from src.config import LOGGING_PATH
from src.init_bot import bot
from src.issues_handler import issues_router


def init_logger() -> None:
    logger.add(
        LOGGING_PATH,
        compression="zip",
        rotation="500 MB",
        enqueue=True)


async def main():

    dp = Dispatcher()
    dp.include_routers(issues_router)

    init_logger()

    logger.info("Bot is starting.")

    await bot.delete_webhook(drop_pending_updates=True)

    await bot.send_message(chat_id=892885258, text='''Ответ на ваш вопрос "Как работает бот?"\nБот является инструментом-помощником для старосты. 
    Подробную информацию о функционале можно получить, если написать команду "Помощь" основному боту @grand_headman_bot''')

    await dp.start_polling(bot)

    logger.info("Bot was turned off.")
