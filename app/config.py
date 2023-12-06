from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_hostname: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int = 10000000
    aws_access_key_id: str
    aws_secret_access_key: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
