from aiogram.utils import executor
from create_bot import dp
from handlers import client, other


client.register_handler_client(dp)
other.register_handler_other(dp)

executor.start_polling(dp, skip_updates=True)
