from pathlib import Path

from .env import StrEnv, IntEnv

__all__ = [
    "BOT_TOKEN",
    "REDIS_HOST",
    "REDIS_PORT",
    "LOGGING_PATH",
    "ADMIN_ID_1",
    "ADMIN_ID_2"
]


BOT_TOKEN: str = StrEnv("BOT_TOKEN")

REDIS_HOST: str = StrEnv("REDIS_HOST")
REDIS_PORT: int = IntEnv("REDIS_PORT")

LOGGING_PATH: Path = Path(StrEnv("LOGGING_PATH"))

ADMIN_ID_1 = IntEnv("ADMIN_ID_1")
ADMIN_ID_2 = IntEnv("ADMIN_ID_2")
