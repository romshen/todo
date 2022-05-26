from fastapi import HTTPException
from sqlalchemy.orm import Session

from api import models, schemas


def create_new_task(db: Session, task: schemas.TaskCreation):
    db_task = models.Task.get_by_description(db, task.description, task.deadline)
    if db_task:
        raise HTTPException(status_code=400, detail="Task already exists.")
    return models.Task.create_task(db, task)


def get_existing_task(db: Session, task_id: int):
    db_task = models.Task.get_by_id(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


def update_existing_task(db: Session, task_id: int, updates: schemas.Task):
    get_existing_task(db, task_id)
    return models.Task.update(db, task_id, updates)


def delete_existing_task(db: Session, task_id: int):
    get_existing_task(db, task_id)
    return models.Task.delete(db, task_id)
