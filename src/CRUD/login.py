
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.models.usuario import usuario
from src.auth.hash import *

async def login(correo:str, clave:str,  db:AsyncSession) -> usuario or None:
    """
    Metodo crud para el login
    Recieves:
        correo
        clave
        session de la base de datos
    Returns:
        objeto usuario con la informacion | None porque no se encontro el usuario o la contraseña es incorrecta
    """
    query = select(usuario).filter(correo == usuario.correo) #unicamente la query

    usr = await db.execute(query) #ejecutar la query
    usr = usr.scalars().first() #obtener el primer usuario o none

    if usr is None:
        return None
    if verify_password(clave, usr.password_hash):
        return usr
    else:
        return None