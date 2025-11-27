# importaciones de librerias
from turtle import back
from sqlalchemy import Column, UUID, TEXT, ForeignKey, VARCHAR
from sqlalchemy.orm import Relationship
from uuid import uuid4

# importacion del modelo base
from src.database.base_class import Base


class ciudad(Base):
    """
    Tabla ciudad:
        Usada como directorio de ciudades
        Atributos
            id_ciudad : UUID
            id_region : UUID
            nombre : varchar(50)
            descripcion : TEXT
    """

    __tablename__ = "ciudad"

    id_ciudad = Column(UUID, primary_key=True, default=uuid4())
    id_region = Column(UUID, ForeignKey("region.id_region"), nullable=False)
    nombre = Column(VARCHAR(50), nullable=False)
    descripcion = Column(TEXT, nullable=False)

    # relaciones
    region = Relationship("region", back_populates="ciudades")

    ubicaciones = Relationship("ubicacion", back_populates="ciudad")
