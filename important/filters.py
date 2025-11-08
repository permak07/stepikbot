#==================Фильтр ChatMemberUpdatedFilter====================
from aiogram import Bot,Dispatcher,F
from aiogram.filters import ChatMemberUpdatedFilter, KICKED
from aiogram.types import ChatMemberUpdated

# ...

# Этот хэндлер будет срабатывать на блокировку бота пользователем
@dp.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=KICKED))
async def process_user_blocked_bot(event: ChatMemberUpdated):
    print(f'Пользователь {event.from_user.id} заблокировал бота')