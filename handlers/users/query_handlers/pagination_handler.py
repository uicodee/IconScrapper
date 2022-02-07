from aiogram.dispatcher import FSMContext

from funcs import paginator
from loader import dp
from aiogram import types
from callback_datas import pagination


@dp.callback_query_handler(pagination.filter())
async def pagination_handler(query: types.CallbackQuery, callback_data: dict, state: FSMContext):
    data = []
    location = callback_data.get("location")
    page = int(callback_data.get("page"))
    images = (await state.get_data()).get("icons")
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    if location == "next":
        current_page = page + 1
        data = await paginator(data=images, page=current_page, products_page=1)
        if current_page == len(images):
            keyboard.add(
                types.InlineKeyboardButton(
                    text="⬅️",
                    callback_data=pagination.new(location="prev", page=current_page)
                )
            )
        else:
            keyboard.add(
                types.InlineKeyboardButton(
                    text="⬅️",
                    callback_data=pagination.new(location="prev", page=current_page)
                ),
                types.InlineKeyboardButton(
                    text="➡️",
                    callback_data=pagination.new(location="next", page=current_page)
                )
            )
    elif location == "prev":
        current_page = page - 1
        data = await paginator(data=images, page=current_page, products_page=1)
        if current_page == 1:
            keyboard.add(
                types.InlineKeyboardButton(
                    text="➡️",
                    callback_data=pagination.new(location="next", page=current_page)
                )
            )
        else:
            keyboard.add(
                types.InlineKeyboardButton(
                    text="⬅️",
                    callback_data=pagination.new(location="prev", page=current_page)
                ),
                types.InlineKeyboardButton(
                    text="➡️",
                    callback_data=pagination.new(location="next", page=current_page)
                )
            )
    for item in data:
        media = types.InputMediaDocument(media=item)
        await query.message.edit_media(media=media, reply_markup=keyboard)