from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from api.config import env

engine = create_engine(
    f"{env.DB_TYPE}://{env.USER_NAME}:{env.PASSWORD}@{env.HOST}:{env.PORT}/"
    f"{env.DB_NAME}"
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
