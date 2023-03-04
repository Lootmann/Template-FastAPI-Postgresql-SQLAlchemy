from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from api.settings import Settings

credential = Settings()

engine = create_engine(credential.db_url, echo=True)

session = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine,
)


Base = declarative_base()


async def get_db():
    async with session() as Session:
        yield Session
