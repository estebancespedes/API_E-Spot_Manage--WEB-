# importaciones de librerias
from sqlalchemy import Column, UUID, VARCHAR
from uuid import uuid4

from sqlalchemy.orm import Relationship

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

    id_etiqueta = Column(UUID, primary_key=True, default=uuid4())
    nombre = Column(VARCHAR(50), nullable=False)

    # relaciones
    evento = Relationship(
        "evento", secondary=etiquetas_eventos, back_populates="etiquetas"
    )
