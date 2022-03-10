from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)
'''***************КЛИЕНСКАЯ ЧАСТЬ*******************'''


@dp.message_handler(commands=['start', 'help'])
async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'boom')
        await message.delete()
    except:
        await message.reply('Общение с ботом только через ЛС, напиши ему:\nhttps://t.me/smithMaxBot')


'''***************АДМИНСКАЯ ЧАСТЬ*******************'''

'''***************ОБЩАЯ ЧАСТЬ*******************'''


@dp.message_handler()
async def echo_send(message: types.Message):
    # await message.answer(message.text)
    await message.reply(message.text)
    # await bot.send_message(message.from_user.id,message.text)


executor.start_polling(dp, skip_updates=True)
