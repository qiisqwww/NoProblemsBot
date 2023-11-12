from loguru import logger

import aioredis

__all__ = ["RedisService"]


class RedisService:
    _con: aioredis.Redis

    def __init__(self) -> None:
        self._con = aioredis.from_url(url='redis://localhost')

    async def set_user_ask(self, user_id: str) -> None:
        await self._con.set("ask"+user_id, "True", ex=600)

    async def get_user_ask(self, user_id: str) -> bool:
        return (await self._con.get("ask"+user_id)) is not None

    async def set_user_throttling(self, user_id: str) -> None:
        await self._con.set("thr"+user_id, 0, ex=10)

    async def increase_user_throttling(self, user_id: str) -> None:
        await self._con.incr("thr"+user_id)

    async def get_user_throttling(self, user_id: str) -> int:
        return await self._con.get("thr"+user_id)

    def __enter__(self) -> "RedisService":
        return self

    def __exit__(self, exc_type, *_) -> None:
        if exc_type is not None:
            logger.error(exc_type)

        self._con.close()
