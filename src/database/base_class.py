from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    """ Definicion de la clase base de sql alchemy para los modelos"""
    metadata = MetaData(schema='e_spot_schema')
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
