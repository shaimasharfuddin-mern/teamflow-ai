from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.project import ProjectCreate, ProjectResponse
from app.services.project_service import (
    create_project,
    get_team_projects,
)

from app.dependencies.auth import get_current_user

router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)


# -------------------------
# CREATE PROJECT (SECURE)
# -------------------------
@router.post("", response_model=ProjectResponse)
def create_new_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user),
):
    return create_project(db, project, current_user_id)


# -------------------------
# GET PROJECTS BY TEAM (SECURE)
# -------------------------
@router.get("/team/{team_id}", response_model=list[ProjectResponse])
def list_projects(
    team_id: int,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user),
):
    return get_team_projects(db, team_id, current_user_id)