from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.dependencies.auth import get_current_user
from app.services.dashboard_service import get_dashboard_stats

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get("/stats")
def dashboard_stats(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    print("Dashboard route called")
    print(current_user)

    return get_dashboard_stats(
        db,
        current_user,
    )