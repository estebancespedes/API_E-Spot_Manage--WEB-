# importaciones de librerias
from turtle import back
from sqlalchemy import Column, UUID, TEXT, ForeignKey, VARCHAR, Nullable
from sqlalchemy.orm import relationship
from uuid import uuid4

# importacion del modelo base
from src.database.base_class import Base


class ciudad(Base):
    id_ciudad = Column(UUID, primary_key=False, default=uuid4())
    id_pais = Column(UUID, ForeignKey("region.id_region"), nullable=False)
    nombre = Column(VARCHAR(50), nullable=False)
    descripcion = Column(TEXT, nullable=False)

    # relaciones
    region = relationship("region", back_populates="ciudades")
        # agregar relacion con direccion