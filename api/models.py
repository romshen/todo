from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import Session

from api import schemas
from api.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    is_active = Column(Boolean, default=False)
    done = Column(Boolean, default=False)
    created = Column(DateTime, default=datetime.now)
    updated = Column(DateTime, onupdate=datetime.now)
    deadline = Column(DateTime, default=None)

    @classmethod
    def _get_task_query(cls, db: Session):
        return db.query(cls)

    @classmethod
    def get_bunch(cls, db: Session, skip: int = 0, limit: int = 50):
        return cls._get_task_query(db).offset(skip).limit(limit).all()

    @classmethod
    def _filter_by_id(cls, db: Session, task_id: int):
        return cls._get_task_query(db).filter(cls.id == task_id)

    @classmethod
    def get_by_id(cls, db: Session, task_id: int):
        return cls._filter_by_id(db, task_id).first()

    @classmethod
    def get_by_description(cls, db: Session, text: str, deadline: datetime):
        return (
            cls._get_task_query(db)
            .filter(cls.description == text, cls.deadline == deadline)
            .first()
        )

    @classmethod
    def get_by_description_piece(cls, db: Session, text: str):
        return cls._get_task_query(db).filter(text in cls.description).first()

    @classmethod
    def create_task(cls, db: Session, task: schemas.TaskCreation):
        db_task = cls(**task.dict())
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task

    @classmethod
    def update(cls, db: Session, task_id: int, task_updates: schemas.Task):
        updated = cls._filter_by_id(db, task_id).update(
            task_updates.dict(exclude_unset=True), synchronize_session="fetch"
        )
        db.commit()
        return updated

    @classmethod
    def delete(cls, db: Session, task_id: int):
        deleted = cls._filter_by_id(db, task_id).delete(synchronize_session="evaluate")
        db.commit()
        return deleted
