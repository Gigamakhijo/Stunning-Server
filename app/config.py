from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    mysql_host: str = "localhost"
    mysql_user: str = "MYSQL_USER"
    mysql_password: str = "MYSQL_PASSWORD"
    mysql_db: str = "MYSQL_DB"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
