# importaciones de librerias
from datetime import datetime
from sqlalchemy import Column, UUID, DateTime, ForeignKey, VARCHAR
from sqlalchemy.orm import relationship
from uuid import uuid4

# importacion del modelo base
from src.database.base_class import Base


class imagen_p_i(Base):
    """
    Tabla imagen_p_i:
        atributos:
            - id_imagen : uuid
            - id_punto_interes : foreign key del punto de interes
            - url : varchar(100)
            - id_usuario_crea : foreignkey id usuario
            - fecha_crea: datetime
            - id_usuario_edita : foreignkey id_usuario
            - fecha_edita : foreignkey id_usuario
    """
    __tablename__ = 'imagen PI'

    id_imagen = Column(UUID, primary_key=True, default=uuid4())
    id_punto_interes = Column(UUID, ForeignKey('punto interes.id_punto_interes'), nullable=False)
    url = Column(VARCHAR(100),nullable=False)
    id_usuario_crea = Column(UUID,ForeignKey('usuario.id_usuario'), nullable=False)
    fecha_crea = Column(DateTime, default=datetime.now(), nullable=False)
    id_usuario_edita =  Column(UUID, ForeignKey('usuario.id_usuario'), nullable=True)
    fecha_edita = Column(DateTime, nullable=True, onupdate=datetime.now())

    #relaciones
    punto_interes = relationship('punto interes', back_populates='imagenes_PI')
