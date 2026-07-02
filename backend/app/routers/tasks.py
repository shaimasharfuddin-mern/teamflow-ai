from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.services.task_service import (
    create_task,
    get_project_tasks,
    update_task,
    filter_tasks,
)
from app.dependencies.auth import get_current_user

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)


@router.post("", response_model=TaskResponse)
def create_new_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user),
):
    return create_task(db, task)


@router.get("/project/{project_id}", response_model=list[TaskResponse])
def list_tasks(
    project_id: int,
    db: Session = Depends(get_db),
):
    return get_project_tasks(db, project_id)


@router.put("/{task_id}", response_model=TaskResponse)
def update_existing_task(
    task_id: int,
    updates: TaskUpdate,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user),
):
    return update_task(db, task_id, updates, current_user_id)


@router.get("/filter", response_model=list[TaskResponse])
def filter_task_endpoint(
    project_id: int | None = None,
    status: str | None = None,
    priority: str | None = None,
    db: Session = Depends(get_db),
):
    return filter_tasks(db, project_id, status, priority)