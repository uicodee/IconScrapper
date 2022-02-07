from aiogram.dispatcher import FSMContext

from loader import dp
from aiogram import types
from states import Search
from funcs import get_icons, paginator
from callback_datas import pagination


@dp.message_handler(state=Search.query)
async def get_query(message: types.Message, state: FSMContext):
    query = message.text
    icons = await get_icons(query=query)
    data = await paginator(data=icons, page=1, products_page=1)
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    await state.update_data(icons=icons)
    for item in data:
        keyboard.add(
            types.InlineKeyboardButton(text="➡️", callback_data=pagination.new(location="next", page=1))
        )
        await message.answer_document(
            document=item,
            reply_markup=keyboard
        )
    await state.reset_state(with_data=False)
