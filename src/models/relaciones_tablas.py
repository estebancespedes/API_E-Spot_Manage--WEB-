from sqlalchemy import Column, ForeignKey, Table, UUID
from src.database.base_class import Base

eventos_ubicaciones = Table(
    Column('id_evento', UUID, ForeignKey('evento.id_evento'), primary_key= True  ),
    Column('id_ubicacion', UUID, ForeignKey('ubicacion.id_ubicacion'), primary_key=True),
    name = 'eventos_ubicaciones',
    metadata= Base.metadata, 
)

organizaciones_eventos = Table(
    Column('id_evento', UUID, ForeignKey('evento.id_evento'), primary_key=True),
    Column('id_organizacion', UUID, ForeignKey('organizacion.id_organizacion'), primary_key=True),
    name= 'organizaciones_eventos',
    metadata= Base.metadata
)

class Eventos_ubicaciones(Base):
    id_evento = Column(UUID, ForeignKey('evento.id_evento'), primary_key=True)
    id_organizacion = Column(UUID, ForeignKey('ubicacion.id_ubicacion'), primary_key=True)

class Organizaciones_eventos(Base):
    id_evento = Column(UUID, ForeignKey('evento.id_evento'), primary_key=True)
    id_organizacion = Column(UUID, ForeignKey('organizacion.id_organizacion'), primary_key=True)