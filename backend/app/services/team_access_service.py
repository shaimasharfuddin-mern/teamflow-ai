from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.team_member import TeamMember


def is_team_member(db: Session, team_id: int, user_id: int) -> bool:
    member = (
        db.query(TeamMember)
        .filter(
            TeamMember.team_id == team_id,
            TeamMember.user_id == user_id,
        )
        .first()
    )

    return member is not None


def require_team_member(db: Session, team_id: int, user_id: int):
    if not is_team_member(db, team_id, user_id):
        raise HTTPException(
            status_code=403,
            detail="Not authorized for this team",
        )