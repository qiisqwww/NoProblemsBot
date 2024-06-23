import asyncio

from aiogram import Dispatcher
from loguru import logger

from src.config import init_logger
from src.bot.init_bot import bot
from src.bot.issues_solver.issues_handler import issues_router


async def main():
    init_logger()
    logger.info("LOGGER INITIALIZED")

    dp = Dispatcher()
    dp.include_routers(issues_router)

    logger.info("STARTING THE BOT...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
