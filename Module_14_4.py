from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from crud_functions import *

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb_reply = ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = KeyboardButton(text="Рассчитать")
btn2 = KeyboardButton(text="Информация")
btn3 = KeyboardButton(text="Купить")
kb_reply.add(btn1, btn2)
kb_reply.add(btn3)
kb_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Продукт 1", callback_data="product_buying")],
    [InlineKeyboardButton(text="Продукт 2", callback_data="product_buying")],
    [InlineKeyboardButton(text="Продукт 3", callback_data="product_buying")],
    [InlineKeyboardButton(text="Продукт 4", callback_data="product_buying")]

])


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb_reply)


@dp.message_handler(text="Купить")
async def get_buying_list(message):
    for i in get_all_products():
        await message.answer(f"Название: {i[1]}|Описание:{i[2]}|Цена:{i[3]}")

    await message.answer("Выберите товар:", reply_markup=kb_inline)

@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.message_handler()
async def all_message(message):
    await message.answer("Введите команду /start, что бы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
