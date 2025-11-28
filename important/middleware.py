#==============Теневой бан=====================================
from typing import Any, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User

CACHE = {
    "banned": [254443334, 214454432, 112221212],
}


class ShadowBanMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any]
    ) -> Any:
        
        user: User = data.get("event_from_user")
        if user is not None:
            if user.id in CACHE.get("banned"):
                return

        return await handler(event, data)
    
dp.update.middleware(ShadowBanMiddleware())

#==============Троттлинг=======================
from typing import Any, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User
from cachetools import TTLCache

CACHE = TTLCache(maxsize=10_000, ttl=5)  # Максимальный размер кэша - 10000 ключей, а время жизни ключа - 5 секунд

class ThrottlingMiddleware(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: dict[str, Any],
    ) -> Any:
        user: User = data.get("event_from_user")

        if user.id in CACHE:
            return

        CACHE[user.id] = True

        return await handler(event, data)
    
dp.update.middleware(ThrottlingMiddleware())
# pip install cachetools

#=================Декорирование миддлварей-функций====================
@some_router.message.outer_middleware()
async def some_middleware(
    handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
    event: TelegramObject,
    data: dict[str, Any]
) -> Any:
        logger.debug("Вошли в миддлварь")

        result = await handler(event, data)

        logger.debug("Выходим из миддлвари")

        return result

