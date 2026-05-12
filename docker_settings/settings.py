from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    secret_text: str = "hello"
    password: Optional[str] = None

    min_num: int = 10
    max_num: int = 100

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()

print(settings.password)
