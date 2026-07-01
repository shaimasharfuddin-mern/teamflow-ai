from sqlalchemy.orm import Session

from app.models.team import Team
from app.schemas.team import TeamCreate


def create_team(
    db: Session,
    team: TeamCreate,
    owner_id: int,
):
    db_team = Team(
        name=team.name,
        description=team.description,
        owner_id=owner_id,
    )

    db.add(db_team)
    db.commit()
    db.refresh(db_team)

    return db_team


def get_user_teams(
    db: Session,
    owner_id: int,
):
    return (
        db.query(Team)
        .filter(Team.owner_id == owner_id)
        .all()
    )