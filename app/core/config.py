from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    DATABASE_URL: str
    GOOGLE_API_KEY: str
    MIGRATION: bool 
    LLM_MODEL: str 
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str


settings = Settings()