# importaciones de librerias
from sqlalchemy import Column, UUID, VARCHAR
from uuid import uuid4

from sqlalchemy.orm import relationship

# importación del modelo base
from src.database.base_class import Base


class rol(Base):
    """
    Tabla roles
        atributos:
        id_rol: uuid
        nombre: varchar(50)
    """

    id_rol = Column(UUID, primary_key=True, default=uuid4())
    nombre = Column(VARCHAR(50), nullable=False)

    # relaciones
    usuarios = relationship("usuario", back_populates="rol")
