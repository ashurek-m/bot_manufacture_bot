from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/регистрация')
b2 = KeyboardButton('/start')
b3 = KeyboardButton('/help')
b4 = KeyboardButton('поделиться номером', request_contact=True)
b5 = KeyboardButton('отправить где я', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
'''
one_time_keyboard -  спрятать клавиатуру после нажатия кнопки

add - клавиша с новой строки
insert - добавляет клавишу в текущую строку
row - добавление всех кнопок в строку

'''
kb_client.add(b1).add(b2).insert(b3).row(b4, b5)
