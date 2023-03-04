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


def get_db():
    with session() as Session:
        yield Session
