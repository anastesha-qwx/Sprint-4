# Автотесты для BooksCollector (Sprint 4)

Проект содержит автотесты для класса `BooksCollector`.

## Что проверяется

- Добавление книги (`add_new_book`)
- Установка жанра (`set_book_genre`)
- Получение жанра книги (`get_book_genre`)
- Список книг по жанру (`get_books_in_genre`)
- Получение всего словаря жанров (`get_books_genre`)
- Фильтрация по возрастному рейтингу (`get_books_for_children`)
- Добавление в избранное (`add_book_in_favorites`)
- Удаление из избранного (`delete_book_from_favorites`)
- Получение списка избранного (`get_list_of_favorites_books`)

## Реализованные тесты

- `test_add_new_book_adds_book`  
- `test_add_new_book_invalid_name` (пустая строка и более 40 символов)  
- `test_set_book_genre_valid`  
- `test_set_book_genre_invalid`  
- `test_get_books_with_specific_genre`  
- `test_get_books_genre_returns_dict`  
- `test_get_books_for_children_filters_age_rating`  
- `test_add_book_to_favorites`  
- `test_get_list_of_favorites_books_empty_by_default`  
- `test_delete_book_from_favorites`  

используется **pytest** и **параметризация**.
