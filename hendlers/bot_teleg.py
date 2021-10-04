from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import StatesGroup, State
from pars_ist import ist, anegdot


class Stat(StatesGroup):
    reg = State()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'], state='*')
    dp.register_message_handler(reg, state=Stat.reg)
    dp.register_message_handler(handler_txt, content_types=['text'], state="*")


# commands=['start'], state='*'
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_ist = types.InlineKeyboardButton(text='Рассказать историю')
    key_aneg = types.InlineKeyboardButton(text='Рассказать анекдот')
    key_end = types.InlineKeyboardButton(text='Нет не хочу!')
    keyboard.add(*[key_ist, key_aneg])
    keyboard.add(*[key_end])
    await message.answer(f'Приветики!\nЯ рад тебя видеть в нашейпереписке.\nПозволь рассказатьо себе.\nМеня зовут '
                         'Смешисторик, я могу рассказатьтебе анекдотили историю, если, ты конечно хочешь этого, '
                         'если ты нет, то какбы зачем тогда ты тут?', reply_markup=keyboard)
    await Stat.reg.set()


# state=Stat.reg
async def reg(message: types.Message):
    if message.text.lower().endswith('историю'):
        await istor(message)
    elif message.text.lower().endswith('анекдот'):
        await aneg(message)
    elif message.text.lower().startswith('нет не хочу!'):
        await one_end(message)
    elif message.text.lower().startswith('хватит, спасибо!'):
        await two_end(message)
    elif message.text.lower().startswith('старт'):
        await start(message)
    else:
        await not_inf(message)


async def istor(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_ist = types.InlineKeyboardButton(text='Рассказать ещё историю')
    key_aneg = types.InlineKeyboardButton(text='Рассказать анекдот')
    key_end = types.InlineKeyboardButton(text='Хватит, спасибо!')
    keyboard.add(*[key_ist, key_aneg])
    keyboard.add(*[key_end])
    await message.answer('Секундочку...')
    await message.answer(ist(), reply_markup=keyboard)


async def aneg(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_ist = types.InlineKeyboardButton(text='Рассказать историю')
    key_aneg = types.InlineKeyboardButton(text='Рассказать ещё анекдот')
    key_end = types.InlineKeyboardButton(text='Хватит, спасибо!')
    keyboard.add(*[key_ist, key_aneg])
    keyboard.add(*[key_end])
    await message.answer(anegdot(), reply_markup=keyboard)


async def not_inf(message: types.Message):
    await message.answer('Не совсем понял что ты написал.\nВоспользуйся кнопочками)))')


async def one_end(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_end = types.InlineKeyboardButton(text='Старт')
    keyboard.add(key_end)
    await message.answer('Надеюсь на скорую встречу, пока!!!', reply_markup=keyboard)


async def two_end(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_end = types.InlineKeyboardButton(text='Старт')
    keyboard.add(key_end)
    await message.answer(f'Думаю ты хорошо провёл время, чтож пора прощаться.\nНадеюсь на скорую встречу, Пока!!!',
                         reply_markup=keyboard)


# content_types=['text'], state="*"
async def handler_txt(message: types.Message):
    await message.answer('Напишите /start')
