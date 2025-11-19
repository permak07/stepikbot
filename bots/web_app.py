import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart,Command
from aiogram.types import (
    KeyboardButton,
    KeyboardButtonRequestChat,
    KeyboardButtonRequestUser,
    KeyboardButtonRequestUsers,
    Message,
    ReplyKeyboardMarkup,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types.web_app_info import WebAppInfo

bot=Bot(token=os.getenv('BOT_TOKEN'))
dp=Dispatcher()

# Создаём кнопку
web_app_btn = KeyboardButton(
    text='Start Web App',
    web_app=WebAppInfo(url="https://stepik.org/")
)
# Создаём объект клавиатуры
web_app_keyboard = ReplyKeyboardMarkup(
    keyboard=[[web_app_btn]],
    resize_keyboard=True
)


# Этот хэндлер будет срабатывать на команду "/web_app"
@dp.message(Command(commands='web_app'))
async def process_web_app_command(message: Message):
    await message.answer(
        text='Экспериментируем со специальными кнопками',
        reply_markup=web_app_keyboard
    )