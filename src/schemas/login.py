from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field, validator, EmailStr


class login(BaseModel):
    Correo: EmailStr = Field(..., description="Correo registrado")
    clave: str = Field(..., description="Clave de usuario")
