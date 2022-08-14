from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, baza


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        ism = message.from_user.first_name
        username = message.from_user.username
        tg = message.from_user.id
        baza.user_qoshish(ism=ism, tg_id=tg, username=username)
    except Exception:
        pass
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!")
    await message.answer(text='Tik tokdan yuklagan ssilkangizni yuboring:')
