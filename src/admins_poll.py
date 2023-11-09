from loguru import logger
from aiogram.enums import ParseMode

from src.config import ADMIN_ID_1, ADMIN_ID_2
from src.init_bot import bot
from src.messages import new_question

__all__ = ["admins_poll"]


async def admins_poll(question: str, user_id: int) -> None:
    for ADMIN_ID in ADMIN_ID_1, ADMIN_ID_2:
        await bot.send_message(ADMIN_ID, new_question(question, user_id),
                               parse_mode=ParseMode.HTML)

        logger.info(f"Admin {ADMIN_ID} was succesfully polled with the question from {user_id}.")
