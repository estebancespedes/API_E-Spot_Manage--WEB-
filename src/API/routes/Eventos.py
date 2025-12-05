from fastapi import Depends, HTTPException, Header, status
from fastapi.routing import APIRouter

from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.config import settings
from src.auth.token_auth import decode_jwt, permission_roles
from src.API.Deps import get_db
from src.schemas.eventos import preview_response
from src.CRUD import eventos as ev_crud


router = APIRouter(
    prefix="/events",
    tags=["Eventos"],
)


@router.get("/prev", response_model=Page[preview_response])
async def get_preview_events(
    auth_header: str |None = Header(default=None, alias="Authentication"),
    db: AsyncSession = Depends(get_db),
):
    ACCEPTED_ROLES = [
        'ORGANIZADOR/ADMINISTRADOR',
        'ORGANIZADOR/EMPLEADO'
    ]
    if auth_header is None or auth_header == '':
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail='No se encontro token de verificacion')
    token: dict = decode_jwt(auth_header) 
    if not permission_roles(token=token, valid_roles=ACCEPTED_ROLES):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    if settings.ORGANIZADOR_ADMINISTRADOR == token['rol_id']:
        return await paginate(db, await  ev_crud.get_event_preview_org_id(token['org_id']))
    if settings.ORGANIZADOR_EMPLEADO == token['org_id']:
        return await paginate(db, await ev_crud.get_event_preview_usr_id(token['id_usuario']))
    

