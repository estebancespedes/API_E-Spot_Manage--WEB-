# importaciones de librerias
from datetime import datetime
from sqlalchemy import Column, UUID, VARCHAR, TEXT, DATETIME, FLOAT, ForeignKey
from uuid import uuid4

from sqlalchemy.orm import Relationship

# importación del modelo base
from models.relaciones_tablas import Organizaciones_eventos, eventos_ubicaciones
from src.database.base_class import Base


class evento(Base):
    """
    Tabla evento:
        atributos:
            - id_evento : uuid
            - nombre : varchar
            - descripcion : text (opcional)
            - fecha_inicio : datetime
            - fecha_fin : datetime
            - url_info : varchar
            - valor : float (opcional)
            - id_usuario_crea : uuid
            - fecha_creacion : datetime
            - id_usuario_edita : uuid (opcional)
            - fecha_edicion : datetime (opcional)
    """

    __tablename__ = "evento"

    id_evento = Column(UUID, primary_key=True, default=uuid4())
    nombre = Column(VARCHAR(50), nullable=False)
    descripcion = Column(TEXT, nullable=True)
    fecha_inicio = Column(DATETIME, nullable=False)
    fecha_fin = Column(DATETIME, nullable=False)
    url_info = Column(VARCHAR(100), nullable=True)
    valor = Column(FLOAT, nullable=True)
    id_usuario_crea = Column(UUID, ForeignKey("usuario.id_usuario"), nullable=False)
    fecha_creacion = Column(DATETIME, nullable=False, default=datetime.now())
    id_usuario_edita = Column(UUID, ForeignKey("usuario.id_usuario"), nullable=True)
    fecha_edicion = Column(DATETIME, nullable=True, onupdate=datetime.now())

    # agregar relaciones
    imagenes = Relationship("imagen_evento", back_populates="evento")
    ubicaciones = Relationship(
        "ubicacion", secondary=eventos_ubicaciones, back_populates="eventos"
    )
    organizaciones = Relationship(
        "organizacion", secondary=Organizaciones_eventos, back_populates="eventos"
    )
