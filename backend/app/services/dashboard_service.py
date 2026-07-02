from sqlalchemy.orm import Session

from app.models.team import Team
from app.models.project import Project
from app.models.task import Task

from app.core.task_constants import TASK_STATUS_DONE


def get_dashboard_stats(db: Session, user):
    total_teams = db.query(Team).count()

    total_projects = db.query(Project).count()

    total_tasks = db.query(Task).count()

    completed_tasks = (
        db.query(Task)
        .filter(Task.status == TASK_STATUS_DONE)
        .count()
    )

    pending_tasks = total_tasks - completed_tasks

    if total_tasks == 0:
        health = 100
    else:
        health = int((completed_tasks / total_tasks) * 100)

    return {
        "user": user["email"],
        "teams": total_teams,
        "projects": total_projects,
        "tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "health": health,
    }