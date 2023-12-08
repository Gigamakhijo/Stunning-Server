from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_hostname: str = "hostname"
    secret_key: str = "secret_key"
    algorithm: str = "algorithm"
    access_token_expire_minutes: int = 100000
    aws_region: str = "region"
    bucket_name: str = "bucket_name"
    aws_access_key_id: str = "access_key_id"
    aws_secret_access_key: str = "secret_access_key"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
