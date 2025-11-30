from typing import Generator

# Importar todos los modelos para que SQLAlchemy pueda resolver las relaciones
from src.database import models
from src.database.session import Sessionlocal


def get_db() -> Generator:
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()
