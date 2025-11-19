import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           Message,  BotCommand, BotCommandScopeDefault)
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder


class TelegramBot:
    def __init__(self, bot: Bot, dp: Dispatcher):
        self.bot = bot
        self.dp = dp
        self.keyboard = self.create_keyboard()

    @staticmethod
    def create_keyboard():
        # Сюда вставляйте код из примеров
        # ---------------------------------------------------

        # Создаем список списков с кнопками
        keyboard: list[list[KeyboardButton]] = [
            [KeyboardButton(text=str(i)) for i in range(1, 4)],
            [KeyboardButton(text=str(i)) for i in range(4, 7)]
        ]

        keyboard.append([KeyboardButton(text='7')])

        # Создаем объект клавиатуры, добавляя в него кнопки
        my_keyboard = ReplyKeyboardMarkup(
            keyboard=keyboard,
            resize_keyboard=True
        )

        # ---------------------------------------------------
        # Это строку не удалять
        return my_keyboard

    async def set_menu_commands(self):
        commands = [
            BotCommand(command="/start", description="Начать"),
        ]
        await self.bot.set_my_commands(commands, scope=BotCommandScopeDefault())

    def register_handlers(self):
        self.dp.message.register(self.process_start_command, CommandStart())

    async def process_start_command(self, message: Message):
        await message.answer(
            text='Вот такая получается клавиатура',
            reply_markup=self.keyboard)

    async def run(self):
        self.register_handlers()
        await self.set_menu_commands()

        await self.bot.delete_webhook(drop_pending_updates=True)
        await self.dp.start_polling(BOT)
        await self.bot.session.close()


if __name__ == '__main__':
    TOKEN = "8581071633:AAFEafdUqqXXiJ9XfPW2cUTanxTbWUQqnZA"
    BOT = Bot(TOKEN)
    DP = Dispatcher()

    telegram_bot = TelegramBot(BOT, DP)
    asyncio.run(telegram_bot.run())
