from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove


async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'boom', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом только через ЛС, напиши ему:\nhttps://t.me/smithMaxBot')


async def beginning_of_work(message: types.Message):
    await bot.send_message(message.from_user.id, 'вы в системе')


def register_handler_client(dp_1: Dispatcher):
    dp_1.register_message_handler(commands_start, commands=['start', 'help'])
    dp_1.register_message_handler(beginning_of_work, commands=['регистрация'])
