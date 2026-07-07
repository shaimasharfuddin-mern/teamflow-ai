from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.dependencies.auth import get_current_user

from app.models.user import User

from app.schemas.project import (
    ProjectCreate,
    ProjectUpdate,
    ProjectResponse,
)

from app.services.project_service import (
    create_project,
    get_team_projects,
    update_project,
    delete_project,
)

router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)


@router.post("", response_model=ProjectResponse)
def create_new_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_project(
        db=db,
        project=project,
        current_user=current_user,
    )


@router.get("/team/{team_id}", response_model=list[ProjectResponse])
def list_projects(
    team_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_team_projects(
        db=db,
        team_id=team_id,
        current_user=current_user,
    )


@router.put("/{project_id}", response_model=ProjectResponse)
def edit_project(
    project_id: int,
    project: ProjectUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return update_project(
        project_id=project_id,
        project=project,
        db=db,
        current_user=current_user,
    )


@router.delete("/{project_id}")
def remove_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return delete_project(
        project_id=project_id,
        db=db,
        current_user=current_user,
    )

print("PROJECT ROUTER LOADED")