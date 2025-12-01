import logging
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.fsm.context import FSMContext
from aiogram.types import TelegramObject

logger = logging.getLogger(__name__)


class SomeMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:

        state: FSMContext = data.get('state')
        user_state = await state.get_state()
        user_data = await state.get_data()
        
        logger.debug('User state is %s, user data is %s', user_state, user_data)

        return await handler(event, data)