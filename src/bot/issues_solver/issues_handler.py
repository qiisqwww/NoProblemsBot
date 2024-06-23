from loguru import logger
from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from src.bot.resources.messages import (
    START_MESSAGE,
    ASK_MESSAGE,
    QUESTION_HANDLED_MESSAGE
)
from src.bot.issues_solver.states import AskStates
from src.bot.issues_solver.admins_poll import admins_poll
from src.bot.middlewares import ThrottlingMiddleware
from src.bot.middlewares import AskTimeoutMiddleware
from src.bot.resources.buttons import load_main_keyboard


issues_router = Router()
issues_router.message.middleware.register(ThrottlingMiddleware())
issues_router.message.middleware.register(AskTimeoutMiddleware())
issues_router.message.filter(F.chat.type.in_({"private"}))


@issues_router.message(Command("start"))
async def start_command(message: types.Message) -> None:
    await message.answer(START_MESSAGE, reply_markup=load_main_keyboard())


@issues_router.message(Command("ask"), flags={"ask": "asking"})
async def start_command(message: types.Message, state: FSMContext) -> None:
    await message.answer(ASK_MESSAGE, reply_markup=load_main_keyboard())
    await state.set_state(AskStates.question_input)


@issues_router.message(AskStates.question_input, F.text, flags={"ask": "asked"})
async def handling_question(message: types.Message, state: FSMContext) -> None:
    logger.info(f"QUESTION FROM {message.from_user.id} {message.from_user.username} HANDLED")

    await message.answer(QUESTION_HANDLED_MESSAGE, reply_markup=load_main_keyboard())
    await state.clear()
    await admins_poll(message.text, message.from_user.id, message.from_user.username)


@issues_router.message(flags={"void": "void"})
async def handles_void() -> None:
    pass
