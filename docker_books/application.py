from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
import json
from settings import settings

app = FastAPI()


class Book(BaseModel):
    id: int
    title: str
    autor: str
    year: int
    pages: int


@app.get("/books/")
def all_books() -> List[Book]:
    with open(settings.data_file_path) as file:
        books = json.load(file)
        return books


@app.get("/books/{id}")
def get_book(id: int):
    with open(settings.data_file_path) as file:
        books = json.load(file)

    for book in books:
        if book["id"] == id:
            return book


@app.post("/books/")
def create_book(book: Book) -> dict[str, str]:
    with open(settings.data_file_path) as file:
        books = json.load(file)

    books.append(book.model_dump())

    with open(settings.data_file_path, "w") as file:
        json.dump(books, file, indent=4)
    return {"message": "Книга додана успішно"}
