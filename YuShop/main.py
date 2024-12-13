import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup


from config import *
from keyboards import *
from key_catalog import *
import text
import textproduct
from classtate import UserState, UserSale
from key_size import size_key
import database

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API)
disp = Dispatcher(bot, storage=MemoryStorage())

@disp.message_handler(commands=['start'])
async def start(message):
    await message.answer(text.start, reply_markup=start_key)

@disp.message_handler(text='О нас')
async def price(message):
    with open('files/vhodnaya-gruppa-magazina-scaled.jpg', "rb") as img:
        await message.answer_photo(img, text.about, reply_markup=start_key)

@disp.message_handler(text='📋Таблица размеров')
async def size(message):
    with open('files/maxresdefault.jpg', "rb") as img:
        await message.answer_photo(img, "Размерная сетка", reply_markup=start_key)

@disp.message_handler(text='🏷️Получить скидку!')
async def set_sale(message):
    with open('files/400w-LcdG9JFW3I0.webp', "rb") as img:
        await message.answer_photo(img, text.sale)
        await UserSale.name.set()

@disp.message_handler(state= UserSale.name)
async def set_number(message, state):
    await state.update_data(age=message.text)
    await message.answer('📝Введите свой номер телефона:')
    await UserSale.number.set()

@disp.message_handler(state= UserSale.number)
async def set_email(message, state):
    await state.update_data(age=message.text)
    await message.answer('📝Введите свой email:')
    await UserSale.email.set()

@disp.message_handler(state= UserSale.email)
async def send_calories(message, state):
    await state.update_data(email=message.text)
    data = await state.get_data()
    await message.answer(f"✅Поздравляем, регистрация прошла успешно, вша скидка - 30%", reply_markup=start_key)
    await state.finish()

@disp.message_handler(text='🖊️Рассчитать свой размер')
async def set_name(message):
    with open('files/razmer-1.jpg', "rb") as img:
        await message.answer_photo(img, 'Измерьте и введите длину стопы в сантиметрах:')
        await UserState.age.set()

@disp.message_handler(state= UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой возраст:')
    await UserState.growth.set()

@disp.message_handler(state= UserState.growth)
async def send_calories(message, state):
    await state.update_data(growth=message.text)
    data = await state.get_data()
    a = data['age']
    g = data['growth']
    if g >= str(18):
        await message.answer(f"Ваш размер: {(16 + int(a))}", reply_markup=start_key)
    else:
        await message.answer(f"Ваш размер: {(15.5 + int(a))}", reply_markup=start_key)
    await state.finish()

@disp.message_handler(text='💸Стоимость')
async def info(message):
    await message.answer("Что вас интересует?", reply_markup=catalog_key)

@disp.callback_query_handler(text='Jordanlow')
async def buy_Jordan_low(call):
    with open('files/3product.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.Jordanlow, reply_markup=buy_key)
    await call.answer()

@disp.callback_query_handler(text='Jordanhigh')
async def buy_Jordan_high(call):
    with open('files/Air-Jordan-1-Mid-Chicago-Black-Toe-554724-069-Release-Date-Price-2-1.jpg.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.Jordanhigh, reply_markup=buy_key)
    await call.answer()

@disp.callback_query_handler(text='Travis')
async def buy_Jordan_Travis(call):
    with open('files/1_5f.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.Travis, reply_markup=buy_key)
    await call.answer()

@disp.callback_query_handler(text='Force')
async def buy_Jordan_Force(call):
    with open('files/9xwx48wdn6dg4x67y4cap1ne5l08adzi.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.Force, reply_markup=buy_key)
    await call.answer()

@disp.callback_query_handler(text='Dunk')
async def buy_Nike_Dunk(call):
    with open('files/AURORA_FQ.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.Dunk, reply_markup=buy_key)
    await call.answer()

@disp.callback_query_handler(text='Max95')
async def buy_Max95(call):
    with open('files/jd_720074_a.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.Max95, reply_markup=buy_key)
    await call.answer()

@disp.callback_query_handler(text='Max97')
async def buy_Max97(call):
    with open('files/2vzj47l4yxsewshjflkxg8p0yvf4wtng.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.Max97, reply_markup=buy_key)
    await call.answer()

@disp.callback_query_handler(text='Yeezy350')
async def buy_Yeezy350(call):
    with open('files/IMG_20200627_021400.jpg.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.Yeezy350, reply_markup=buy_key)
    await call.answer()

@disp.callback_query_handler(text='Yeezy700')
async def buy_Yeezy700(call):
    with open('files/main-square_db919406-f9a5-41e3-97bd-088b16d10731.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.Yeezy700, reply_markup=buy_key)
    await call.answer()

@disp.callback_query_handler(text='Raf')
async def buy_Raf(call):
    with open('files/d440e516e889471cba66074dda282874.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.Raf, reply_markup=buy_key)
    await call.answer()

@disp.callback_query_handler(text='Off_White')
async def buy_Off_White(call):
    with open('files/off-white-out-of-office-white-grey-trainers-side.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.Off_White, reply_markup=buy_key)
    await call.answer()

@disp.callback_query_handler(text='Off_White_Odsy')
async def buy_Off_White_Odsy(call):
    with open('files/e6kwxxs85oy4aw499qfyr0q0vzm6p4m5.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.Off_White_Odsy, reply_markup=buy_key)
    await call.answer()

@disp.callback_query_handler(text='Balen')
async def buy_Balen(call):
    with open('files/826217_01.jpg.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.Balen, reply_markup=buy_key)
    await call.answer()

@disp.callback_query_handler(text='LouisSkate')
async def buy_LouisSkate(call):
    with open('files/imglouis.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.LouisSkate, reply_markup=buy_key)
    await call.answer()

@disp.callback_query_handler(text='LouisTrain')
async def buy_LouisTrain(call):
    with open('files/louis-vuitton-lv-skate-monogram-trainer-green-sneaker-nvprod4640020v-side.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.LouisTrain, reply_markup=buy_key)
    await call.answer()

@disp.callback_query_handler(text='MM')
async def buy_MM(call):
    with open('files/MM6MaisonMargiela.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.MM, reply_markup=buy_key)
    await call.answer()

@disp.callback_query_handler(text='MMFut')
async def buy_MMFut(call):
    with open('files/s-l1200.jpg', "rb") as img:
        await call.message.answer_photo(img, textproduct.MMFut, reply_markup=buy_key)
    await call.answer()

@disp.callback_query_handler(text='Lanvin')
async def buy_Lanvin(call):
    with open('files/nm_4837489_100296_m.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.Lanvin, reply_markup=buy_key)
    await call.answer()

@disp.callback_query_handler(text='Rick')
async def buy_Rick(call):
    with open('files/Untitled-33_22dba556-beaa-4fd2-8fe5-5d829b73a1a2.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.Rick, reply_markup=buy_key)
    await call.answer()

@disp.callback_query_handler(text='other')
async def buy_other(call):
    await call.message.answer(text.other, reply_markup=back_key)
    await call.answer()

@disp.callback_query_handler(text='back_to_catalog')
async def back(call):
    await call.message.answer("Что вас интересует?", reply_markup=catalog_key)
    await call.answer()

@disp.callback_query_handler(text='back_to_start')
async def back_start(call):
    await call.message.answer("Что вас интересует?", reply_markup=start_key)
    await call.answer()

@disp.callback_query_handler(text='choose_size')
async def choose_size(call):
    await call.message.answer("Все размеры в наличии:", reply_markup=size_key)
    await call.answer()

@disp.callback_query_handler(text='buy_size')
async def pay(call):
    await call.message.answer(text.pay, reply_markup=buy_size)
    await call.answer()

@disp.message_handler()
async def all_massages(message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == "__main__":
    executor.start_polling(disp, skip_updates=True)