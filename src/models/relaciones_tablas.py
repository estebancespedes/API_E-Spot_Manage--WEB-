from sqlalchemy import Column, ForeignKey, Table, UUID
from src.database.base_class import Base

eventos_ubicaciones = Table(
    "eventos_ubicaciones",
    Base.metadata,
    Column("id_evento", UUID, ForeignKey("e_spot_schema.evento.id_evento"), primary_key=True),
    Column(
        "id_ubicacion", UUID, ForeignKey("e_spot_schema.ubicacion.id_ubicacion"), primary_key=True
    ),
    schema='e_spot_schema'
    
)

organizaciones_eventos = Table(
    "organizaciones_eventos",
    Base.metadata,
    Column("id_evento", UUID, ForeignKey("e_spot_schema.evento.id_evento"), primary_key=True),
    Column(
        "id_organizacion",
        UUID,
        ForeignKey("e_spot_schema.organizacion.id_organizacion"),
        primary_key=True,
    ),
    schema='e_spot_schema'
)

usuarios_eventos = Table(
    "usuarios_eventos",
    Base.metadata,
    Column("id_usuario", UUID, ForeignKey("e_spot_schema.usuario.id_usuario"), primary_key=True),
    Column("id_evento", UUID, ForeignKey("e_spot_schema.evento.id_evento"), primary_key=True),
    schema='e_spot_schema'
)

etiquetas_eventos = Table(
    "etiquetas_eventos",
    Base.metadata,
    Column("id_etiqueta", UUID, ForeignKey("e_spot_schema.etiqueta.id_etiqueta"), primary_key=True),
    Column("id_evento", UUID, ForeignKey("e_spot_schema.evento.id_evento"), primary_key=True),
    schema='e_spot_schema'
)
