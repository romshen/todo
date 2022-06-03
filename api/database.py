from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.config import env

engine = create_engine(
    f"{env.DB_TYPE}://{env.USER_NAME}:{env.PASSWORD}@{env.DB_HOST}:{env.DB_PORT}/"
    f"{env.DB_NAME}"
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
