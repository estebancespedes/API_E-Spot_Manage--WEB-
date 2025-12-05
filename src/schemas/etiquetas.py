from uuid import UUID
from pydantic import BaseModel, Field


class etiquetaRead(BaseModel):
    id_etiqueta: UUID = Field(..., description="id unico de la etiqueta")
    nombre: str = Field(..., description="Nombre que recibe la etiqueta")

    class Config:
        from_attributes = True
