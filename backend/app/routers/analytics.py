from fastapi import APIRouter
from app.services.task_analytics_service import get_project_health

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/project/{project_id}/health")
def project_health(project_id: int):
    return get_project_health(project_id)