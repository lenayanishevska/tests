import typing as t

from telebot import types


def build_reply_markup(button_list: t.Iterable[str],one_time_keyboard: bool = True,row_width: int = 2,resize_keyboard: bool = True) -> types.ReplyKeyboardMarkup:

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=one_time_keyboard,resize_keyboard=resize_keyboard,row_width=row_width,)

    buttons = [types.KeyboardButton(i) for i in button_list]
    markup.add(*buttons)

    return markup
