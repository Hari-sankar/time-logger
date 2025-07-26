from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    DATABASE_URL: str
    GOOGLE_API_KEY: str
    MIGRATION: bool 
    LLM_MODEL: str 


settings = Settings()