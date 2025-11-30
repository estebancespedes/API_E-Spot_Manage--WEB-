from sqlalchemy.orm import Session

from src.models.usuario import usuario
from src.auth.hash import *

def login(correo:str, clave:str,  db:Session) -> usuario or None:
    """
    Metodo crud para el login
    Recieves:
        correo
        clave
        session de la base de datos
    Returns:
        objeto usuario con la informacion | None porque no se encontro el usuario o la contraseña es incorrecta
    """
    usr = db.query(usuario).filter(correo == usuario.correo).first()
    if usr is None:
        return None
    if verify_password(clave, usr.password_hash):
        return usr
    else:
        return None