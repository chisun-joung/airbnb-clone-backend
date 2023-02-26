import strawberry
import typing


@strawberry.type
class Movie:
    pk: int
    title: str
    year: int
    rating: int


movies_db = [
    Movie(pk=1, title="Inception", year=2010, rating=8),
]


def movies():
    return movies_db


def movie(pk: int):
    return movies_db[pk - 1]


def addMovie(title: str, year: int, rating: int):
    movie = Movie(pk=len(movies_db) + 1, title=title, year=year, rating=rating)
    movies_db.append(movie)
    return movie


@strawberry.type
class Query:
    movies: typing.List[Movie] = strawberry.field(resolver=movies)
    movie: Movie = strawberry.field(resolver=movie)


@strawberry.type
class Mutation:
    addMovie: Movie = strawberry.mutation(resolver=addMovie)


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
)
