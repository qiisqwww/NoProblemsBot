from pathlib import Path

from .env import StrEnv, IntEnv

__all__ = [
    "BOT_TOKEN",
    "LOGGING_PATH",
    "ADMIN_ID_1",
    "ADMIN_ID_2"
]


BOT_TOKEN: str = StrEnv("BOT_TOKEN")
LOGGING_PATH: Path = Path(StrEnv("LOGGING_PATH"))
ADMIN_ID_1 = IntEnv("ADMIN_ID_1")
ADMIN_ID_2 = IntEnv("ADMIN_ID_2")
