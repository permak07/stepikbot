# Этот хэндлер срабатывает на команду /start
@user_router.message(CommandStart(), MyTrueFilter())
async def process_start_command(message: Message, i18n: dict[str, str]):
    # Создаём объект инлайн-кнопки
    button = InlineKeyboardButton(
        text=i18n.get("button"),
        callback_data="button_pressed"
    )
    # Создаём объект инлайн-клавиатуры
    markup = InlineKeyboardMarkup(inline_keyboard=[[button]])
    # Отправляем сообщение пользователю
    await message.answer(text=i18n.get("/start"), reply_markup=markup)