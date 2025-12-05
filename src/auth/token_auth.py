from fastapi import HTTPException, status
import jwt
import datetime
from src.core.config import settings





def gen_jwt(user_id: str, org_id: str, rol_id: str) -> str:
    """
    Metodo de generacion del token jwt
    Recives:
        id_usuario
        id_organizacion
        id_rol
    Returns:
        str token de autenticacion
    """
    payload = {
        "exp": datetime.datetime.now(datetime.timezone.utc)
        + datetime.timedelta(hours=8),
        "iat": datetime.datetime.now(datetime.timezone.utc),
        "id_usuario": user_id,
        "org_id": org_id,
        "rol_id": rol_id,
    }
    return jwt.encode(payload=payload, key=settings.SECRETAPI_KEY, algorithm=settings.ALGORITHM)


def decode_jwt(token: str) -> dict:
    """
    Metodo de decodificacion del token
    Recives
        str: token codificado
    Returns
        dict: diccionario con el contenido del payload o informacion de error
    """
    try:
        return jwt.decode(jwt=token, algorithms=settings.ALGORITHM, key=settings.SECRETAPI_KEY)
    except jwt.exceptions.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="El token ha expirado") 
    except jwt.exceptions.InvalidSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail= "La firma del token no es correcta")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Error {e}") 


def permission_roles( token:dict, valid_roles:list[str] = None):
    """ 
    Metodo para verificar los permisos de los roles segun una lista de roles admitidos
    Recieves:
        token : token jwt con los datos ncesarios y previamente decodificados
        valid_roles: lista con los strings para los roles validos
            USUARIO,
            ORGANIZADOR/EMPLEADO
            ORGANIZADOR/ADMINISTRADOR
            (ADMINISTRADOR ya cuenta con permiso automatico)
    returns
        boolean 
            True el usuario tiene permiso de entrar al endpoint
            False el usuario no cuenta con permisos para entrar al endpoint
    """
    if token['rol_id'] == settings.ADMINISTRADOR:
        return True
    elif 'USUARIO' in valid_roles and token['rol_id'] == settings.USUARIO:
        return True
    elif 'ORGANIZADOR/ADMINISTRADOR' in valid_roles and token['rol_id'] == settings.ORGANIZADOR_ADMINISTRADOR:
        return True
    elif 'ORGANIZADOR/EMPLEADO' in valid_roles and token['rol_id'] == settings.ORGANIZADOR_EMPLEADO:
        return True
    else:
        return False