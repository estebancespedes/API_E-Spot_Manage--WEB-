# importacion de librerias
from datetime import datetime
from sqlalchemy import Column, UUID, ForeignKey, VARCHAR, FLOAT, DATETIME
from sqlalchemy.orm import Relationship
from uuid import uuid4

# importacion de modelo base
from models.relaciones_tablas import eventos_ubicaciones
from src.database.base_class import Base


class ubicacion(Base):
    """
    Tabla ubicacion:
        guarda las ubicaciones de los puntos de interes y de los eventos
        atributos:
            id_ubicacion : UUID
            direccion : varchar(50)
            complemento_1 : varchar(30)
            complemento_2 : varchar(30)
            latitud : float
            longitud : float
            id_usuario_crea : UUID
            fecha_crea : Datetime
            id_usuario_edita : UUID
            fecha_edita : Datetime
    """

    __tablename__ = "ubicacion"

    id_ubicacion = Column(UUID, primary_key=True, default=uuid4())
    direccion = Column(VARCHAR(50), nullable=False)
    complemento_1 = Column(VARCHAR(30), nullable=True)
    complemento_2 = Column(VARCHAR(30), nullable=True)
    latitud = Column(FLOAT, nullable=False)
    longitud = Column(FLOAT, nullable=False)
    id_usuario_crea = Column(UUID, ForeignKey("usuario.id_usuario"), nullable=False)
    fecha_crea = Column(DATETIME, nullable=False, default=datetime.now())
    id_usuario_edita = Column(UUID, ForeignKey("usuario.id_usuario"), nullable=True)
    fecha_edita = Column(DATETIME, nullable=True, onupdate=datetime.now())

    # relaciones
    ciudad = Relationship("ciudad", back_populates="ubicaciones")
    puntos_interes = Relationship("punto interes", back_populates="ubicacion")
    usuario_creacion = Relationship(
        "usuario", foreign_keys=[id_usuario_crea], back_populates="ubicaciones_creadas"
    )
    usuario_edicion = Relationship(
        "usuario",
        foreign_keys=[id_usuario_edita],
        back_populates="ubicaciones_editadas",
    )
    eventos = Relationship(
        "eventos", secondary=eventos_ubicaciones, back_populates="ubicaciones"
    )
