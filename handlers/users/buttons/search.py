from aiogram.dispatcher import FSMContext

from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Text
from keyboards.inline import cancel
from states import Search


@dp.message_handler(Text(equals="Qidirish"), state="*")
async def search(message: types.Message, state: FSMContext):
    await state.reset_state(with_data=True)
    await message.answer(
        text="Qidiruv so'rovini kiriting",
        reply_markup=cancel
    )
    await Search.query.set()
