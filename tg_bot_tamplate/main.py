from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
# ...

bot = Bot(token=config.bot.token)
dp = Dispatcher()

some_var_1 = 1
some_var_2 = 'Some text'

dp.workflow_data.update({'my_int_var': some_var_1, 'my_text_var': some_var_2})

# ...
@router.message(CommandStart())
async def process_start_command(message: Message, my_int_var, my_text_var):
    await message.answer(text=str(my_int_var))
    await message.answer(text=my_text_var)









from config.config import Config, load_config

config: Config = load_config('.env')
bot_token = config.bot.token           # Сохраняем токен в переменную bot_token
superadmin = config.bot.admin_ids[0]   # Сохраняем ID админа в переменную superadmin