from sqlalchemy.orm import Session

from app.models.task import Task
from app.services.task_analytics_service import get_overdue_tasks


def calculate_project_health(db: Session, project_id: int):

    tasks = db.query(Task).filter(Task.project_id == project_id).all()

    total = len(tasks)
    done = len([t for t in tasks if t.status == "done"])
    in_progress = len([t for t in tasks if t.status == "in_progress"])
    todo = len([t for t in tasks if t.status == "todo"])

    overdue_tasks = get_overdue_tasks(db, project_id)
    overdue_count = len(overdue_tasks)

    # -------------------------
    # Completion Score
    # -------------------------
    completion_score = (done / total * 100) if total > 0 else 0

    # -------------------------
    # Risk Score
    # -------------------------
    risk_score = 0

    if overdue_count > 0:
        risk_score += overdue_count * 10

    if in_progress > total * 0.6:
        risk_score += 20

    # Normalize
    if risk_score >= 70:
        risk_level = "HIGH"
    elif risk_score >= 30:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    # -------------------------
    # Final Health Score
    # -------------------------
    health_score = max(0, 100 - risk_score + completion_score * 0.3)

    if health_score > 85:
        status = "HEALTHY 🟢"
    elif health_score > 60:
        status = "MODERATE 🟠"
    else:
        status = "AT RISK 🔴"

    return {
        "project_id": project_id,
        "total_tasks": total,
        "done": done,
        "in_progress": in_progress,
        "todo": todo,
        "overdue_tasks": overdue_count,
        "completion_score": round(completion_score, 2),
        "risk_level": risk_level,
        "health_score": round(health_score, 2),
        "status": status
    }