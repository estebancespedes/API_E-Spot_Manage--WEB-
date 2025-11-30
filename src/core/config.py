from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "API Manager E-Spot App"
    PROJECT_VERSION: str = "0.1.0"
    PROJECT_DESCRIPTION: str = (
        "API-Rest para la gestion de datos en la aplicacion E-Spot."
    )
    DATABASE_URL: str
    SECRETAPI_KEY: str
    ALGORITHM: str

    class Config:
        env_file = ".env"


settings = Settings()
