from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    host: str = "localhost"
    port: int = 8080

    max_books: int | None = None
    data_file_path: str = "./books.json"

settings = Settings()
