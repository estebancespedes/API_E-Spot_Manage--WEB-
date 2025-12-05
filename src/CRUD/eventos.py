from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload

from src.models.organizacion import organizacion
from src.models.evento import evento


async def get_event_preview_usr_id(id_usuario: str):
    """
    Metodo asincrono para obtener todos los eventos
    con sus etiquetas e imagenes
    """

    query = (
        select(evento)
        .options(joinedload(evento.etiquetas))
        .options(joinedload(evento.imagenes))
        .where(evento.id_usuario_crea == id_usuario)
        .order_by(evento.fecha_creacion.desc())
    )
    return query

async def get_event_preview_org_id(org_id:str):
    """
    Metodo asincrono para obtener todos los eventos
    con sus etiquetas e imagenes
    """

    query = (
        select(evento)
        .options(joinedload(evento.etiquetas))
        .options(joinedload(evento.imagenes))
        .options(joinedload(evento.organizaciones))
        .where(evento.organizaciones.any(organizacion.id_organizacion == org_id))
        .order_by(evento.fecha_creacion.desc())
    )
    return query