from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.project import Project
from app.models.team import Team
from app.models.user import User

from app.schemas.project import (
    ProjectCreate,
    ProjectUpdate,
)


def create_project(
    db: Session,
    project: ProjectCreate,
    current_user: User,
):
    team = (
        db.query(Team)
        .filter(
            Team.id == project.team_id,
            Team.owner_id == current_user.id,
        )
        .first()
    )

    if not team:
        raise HTTPException(
            status_code=404,
            detail="Team not found",
        )

    db_project = Project(
        name=project.name,
        description=project.description,
        team_id=project.team_id,
    )

    db.add(db_project)
    db.commit()
    db.refresh(db_project)

    return db_project


def get_team_projects(
    db: Session,
    team_id: int,
    current_user: User,
):
    team = (
        db.query(Team)
        .filter(
            Team.id == team_id,
            Team.owner_id == current_user.id,
        )
        .first()
    )

    if not team:
        raise HTTPException(
            status_code=404,
            detail="Team not found",
        )

    return (
        db.query(Project)
        .filter(Project.team_id == team_id)
        .all()
    )


def update_project(
    project_id: int,
    project: ProjectUpdate,
    db: Session,
    current_user: User,
):
    db_project = (
        db.query(Project)
        .join(Team)
        .filter(
            Project.id == project_id,
            Team.owner_id == current_user.id,
        )
        .first()
    )

    if not db_project:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )

    db_project.name = project.name
    db_project.description = project.description

    db.commit()
    db.refresh(db_project)

    return db_project


def delete_project(
    project_id: int,
    db: Session,
    current_user: User,
):
    db_project = (
        db.query(Project)
        .join(Team)
        .filter(
            Project.id == project_id,
            Team.owner_id == current_user.id,
        )
        .first()
    )

    if not db_project:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )

    db.delete(db_project)
    db.commit()

    return {
        "message": "Project deleted successfully"
    }