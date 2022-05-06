from aiogram import types, Dispatcher
from keyboards.inline_test import urlkb
from create_bot import dp


# @dp.message_handler()
async def echo_send(message: types.Message):
    # await message.answer(message.text)
    await message.reply(message.from_user.id, message.text)
    # await bot.send_message(message.from_user.id,message.text)


'''
async def url(message: types.Message):
    await message.answer('Ссылочки', reply_markup=urlkb)
'''


def register_handler_other(dp_1: Dispatcher):
    dp_1.register_message_handler(echo_send)
