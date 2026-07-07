from datetime import datetime
from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    project_id: int
    assignee_id: int | None = None
    priority: str = "medium"
    due_date: datetime | None = None


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None
    priority: str | None = None
    assignee_id: int | None = None
    due_date: datetime | None = None


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    status: str
    priority: str
    project_id: int
    assignee_id: int | None = None
    due_date: datetime | None = None

    class Config:
        from_attributes = True