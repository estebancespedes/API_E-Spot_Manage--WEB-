from sqlalchemy import Column, ForeignKey, Table, UUID
from src.database.base_class import Base

eventos_ubicaciones = Table(
    "eventos_ubicaciones",
    Base.metadata,
    Column("id_evento", UUID, ForeignKey("evento.id_evento"), primary_key=True),
    Column(
        "id_ubicacion", UUID, ForeignKey("ubicacion.id_ubicacion"), primary_key=True
    )
)

organizaciones_eventos = Table(
    "organizaciones_eventos",
    Base.metadata,
    Column("id_evento", UUID, ForeignKey("evento.id_evento"), primary_key=True),
    Column(
        "id_organizacion",
        UUID,
        ForeignKey("organizacion.id_organizacion"),
        primary_key=True,
    )
)


