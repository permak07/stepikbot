# =====================================================================версия 1 =========================================================================

# from aiogram import Bot, Dispatcher,F
# from aiogram.filters import Command
# from aiogram.types import Message

# # Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
# BOT_TOKEN = '8581071633:AAFEafdUqqXXiJ9XfPW2cUTanxTbWUQqnZA'

# # Создаем объекты бота и диспетчера
# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher()


# # Этот хэндлер будет срабатывать на команду "/start"
# @dp.message(Command(commands="start"))
# async def process_start_command(message: Message):
#     await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# # Этот хэндлер будет срабатывать на команду "/help"
# @dp.message(Command(commands="help"))
# async def process_help_command(message: Message):
#     await message.answer(
#         'Напиши мне что-нибудь и в ответ '
#         'я пришлю тебе твое сообщение'
#     )

# @dp.message(F.voice)
# async def process_sent_voice(message: Message):
#     # Выводим апдейт в терминал
#     print(message)
#     # Отправляем сообщение в чат, откуда пришло голосовое
#     await message.answer(text='Вы прислали голосовое сообщение!')

# # Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# # кроме команд "/start" и "/help"
# @dp.message()
# async def send_echo(message: Message):
#     await message.reply(text=message.text)


# if __name__ == '__main__':
#     dp.run_polling(bot)

# ===================================================================== версия 2 =========================================================================
# from aiogram import Bot , Dispatcher, F
# from aiogram.filters import Command
# from aiogram.types import Message
# BOT_TOKEN='8581071633:AAFEafdUqqXXiJ9XfPW2cUTanxTbWUQqnZA'
# bot=Bot(token=BOT_TOKEN)
# dp=Dispatcher()

# async def process_start_command(message: Message):
#     await message.answer('Привет!\nМеня зовут эхо-бот!\nНапиши мне что-нибудь')

# async def process_help_command(message: Message):
#     await message.answer(
#         'Напиши мне что-нибудь и в ответ '
#         'я пришлю тебе твоё сообщение'
#     )
# async def send_photo_echo(message: Message):
#     await message.reply_photo(message.photo[0].file_id)

# @dp.message(F.voice)
# async def process_sent_voice(message: Message):
#     # Выводим апдейт в терминал
#     print(message)
#     # Отправляем сообщение в чат, откуда пришло голосовое
#     await message.answer(text='Вы прислали голосовое сообщение!')

# async def send_echo(message:Message):
#     await message.reply(text=message.text)

# dp.message.register(process_start_command, Command(commands='start'))
# dp.message.register(process_help_command, Command(commands='help'))
# dp.message.register(send_photo_echo, F.photo)
# dp.message.register(send_echo)

# if __name__=='__main__':
#     dp.run_polling(bot)

# # ===================================================================== версия 3 =========================================================================
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import os

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather

# Создаем объекты бота и диспетчера
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands='start'))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )


# Этот хэндлер будет срабатывать на любые ваши сообщения, кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(
            text='Данный тип апдейтов не поддерживается '
                 'методом send_copy'
        )


if __name__ == '__main__':
    dp.run_polling(bot)