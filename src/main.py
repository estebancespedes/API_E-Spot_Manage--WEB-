from sqlalchemy import text
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.config import settings

from src.database import models
from src.API.Deps import get_db
from src.schemas.login import login as loginschema, loginResponse as LoginResponseS
from src.CRUD.login import *
from src.auth.token_auth import *

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
)


@app.get("/", status_code=status.HTTP_200_OK, tags=["Raiz"])
async def app_health(db: AsyncSession = Depends(get_db)):
    consulta: bool
    try:
        db.execute(text("SELECT 1"))
        consulta = True
    except:
        consulta = False

    return{
        "Bienvenido": settings.PROJECT_NAME,
        "Api_status": "Health",
        "Database_Status": ("Health") if consulta else "Error",
    }


@app.post(
    "/Login",
    status_code=status.HTTP_200_OK,
    response_model=LoginResponseS,
    tags=["Login"],
)
async def app_login(credentials: loginschema, db: AsyncSession = Depends(get_db)):
    user = await login(correo=credentials.Correo, clave=credentials.clave, db=db)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos",
        )
    return {
        "Token": gen_jwt(
            user_id=str(user.id_usuario),
            org_id=str(user.id_organizacion),
            rol_id=str(user.id_rol),
        )
    }


# inclusion de los routers
