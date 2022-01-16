from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import tictactoe, choice
from aiogram.dispatcher.filters import Command, Text
from random import randint
from keyboards.default import choice_yes_no, menu
from asyncio import sleep
from aiohttp import ClientSession
from data.config import BOT_TOKEN


@dp.message_handler(Text(equals="Да"))
async def game(message: Message):
    await message.answer("Камень, ножницы, бумага\nРаз, два, три...", reply_markup=tictactoe)
    #await message.delete()
    if message.text == 'Да':
        await delete_message_http(message, message.message_id-4, message.message_id)


@dp.message_handler(Text(equals=choice))
async def game_result(message: Message):
    player_choice = choice.index(message.text)
    bot_choice = randint(0,2)
    await message.answer(choice[bot_choice], reply_markup=ReplyKeyboardRemove())
    if player_choice == bot_choice:
        result = 'ничья'
    elif player_choice < bot_choice or (player_choice==0 and bot_choice==2):
        result = f'победил {message.from_user.first_name}'
    else:
        result = f'победил Бот'

    await message.answer(f"В этом раунде {result}.\nЕще разок?", reply_markup=choice_yes_no)


@dp.message_handler(Text(equals="Нет"))
async def game_over(message: Message):
    await message.answer("Ты был не плох", reply_markup=menu)
    await message.delete()


async def delete_message(message: Message, sleep_time: int = 0):
    await sleep(sleep_time)
    await message.delete()


async def delete_message_http(message: Message, from_message_id: int = -1, to_message_id: int = -1, sleep_time: int = 0):
    for message_id in range(from_message_id,to_message_id+1):
        url = f'https://api.telegram.org/bot{BOT_TOKEN}/deletemessage?chat_id={message.chat.id}&message_id={message_id}'
        async with ClientSession() as session:
            async with session.get(url) as response:
                html = response.text
                print(html)
