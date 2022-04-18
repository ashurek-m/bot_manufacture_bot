from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# кномпка ссылка
urlkb = InlineKeyboardMarkup(row_width=1)
urlbutton1 = InlineKeyboardButton(text='Google', url=r'https://www.google.com/')
urlbutton2 = InlineKeyboardButton(text='youtube', url=r'https://www.youtube.com/')
urlkb.add(urlbutton1, urlbutton2)