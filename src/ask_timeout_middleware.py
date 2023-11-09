from typing import Callable, Any, Awaitable

from loguru import logger
from aiogram import BaseMiddleware
from aiogram.types import Message
from aiogram.dispatcher.flags import get_flag

from src.messages import TIMEOUT_MESSAGE
from src.redis_service import RedisService

__all__ = ["AskTimeoutMiddleware"]


class AskTimeoutMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: dict[str, Any]
    ) -> Any:

        user_id = str(event.from_user.id)

        ask = get_flag(data, "ask")
        if not ask:
            return await handler(event,data)

        with RedisService() as storage:
            user_activity = storage.get_user_ask(user_id)

            if not user_activity and ask == "asked":
                storage.set_user_ask(user_id)
                return await handler(event, data)

            if user_activity and ask == "asking":
                logger.exception(f"User's {user_id} ask wasn't handled (user in timeout).")
                await event.answer(TIMEOUT_MESSAGE)
                return

        return await handler(event, data)