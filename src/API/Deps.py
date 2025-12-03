from typing import Generator

# Importar todos los modelos para que SQLAlchemy pueda resolver las relaciones
from src.database import models
from src.database.session import AsyncLocalSession


async def get_db() -> Generator:
    async with AsyncLocalSession() as db:
        yield db
