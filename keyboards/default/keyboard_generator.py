from aiogram import types


def keyboard_generator(
        data: list,
        row_width: int,
        resize_keyboard: bool,
        one_time_keyboard: bool) -> types.ReplyKeyboardMarkup:
    buttons = []
    keyboard = types.ReplyKeyboardMarkup(
        row_width=row_width,
        resize_keyboard=resize_keyboard,
        one_time_keyboard=one_time_keyboard
    )
    for item in data:
        buttons.append(
            types.KeyboardButton(text=item)
        )

    keyboard.add(*buttons)
    return keyboard
