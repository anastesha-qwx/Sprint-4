import pytest

def test_add_new_book_adds_book(collector):
    collector.add_new_book("Гарри Поттер")
    assert "Гарри Поттер" in collector.books_genre
    assert collector.books_genre["Гарри Поттер"] == ""

@pytest.mark.parametrize("name", ["", "A"*41])
def test_add_new_book_invalid_name(collector, name):
    collector.add_new_book(name)
    assert name not in collector.books_genre

def test_set_book_genre_valid(collector):
    collector.add_new_book("Гарри Поттер")
    collector.set_book_genre("Гарри Поттер", "Фантастика")
    assert collector.books_genre["Гарри Поттер"] == "Фантастика"

def test_set_book_genre_invalid(collector):
    collector.add_new_book("Гарри Поттер")
    collector.set_book_genre("Гарри Поттер", "Роман")
    assert collector.books_genre["Гарри Поттер"] == ""

def test_get_book_genre_returns_correct_genre(collector):
    collector.add_new_book("Гарри Поттер")
    collector.set_book_genre("Гарри Поттер", "Фантастика")
    assert collector.get_book_genre("Гарри Поттер") == "Фантастика"

def test_get_books_with_specific_genre(collector):
    collector.add_new_book("Гарри Поттер")
    collector.set_book_genre("Гарри Поттер", "Фантастика")
    assert "Гарри Поттер" in collector.get_books_with_specific_genre("Фантастика")

def test_get_books_genre_returns_dict(collector):
    collector.add_new_book("Гарри Поттер")
    assert isinstance(collector.get_books_genre(), dict)

def test_get_books_for_children_filters_age_rating(collector):
    collector.add_new_book("Гарри Поттер")
    collector.set_book_genre("Гарри Поттер", "Фантастика")

    collector.add_new_book("Дракула")
    collector.set_book_genre("Дракула", "Ужасы")

    books = collector.get_books_for_children()
    assert "Гарри Поттер" in books
    assert "Дракула" not in books

def test_add_and_delete_book_in_favorites(collector):
    collector.add_new_book("Гарри Поттер")
    collector.add_book_in_favorites("Гарри Поттер")
    assert "Гарри Поттер" in collector.get_list_of_favorites_books()

    collector.delete_book_from_favorites("Гарри Поттер")
    assert "Гарри Поттер" not in collector.get_list_of_favorites_books()
