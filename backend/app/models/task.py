from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func

from app.db.database import Base
from app.core.task_constants import TASK_STATUS_TODO


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255), nullable=False)
    description = Column(String(500), nullable=True)

    status = Column(String(50), default=TASK_STATUS_TODO, index=True)

    priority = Column(String(20), default="medium")

    team_id = Column(Integer, ForeignKey("teams.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))
    assignee_id = Column(Integer, ForeignKey("users.id"))

    due_date = Column(DateTime, nullable=True)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())