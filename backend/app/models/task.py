from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from app.db.database import Base


# -----------------------------
# ENUMS
# -----------------------------

class TaskStatus(str, enum.Enum):
    todo = "todo"
    in_progress = "in_progress"
    review = "review"
    done = "done"


class TaskPriority(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"
    urgent = "urgent"


# -----------------------------
# TASK MODEL
# -----------------------------

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)

    status = Column(Enum(TaskStatus), default=TaskStatus.todo)
    priority = Column(Enum(TaskPriority), default=TaskPriority.medium)

    due_date = Column(DateTime, nullable=True)

    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)

    assignee_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    project = relationship("Project", back_populates="tasks")
    team = relationship(
    "Team",
    back_populates="tasks"
)
    assignee = relationship("User", back_populates="tasks")