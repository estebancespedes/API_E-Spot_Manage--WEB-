# importaciones de librerias
from sqlalchemy import Column, UUID, VARCHAR, TEXT, ForeignKey
from uuid import uuid4

from sqlalchemy.orm import relationship

# importación del modelo base
from src.database.base_class import Base


class reporte(Base):
    """
    Tabla etiqueta
        atributos:
        id_reporte: uuid
        nombre: TEXT
        id_evento: uuid
    """

    __table_args__ = {"schema": "e_spot_schema"}

    id_reporte = Column(UUID, primary_key=True, default=uuid4())
    nombre = Column(TEXT, nullable=False)
    id_evento = Column(
        UUID, ForeignKey("e_spot_schema.evento.id_evento"), nullable=False
    )

    # relaciones
    evento = relationship("evento", back_populates="reportes")
