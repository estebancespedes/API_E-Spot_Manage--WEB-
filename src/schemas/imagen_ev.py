from uuid import UUID
from pydantic import BaseModel, Field

class imagen_base(BaseModel):
    url : str = Field(..., description='url de la imagen guardada')

    class Config:
        from_attributes = True

class imagen_read(imagen_base):
    id_imagen: UUID =Field(..., description='id unico de la imagen')