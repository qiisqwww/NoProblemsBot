import logging

import redis

__all__ = ["RedisService"]


class RedisService:
    _con: redis.Redis

    def __init__(self) -> None:
        self._con = redis.Redis(host='localhost',
                                port=6379,
                                decode_responses=True)

    def set_user(self, user_id: str) -> None:
        self._con.set(user_id, "True", ex=3600)

    def get_user(self, user_id: str) -> bool:
        return self._con.get(user_id) is not None

    def __enter__(self) -> "RedisService":
        return self

    def __exit__(self, exc_type, *_) -> None:
        if exc_type is not None:
            logging.error(exc_type)

        self._con.close()
