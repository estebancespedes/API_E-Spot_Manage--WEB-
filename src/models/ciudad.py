# importaciones de librerias
from sqlalchemy import Column, UUID, TEXT, ForeignKey, VARCHAR
from sqlalchemy.orm import relationship
from uuid import uuid4

# importacion del modelo base
from src.database.base_class import Base


class ciudad(Base):
    """
    Tabla ciudad:
        Usada como directorio de ciudades
        Atributos
            id_ciudad : UUID
            id_region : UUID
            nombre : varchar(50)
            descripcion : TEXT
    """

    __tablename__ = "ciudad"
    __table_args__ = {'schema': 'e_spot_schema'}

    id_ciudad = Column(UUID, primary_key=True, default=uuid4())
    id_region = Column(UUID, ForeignKey("e_spot_schema.region.id_region"), nullable=False)
    nombre = Column(VARCHAR(50), nullable=False)
    descripcion = Column(TEXT, nullable=False)

    # relaciones
    region = relationship("region", back_populates="ciudades")

    ubicaciones = relationship("ubicacion", back_populates="ciudad")
