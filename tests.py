import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

def test_add_new_book_adds_book(collector):
    collector.add_new_book("Гарри Поттер")
    assert "Гарри Поттер" in collector.get_books_list()

@pytest.mark.parametrize("name", ["", "A" * 41])
def test_add_new_book_invalid_name(collector, name):
    collector.add_new_book(name)
    assert name not in collector.get_books_list()

def test_set_book_genre_valid(collector):
    collector.add_new_book("Властелин колец")
    collector.set_book_genre("Властелин колец", "Фантастика")
    assert collector.get_book_genre("Властелин колец") == "Фантастика"

def test_set_book_genre_invalid(collector):
    collector.add_new_book("Властелин колец")
    collector.set_book_genre("Властелин колец", "Роман")
    assert collector.get_book_genre("Властелин колец") == ""

def test_get_books_with_specific_genre(collector):
    collector.add_new_book("Гарри Поттер")
    collector.set_book_genre("Гарри Поттер", "Фантастика")
    collector.add_new_book("Властелин колец")
    collector.set_book_genre("Властелин колец", "Фантастика")
    assert set(collector.get_books_in_genre("Фантастика")) == {"Гарри Поттер", "Властелин колец"}

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

def test_add_book_to_favorites(collector):
    collector.add_new_book("Айболит")
    collector.add_book_in_favorites("Айболит")
    assert "Айболит" in collector.get_list_of_favorites_books()

def test_get_list_of_favorites_books_empty_by_default(collector):
    assert collector.get_list_of_favorites_books() == []

def test_delete_book_from_favorites(collector):
    collector.add_new_book("Айболит")
    collector.add_book_in_favorites("Айболит")
    assert "Айболит" in collector.get_list_of_favorites_books()
    collector.delete_book_from_favorites("Айболит")
    assert "Айболит" not in collector.get_list_of_favorites_books()




   
