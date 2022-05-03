from aiogram import Bot, Dispatcher, executor, types



# Клавиатура
menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.row(
	types.KeyboardButton('🔰 Спонсоры')
)

menu.add(
	types.KeyboardButton('👤 Баланс'),
	types.KeyboardButton('🍓 Клик'),
	types.KeyboardButton('🎰 Вывод'),
)
menu.row(
	types.KeyboardButton('🏆 Топ'),
)
menu.add(
	types.KeyboardButton('🌹 О сервисе'),
)


pay = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
pay.add(
	types.KeyboardButton('Оплатить')
)

accept = types.InlineKeyboardMarkup(row_width=3)
accept.add(
    types.InlineKeyboardButton(text='✅ Принимаю', callback_data='accept')
)

buy1 = types.InlineKeyboardMarkup(row_width=3)
buy1.add(
    types.InlineKeyboardButton(text='Проверить оплату', callback_data='check'),
    types.InlineKeyboardButton(text='Назад', callback_data='back')
    )

apanel = types.InlineKeyboardMarkup(row_width=3)
apanel.add(
    types.InlineKeyboardButton(text='Статистика', callback_data='stats'),
		types.InlineKeyboardButton(text='Рассылка', callback_data='pizda')
    )

a1 = types.InlineKeyboardMarkup(row_width=3)
a1.add(
    types.InlineKeyboardButton(text='Наш канал', url='https://t.me/DarkkScum', callback_data='pizda')
    )