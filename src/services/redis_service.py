from enum import StrEnum, IntEnum, verify, UNIQUE

from loguru import logger
import redis.asyncio as redis

from src.config.config import REDIS_PORT, REDIS_HOST

__all__ = [
    "RedisService"
]


@verify(UNIQUE)
class RedisKeys(str, StrEnum):
    ASK_KEY = "ask_"
    THROTTLING_KEY = "throttling_"


@verify(UNIQUE)
class RedisServiceSettings(str, IntEnum):
    TIME_OUT_TIME_SECONDS = 60
    THROTTLING_TIME_SECONDS = 10


class RedisService:
    _con: redis.Redis

    async def set_user_ask(self, user_id: str) -> None:
        await self._con.set(
            RedisKeys.ASK_KEY + user_id,
            "True",
            ex=RedisServiceSettings.TIME_OUT_TIME_SECONDS
        )

    async def get_user_ask(self, user_id: str) -> bool:
        return await self._con.get(RedisKeys.ASK_KEY + user_id) is not None

    async def set_user_throttling(self, user_id: str) -> None:
        await self._con.set(
            RedisKeys.THROTTLING_KEY + user_id,
            0,
            ex=RedisServiceSettings.THROTTLING_TIME_SECONDS
        )

    async def increase_user_throttling(self, user_id: str) -> None:
        await self._con.incr(RedisKeys.THROTTLING_KEY + user_id)

    async def get_user_throttling(self, user_id: str) -> int:
        return await self._con.get(RedisKeys.THROTTLING_KEY + user_id)

    async def __aenter__(self) -> "RedisService":
        self._con = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            decode_responses=True
        )

        return self

    async def __aexit__(self, exc_type, *_) -> None:
        if exc_type is not None:
            logger.error(exc_type)

        await self._con.aclose()
