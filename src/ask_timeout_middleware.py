import logging
from typing import Callable, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message
from aiogram.dispatcher.flags import get_flag
from aiogram.fsm.storage.redis import RedisStorage

from src.messages import TIMEOUT_MESSAGE

__all__ = ["AskTimeoutMiddleware"]


class AskTimeoutMiddleware(BaseMiddleware):
    _storage: RedisStorage

    def __init__(self, storage: RedisStorage):
        self._storage = storage

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

        user_activity = await self._storage.redis.get("ask"+user_id)

        if not user_activity and ask == "asked":
            logging.info("600")
            await self._storage.redis.set("ask"+user_id, "asked", ex=600)
            return await handler(event, data)

        if user_activity is not None and ask == "asking":
            logging.info("timeout")
            await event.answer(TIMEOUT_MESSAGE)
            return

        return await handler(event, data)