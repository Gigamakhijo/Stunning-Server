from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_hostname: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int = 10000000

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
