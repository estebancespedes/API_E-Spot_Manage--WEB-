from fastapi import Depends, FastAPI, HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED

from src.core.config import settings

from src.database import models
from src.API.Deps import get_db
from src.schemas.login import login as loginschema
from src.CRUD.login import *
from src.auth.token_auth import *

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
)


@app.post("/Login", response_model= str, status_code=200)
def app_login(credentials: loginschema, db:Session = Depends(get_db)):
    user = login(correo=credentials.Correo, clave=credentials.clave, db=db)
    if user is None:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail='Usuario o contraseña incorrectos')
    return gen_jwt(user.id_usuario, org_id=user.id_organizacion,rol_id=user.id_rol)

