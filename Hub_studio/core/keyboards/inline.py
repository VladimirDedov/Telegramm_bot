from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_callback_btns(
        *,
        btns: dict,
        sizes: tuple=(2,),):
    keyboard = InlineKeyboardBuilder()

    for text, data in btns.items():
        keyboard.add(InlineKeyboardButton(text=text, callback_data=data))#callback_data - отправляется в чат, можно поймать хэндлером события callback
    return keyboard.adjust(*sizes).as_markup()
