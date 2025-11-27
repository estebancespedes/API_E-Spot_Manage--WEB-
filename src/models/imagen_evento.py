# importaciones de librerias
from datetime import datetime
from sqlalchemy import Column, UUID, VARCHAR, DateTime, ForeignKey
from uuid import uuid4

from sqlalchemy.orm import Relationship

# importación del modelo base
from src.database.base_class import Base


class imagen_evento(Base):
    """
    Tabla imagen_evento:
        atributos:
            - id_imagen : uuid
            - url : varchar
            - id_evento : uuid
            - id_usuario_crea : uuid
            - fecha_creacion : datetime
    """

    __tablename__ = "imagen_evento"

    id_imagen = Column(UUID, primary_key=True, default=uuid4())
    url = Column(VARCHAR(100), nullable=False)
    id_evento = Column(UUID, nullable=False)
    id_usuario_crea = Column(UUID, ForeignKey("usuario.id_usuario"), nullable=False)
    fecha_creacion = Column(DateTime, nullable=False, default=datetime.now())

    # relaciones
    evento = Relationship("evento", back_populates="imagenes")
    usuario_crea = Relationship("usuario", back_populates="imagenes_eventos_creadas")
