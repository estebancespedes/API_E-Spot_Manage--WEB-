# importaciones de librerias
from sqlalchemy import Column, UUID, VARCHAR
from uuid import uuid4

from sqlalchemy.orm import relationship

# importación del modelo base
from src.database.base_class import Base

from src.models.relaciones_tablas import etiquetas_eventos


class etiqueta(Base):
    """
    Tabla etiqueta
        atributos:
        id_etiqueta: uuid
        nombre: varchar(50)
    """

    __tablename__ = "etiqueta"
    __table_args__ = {"schema": "e_spot_schema"}

    id_etiqueta = Column(UUID, primary_key=True, default=uuid4())
    nombre = Column(VARCHAR(50), nullable=False)

    # relaciones
    eventos = relationship(
        "evento", secondary=etiquetas_eventos, back_populates="etiquetas"
    )
