from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu
from aiogram.dispatcher.filters import Command, Text
from .game import game


@dp.message_handler(Command("start"))
async def start_bot(message: Message):
    await message.answer("Привет))", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Енто меню", reply_markup=menu)


@dp.message_handler(Text(equals="Старт"))
async def start_game(message: Message):
    await message.answer("Ну давай начнем", reply_markup=ReplyKeyboardRemove())
    await game(message)

