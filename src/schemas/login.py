from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field, validator, EmailStr


class login(BaseModel):
    Correo: EmailStr = Field(..., description="Correo registrado")
    clave: str = Field(..., description="Clave de usuario")

    class Config:
        from_attributes = True


class loginResponse(BaseModel):
    Token: str = Field(..., description="Token generado despues de iniciar sesion")
