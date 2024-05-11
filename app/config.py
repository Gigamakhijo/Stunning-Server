from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    mysql_host: str = "localhost"
    mysql_user: str = "MYSQL_USER"
    mysql_password: str = "MYSQL_PASSWORD"
    mysql_db: str = "MYSQL_DB"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()


class AuthSettings(BaseSettings):
    auth0_domain: str
    auth0_api_audience: str
    auth0_issuer: str
    auth0_algorithms: str

    class Config:
        env_file = ".env"


@lru_cache
def get_auth_settings():
    return AuthSettings()