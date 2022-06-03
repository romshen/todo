from typing import Optional

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from api import models, schemas, services
from api.database import get_db

app = FastAPI()


@app.post("/tasks", response_model=schemas.Task)
def create(task: schemas.TaskCreation, db: Session = Depends(get_db)):
    return services.create_new_task(db, task)


@app.get("/tasks", response_model=list[schemas.Task])
def get_tasks(
    skip: Optional[int] = 0, limit: Optional[int] = 50, db: Session = Depends(get_db)
):
    return models.Task.get_bunch(db, skip, limit)


@app.get("/tasks/{task_id}", response_model=schemas.Task)
def get_task(task_id: int, db: Session = Depends(get_db)):
    return services.get_existing_task(db, task_id)


@app.patch("/tasks/{task_id}", response_model=int)
def update_task(task_id: int, updates: schemas.Task, db: Session = Depends(get_db)):
    return services.update_existing_task(db, task_id, updates)


@app.delete("/tasks/{task_id}", response_model=int)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return services.delete_existing_task(db, task_id)
