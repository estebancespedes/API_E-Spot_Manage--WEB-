# importaciones de librerias
from sqlalchemy import Column, UUID, VARCHAR, TEXT, ForeignKey
from uuid import uuid4

from sqlalchemy.orm import Relationship

# importación del modelo base
from src.database.base_class import Base


class usuario(Base):
    """
    Tabla usuario:
        atributos:
            - id_usuario : uuid
            - id_organizacion : uuid (opcional)
            - id_rol : uuid
            - nombre_1 : varchar
            - nombre_2 : varchar (opcional)
            - apellido_1 : varchar
            - apellido_2 : varchar (opcional)
            - correo : varchar
            - password_hash : text
    """

    __tablename__ = "usuario"

    id_usuario = Column(UUID, primary_key=True, default=uuid4())
    id_organizacion = Column(
        UUID, ForeignKey("organizacion.id_organizacion"), nullable=True
    )
    id_rol = Column(UUID, ForeignKey("rol.id_rol"), nullable=False)
    nombre_1 = Column(VARCHAR(50), nullable=False)
    nombre_2 = Column(VARCHAR(50), nullable=True)
    apellido_1 = Column(VARCHAR(50), nullable=False)
    apellido_2 = Column(VARCHAR(50), nullable=True)
    correo = Column(VARCHAR(100), nullable=False, unique=True, index=True)
    password_hash = Column(TEXT, nullable=False)

    rol = Relationship("rol", back_populates="usuarios")
    organizacion = Relationship("organizacion", back_populates="usuarios")
    imagenes_eventos_creadas = Relationship(
        "imagen_evento", back_populates="usuario_crea"
    )
    imagenes_pi_creadas = Relationship("imagen_PI", back_populates="usuario_creacion")
    eventos_creados = Relationship(
        "evento",
        foreign_keys="[evento.id_usuario_crea]",
        back_populates="usuario_creacion",
    )
    eventos_editados = Relationship(
        "evento",
        foreign_keys="[evento.id_usuario_edita]",
        back_populates="usuario_edicion",
    )
    ubicaciones_creadas = Relationship(
        "ubicacion",
        foreign_keys="[ubicacion.id_usuario_crea]",
        back_populates="usuario_creacion",
    )
    ubicaciones_editadas = Relationship(
        "ubicacion",
        foreign_keys="[ubicacion.id_usuario_edita]",
        back_populates="usuario_edicion",
    )
    puntos_interes_creados = Relationship(
        "punto_interes",
        foreign_keys="[punto_interes.id_usuario_crea]",
        back_populates="usuario_creacion",
    )
    puntos_interes_editados = Relationship(
        "punto_interes",
        foreign_keys="[punto_interes.id_usuario_edita]",
        back_populates="usuario_edicion",
    )
    puntos_interes_creados = Relationship(
        "punto_interes",
        foreign_keys="[punto_interes.id_usuario_crea]",
        back_populates="usuario_creacion",
    )
    puntos_interes_editados = Relationship(
        "punto_interes",
        foreign_keys="[punto_interes.id_usuario_edita]",
        back_populates="usuario_edicion",
    )
