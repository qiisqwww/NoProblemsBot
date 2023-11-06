from aiogram.fsm.state import State, StatesGroup

__all__ = ["AskStates"]


class AskStates(StatesGroup):
    question_input = State()