import logging
import os

logger=logging.getLogger(__name__)

# Функция, возвращающая строку с текстом страницы и её размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    end = min(start + size, len(text))
    page_text = text[start:end]
    punctuation = ',.!:;?'
    for i in range(min(size, len(page_text)) - 1, -1, -1):
        if page_text[i] in punctuation:
            left_ok = (i == 0 or page_text[i-1] not in punctuation)
            right_ok = (i == len(page_text)-1 or page_text[i+1] not in punctuation)
            
            if left_ok and right_ok:
                return page_text[:i+1], i+1
    
    return page_text, len(page_text)

text = 'Да? Вы точно уверены? Может быть, вам это показалось?.. Ну, хорошо, приходите завтра, тогда и посмотрим, что можно сделать. И никаких возражений! Завтра, значит, завтра!'

print(*_get_part_text(text, 22, 145), sep='\n')


# Функция, формирующая словарь книги
def prepare_book(path: str, page_size: int = 1050) -> dict[int, str]:
    book = {}
    with open(path, "r", encoding='utf-8') as file:
        text = file.read()
        count = 0
        page_number = 1
        
        while count < len(text):
            page_text, chars_processed = _get_part_text(text, count, page_size)
            page_text = page_text.lstrip()
            
            if page_text:
                book[page_number] = page_text
                page_number += 1
            
            count += chars_processed
    
    return book