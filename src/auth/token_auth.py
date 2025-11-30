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


def decode_jwt(token: str) -> dict or str:
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
        return "El token ha expirado"
    except jwt.exceptions.InvalidSignatureError:
        return "La firma del token no es correcta"
    except:
        return "Error"
