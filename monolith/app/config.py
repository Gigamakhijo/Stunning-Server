from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    mysql_host: str = "127.0.0.1"
    mysql_user: str = "MYSQL_USRER"
    mysql_password: str = "MYSQL_PASSWORD"
    mysql_db: str = "MYSQL_DB"

    auth0_audience: str = "todos"
    auth0_domain: str = ""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
