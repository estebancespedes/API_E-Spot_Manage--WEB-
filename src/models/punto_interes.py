# importaciones de librerias
from datetime import datetime
from sqlalchemy import Column, UUID, DateTime, ForeignKey, VARCHAR, TEXT
from sqlalchemy.orm import relationship
from uuid import uuid4

# importacion del modelo base
from src.database.base_class import Base


class punto_interes(Base):
    """
    Tabla punto de interes
        atributos:
            -id_punto_interes : uuid
            -nombre :varchar (50)
            -descripcion : TEXT
            -id_ubicacion: foreign key tabla ubicacion
            -url_info : varchar(100)
            -id_usuario_crea : foreignkey id usuario
            -fecha_crea: datetime
            -id_usuario_edita : foreignkey id_usuario
            -fecha_edita : foreignkey id_usuario
    """

    __tablename__ = "punto interes"

    id_punto_interes = Column(UUID, primary_key=True, default=uuid4())
    nombre = Column(VARCHAR(50), nullable=False)
    descripcion = Column(TEXT, nullable=True)
    id_ubicacion = Column(UUID, ForeignKey("ubicacion.id_ubicacion"), nullable=False)
    url_info = Column(VARCHAR(100), nullable=True)
    id_usuario_crea = Column(UUID, ForeignKey("usuario.id_usuario"), nullable=False)
    fecha_crea = Column(DateTime, nullable=False, default=datetime.now())
    id_usuario_edita = Column(UUID, ForeignKey("usuario.id_usuario"), nullable=True)
    fecha_edita = Column(DateTime, nullable=True, onupdate=datetime.now())

    # relaciones
    ubicacion = relationship("ubicacion", back_populates="puntos_interes")
    imagenes_PI = relationship("imagen PI", back_populates="punto_interes")
    # agregar 1 relacion mas
