from sqlalchemy import create_engine

from api.models.users import Base as UserBase
from api.settings import Settings

credential = Settings()
engine = create_engine(credential.db_url, echo=True)


def reset_database():
    UserBase.metadata.drop_all(bind=engine)
    UserBase.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()
