import logging
from typing import Callable, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message

from src.redis_service import RedisService
from src.messages import TIMEOUT_MESSAGE

__all__ = ["ThrottlingMiddleware"]


class ThrottlingMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, dict[str, Any]],
            Awaitable[Any]],
            event: Message,
            data: dict[str, Any]
    ) -> Any:

        user_id = str(event.from_user.id)
        with RedisService() as redis:
            if redis.get_user(user_id):
                logging.info(f"user {user_id} in timeout")

                await event.answer(TIMEOUT_MESSAGE)
                return

            redis.set_user(user_id)

        return await handler(event,data)
