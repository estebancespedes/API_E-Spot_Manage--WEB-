# importacciones de librerias
from sqlalchemy import Column, UUID, VARCHAR
from sqlalchemy.orm import relationship
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

    id_pais = Column(UUID, primary_key=True, default=uuid4())
    nombre = Column(VARCHAR(50), index=True, nullable=False)

    # relaciones
    regiones = relationship("region", back_populates="pais")
