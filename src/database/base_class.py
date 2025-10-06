from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    """ Definicion de la clase base de sql alchemy para los modelos"""
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
