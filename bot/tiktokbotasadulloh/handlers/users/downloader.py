from aiogram import types
from tiktok import tk
from loader import dp, bot
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


# Echo bot
@dp.message_handler(Text(startswith='https://www.tiktok.com'))
async def test(message: types.Message):
    id = message.from_user.id
    natija = tk(message.text)
    tugma = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Musiqasini yuklab olish", callback_data="musiqa")
            ]
        ]
    )

    @dp.callback_query_handler(text='musiqa')
    async def bot_echo(message: CallbackQuery):
        id = message.from_user.id
        await message.message.answer(text='⏳')
        await bot.send_audio(chat_id=id, audio=natija['music'], caption="VIDEO Musiqasi")

    await message.answer(text='⏳')
    await bot.send_video (chat_id=id, video=natija['video'],reply_markup=tugma, caption="Dasturchi : https://t.me/Pythonchi_UZB")

@dp.message_handler(Text(startswith='https://vt.tiktok.com'))
async def test(message: types.Message):
    id = message.from_user.id
    natija = tk(message.text)
    tugma = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Musiqasini yuklab olish", callback_data="musiqa")
            ]
        ]
    )

    @dp.callback_query_handler(text='musiqa')
    async def bot_echo(message: CallbackQuery):
        id = message.from_user.id
        await message.message.answer(text='⏳')
        await bot.send_audio(chat_id=id, audio=natija['music'] , caption="VIDEO Musiqasi")

    await message.answer(text='⏳')
    await bot.send_video (chat_id=id, video=natija['video'],reply_markup=tugma, caption="Dasturchi : https://t.me/Pythonchi_UZB")

