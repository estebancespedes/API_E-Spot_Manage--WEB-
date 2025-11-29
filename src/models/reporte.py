# importaciones de librerias
from sqlalchemy import Column, UUID, VARCHAR, TEXT, ForeignKey
from uuid import uuid4

from sqlalchemy.orm import Relationship

# importación del modelo base
from src.database.base_class import Base


class etiqueta(Base):
    """
    Tabla etiqueta
        atributos:
        id_reporte: uuid
        nombre: TEXT
        id_evento: uuid
    """

    id_reporte = Column(UUID, primary_key=True, default=uuid4())
    nombre = Column(TEXT, nullable=False)
    id_evento = Column(UUID, ForeignKey("evento.id_evento"), nullable=False)

    # relaciones
    evento = Relationship(
        "evento", back_populates="reportes"
    )
