class BooksCollector:
    def __init__(self):
       
        self.books_genre = {}
        self.favorites = []
        self.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        self.genre_age_rating = ['Ужасы', 'Детективы']
    
    def add_new_book(self, name):
        """Добавить новую книгу с пустым жанром, если её ещё нет и длина имени 1…40."""
        if not self.books_genre.get(name) and 0 < len(name) < 41:
            self.books_genre[name] = ''

    def set_book_genre(self, name, genre):
        """Назначить существующей книге один из допустимых жанров."""
        if name in self.books_genre and genre in self.genre:
            self.books_genre[name] = genre

    def get_book_genre(self, name):
        """Получить жанр книги (или None, если книги нет)."""
        return self.books_genre.get(name)

    def get_books_list(self) -> list:
        """Возвращает список всех добавленных книг."""
        return list(self.books_genre.keys())

    def get_books_with_specific_genre(self, genre):
        """Внутренний метод: вернуть все книги заданного жанра."""
        books_with_specific_genre = []
        if genre in self.genre:
            for name, book_genre in self.books_genre.items():
                if book_genre == genre:
                    books_with_specific_genre.append(name)
        return books_with_specific_genre

    def get_books_in_genre(self, genre: str) -> list:
        """(Тестовый обёрточный метод) Возвращает список книг в указанном жанре."""
        return self.get_books_with_specific_genre(genre)

    def get_books_genre(self):
        """Вернуть весь словарь «книга - жанр»."""
        return self.books_genre

    def get_books_for_children(self):
        """
        Вернуть список книг, жанр которых разрешён для детей:
        допускаются жанры из self.genre, кроме тех, что в self.genre_age_rating.
        """
        books_for_children = []
        for name, book_genre in self.books_genre.items():
            if book_genre in self.genre and book_genre not in self.genre_age_rating:
                books_for_children.append(name)
        return books_for_children

    def add_book_in_favorites(self, name):
        """Добавить книгу в избранное, если она существует и ещё не в избранном."""
        if name in self.books_genre and name not in self.favorites:
            self.favorites.append(name)

    def delete_book_from_favorites(self, name):
        """Удалить книгу из избранного, если она там есть."""
        if name in self.favorites:
            self.favorites.remove(name)

    def get_list_of_favorites_books(self):
        """Вернуть список всех избранных книг."""
        return self.favorites

