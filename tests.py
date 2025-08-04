import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

# Проверяем, что можно добавить две книги
def test_add_new_book_add_two_books(collector):
    collector.add_new_book('Гарри Поттер')
    collector.add_new_book('Властелин колец')
    assert len(collector.get_books_genre()) == 2

# Проверяем, что у добавленной книги жанр пустой
def test_add_new_book_one_book_has_no_genre(collector):
    collector.add_new_book('Гарри Поттер')
    assert collector.books_genre['Гарри Поттер'] == ''

# Проверяем, что книгу с названием >40 символов нельзя добавить
def test_add_new_book_name_of_book_over_40_symb_not_added(collector):
    collector.add_new_book('Гарри Поттер. Гарри Поттер. Гарри Поттер.')
    assert len(collector.books_genre) == 0

# Проверяем, что жанр успешно установлен
def test_set_book_genre_one_book_genre_is_added(collector):
    collector.add_new_book('Оно')
    collector.set_book_genre('Оно', 'Ужасы')
    assert collector.books_genre['Оно'] == 'Ужасы'

# Проверяем, что по имени книги можно получить жанр
def test_get_book_genre_one_book_got_genre(collector):
    collector.add_new_book('Властелин колец')
    collector.set_book_genre('Властелин колец', 'Фантастика')
    assert collector.get_book_genre('Властелин колец') == 'Фантастика'

# Проверяем, что можно получить список книг по определённому жанру
def test_get_books_with_specific_genre_two_books_detective(collector):
    collector.add_new_book('Восточный экспресс')
    collector.set_book_genre('Восточный экспресс', 'Детективы')
    collector.add_new_book('Десять негретят')
    collector.set_book_genre('Десять негретят', 'Детективы')
    assert collector.get_books_with_specific_genre('Детективы') == ['Восточный экспресс', 'Десять негретят']

# Проверяем, что возвращается словарь книг с жанрами
def test_get_books_genre_of_two_books(collector):
    collector.add_new_book('Дракула')
    collector.set_book_genre('Дракула', 'Ужасы')
    collector.add_new_book('Восточный экспресс')
    collector.set_book_genre('Восточный экспресс', 'Детективы')
    assert collector.get_books_genre() == {
        'Дракула': 'Ужасы',
        'Восточный экспресс': 'Детективы'
    }

# Проверяем, что в список книг для детей не попадают книги с возрастным рейтингом
def test_get_books_for_children_one_book_mult(collector):
    collector.add_new_book('Золушка')
    collector.set_book_genre('Золушка', 'Мультфильмы')
    collector.add_new_book('Оно')
    collector.set_book_genre('Оно', 'Ужасы')
    assert collector.get_books_for_children() == ['Золушка']

# Проверяем, что можно добавить книгу в избранное
def test_add_book_in_favorites_one_book_added(collector):
    collector.add_new_book('Гарри Поттер')
    collector.add_book_in_favorites('Гарри Поттер')
    assert 'Гарри Поттер' in collector.favorites

# Проверяем, что можно удалить книгу из избранного
def test_delete_book_from_favorites_deleted(collector):
    collector.add_new_book('Гарри Поттер')
    collector.add_book_in_favorites('Гарри Поттер')
    collector.delete_book_from_favorites('Гарри Поттер')
    assert 'Гарри Поттер' not in collector.favorites

# Проверяем, что можно получить список избранных книг
def test_get_list_of_favorites_books_got_list(collector):
    collector.add_new_book('Властелин колец')
    collector.add_new_book('Гарри Поттер')
    collector.add_book_in_favorites('Властелин колец')
    collector.add_book_in_favorites('Гарри Поттер')
    assert collector.get_list_of_favorites_books() == ['Властелин колец', 'Гарри Поттер']
