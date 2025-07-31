import pytest
from main import BooksCollector  

@pytest.fixture
def collector():
    return BooksCollector()

# ТЕСТЫ НА ДОБАВЛЕНИЕ КНИГ 

@pytest.mark.parametrize("book_name", ["Гарри Поттер", "Властелин колец", "Приключения Буратино"])
def test_add_new_book_and_get_book_genre(collector, book_name):
    collector.add_new_book(book_name)
    assert book_name in collector.get_books_genre()
    assert collector.get_book_genre(book_name) == ""


@pytest.mark.parametrize("book_name", ["Гарри Поттер", ""])
def test_add_book_duplicates_and_empty_name(collector, book_name):
    collector.add_new_book(book_name)
    collector.add_new_book(book_name)  

    if book_name == "":
        assert "" not in collector.get_books_genre()
    else:
        assert list(collector.get_books_genre().keys()).count(book_name) == 1

# ТЕСТЫ НА ЖАНРЫ 

@pytest.mark.parametrize("book_name, genre, expected", [
    ("Гарри Поттер", "Фантастика", "Фантастика"),
    ("Приключения Буратино", "Фантастика", "Фантастика"),
    ("Гарри Поттер", "Неизвестный жанр", ""),
])
def test_set_book_genre_and_get_it(collector, book_name, genre, expected):
    collector.add_new_book(book_name)
    collector.set_book_genre(book_name, genre)
    assert collector.get_book_genre(book_name) == expected


def test_get_books_with_specific_genre_returns_correct_books(collector):
    books = [
        ("Гарри Поттер", "Фантастика"),
        ("Властелин колец", "Фантастика"),
        ("Приключения Буратино", "Фантастика"),
    ]
    for name, genre in books:
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

    result = collector.get_books_with_specific_genre("Фантастика")
    assert set(result) == {"Гарри Поттер", "Властелин колец", "Приключения Буратино"}

# ТЕСТЫ НА ИЗБРАННОЕ 

@pytest.mark.parametrize("book_name", ["Гарри Поттер", "Властелин колец"])
def test_add_and_delete_book_in_favorites(collector, book_name):
    collector.add_new_book(book_name)
    collector.add_book_in_favorites(book_name)

    assert book_name in collector.get_list_of_favorites_books()

    collector.delete_book_from_favorites(book_name)
    assert book_name not in collector.get_list_of_favorites_books()


def test_get_list_of_favorites_books_returns_all_added(collector):
    books = ["Гарри Поттер", "Приключения Буратино"]
    for book in books:
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)

    result = collector.get_list_of_favorites_books()
    assert set(result) == set(books)

# ТЕСТЫ НА КНИГИ ДЛЯ ДЕТЕЙ 

@pytest.mark.parametrize(
    "books, expected_children",
    [
        (
            [("Гарри Поттер", "Фантастика"), ("Приключения Буратино", "Фантастика")],
            {"Гарри Поттер", "Приключения Буратино"},
        ),
        (
            [("Оно", "Ужасы"), ("Шерлок Холмс", "Детектив")],
            set(),
        ),
    ],
)
def test_get_books_for_children(collector, books, expected_children):
    for name, genre in books:
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

    result = set(collector.get_books_for_children())
    assert result == expected_children


   
