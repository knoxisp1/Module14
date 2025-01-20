from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio
import os

api = "7993073270:AAFjsMFNPo_sL-4wG7cuM_BCYIrgHJKNS6M"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb_reply = ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = KeyboardButton(text="Рассчитать")
btn2 = KeyboardButton(text="Информация")
btn3 = KeyboardButton(text="Купить")
kb_reply.add(btn1, btn2)
kb_reply.add(btn3)
kb_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Product1", callback_data="product_buying")],
    [InlineKeyboardButton(text="Product2", callback_data="product_buying")],
    [InlineKeyboardButton(text="Product3", callback_data="product_buying")],
    [InlineKeyboardButton(text="Product4", callback_data="product_buying")]

])


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью", reply_markup=kb_reply)


@dp.message_handler(text="Купить")
async def get_buying_list(message):
    for j in range(1, 5):
        await message.answer(f"Название:Product{j}|Описание:описание{j}|Цена:{j * 100}")
        with open(f'Images/{j}.png', "rb") as file1:
            await message.answer_photo(file1)

    await message.answer("Выберите продукт для покупки:", reply_markup=kb_inline)

@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт.")
    await call.answer()

@dp.message_handler()
async def all_messages(message):
    await message.answer("Введите команду /start, что бы начать общение")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
