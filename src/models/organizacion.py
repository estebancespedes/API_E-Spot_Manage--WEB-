# importaciones de librerias
from sqlalchemy import Column, UUID, VARCHAR, BOOLEAN
from uuid import uuid4

from sqlalchemy.orm import relationship

# importación del modelo base
from src.models.relaciones_tablas import organizaciones_eventos
from src.database.base_class import Base


class organizacion(Base):
    """
    Tabla organizacion:
        Atributos:
            id_organizacion:uuid
            nombre : varchar(50)
    """

    __table_args__ = {'schema': 'e_spot_schema'}

    id_organizacion = Column(UUID, primary_key=True, default=uuid4())
    nombre = Column(VARCHAR(50), nullable=False)
    is_verified = Column(BOOLEAN, nullable=False, default=False)

    # relaciones
    usuarios = relationship("usuario", back_populates="organizacion")
    eventos = relationship(
        "evento", secondary=organizaciones_eventos, back_populates="organizaciones"
    )
