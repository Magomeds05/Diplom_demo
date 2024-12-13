
from aiogram.dispatcher.filters.state import State, StatesGroup


class UserState(StatesGroup):
    age = State()
    growth = State()
    size = State()


class UserSale(StatesGroup):
    name = State()
    number = State()
    email = State()