from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TaskCreation(BaseModel):
    description: Optional[str]
    is_active: Optional[bool] = False
    done: Optional[bool] = False
    deadline: Optional[datetime]


class Task(TaskCreation):
    id: Optional[int]
    created: Optional[datetime]
    updated: Optional[datetime]

    class Config:
        orm_mode = True
