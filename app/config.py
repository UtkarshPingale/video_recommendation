from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    flic_token: str
    api_base_url: str

    class Config:
        env_file = ".env"

settings = Settings()
