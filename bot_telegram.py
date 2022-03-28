from aiogram.utils import executor
from create_bot import dp
from handlers import client, other, admin


client.register_handler_client(dp)
admin.register_handler_admin(dp)
other.register_handler_other(dp)

executor.start_polling(dp, skip_updates=True)
