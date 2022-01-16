from aiogram import executor
from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from loader import dp


@dp.message_handler()
async def echo(message: Message):
    await message.answer(text=f"{message.chat.id}\n{message.message_id}")