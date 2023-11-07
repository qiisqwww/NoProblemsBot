from typing import Callable, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message
from aiogram.dispatcher.flags import get_flag
from aiogram.fsm.storage.redis import RedisStorage

__all__ = ["ThrottlingMiddleware"]


class ThrottlingMiddleware(BaseMiddleware):
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

        void = get_flag(data, "void")
        if void:
            return

        user_activity = await self._storage.redis.get("thr"+user_id)
        if not user_activity:
            await self._storage.redis.set("thr"+user_id, 0, ex=20)
            return await handler(event, data)

        if int(user_activity.decode()) >= 10:
            return

        await self._storage.redis.incr("thr"+user_id)
        return await handler(event, data)
