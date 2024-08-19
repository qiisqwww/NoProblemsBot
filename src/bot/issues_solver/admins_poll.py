from loguru import logger
from aiogram.enums import ParseMode

from src.config import ADMIN_ID_1, ADMIN_ID_2
from src.bot.init_bot import bot
from src.bot.resources.messages import new_question

__all__ = [
    "admins_poll"
]


@logger.catch(message=f"Admins were not polled ")
async def admins_poll(question: str, user_id: int, username: str) -> None:
    for ADMIN_ID in ADMIN_ID_1, ADMIN_ID_2:
        await bot.send_message(
            ADMIN_ID,
            new_question(question, user_id, username),
            parse_mode=ParseMode.HTML
        )

        logger.info(f"Admin {ADMIN_ID} was succesfully polled with the question from {user_id}.")
