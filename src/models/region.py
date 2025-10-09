# importaciones de librerias
from sqlalchemy import Column, UUID, ForeignKey, VARCHAR
from sqlalchemy.orm import relationship
from uuid import uuid4

# importacion del modelo base
from src.database.base_class import Base


class region(Base):
    """
    Tabla region:
    Se usa como directorio de regiones para las ubicaciones.
    Atributos:
        id_region : UUID
        id_pais : UUID
        nombre : varchar(50)
    """

    __tablename__ = "region"

    id_region = Column(UUID, primary_key=True, default=uuid4())
    id_pais = Column(UUID, ForeignKey("pais.id_pais"), nullable=False)
    nombre = Column(VARCHAR(50), index=True, nullable=False)

    # relaciones
    pais = relationship("pais", back_populates="regiones")
