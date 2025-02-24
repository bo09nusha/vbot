from aiogram.fsm.state import State, StatesGroup


class LevelState(StatesGroup):
    level = State()
    answer = State()