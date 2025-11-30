import bcrypt


def encrypt_password(password: str) -> str:
    """
    Metodo de encriptacion de contraseña se encarga de generar una salt unica y
    generar un unico valor encriptado para guardar en la bd
    Returns:
        pasword hash (salt + hash)
    """
    password = password.encode(encoding="utf-8")
    salt = bcrypt.gensalt(rounds=14)
    return bcrypt.hashpw(password=password, salt=salt)


def verify_password(password_ingressed: str, password_hash: str) -> bool:
    '''
    Metodo de verificacion si la contraseña es corecta o no
    Returns:
        True : contraseña correcta
        False : contraseña incorrecta 
    '''
    password_ingressed = password_ingressed.encode(encoding="utf-8")
    password_hash = password_hash.encode(encoding="utf-8")

    return bcrypt.checkpw(password=password_ingressed, hashed_password=password_hash)
