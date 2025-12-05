from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field

from src.schemas.etiquetas import etiquetaRead
from src.schemas.imagen_ev import imagen_read


class etiqueta_base(BaseModel):
    nombre : str = Field(..., description='Titulo del evento')
    fecha_inicio :  datetime =Field(..., description='Fecha de inicializacion del evento')
    imagenes : list[imagen_read] = Field(..., description='lista de imagenes del evento')
    etiquetas : list[etiquetaRead] = Field(..., description='lista de etiquetas del evento')
    class Config:
        from_attributes = True

class preview_response(etiqueta_base):
    id_evento : UUID = Field(..., description='id unico de la etiqueta')