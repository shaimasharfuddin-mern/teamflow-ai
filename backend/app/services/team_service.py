from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.team import Team
from app.models.team_member import TeamMember
from app.models.user import User
from app.schemas.team import TeamCreate, TeamUpdate


def create_team(
    db: Session,
    team: TeamCreate,
    current_user: User,
):
    db_team = Team(
        name=team.name,
        description=team.description,
        owner_id=current_user.id,
    )

    db.add(db_team)
    db.commit()
    db.refresh(db_team)

    db_member = TeamMember(
        team_id=db_team.id,
        user_id=current_user.id,
    )

    db.add(db_member)
    db.commit()

    return db_team


def get_user_teams(
    db: Session,
    current_user: User,
):
    return (
        db.query(Team)
        .filter(Team.owner_id == current_user.id)
        .all()
    )


def update_team(
    team_id: int,
    team: TeamUpdate,
    db: Session,
    current_user: User,
):
    db_team = (
        db.query(Team)
        .filter(
            Team.id == team_id,
            Team.owner_id == current_user.id,
        )
        .first()
    )

    if not db_team:
        raise HTTPException(
            status_code=404,
            detail="Team not found",
        )

    db_team.name = team.name
    db_team.description = team.description

    db.commit()
    db.refresh(db_team)

    return db_team


def delete_team(
    team_id: int,
    db: Session,
    current_user: User,
):
    db_team = (
        db.query(Team)
        .filter(
            Team.id == team_id,
            Team.owner_id == current_user.id,
        )
        .first()
    )

    if not db_team:
        raise HTTPException(
            status_code=404,
            detail="Team not found",
        )

    db.delete(db_team)
    db.commit()

    return {
        "message": "Team deleted successfully"
    }