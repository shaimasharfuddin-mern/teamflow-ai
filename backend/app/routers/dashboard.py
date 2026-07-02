from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.db.database import get_db
from app.services.dashboard_service import get_dashboard_stats

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get("/stats")
def dashboard_stats(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return get_dashboard_stats(db, current_user)