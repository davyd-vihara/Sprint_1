class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

class Comedy(Movies):
    def __init__(self):
        super().__init__()
        self.genre = "Комедия"

    def add_movie(self, movie):
        super().add_movie(movie)
        return f'{self.genre}: {self.movies}'

class Drama(Movies):
    def __init__(self):
        super().__init__()
        self.genre = "Драма"

    def add_movie(self, movie):
        super().add_movie(movie)
        return f'{self.genre}: {self.movies}'

comedy = Comedy()
print(comedy.add_movie('Большой куш'))

drama = Drama()
print(drama.add_movie('Оружейный барон'))