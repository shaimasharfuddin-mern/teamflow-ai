from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.team import TeamCreate, TeamResponse
from app.services.team_service import create_team, get_user_teams

router = APIRouter(
    prefix="/teams",
    tags=["Teams"],
)


@router.post("", response_model=TeamResponse)
def create_new_team(
    team: TeamCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_team(
        db=db,
        team=team,
        owner_id=current_user.id,
    )


@router.get("", response_model=list[TeamResponse])
def list_my_teams(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_user_teams(
        db=db,
        owner_id=current_user.id,
    )