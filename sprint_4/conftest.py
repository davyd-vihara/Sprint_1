import pytest
from main import BooksCollector


@pytest.fixture(scope='function')
def one_book():
    collector = BooksCollector()

    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

    return collector


@pytest.fixture(scope='function')
def several_books():
    collector = BooksCollector()

    collector.add_new_book('Шрек')
    collector.set_book_genre('Шрек', 'Мультфильмы')
    collector.add_new_book('Оно')
    collector.set_book_genre('Оно', 'Ужасы')
    collector.add_new_book('Гарри Поттер')
    collector.set_book_genre('Гарри Поттер', 'Фантастика')

    return collector

