from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.task import Task
from app.models.project import Project
from app.core.task_constants import VALID_STATUS_FLOW
from app.services.team_access_service import is_team_member


# -----------------------------
# CREATE TASK (SECURED)
# -----------------------------
def create_task(db: Session, task_data, user_id: int):

    project = (
        db.query(Project)
        .filter(Project.id == task_data.project_id)
        .first()
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    if not is_team_member(db, project.team_id, user_id):
        raise HTTPException(
            status_code=403,
            detail="You are not a member of this team"
        )

    task = Task(
        title=task_data.title,
        description=task_data.description,
        status="todo",
        priority=task_data.priority,
        project_id=task_data.project_id,
        team_id=project.team_id,
        assignee_id=task_data.assignee_id,
        due_date=task_data.due_date,
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


# -----------------------------
# UPDATE TASK
# -----------------------------
def update_task(db: Session, task_id: int, updates, user_id: int):

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if not is_team_member(db, task.team_id, user_id):
        raise HTTPException(status_code=403, detail="Not allowed")

    if updates.status:

        allowed_next = VALID_STATUS_FLOW.get(task.status, [])

        if updates.status not in allowed_next:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid transition: {task.status} → {updates.status}"
            )

        if updates.status == "done" and task.assignee_id != user_id:
            raise HTTPException(
                status_code=403,
                detail="Only assignee can mark task as done"
            )

        task.status = updates.status

    if updates.title is not None:
        task.title = updates.title

    if updates.description is not None:
        task.description = updates.description

    if updates.priority is not None:
        task.priority = updates.priority

    if updates.assignee_id is not None:
        task.assignee_id = updates.assignee_id

    if updates.due_date is not None:
        task.due_date = updates.due_date

    db.commit()
    db.refresh(task)

    return task


# -----------------------------
# GET TASKS
# -----------------------------
def get_project_tasks(db: Session, project_id: int):
    return db.query(Task).filter(Task.project_id == project_id).all()


# -----------------------------
# FILTER TASKS
# -----------------------------
def filter_tasks(db: Session, project_id=None, status=None, priority=None):

    query = db.query(Task)

    if project_id:
        query = query.filter(Task.project_id == project_id)

    if status:
        query = query.filter(Task.status == status)

    if priority:
        query = query.filter(Task.priority == priority)

    return query.all()