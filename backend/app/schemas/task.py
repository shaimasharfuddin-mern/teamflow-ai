from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    project_id: int
    assignee_id: int | None = None
    due_date: str | None = None


class TaskUpdate(BaseModel):
    status: str | None = None
    priority: str | None = None
    assignee_id: int | None = None


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    status: str
    priority: str
    due_date: str | None = None
    project_id: int
    assignee_id: int | None = None

    class Config:
        from_attributes = True