from aiogram import types

cancel = types.InlineKeyboardMarkup(row_width=1)
cancel.add(
    types.InlineKeyboardButton(text="Bekor qilish", callback_data="cancel")
)
