from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



catalog_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Nike air jordan 1 low', callback_data='Jordanlow')],
        [InlineKeyboardButton(text='Nike air jordan 1 X Travis Scott', callback_data='Travis')],
        [InlineKeyboardButton(text='Nike air jordan 1 high', callback_data='Jordanhigh')],
        [InlineKeyboardButton(text='Nike air force 1', callback_data='Force')],
        [InlineKeyboardButton(text='Nike Dunk', callback_data='Dunk')],
        [InlineKeyboardButton(text='Nike air max 95', callback_data='Max95')],
        [InlineKeyboardButton(text='Nike air max 97', callback_data='Max97')],
        [InlineKeyboardButton(text='Adidas yeezy 350', callback_data='Yeezy350')],
        [InlineKeyboardButton(text='Adidas yeezy 700', callback_data='Yeezy700')],
        [InlineKeyboardButton(text='Adidas Raf Simons', callback_data='Raf')],
        [InlineKeyboardButton(text='Off white out of office', callback_data='Off_White')],
        [InlineKeyboardButton(text='Off white Odsy', callback_data='Off_White_Odsy')],
        [InlineKeyboardButton(text='Balenciaga runner', callback_data='Balen')],
        [InlineKeyboardButton(text='LV Skate sneaker', callback_data='LouisSkate')],
        [InlineKeyboardButton(text='LV Trainer', callback_data='LouisTrain')],
        [InlineKeyboardButton(text='Maison Margiela Replica', callback_data='MM')],
        [InlineKeyboardButton(text='Maison Margiela Future', callback_data='MMFut')],
        [InlineKeyboardButton(text='Lanvin curb sneakers', callback_data='Lanvin')],
        [InlineKeyboardButton(text='Rick Owens ramones', callback_data='Rick')],
        [InlineKeyboardButton(text='Другие предложения', callback_data='other')],
        [InlineKeyboardButton(text='Назад', callback_data='back_to_start')]
    ]
)