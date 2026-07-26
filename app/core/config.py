from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "BioMind"
    VERSION: str = "1.0.0"
    ENGINE_NAME: str = "BCRE"


settings = Settings()
