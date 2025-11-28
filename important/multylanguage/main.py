from lexicon.lexicon_en import LEXICON_EN
from lexicon.lexicon_ru import LEXICON_RU
from middlewares.i18n import TranslatorMiddleware
# ...

translations = {
    'default': 'ru',
    'en': LEXICON_EN,
    'ru': LEXICON_RU,
}

async def main():
    
    # ...
    dp.update.middleware(TranslatorMiddleware())
    await dp.start_polling(bot, translations=translations)