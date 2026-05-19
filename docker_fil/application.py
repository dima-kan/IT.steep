from fastapi import FastAPI
import json
from pydantic import BaseModel

app = FastAPI()


class Film(BaseModel):
    title: str
    year: int
    id: int
    director: str


@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    with open("films.json", "r") as file:
        movies = json.load(file)

    for movie in movies:
        if movie["id"] == movie_id:
            return movie


@app.post("/movies")
def create_movie(movie: Film):
    with open("films.json", "r") as file:
        movies = json.load(file)

    movies.append(movie.model_dump())

    with open("films.json", "w") as file:
        json.dump(movies, file, indent=4)
    return {"massage": "film added"}


@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    with open("films.json", "r") as file:
        movies = json.load(file)

    for movie in movies:
        if movie["id"] == movie_id:
            movies.remove(movie)

            with open("films.json", "w") as file:
                json.dump(movies, file, indent=4)
            return movie
