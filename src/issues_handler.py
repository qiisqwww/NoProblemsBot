import logging

from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from src.messages import (START_MESSAGE,
                      ASK_MESSAGE,
                      QUESTION_HANDLED_MESSAGE)
from src.states import AskStates
from src.admins_poll import admins_poll
from src. throttling_middleware import ThrottlingMiddleware


issues_router = Router()
issues_router.message.outer_middleware(ThrottlingMiddleware())
issues_router.message.filter(F.chat.type.in_({"private"}))


@issues_router.message(Command("start"))
async def start_command(message: types.Message) -> None:
    logging.info("start command handled")

    await message.answer(START_MESSAGE)


@issues_router.message(Command("ask"))
async def start_command(message: types.Message, state: FSMContext) -> None:
    logging.info("ask command handled")

    await message.answer(ASK_MESSAGE)
    await state.set_state(AskStates.question_input)


@issues_router.message(AskStates.question_input, F.text)
async def handling_quiestion(message: types.Message, state: FSMContext) -> None:
    logging.info("question handled")

    await message.answer(QUESTION_HANDLED_MESSAGE)
    await state.clear()
    await admins_poll(message.text, message.from_user.id)
