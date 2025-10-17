from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
class TestBooksCollector:

    # Проверяет, что при добавлении второй книги общее количество книг увеличивается до двух. one_book фикстура которая содержит одну книгу с указанным жанром
    def test_add_new_book_adds_two_books(self, one_book):

        one_book.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        assert len(one_book.get_books_genre()) == 2

    # Проверяет, что метод корректно устанавливает жанр книги
    def test_set_book_genre_sets_correct_genre(self, one_book):

        assert one_book.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    # Проверяет, что новая книга без жанра имеет пустое значение жанра
    def test_set_book_genre_does_not_affect_other_books(self):
        collector = BooksCollector()

        collector.add_new_book('Кот в сапогах')
        assert collector.get_book_genre('Кот в сапогах') == ''

    # Проверяет, что книга добавляется только при длине названия от 1 до 40 символов
    @pytest.mark.parametrize('name, expected', [
        ('V', True),  # 1 символ - должна добавиться
        ('r' * 40, True),  # 40 символов - должна добавиться
        ('', False),  # 0 символов - не должна добавиться
        ('z' * 41, False)  # 41 символ - не должна добавиться
    ])
    def test_add_new_book_respects_name_length_limit(self, name, expected):
        collector = BooksCollector()
        collector.add_new_book(name)

        assert (name in collector.get_books_genre()) == expected

    # Проверяет, что метод возвращает список книг заданного жанра. Фикстура several_book со списком из трёх книг.
    def test_get_books_with_specific_genre_returns_correct_list(self, several_books):

        assert several_books.get_books_with_specific_genre('Мультфильмы') == ['Шрек']

    # Проверяет, что книги с возрастным рейтингом не попадают в список детских
    def test_get_books_for_children_excludes_age_restricted_genres(self, several_books):
        children_books = several_books.get_books_for_children()
        expected_books = ['Шрек', 'Гарри Поттер']

        assert children_books == expected_books

    # Проверяет, что жанр книги корректно обновляется на допустимые значения
    @pytest.mark.parametrize('genre', ['Фантастика', 'Комедии', 'Ужасы', 'Детективы', 'Мультфильмы'])
    def test_set_book_genre_updates_existing_genre(self, genre, one_book):
        book_name = 'Гордость и предубеждение и зомби'
        one_book.set_book_genre(book_name, genre)

        assert one_book.get_book_genre(book_name) == genre

    # Проверяет, что при установке недопустимого жанра значение не изменяется
    def test_set_book_genre_does_not_set_invalid_genre(self, one_book):
        one_book.set_book_genre('Гордость и предубеждение и зомби', 'Несуществующий жанр')

        assert one_book.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    # Проверяет, что книга корректно добавляется в избранное
    def test_add_book_in_favorites_adds_book(self, one_book):
        one_book.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert one_book.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']

    # Проверяет, что книга корректно удаляется из избранного
    def test_delete_book_from_favorites_removes_book(self, one_book):
        one_book.add_book_in_favorites('Гордость и предубеждение и зомби')
        one_book.delete_book_from_favorites('Гордость и предубеждение и зомби')

        assert one_book.get_list_of_favorites_books() == []

    # Проверяет, что список избранных книг возвращается корректно
    def test_get_list_of_favorites_books_returns_correct_list(self, one_book):
        one_book.add_new_book('Война и мир')
        one_book.add_book_in_favorites('Гордость и предубеждение и зомби')
        one_book.add_book_in_favorites('Война и мир')

        assert one_book.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби', 'Война и мир']
