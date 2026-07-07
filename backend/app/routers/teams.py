from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.dependencies.auth import get_current_user

from app.models.user import User
from app.schemas.team import (
    TeamCreate,
    TeamUpdate,
    TeamResponse,
)

from app.services.team_service import (
    create_team,
    get_user_teams,
    update_team,
    delete_team,
)

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
        current_user=current_user,
    )


@router.get("", response_model=list[TeamResponse])
def list_my_teams(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_user_teams(
        db=db,
        current_user=current_user,
    )


@router.put("/{team_id}", response_model=TeamResponse)
def edit_team(
    team_id: int,
    team: TeamUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return update_team(
        team_id=team_id,
        team=team,
        db=db,
        current_user=current_user,
    )


@router.delete("/{team_id}")
def remove_team(
    team_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return delete_team(
        team_id=team_id,
        db=db,
        current_user=current_user,
    )