from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


start_key = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='💸Стоимость'),
            KeyboardButton(text='О нас'),
            KeyboardButton(text='📋Таблица размеров'),
            KeyboardButton(text='🖊️Рассчитать свой размер'),
            KeyboardButton(text='🏷️Получить скидку!')

        ]
    ], resize_keyboard=True
)


buy_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Выбрать свой размер:', callback_data='choose_size')],
        [InlineKeyboardButton(text='Назад', callback_data='back_to_catalog')]
    ]
)


buy_size = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Купить', url='https://brandshop.ru')],
    ]
)

back_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Назад', callback_data='back_to_start')]
    ]
)

AdminPanel = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Пользователи", callback_data="users")],
        [InlineKeyboardButton(text="Статистика", callback_data="statistick")],
        [InlineKeyboardButton(text="Рассылка", callback_data="mailing")],
        [InlineKeyboardButton(text="Блокировка", callback_data="block")],
    ]
)

back_to_admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data="back_to_admin"),
        ],
    ]
)


