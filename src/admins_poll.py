import logging

from aiogram.enums import ParseMode

from config import ADMIN_ID_1, ADMIN_ID_2
from init_bot import bot
from messages import new_question

__all__ = ["admins_poll"]


async def admins_poll(question: str, user_id: int) -> None:
    for ADMIN_ID in ADMIN_ID_1, ADMIN_ID_2:
        try:
            await bot.send_message(ADMIN_ID, new_question(question, user_id),
                                   parse_mode=ParseMode.HTML)
            logging.info(f"admin {ADMIN_ID} was succesfully polled with the question from {user_id}")
        except Exception as e:
            logging.warning(f"admin {ADMIN_ID} wasn't polled, {e}")
