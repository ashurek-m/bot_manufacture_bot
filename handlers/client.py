from aiogram import types, Dispatcher
from create_bot import dp, bot


async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'boom')
        await message.delete()
    except:
        await message.reply('Общение с ботом только через ЛС, напиши ему:\nhttps://t.me/smithMaxBot')


async def beginning_of_work(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'вы в системе')
    except:
        await message.reply('Общение с ботом только через ЛС, напиши ему:\nhttps://t.me/smithMaxBot')


def register_handler_client(dp_1: Dispatcher):
    dp_1.register_message_handler(commands_start, commands=['start', 'help'])
    dp_1.register_message_handler(beginning_of_work, commands=['регистрация'])
