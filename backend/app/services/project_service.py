from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.project import Project
from app.schemas.project import ProjectCreate
from app.services.team_access_service import is_team_member


def create_project(db: Session, project: ProjectCreate, user_id: int):
    if not is_team_member(db, project.team_id, user_id):
        raise HTTPException(status_code=403, detail="Not a team member")

    db_project = Project(
        name=project.name,
        description=project.description,
        team_id=project.team_id,
    )

    db.add(db_project)
    db.commit()
    db.refresh(db_project)

    return db_project


def get_team_projects(db: Session, team_id: int, user_id: int):
    if not is_team_member(db, team_id, user_id):
        raise HTTPException(status_code=403, detail="Not allowed")

    return db.query(Project).filter(Project.team_id == team_id).all()