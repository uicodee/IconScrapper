from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.default import keyboard_generator


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    keyboard = keyboard_generator(
        data=['Qidirish'],
        row_width=1,
        resize_keyboard=True,
        one_time_keyboard=False
    )
    await message.answer(
        text=f"Salom, {message.from_user.full_name}",
        reply_markup=keyboard
    )
