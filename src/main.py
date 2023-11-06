import logging

from aiogram import Dispatcher

from config import LOGGING_PATH
from init_bot import bot
from issues_handler import issues_router


def init_logger() -> None:
    logging.basicConfig(
        filename=LOGGING_PATH,
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
    )


async def main():

    dp = Dispatcher()
    dp.include_routers(issues_router)

    init_logger()

    logging.info("bot is starting")

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

    logging.info("bot was turned off")
