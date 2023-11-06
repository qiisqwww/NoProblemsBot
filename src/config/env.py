from os import getenv
from dotenv import load_dotenv

__all__ = [
    "UndefinedEnvError",
    "StrEnv",
]


class UndefinedEnvError(Exception):
    def __init__(self, env_name: str) -> None:
        msg = f'Env name="{env_name}"'
        super().__init__(msg)


class StrEnv(str):
    def __new__(cls, env_name: str):
        load_dotenv()
        env = getenv(env_name, None)

        if env is None:
            raise UndefinedEnvError(env_name)

        obj = str.__new__(cls, env)

        return obj

class IntEnv(int):
    def __new__(cls, env_name: str):
        load_dotenv()
        env = getenv(env_name, None)

        if env is None:
            raise UndefinedEnvError(env_name)

        obj = super().__new__(cls, int(env))

        return obj
