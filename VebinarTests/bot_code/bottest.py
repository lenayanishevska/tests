import unittest
from unittest.mock import MagicMock, patch, Mock
from bot import MAIN_SCREEN_BUTTON, start
from utils import build_reply_markup
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


class TestHandlers(unittest.TestCase):

    def test_start_message_handler_initial(self):
        bot_mock = MagicMock()
        message_mock = MagicMock(chat=MagicMock(id=123))
        with patch("bot.telebot.TeleBot") as bot_class_mock:
            bot_class_mock.return_value = bot_mock
            start(message_mock)
            bot_mock.send_message.assert_called_once_with(
                123,
                "HELLO",
                reply_markup=build_reply_markup(MAIN_SCREEN_BUTTON),
            )

    def test_start_message_handler_final(self):
        markup = build_reply_markup(MAIN_SCREEN_BUTTON)
        self.assertIsInstance(markup, ReplyKeyboardMarkup)

        self.assertEqual(markup.one_time_keyboard, True)
        self.assertEqual(markup.row_width, 2)
        self.assertEqual(markup.resize_keyboard, True)

        expected_buttons = [KeyboardButton(button) for button in MAIN_SCREEN_BUTTON]
        self.assertEqual(markup.keyboard, [expected_buttons])


if __name__ == '__main__':
    unittest.main()
    