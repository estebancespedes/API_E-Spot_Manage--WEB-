# importacciones de librerias
from sqlalchemy import Column, UUID, VARCHAR
from sqlalchemy.orm import Relationship
from uuid import uuid4

# importacion de base model
from src.database.base_class import Base


class pais(Base):
    """
    Tabla pais:
        Usada como directorio de paises para las ubicaciones.
        Atributos:
            id_pais : UUID
            nombre : varchar(50)
    """

    __tablename__ = "pais"

    id_pais = Column(UUID, primary_key=True, default=uuid4())
    nombre = Column(VARCHAR(50), index=True, nullable=False)

    # relaciones
    regiones = Relationship("region", back_populates="pais")
