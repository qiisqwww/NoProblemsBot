from loguru import logger
from src.config.config import LOGGING_PATH

__all__ = [
    "init_logger"
]


def init_logger() -> None:
    logger.add(
        LOGGING_PATH,
        compression="zip",
        rotation="500 MB",
        enqueue=True
    )
