# importaciones de librerias
from datetime import datetime
from sqlalchemy import Column, UUID, VARCHAR, TEXT, DateTime, FLOAT, ForeignKey
from uuid import uuid4

from sqlalchemy.orm import relationship

# importación del modelo base
from src.models.relaciones_tablas import (
    organizaciones_eventos,
    eventos_ubicaciones,
    usuarios_eventos,
    etiquetas_eventos,
)
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
    __table_args__ = {"schema": "e_spot_schema"}

    id_evento = Column(UUID, primary_key=True, default=uuid4())
    nombre = Column(VARCHAR(50), nullable=False)
    descripcion = Column(TEXT, nullable=True)
    fecha_inicio = Column(DateTime, nullable=False)
    fecha_fin = Column(DateTime, nullable=False)
    url_info = Column(VARCHAR(100), nullable=True)
    valor = Column(FLOAT, nullable=True)
    id_usuario_crea = Column(
        UUID, ForeignKey("e_spot_schema.usuario.id_usuario"), nullable=False
    )
    fecha_creacion = Column(DateTime, nullable=False, default=datetime.now())
    id_usuario_edita = Column(
        UUID, ForeignKey("e_spot_schema.usuario.id_usuario"), nullable=True
    )
    fecha_edicion = Column(DateTime, nullable=True, onupdate=datetime.now())

    # relaciones
    imagenes = relationship("imagen_evento", back_populates="evento")
    ubicaciones = relationship(
        "ubicacion", secondary=eventos_ubicaciones, back_populates="eventos"
    )
    organizaciones = relationship(
        "organizacion", secondary=organizaciones_eventos, back_populates="eventos"
    )
    usuario_creacion = relationship(
        "usuario", foreign_keys=[id_usuario_crea], back_populates="eventos_creados"
    )
    usuario_edicion = relationship(
        "usuario", foreign_keys=[id_usuario_edita], back_populates="eventos_editados"
    )

    usuarios = relationship(
        "usuario", secondary=usuarios_eventos, back_populates="eventos"
    )

    etiquetas = relationship(
        "etiqueta", secondary=etiquetas_eventos, back_populates="eventos"
    )

    reportes = relationship("reporte", back_populates="evento")
