from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import engine
from src.core.config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=True)
AsyncLocalSession = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
)
