from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    KAFKA_BOOTSTRAP: str
    KAFKA_TOPIC: str


    model_config = SettingsConfigDict(env_file=".env")